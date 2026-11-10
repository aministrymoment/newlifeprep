'use client';
import { useCallback, useEffect, useMemo, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { AREAS, ALL_NLPA_TITLES, REQUIRED, TOTAL_NEEDED, buildPlan, type Area, type TCourse, type TStatus } from '@/lib/graduation';

type Person = { id: string; email: string | null; full_name: string | null; student_id: string | null; grade_level: number | null };
type Saved = { id: string; created_at: string; user_id: string | null; applicant_name: string | null; entering_grade: number; count_in_progress: boolean; courses: TCourse[]; notes: string | null };
const uid = () => Math.random().toString(36).slice(2, 10);

export default function TranscriptPlanner({ people, credit }: { people: Person[]; credit: (t: string) => number }) {
  const [name, setName] = useState('');
  const [link, setLink] = useState('');
  const [grade, setGrade] = useState(9);
  const [countIP, setCountIP] = useState(true);
  const [courses, setCourses] = useState<TCourse[]>([]);
  const [notes, setNotes] = useState('');
  const [text, setText] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState('');
  const [saved, setSaved] = useState<Saved[]>([]);

  const loadSaved = useCallback(async () => {
    const { data } = await supabase().from('graduation_plans').select('*').order('created_at', { ascending: false }).limit(50);
    setSaved((data || []) as Saved[]);
  }, []);
  useEffect(() => { loadSaved(); }, [loadSaved]);

  const read = async () => {
    setMsg(''); if (!file && !text.trim()) { setMsg('Choose a transcript file or paste its text first.'); return; }
    setBusy(true);
    try {
      const body: any = { text };
      if (file) {
        if (file.size > 3 * 1024 * 1024) throw new Error('That file is larger than 3 MB. Use a smaller file or paste the text.');
        const buf = new Uint8Array(await file.arrayBuffer()); let bin = '';
        for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode(...buf.subarray(i, i + 0x8000));
        body.data = btoa(bin); body.mime = file.type || (file.name.toLowerCase().endsWith('.pdf') ? 'application/pdf' : '');
      }
      const { data: s } = await supabase().auth.getSession();
      const r = await fetch('/api/admin/transcript-read', { method: 'POST', headers: { 'content-type': 'application/json', authorization: `Bearer ${s.session?.access_token}` }, body: JSON.stringify(body) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.error || 'The transcript could not be read.');
      setCourses(j.courses.map((c: any) => ({ ...c, id: uid() })));
      if (j.studentName && !name) setName(j.studentName);
      setNotes([j.school ? `Previous school: ${j.school}.` : '', j.notes].filter(Boolean).join(' '));
      setMsg(`Read ${j.courses.length} courses. Please check each line before relying on the plan.`);
    } catch (e: any) { setMsg(e.message || 'The transcript could not be read.'); }
    setBusy(false);
  };

  const edit = (id: string, patch: Partial<TCourse>) => setCourses((cs) => cs.map((c) => (c.id === id ? { ...c, ...patch } : c)));
  const addRow = () => setCourses((cs) => [...cs, { id: uid(), title: '', credits: 1, area: 'Electives', match: null, status: 'completed' }]);
  const result = useMemo(() => buildPlan(courses.filter((c) => c.title.trim()), grade, countIP, credit), [courses, grade, countIP, credit]);

  const save = async () => {
    if (!name.trim()) { setMsg('Enter the applicant name before saving.'); return; }
    const { error } = await supabase().from('graduation_plans').insert({ user_id: link || null, applicant_name: name.trim(), entering_grade: grade, count_in_progress: countIP, courses, notes });
    setMsg(error ? 'Could not save the plan.' : 'Plan saved.'); if (!error) loadSaved();
  };
  const open = (p: Saved) => { setName(p.applicant_name || ''); setLink(p.user_id || ''); setGrade(p.entering_grade); setCountIP(p.count_in_progress); setCourses((p.courses || []).map((c) => ({ ...c, id: c.id || uid() }))); setNotes(p.notes || ''); setMsg('Plan opened.'); window.scrollTo({ top: 0, behavior: 'smooth' }); };
  const del = async (id: string) => { if (!confirm('Delete this saved plan?')) return; await supabase().from('graduation_plans').delete().eq('id', id); loadSaved(); };
  const pickPerson = (id: string) => { setLink(id); const p = people.find((x) => x.id === id); if (p) { if (!name) setName(p.full_name || p.email || ''); } };

  return (
    <>
      <h2 className="p-h2 no-print">Transcript to Graduation Plan</h2>
      <div className="p-card no-print">
        <p className="p-small">Upload an incoming transcript (PDF, PNG or JPG, up to 3 MB) or paste its text. Claude reads it into a course list you can correct, then the page builds what the student still needs at New Life Preparatory Academy. The file is sent to Claude to be read and is not kept. Only the course list is saved if you press Save.</p>
        <div className="p-row">
          <input type="file" accept="application/pdf,image/png,image/jpeg,image/webp" onChange={(e) => setFile(e.target.files?.[0] || null)} />
        </div>
        <textarea rows={4} style={{ width: '100%' }} placeholder="Or paste the transcript text here" value={text} onChange={(e) => setText(e.target.value)} />
        <div className="p-row">
          <button className="p-btn" disabled={busy} onClick={read}>{busy ? 'Reading, please wait…' : 'Read transcript'}</button>
          <button className="p-btn" onClick={addRow}>Add a course by hand</button>
        </div>
      </div>
      {msg && <p className="p-note no-print">{msg}</p>}

      <div className="p-card">
        <h3>Applicant</h3>
        <div className="p-row no-print">
          <input placeholder="Applicant name" value={name} onChange={(e) => setName(e.target.value)} />
          <select value={link} onChange={(e) => pickPerson(e.target.value)}>
            <option value="">Not linked to a student account</option>
            {people.map((x) => <option key={x.id} value={x.id}>{x.full_name || x.email}</option>)}
          </select>
          <label>Entering grade <select value={grade} onChange={(e) => setGrade(Number(e.target.value))}>{[9, 10, 11, 12].map((g) => <option key={g} value={g}>{g}</option>)}</select></label>
          <label><input type="checkbox" checked={countIP} onChange={(e) => setCountIP(e.target.checked)} /> Count courses in progress</label>
        </div>
        <p className="p-small">{name || 'Applicant'} · Entering Grade {grade}</p>
        {notes && <p className="p-small">Reader notes: {notes}</p>}
      </div>

      {courses.length > 0 && (
        <>
          <h2 className="p-h2">Courses on the transcript</h2>
          <div className="p-card" style={{ overflowX: 'auto' }}>
            <table className="p-table">
              <thead><tr><th>Course</th><th>Credits</th><th>Grade</th><th>Status</th><th>Counts toward</th><th>NLPA course it covers</th><th className="no-print"></th></tr></thead>
              <tbody>
                {courses.map((c) => (
                  <tr key={c.id}>
                    <td><input value={c.title} onChange={(e) => edit(c.id, { title: e.target.value })} /></td>
                    <td><input type="number" step="0.5" min="0" max="4" style={{ width: 64 }} value={c.credits} onChange={(e) => edit(c.id, { credits: Number(e.target.value) || 0 })} /></td>
                    <td>{c.grade || ''}</td>
                    <td><select value={c.status} onChange={(e) => edit(c.id, { status: e.target.value as TStatus })}><option value="completed">Completed</option><option value="in_progress">In progress</option><option value="failed">Failed</option></select></td>
                    <td><select value={c.area} onChange={(e) => edit(c.id, { area: e.target.value as Area })}>{AREAS.map((a) => <option key={a}>{a}</option>)}</select></td>
                    <td><select value={c.match || ''} onChange={(e) => edit(c.id, { match: e.target.value || null })}><option value="">None</option>{ALL_NLPA_TITLES.map((t) => <option key={t}>{t}</option>)}</select></td>
                    <td className="no-print"><button className="p-link p-danger" onClick={() => setCourses((cs) => cs.filter((x) => x.id !== c.id))}>Remove</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <h2 className="p-h2">Graduation requirements status</h2>
          <div className="p-card">
            <table className="p-table">
              <thead><tr><th>Subject area</th><th>Required</th><th>Counted so far</th><th>Still needed</th></tr></thead>
              <tbody>
                {REQUIRED.map((r) => { const got = result.counted[r.area] || 0; return <tr key={r.area}><td>{r.area}</td><td>{r.need.toFixed(1)}</td><td>{got.toFixed(1)}</td><td>{Math.max(0, r.need - got).toFixed(1)}</td></tr>; })}
                <tr><td><b>Total</b></td><td><b>{TOTAL_NEEDED.toFixed(1)}</b></td><td><b>{result.rawEarned.toFixed(1)} earned</b></td><td><b>{Math.max(0, TOTAL_NEEDED - result.rawEarned).toFixed(1)}</b></td></tr>
              </tbody>
            </table>
          </div>

          <h2 className="p-h2">Plan at New Life Preparatory Academy</h2>
          {result.years.map((y) => (
            <div key={y.grade} className="p-card">
              <h3>Grade {y.grade} ({y.credits.toFixed(1)} credits)</h3>
              {y.items.length === 0 ? <p className="p-small">No new courses planned.</p> : (
                <table className="p-table">
                  <thead><tr><th>Course</th><th>Credits</th><th>Counts toward</th><th>Why</th></tr></thead>
                  <tbody>{y.items.map((i) => <tr key={i.title}><td>{i.title}{i.doubled ? ' (doubled up)' : ''}</td><td>{i.credits.toFixed(1)}</td><td>{i.area}</td><td>{i.reason}</td></tr>)}</tbody>
                </table>
              )}
            </div>
          ))}
          <p><b>Projected total: {result.finalTotal.toFixed(1)} credits</b> of {TOTAL_NEEDED}.</p>
          {result.flags.length > 0 && <div className="p-card"><h3>For Dr. Jenkins to review</h3><ul>{result.flags.map((f, i) => <li key={i}>{f}</li>)}</ul></div>}
          <p className="p-small">This plan is a recommendation built from an unofficial reading of the transcript. Verify the original transcript. Dr. Jenkins decides credit acceptance and each schedule.</p>
          <div className="p-row no-print">
            <button className="p-btn" onClick={save}>Save plan</button>
            <button className="p-btn" onClick={() => { window.print(); }}>Print plan</button>
          </div>
        </>
      )}

      {saved.length > 0 && (
        <div className="no-print">
          <h2 className="p-h2">Saved plans</h2>
          <div className="p-card">
            <table className="p-table">
              <thead><tr><th>Applicant</th><th>Entering</th><th>Saved</th><th></th></tr></thead>
              <tbody>{saved.map((p) => (
                <tr key={p.id}><td>{p.applicant_name}</td><td>Grade {p.entering_grade}</td><td>{new Date(p.created_at).toLocaleDateString()}</td>
                  <td><button className="p-link" onClick={() => open(p)}>Open</button> <button className="p-link p-danger" onClick={() => del(p.id)}>Delete</button></td></tr>
              ))}</tbody>
            </table>
          </div>
        </div>
      )}
    </>
  );
}
