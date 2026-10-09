'use client';
import { useCallback, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';

type P = { id: string; email: string | null; full_name: string | null; student_id: string | null; role: string };
type C = { id: string; title: string; slug: string };
type S = { id: string; body: string; created_at: string; user_id: string; item_id: string; score: number | null; feedback: string | null; status: string };

function Admin() {
  const [people, setPeople] = useState<P[]>([]);
  const [courses, setCourses] = useState<C[]>([]);
  const [subs, setSubs] = useState<S[]>([]);
  const [titles, setTitles] = useState<Record<string, string>>({});
  const [enr, setEnr] = useState<Record<string, string[]>>({});
  const [msg, setMsg] = useState('');

  const load = useCallback(async () => {
    const sb = supabase();
    const [p, c, s, e, it] = await Promise.all([
      sb.from('profiles').select('*').order('created_at', { ascending: false }),
      sb.from('courses').select('id,title,slug').order('title'),
      sb.from('submissions').select('*').eq('status', 'submitted').order('created_at'),
      sb.from('enrollments').select('user_id, course_id').neq('status', 'withdrawn'),
      sb.from('course_items').select('id,title'),
    ]);
    setPeople((p.data || []) as P[]); setCourses((c.data || []) as C[]); setSubs((s.data || []) as S[]);
    const m: Record<string, string[]> = {}; (e.data || []).forEach((r: any) => { (m[r.user_id] ||= []).push(r.course_id); }); setEnr(m);
    const t: Record<string, string> = {}; (it.data || []).forEach((r: any) => { t[r.id] = r.title; }); setTitles(t);
  }, []);
  useEffect(() => { load(); }, [load]);

  async function saveProfile(p: P, name: string, sid: string) {
    const { error } = await supabase().from('profiles').update({ full_name: name, student_id: sid.trim() || null }).eq('id', p.id);
    setMsg(error ? `Could not save: ${error.message}` : 'Saved.'); load();
  }
  async function enroll(userId: string, courseId: string) {
    if (!courseId) return;
    const { error } = await supabase().from('enrollments').upsert({ user_id: userId, course_id: courseId, status: 'active' });
    setMsg(error ? `Could not enroll: ${error.message}` : 'Enrolled.'); load();
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
      <h2 className="p-h2">Students and staff ({people.length})</h2>
      <p className="p-small">To add a student: Supabase, Authentication, Users, Add user. They appear here automatically. Then set their name and Student ID (NLPA-20XX-XXX) and enroll them.</p>
      {people.map((p) => <Person key={p.id} p={p} courses={courses} enrolled={enr[p.id] || []} onSave={saveProfile} onEnroll={enroll} />)}
    </>
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

function Person({ p, courses, enrolled, onSave, onEnroll }: { p: P; courses: C[]; enrolled: string[]; onSave: (p: P, n: string, s: string) => void; onEnroll: (u: string, c: string) => void }) {
  const [n, setN] = useState(p.full_name || ''); const [sid, setSid] = useState(p.student_id || ''); const [c, setC] = useState('');
  return (
    <div className="p-card">
      <p className="p-small">{p.email} · {p.role}</p>
      <div className="p-row"><input placeholder="Full name" value={n} onChange={(e) => setN(e.target.value)} /><input placeholder="NLPA-2026-001" value={sid} onChange={(e) => setSid(e.target.value)} /><button className="p-btn" onClick={() => onSave(p, n, sid)}>Save</button></div>
      <div className="p-row">
        <select value={c} onChange={(e) => setC(e.target.value)}><option value="">Enroll in a course</option>{courses.map((x) => <option key={x.id} value={x.id}>{x.title}</option>)}</select>
        <button className="p-btn" onClick={() => onEnroll(p.id, c)} disabled={!c}>Enroll</button>
      </div>
      {enrolled.length > 0 && <p className="p-small">Enrolled: {enrolled.map((id) => courses.find((x) => x.id === id)?.title).filter(Boolean).join(', ')}</p>}
    </div>
  );
}

export default function Page() { return <PortalFrame adminOnly>{() => <Admin />}</PortalFrame>; }
