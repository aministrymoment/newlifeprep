'use client';
import { useCallback, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';
import { AVERY_NUMBERS } from '@/lib/avery';

type P = { id: string; email: string | null; full_name: string | null; student_id: string | null; grade_level?: number | null; role: string };
type C = { id: string; title: string; slug: string };
type Q = { id: string; created_at: string; name: string; email: string; phone: string | null; program: string | null; message: string; status: string; emailed: boolean; street: string | null; city: string | null; state: string | null; zip: string | null };
type Pay = { id: string; created_at: string; receipt_no: string | null; label: string | null; item: string; amount_cents: number; payer_name: string | null; payer_email: string | null; reference: string | null; status: string; refunded_cents: number };
type S = { id: string; body: string; created_at: string; user_id: string; item_id: string; score: number | null; feedback: string | null; status: string };

function Admin() {
  const [people, setPeople] = useState<P[]>([]);
  const [courses, setCourses] = useState<C[]>([]);
  const [subs, setSubs] = useState<S[]>([]);
  const [titles, setTitles] = useState<Record<string, string>>({});
  const [enr, setEnr] = useState<Record<string, string[]>>({});
  const [msg, setMsg] = useState('');
  const [inq, setInq] = useState<Q[]>([]);
  const [pays, setPays] = useState<Pay[]>([]);
  const [pick, setPick] = useState<string[]>([]);
  const [avery, setAvery] = useState('5160');
  const [startAt, setStartAt] = useState('1');
  const [locked, setLocked] = useState<{ user_id: string; item_id: string; best: number }[]>([]);

  const load = useCallback(async () => {
    const sb = supabase();
    const [p, c, s, e, it, qa, iq, py] = await Promise.all([
      sb.from('profiles').select('*').order('created_at', { ascending: false }),
      sb.from('courses').select('id,title,slug').order('title'),
      sb.from('submissions').select('*').eq('status', 'submitted').order('created_at'),
      sb.from('enrollments').select('user_id, course_id').neq('status', 'withdrawn'),
      sb.from('course_items').select('id,title'),
      sb.from('quiz_attempts').select('user_id,item_id,score,passed').eq('voided', false),
      sb.from('inquiries').select('*').order('created_at', { ascending: false }).limit(100),
      sb.from('payments').select('*').order('created_at', { ascending: false }).limit(200),
    ]);
    setInq((iq.data || []) as Q[]);
    setPays((py.data || []) as Pay[]);
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
  async function removeStudent(p: P) {
    const who = p.full_name || p.email || 'this student';
    if (!window.confirm(`Delete ${who}? This permanently removes the login, enrollments, quiz attempts and submitted work. It cannot be undone.`)) return;
    const { data } = await supabase().auth.getSession();
    const r = await fetch('/api/admin/students', { method: 'DELETE', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${data.session?.access_token}` }, body: JSON.stringify({ userId: p.id }) });
    const j = await r.json().catch(() => ({}));
    setMsg(r.ok ? `${who} was deleted.` : j.error || 'Could not delete the account.'); load();
  }
  async function removeCourse(c: C) {
    const typed = window.prompt(`Deleting "${c.title}" permanently removes the course, all of its lessons and quizzes, and every student's progress in it.\n\nType the course name exactly to confirm:`);
    if (typed === null) return;
    if (typed.trim() !== c.title) { setMsg('The name did not match, so nothing was deleted.'); return; }
    const { error } = await supabase().from('courses').delete().eq('id', c.id);
    setMsg(error ? `Could not delete the course: ${error.message}` : `${c.title} was deleted.`); load();
  }
  const hasAddr = (q: Q) => !!(q.street && (q.city || q.zip));
  function toggle(id: string) { setPick((p) => (p.includes(id) ? p.filter((x) => x !== id) : [...p, id])); }
  function csvCell(v: unknown) { const t = String(v ?? '').replace(/"/g, '""'); return `"${t}"`; }
  function downloadCsv() {
    const head = ['Date', 'Name', 'Email', 'Phone', 'Program', 'Street', 'City', 'State', 'ZIP', 'Message', 'Status'];
    const lines = inq.map((q) => [new Date(q.created_at).toLocaleString(), q.name, q.email, q.phone, q.program, q.street, q.city, q.state, q.zip, q.message, q.status].map(csvCell).join(','));
    const blob = new Blob(['\uFEFF' + [head.map(csvCell).join(','), ...lines].join('\r\n')], { type: 'text/csv;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `NLPA website messages ${new Date().toISOString().slice(0, 10)}.csv`;
    a.click(); URL.revokeObjectURL(a.href);
  }
  const money = (c: number) => `$${(c / 100).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  function downloadPayCsv() {
    const head = ['Receipt', 'Date', 'Payer', 'Email', 'Item', 'Reference', 'Amount', 'Refunded', 'Status'];
    const lines = pays.map((x) => [x.receipt_no, new Date(x.created_at).toLocaleString(), x.payer_name, x.payer_email, x.label || x.item, x.reference, (x.amount_cents / 100).toFixed(2), (x.refunded_cents / 100).toFixed(2), x.status].map(csvCell).join(','));
    const blob = new Blob(['\uFEFF' + [head.map(csvCell).join(','), ...lines].join('\r\n')], { type: 'text/csv;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `NLPA payments ${new Date().toISOString().slice(0, 10)}.csv`;
    a.click(); URL.revokeObjectURL(a.href);
  }
  function printLabels() {
    const chosen = inq.filter((q) => pick.includes(q.id) && hasAddr(q)).map((q) => q.id);
    if (!chosen.length) { setMsg('Tick at least one message that has a mailing address.'); return; }
    window.open(`/portal/admin/labels?avery=${encodeURIComponent(avery)}&start=${encodeURIComponent(startAt || '1')}&ids=${chosen.join(',')}`, '_blank');
  }
  async function inquiryStatus(q: Q, status: string) {
    const { error } = await supabase().from('inquiries').update({ status }).eq('id', q.id);
    setMsg(error ? `Could not update: ${error.message}` : status === 'handled' ? 'Marked as handled.' : 'Marked as new.'); load();
  }
  async function inquiryDelete(q: Q) {
    if (!window.confirm(`Delete the message from ${q.name}? This cannot be undone.`)) return;
    const { error } = await supabase().from('inquiries').delete().eq('id', q.id);
    setMsg(error ? `Could not delete: ${error.message}` : 'Message deleted.'); load();
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
      <div className="p-card"><div className="p-row"><b>Transcript Generator</b><a className="p-btn" href="/portal/admin/transcripts">Open the transcript generator</a></div><p className="p-small">Enter a student's real record and download a one page official transcript.</p></div>
      <h2 className="p-h2">Work to review ({subs.length})</h2>
      {subs.length === 0 && <p className="p-muted">Nothing waiting for review.</p>}
      {subs.map((s) => <Grader key={s.id} s={s} who={name(s.user_id)} title={titles[s.item_id] || ''} onGrade={grade} />)}
      <h2 className="p-h2">Website messages ({inq.filter((q) => q.status === 'new').length} new)</h2>
      {inq.length === 0 && <p className="p-muted">No website messages yet.</p>}
      {inq.length > 0 && (
        <div className="p-card">
          <div className="p-row">
            <button className="p-btn" onClick={downloadCsv}>Download spreadsheet</button>
            <button className="p-link" onClick={() => setPick(inq.filter(hasAddr).map((q) => q.id))}>Select all with an address</button>
            <button className="p-link" onClick={() => setPick([])}>Clear selection</button>
          </div>
          <div className="p-row">
            <label>Avery label number<select value={avery} onChange={(e) => setAvery(e.target.value)}>{AVERY_NUMBERS.map((n) => <option key={n} value={n}>{n}</option>)}</select></label>
            <label>Start at label<input type="number" min={1} value={startAt} onChange={(e) => setStartAt(e.target.value)} /></label>
            <button className="p-btn" onClick={printLabels}>Print labels for selected ({inq.filter((q) => pick.includes(q.id) && hasAddr(q)).length})</button>
          </div>
          <p className="p-small">Only messages with a mailing address can be printed. Use Start at label to reuse a sheet that has already been partly used. Print a test on plain paper first.</p>
        </div>
      )}
      {inq.map((q) => (
        <div key={q.id} className="p-card" style={q.status === 'handled' ? { opacity: 0.6 } : undefined}>
          <label style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}><input type="checkbox" checked={pick.includes(q.id)} onChange={() => toggle(q.id)} disabled={!hasAddr(q)} />{hasAddr(q) ? 'Select for labels' : 'No mailing address'}</label>
          <p className="p-small"><b>{q.name}</b> · <a href={`mailto:${q.email}`}>{q.email}</a>{q.phone ? ` · ${q.phone}` : ''}{q.program ? ` · ${q.program}` : ''} · {new Date(q.created_at).toLocaleString()} · {q.status === 'new' ? 'New' : 'Handled'}{q.emailed ? '' : ' · Email did not send'}</p>
          {hasAddr(q) && <p className="p-small">Mail to: {q.street}, {q.city} {q.state} {q.zip}</p>}
          <p className="p-pre">{q.message}</p>
          <div className="p-row">
            {q.status === 'new' ? <button className="p-btn" onClick={() => inquiryStatus(q, 'handled')}>Mark handled</button> : <button className="p-btn" onClick={() => inquiryStatus(q, 'new')}>Mark as new</button>}
            <button className="p-danger" onClick={() => inquiryDelete(q)}>Delete</button>
          </div>
        </div>
      ))}
      <h2 className="p-h2">Payments ({pays.length})</h2>
      {pays.length === 0 && <p className="p-muted">No online payments recorded yet. Payments appear here after the Stripe webhook is connected.</p>}
      {pays.length > 0 && (
        <div className="p-card">
          <p><b>Net received: {money(pays.reduce((a, x) => a + x.amount_cents - x.refunded_cents, 0))}</b> across {pays.length} payment{pays.length === 1 ? '' : 's'}</p>
          <button className="p-btn" onClick={downloadPayCsv}>Download spreadsheet</button>
        </div>
      )}
      {pays.map((x) => (
        <div key={x.id} className="p-card">
          <p><b>{x.receipt_no}</b> · {new Date(x.created_at).toLocaleString()} · {money(x.amount_cents)}{x.refunded_cents ? ` (refunded ${money(x.refunded_cents)})` : ''} · {x.status === 'paid' ? 'Paid' : x.status === 'refunded' ? 'Refunded' : 'Partly refunded'}</p>
          <p className="p-small">{x.payer_name || 'Unnamed'}{x.payer_email ? ` · ${x.payer_email}` : ''} · {x.label || x.item}{x.reference ? ` · ${x.reference}` : ''}</p>
        </div>
      ))}
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
      {people.map((p) => <Person key={p.id} p={p} courses={courses} enrolled={enr[p.id] || []} onSave={saveProfile} onEnroll={enroll} onDelete={removeStudent} />)}
      <h2 className="p-h2">Courses ({courses.length})</h2>
      {courses.map((c) => (
        <div key={c.id} className="p-card"><div className="p-row"><p><b>{c.title}</b></p><button className="p-danger" onClick={() => removeCourse(c)}>Delete course</button></div></div>
      ))}
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

function Person({ p, courses, enrolled, onSave, onEnroll, onDelete }: { p: P; courses: C[]; enrolled: string[]; onSave: (p: P, n: string, s: string, g: string) => void; onEnroll: (u: string, c: string) => void; onDelete: (p: P) => void }) {
  const [n, setN] = useState(p.full_name || ''); const [sid, setSid] = useState(p.student_id || ''); const [c, setC] = useState(''); const [g, setG] = useState(p.grade_level ? String(p.grade_level) : '');
  return (
    <div className="p-card">
      <p className="p-small">{p.email} · {p.role}</p>
      <div className="p-row"><input placeholder="Full name" value={n} onChange={(e) => setN(e.target.value)} /><input placeholder="NLPA-2026-001" value={sid} onChange={(e) => setSid(e.target.value)} /><select value={g} onChange={(e) => setG(e.target.value)}><option value="">Grade level</option><option value="9">9th Grade</option><option value="10">10th Grade</option><option value="11">11th Grade</option><option value="12">12th Grade</option></select><button className="p-btn" onClick={() => onSave(p, n, sid, g)}>Save</button></div>
      <div className="p-row">
        <select value={c} onChange={(e) => setC(e.target.value)}><option value="">Enroll in a course</option>{courses.map((x) => <option key={x.id} value={x.id}>{x.title}</option>)}</select>
        <button className="p-btn" onClick={() => onEnroll(p.id, c)} disabled={!c}>Enroll</button>
      </div>
      {p.role !== 'admin' && <div className="p-row"><button className="p-danger" onClick={() => onDelete(p)}>Delete student</button></div>}
      {enrolled.length > 0 && <p className="p-small">Enrolled: {enrolled.map((id) => courses.find((x) => x.id === id)).filter(Boolean).map((x) => <a key={x!.id} href={`/portal/courses/${x!.slug}`} style={{ marginRight: 12 }}>{x!.title}</a>)}</p>}
    </div>
  );
}

export default function Page() { return <PortalFrame adminOnly>{() => <Admin />}</PortalFrame>; }
