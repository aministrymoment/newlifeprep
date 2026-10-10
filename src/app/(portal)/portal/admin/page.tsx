'use client';
import { useCallback, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';

type P = { id: string; email: string | null; full_name: string | null; student_id: string | null; grade_level?: number | null; role: string };
type C = { id: string; title: string; slug: string };
type S = { id: string; body: string; created_at: string; user_id: string; item_id: string; score: number | null; feedback: string | null; status: string };

function Admin() {
  const [people, setPeople] = useState<P[]>([]);
  const [courses, setCourses] = useState<C[]>([]);
  const [subs, setSubs] = useState<S[]>([]);
  const [titles, setTitles] = useState<Record<string, string>>({});
  const [enr, setEnr] = useState<Record<string, string[]>>({});
  const [msg, setMsg] = useState('');
  const [locked, setLocked] = useState<{ user_id: string; item_id: string; best: number }[]>([]);

  const load = useCallback(async () => {
    const sb = supabase();
    const [p, c, s, e, it, qa] = await Promise.all([
      sb.from('profiles').select('*').order('created_at', { ascending: false }),
      sb.from('courses').select('id,title,slug').order('title'),
      sb.from('submissions').select('*').eq('status', 'submitted').order('created_at'),
      sb.from('enrollments').select('user_id, course_id').neq('status', 'withdrawn'),
      sb.from('course_items').select('id,title'),
      sb.from('quiz_attempts').select('user_id,item_id,score,passed').eq('voided', false),
    ]);
    const g: Record<string, { user_id: string; item_id: string; n: number; best: number; passed: boolean }> = {};
    (qa.data || []).forEach((r: any) => { const k = r.user_id + r.item_id; const x = (g[k] ||= { user_id: r.user_id, item_id: r.item_id, n: 0, best: 0, passed: false }); x.n++; x.best = Math.max(x.best, r.score); x.passed = x.passed || r.passed; });
    setLocked(Object.values(g).filter((x) => x.n >= 3 && !x.passed).map((x) => ({ user_id: x.user_id, item_id: x.item_id, best: x.best })));
    setPeople((p.data || []) as P[]); setCourses((c.data || []) as C[]); setSubs((s.data || []) as S[]);
    const m: Record<string, string[]> = {}; (e.data || []).forEach((r: any) => { (m[r.user_id] ||= []).push(r.course_id); }); setEnr(m);
    const t: Record<string, string> = {}; (it.data || []).forEach((r: any) => { t[r.id] = r.title; }); setTitles(t);
  }, []);
  useEffect(() => { load(); }, [load]);

  async function saveProfile(p: P, name: string, sid: string, grade: string) {
    const { error } = await supabase().from('profiles').update({ full_name: name, student_id: sid.trim() || null, grade_level: grade ? Number(grade) : null }).eq('id', p.id);
    setMsg(error ? `Could not save: ${error.message}` : 'Saved.'); load();
  }
  async function enroll(userId: string, courseId: string) {
    if (!courseId) return;
    const { error } = await supabase().from('enrollments').upsert({ user_id: userId, course_id: courseId, status: 'active' });
    setMsg(error ? `Could not enroll: ${error.message}` : 'Enrolled. Open the course from the link under the student, or from the Dashboard.'); load();
  }
  async function unlock(userId: string, itemId: string) {
    const { error } = await supabase().rpc('admin_reset_attempts', { p_user: userId, p_item: itemId });
    setMsg(error ? `Could not reset: ${error.message}` : 'Three more attempts given.'); load();
  }
  async function grade(s: S, score: string, feedback: string) {
    const n = Number(score);
    if (!Number.isFinite(n) || n < 0 || n > 100) { setMsg('Enter a score from 0 to 100.'); return; }
    const { error } = await supabase().from('submissions').update({ score: n, feedback, status: 'graded', graded_at: new Date().toISOString() }).eq('id', s.id);
    setMsg(error ? `Could not save: ${error.message}` : 'Graded.'); load();
  }
  const name = (id: string) => people.find((p) => p.id === id)?.full_name || people.find((p) => p.id === id)?.email || id;

  return (
    <>
      <h1 className="p-h1">Administration</h1>
      {msg && <p className="p-note">{msg}</p>}
      <h2 className="p-h2">Work to review ({subs.length})</h2>
      {subs.length === 0 && <p className="p-muted">Nothing waiting for review.</p>}
      {subs.map((s) => <Grader key={s.id} s={s} who={name(s.user_id)} title={titles[s.item_id] || ''} onGrade={grade} />)}
      <h2 className="p-h2">Quizzes locked after 3 attempts ({locked.length})</h2>
      {locked.length === 0 && <p className="p-muted">No student is locked out of a quiz.</p>}
      {locked.map((l) => (
        <div key={l.user_id + l.item_id} className="p-card">
          <p><b>{name(l.user_id)}</b>: {titles[l.item_id] || 'Quiz'} (best score {l.best})</p>
          <button className="p-btn" onClick={() => unlock(l.user_id, l.item_id)}>Give 3 more attempts</button>
        </div>
      ))}
      <h2 className="p-h2">Students and staff ({people.length})</h2>
      <AddStudent onDone={(m) => { setMsg(m); load(); }} />
      {people.map((p) => <Person key={p.id} p={p} courses={courses} enrolled={enr[p.id] || []} onSave={saveProfile} onEnroll={enroll} />)}
    </>
  );
}

function AddStudent({ onDone }: { onDone: (m: string) => void }) {
  const [f, setF] = useState({ name: '', email: '', password: '', studentId: '', gradeLevel: '' });
  const [busy, setBusy] = useState(false);
  const [open, setOpen] = useState(false);
  async function go() {
    setBusy(true);
    const { data } = await supabase().auth.getSession();
    const r = await fetch('/api/admin/students', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${data.session?.access_token}` }, body: JSON.stringify(f) });
    const j = await r.json().catch(() => ({}));
    if (r.ok) { onDone(j.warning || `Student account created for ${f.name}. Share the email and temporary password with the student.`); setF({ name: '', email: '', password: '', studentId: '', gradeLevel: '' }); }
    else onDone(j.error || 'Could not create the account.');
    setBusy(false);
  }
  if (!open) return <button className="p-btn" onClick={() => setOpen(true)}>Add a student</button>;
  return (
    <div className="p-card">
      <h3>Add a student</h3>
      <div className="p-row"><input placeholder="Full name" value={f.name} onChange={(e) => setF({ ...f, name: e.target.value })} /><input placeholder="Email" value={f.email} onChange={(e) => setF({ ...f, email: e.target.value })} /></div>
      <div className="p-row"><input placeholder="Temporary password (8 or more)" value={f.password} onChange={(e) => setF({ ...f, password: e.target.value })} /><input placeholder="Student ID NLPA-2026-001" value={f.studentId} onChange={(e) => setF({ ...f, studentId: e.target.value })} /></div>
      <div className="p-row"><select value={f.gradeLevel} onChange={(e) => setF({ ...f, gradeLevel: e.target.value })}><option value="">Grade level</option><option value="9">9th Grade</option><option value="10">10th Grade</option><option value="11">11th Grade</option><option value="12">12th Grade</option></select></div>
      <div className="p-row"><button className="p-btn" onClick={go} disabled={busy}>{busy ? 'Creating...' : 'Create Student'}</button><button className="p-link" onClick={() => setOpen(false)}>Cancel</button></div>
    </div>
  );
}

function Grader({ s, who, title, onGrade }: { s: S; who: string; title: string; onGrade: (s: S, score: string, fb: string) => void }) {
  const [score, setScore] = useState(''); const [fb, setFb] = useState('');
  return (
    <div className="p-card">
      <p className="p-small"><b>{who}</b> · {title} · {new Date(s.created_at).toLocaleString()}</p>
      <p className="p-pre">{s.body}</p>
      <div className="p-row"><input placeholder="Score 0 to 100" value={score} onChange={(e) => setScore(e.target.value)} /><input placeholder="Feedback" value={fb} onChange={(e) => setFb(e.target.value)} /><button className="p-btn" onClick={() => onGrade(s, score, fb)}>Save Grade</button></div>
    </div>
  );
}

function Person({ p, courses, enrolled, onSave, onEnroll }: { p: P; courses: C[]; enrolled: string[]; onSave: (p: P, n: string, s: string, g: string) => void; onEnroll: (u: string, c: string) => void }) {
  const [n, setN] = useState(p.full_name || ''); const [sid, setSid] = useState(p.student_id || ''); const [c, setC] = useState(''); const [g, setG] = useState(p.grade_level ? String(p.grade_level) : '');
  return (
    <div className="p-card">
      <p className="p-small">{p.email} · {p.role}</p>
      <div className="p-row"><input placeholder="Full name" value={n} onChange={(e) => setN(e.target.value)} /><input placeholder="NLPA-2026-001" value={sid} onChange={(e) => setSid(e.target.value)} /><select value={g} onChange={(e) => setG(e.target.value)}><option value="">Grade level</option><option value="9">9th Grade</option><option value="10">10th Grade</option><option value="11">11th Grade</option><option value="12">12th Grade</option></select><button className="p-btn" onClick={() => onSave(p, n, sid, g)}>Save</button></div>
      <div className="p-row">
        <select value={c} onChange={(e) => setC(e.target.value)}><option value="">Enroll in a course</option>{courses.map((x) => <option key={x.id} value={x.id}>{x.title}</option>)}</select>
        <button className="p-btn" onClick={() => onEnroll(p.id, c)} disabled={!c}>Enroll</button>
      </div>
      {enrolled.length > 0 && <p className="p-small">Enrolled: {enrolled.map((id) => courses.find((x) => x.id === id)).filter(Boolean).map((x) => <a key={x!.id} href={`/portal/courses/${x!.slug}`} style={{ marginRight: 12 }}>{x!.title}</a>)}</p>}
    </div>
  );
}

export default function Page() { return <PortalFrame adminOnly>{() => <Admin />}</PortalFrame>; }
