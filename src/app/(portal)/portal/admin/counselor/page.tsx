'use client';
import { useCallback, useEffect, useMemo, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';
import TranscriptPlanner from '@/components/portal/TranscriptPlanner';
import { PLAN, ALTERNATES, REQUIRED, areaOf, PFL_STATE_CREDIT } from '@/lib/graduation';

type Course = { id: string; title: string; slug: string; subject: string | null; credits: number | string | null };
type Person = { id: string; email: string | null; full_name: string | null; student_id: string | null; grade_level: number | null; role: string };

function Counselor() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [people, setPeople] = useState<Person[]>([]);
  const [enr, setEnr] = useState<Record<string, string[]>>({});
  const [who, setWho] = useState('');

  const load = useCallback(async () => {
    const sb = supabase();
    const [c, p, e] = await Promise.all([
      sb.from('courses').select('id,title,slug,subject,credits').order('title'),
      sb.from('profiles').select('id,email,full_name,student_id,grade_level,role').order('full_name'),
      sb.from('enrollments').select('user_id, course_id').neq('status', 'withdrawn'),
    ]);
    setCourses((c.data || []) as Course[]);
    setPeople(((p.data || []) as Person[]).filter((x) => x.role !== 'admin'));
    const m: Record<string, string[]> = {};
    (e.data || []).forEach((r: any) => { (m[r.user_id] ||= []).push(r.course_id); });
    setEnr(m);
  }, []);
  useEffect(() => { load(); }, [load]);

  const byTitle = useMemo(() => new Map(courses.map((c) => [c.title, c])), [courses]);
  const credit = (t: string) => Number(byTitle.get(t)?.credits ?? 0);
  const student = people.find((x) => x.id === who);
  const enrolledIds = new Set(student ? enr[student.id] || [] : []);
  const isEnrolled = (t: string) => { const c = byTitle.get(t); return !!c && enrolledIds.has(c.id); };

  const planTotal = (g: number) => PLAN[g].reduce((a, t) => a + credit(t), 0);
  const grandTotal = [9, 10, 11, 12].reduce((a, g) => a + planTotal(g), 0);
  const allPlanned = [9, 10, 11, 12].flatMap((g) => PLAN[g]);
  // Personal Finance and Stewardship is 1.0 here. Only 0.5 is reserved for the Florida requirement; the other 0.5 counts toward electives, provisionally.
  const sumArea = (titles: string[], area: string) => titles.filter((t) => areaOf(t) === area).reduce((a, t) => a + credit(t), 0);
  const byArea = (titles: string[], area: string) => {
    const pfl = sumArea(titles, 'Personal Financial Literacy');
    if (area === 'Personal Financial Literacy') return Math.min(pfl, PFL_STATE_CREDIT);
    if (area === 'Electives') return sumArea(titles, 'Electives') + Math.max(0, pfl - PFL_STATE_CREDIT);
    return sumArea(titles, area);
  };
  const areaPlanned = (area: string) => byArea(allPlanned, area);
  const areaEnrolled = (area: string) => byArea(allPlanned.concat(ALTERNATES.map((x) => x.title)).filter((t) => isEnrolled(t)), area);
  const missing = allPlanned.filter((t) => !byTitle.has(t));

  return (
    <>
      <h1 className="p-h1">Virtual Counselor</h1>
      <p className="p-muted">Graduation plan by grade. Use it at registration to see what each student needs. The plan follows the Florida 24 credit diploma structure and totals {grandTotal.toFixed(1)} credits.</p>
      <div className="p-row"><a className="p-btn" href="/portal/admin">Back to Administration</a></div>
      {missing.length > 0 && <p className="p-note">These planned courses were not found in the course list: {missing.join(', ')}.</p>}

      <div className="p-card">
        <h3>Look at a student</h3>
        <div className="p-row">
          <select value={who} onChange={(e) => setWho(e.target.value)}>
            <option value="">Choose a student (optional)</option>
            {people.map((x) => <option key={x.id} value={x.id}>{x.full_name || x.email}{x.grade_level ? ` · Grade ${x.grade_level}` : ''}</option>)}
          </select>
        </div>
        {student && <p className="p-small">{student.full_name || student.email}{student.student_id ? ` · ${student.student_id}` : ''} · {student.grade_level ? `Grade ${student.grade_level}` : 'No grade level set. Set it in Administration.'} · Courses marked Enrolled are ones the student is currently enrolled in.</p>}
      </div>

      <TranscriptPlanner people={people} credit={credit} />

      <div className="no-print">
      <h2 className="p-h2">Graduation requirements</h2>
      <div className="p-card">
        <table className="p-table">
          <thead><tr><th>Subject area</th><th>Required</th><th>In the plan</th>{student && <th>Enrolled</th>}</tr></thead>
          <tbody>
            {REQUIRED.map((r) => (
              <tr key={r.area}><td>{r.area}</td><td>{r.need.toFixed(1)}</td><td>{areaPlanned(r.area).toFixed(1)}</td>{student && <td>{areaEnrolled(r.area).toFixed(1)}</td>}</tr>
            ))}
            <tr><td><b>Total</b></td><td><b>24.0</b></td><td><b>{grandTotal.toFixed(1)}</b></td>{student && <td><b>{REQUIRED.reduce((a, r) => a + areaEnrolled(r.area), 0).toFixed(1)}</b></td>}</tr>
          </tbody>
        </table>
        <p className="p-small">Social Studies includes 0.5 Economics. Personal Financial Literacy reserves 0.5 credit for Personal Finance and Money Management (2102371). Personal Finance and Stewardship carries 1.0 credit here, so its other 0.5 is counted toward electives provisionally until it is classified.</p>
      </div>

      {[9, 10, 11, 12].map((g) => (
        <div key={g}>
          <h2 className="p-h2" style={student?.grade_level === g ? { color: '#C9A84C' } : undefined}>{g}th Grade ({planTotal(g).toFixed(1)} credits){student?.grade_level === g ? ' · this student' : ''}</h2>
          <div className="p-card">
            <table className="p-table">
              <thead><tr><th>Course</th><th>Credits</th><th>Counts toward</th>{student && <th>Status</th>}</tr></thead>
              <tbody>
                {PLAN[g].map((t) => {
                  const c = byTitle.get(t);
                  return (
                    <tr key={t}>
                      <td>{c ? <a href={`/portal/courses/${c.slug}`}>{t}</a> : t}</td>
                      <td>{credit(t).toFixed(1)}</td>
                      <td>{areaOf(t)}</td>
                      {student && <td>{isEnrolled(t) ? <em>Enrolled</em> : ''}</td>}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      ))}

      <h2 className="p-h2">Alternates</h2>
      <div className="p-card">
        <table className="p-table">
          <thead><tr><th>Course</th><th>Credits</th><th>Use</th>{student && <th>Status</th>}</tr></thead>
          <tbody>
            {ALTERNATES.map((a) => (
              <tr key={a.title}><td>{byTitle.get(a.title) ? <a href={`/portal/courses/${byTitle.get(a.title)!.slug}`}>{a.title}</a> : a.title}</td><td>{credit(a.title).toFixed(1)}</td><td>{a.use}</td>{student && <td>{isEnrolled(a.title) ? <em>Enrolled</em> : ''}</td>}</tr>
            ))}
          </tbody>
        </table>
        <p className="p-small">Transfer students: review the transcript first, then give priority to required courses still missing in English, math, science, social studies, PE and fine arts. Placements are recommendations. Dr. Jenkins decides each student's schedule.</p>
      </div>
      </div>
    </>
  );
}

export default function Page() { return <PortalFrame adminOnly>{() => <Counselor />}</PortalFrame>; }
