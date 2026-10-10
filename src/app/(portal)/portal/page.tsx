'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';
import type { Profile } from '@/components/portal/useAuth';
import { buildPath, flat, stepStatus, computeGrade, letter, type Item, type Att, type Sub } from '@/lib/coursePath';

type CourseRow = {
  id: string; slug: string; title: string; subject: string | null; credits: number;
  steps: number; done: number; pct: number; grade: number | null;
  next: { id: string; label: string; title: string } | null;
  modules: { key: string; title: string; steps: number; done: number }[];
};

const ordinal = (n: number) => `${n}th Grade`;

function Dash({ userId, profile, fallbackName }: { userId: string; profile: Profile | null; fallbackName: string }) {
  const [rows, setRows] = useState<CourseRow[] | null>(null);
  const [err, setErr] = useState('');

  useEffect(() => {
    (async () => {
      const sb = supabase();
      const { data: enr, error } = await sb.from('enrollments').select('course_id, courses(id, slug, title, subject, credits)').eq('user_id', userId).neq('status', 'withdrawn');
      if (error) { setErr('We could not load your courses. Please refresh.'); return; }
      const courses = (enr || []).map((e: any) => e.courses).filter(Boolean);
      if (!courses.length) { setRows([]); return; }
      const ids = courses.map((c: any) => c.id);
      const { data: items } = await sb.from('course_items').select('id, course_id, kind, position, title').in('course_id', ids);
      const itemIds = (items || []).map((i: any) => i.id);
      const [a, s, p] = await Promise.all([
        sb.from('quiz_attempts').select('item_id, score, passed, created_at').eq('user_id', userId).eq('voided', false).in('item_id', itemIds),
        sb.from('submissions').select('id, item_id, body, score, feedback, status, created_at').eq('user_id', userId).eq('voided', false).in('item_id', itemIds),
        sb.from('item_progress').select('item_id').eq('user_id', userId).eq('voided', false).in('item_id', itemIds),
      ]);
      const atts = (a.data || []) as Att[]; const subs = (s.data || []) as Sub[];
      const prog = new Set<string>((p.data || []).map((r: any) => r.item_id));
      setRows(courses.map((c: any): CourseRow => {
        const its = ((items || []).filter((i: any) => i.course_id === c.id)).map((i: any) => ({ ...i, content: {} })) as Item[];
        const mods = buildPath(its);
        const steps = flat(mods);
        const st = steps.map((x) => stepStatus(x.item, prog, atts, subs));
        const done = st.filter((x) => x.done).length;
        const ni = st.findIndex((x) => !x.done);
        return {
          ...c, steps: steps.length, done, pct: steps.length ? Math.round((100 * done) / steps.length) : 0,
          grade: computeGrade(its, atts, subs).percent,
          next: ni >= 0 ? { id: steps[ni].item.id, label: steps[ni].label, title: steps[ni].item.title } : null,
          modules: mods.map((m) => ({ key: m.key, title: m.title, steps: m.steps.length, done: m.steps.filter((x) => stepStatus(x.item, prog, atts, subs).done).length })),
        };
      }));
    })();
  }, [userId]);

  const totalSteps = rows?.reduce((a, r) => a + r.steps, 0) || 0;
  const totalDone = rows?.reduce((a, r) => a + r.done, 0) || 0;
  const overall = totalSteps ? Math.round((100 * totalDone) / totalSteps) : 0;
  const graded = (rows || []).filter((r) => r.grade !== null);
  const cw = graded.reduce((a, r) => a + (r.credits || 1), 0);
  const cumulative = cw ? Math.round(graded.reduce((a, r) => a + (r.grade as number) * (r.credits || 1), 0) / cw) : null;
  const credits = (rows || []).reduce((a, r) => a + Number(r.credits || 0), 0);
  const name = profile?.full_name || fallbackName;

  return (
    <>
      <h1 className="p-h1">Welcome, {name}</h1>
      <p className="p-muted">Your courses, progress and grades are all here. Every quiz needs 70 percent or better, and you have 3 attempts on each quiz.</p>
      {err && <p className="p-note">{err}</p>}

      <div className="p-profile">
        <div className="p-card p-who-card">
          <span className="p-tag">Student Profile</span>
          <h2>{name}</h2>
          <dl>
            <div><dt>Grade level</dt><dd>{profile?.grade_level ? ordinal(profile.grade_level) : 'Not set yet'}</dd></div>
            <div><dt>Student ID</dt><dd>{profile?.student_id || 'Not assigned yet'}</dd></div>
            <div><dt>Email</dt><dd>{profile?.email || ''}</dd></div>
            <div><dt>Courses</dt><dd>{rows ? `${rows.length} enrolled, ${credits} credit${credits === 1 ? '' : 's'}` : '...'}</dd></div>
          </dl>
          {(!profile?.grade_level || !profile?.student_id) && <p className="p-small">If your grade level or Student ID is missing, please contact the office at (954) 851-6608.</p>}
        </div>
        <div className="p-stat"><span>Overall completion</span><b>{rows ? `${overall}%` : '...'}</b><div className="p-bar"><span style={{ width: `${overall}%` }} /></div><small>{totalDone} of {totalSteps} steps across all courses</small></div>
        <div className="p-stat"><span>Cumulative grade</span><b>{cumulative === null ? 'No grade yet' : `${cumulative}%`}</b><small>{cumulative === null ? 'Your grade appears after your first quiz or scored work' : `${letter(cumulative)}. 70 percent or better passes.`}</small></div>
      </div>

      <h2 className="p-h2">My Courses</h2>
      {rows === null && !err && <p className="p-muted">Loading your courses...</p>}
      {rows && rows.length === 0 && <div className="p-card"><p>You are not enrolled in a course yet. The office will add your courses soon. Questions? Call (954) 851-6608.</p></div>}
      <div className="p-grid">
        {rows?.map((r) => (
          <div key={r.id} className="p-card p-course">
            <span className="p-tag">{r.subject || 'Course'} · {r.credits} credit</span>
            <h2>{r.title}</h2>
            <div className="p-bar"><span style={{ width: `${r.pct}%` }} /></div>
            <p className="p-small"><b>{r.pct}% complete</b> · {r.done} of {r.steps} steps · {r.grade === null ? 'No grade yet' : `Grade ${r.grade}% (${letter(r.grade)})`}</p>
            {r.next && <p className="p-small">Next: {r.next.label}, {r.next.title}</p>}
            <div className="p-row">
              <Link className="p-btn" href={r.next ? `/portal/courses/${r.slug}/step/${r.next.id}` : `/portal/courses/${r.slug}`}>{r.done ? (r.next ? 'Continue' : 'Review') : 'Start'}</Link>
              <Link className="p-link" href={`/portal/courses/${r.slug}`}>Course home</Link>
              <Link className="p-link" href={`/portal/courses/${r.slug}/grades`}>Grades</Link>
            </div>
            {r.modules.length > 0 && (
              <details className="p-mods"><summary>Modules ({r.modules.length})</summary>
                <ul>{r.modules.map((m) => <li key={m.key}><span>{m.title}</span><small>{m.done} of {m.steps}</small><div className="p-bar"><span style={{ width: `${m.steps ? Math.round((100 * m.done) / m.steps) : 0}%` }} /></div></li>)}</ul>
              </details>
            )}
          </div>
        ))}
      </div>
    </>
  );
}

export default function Page() {
  return <PortalFrame>{({ session, profile }) => <Dash userId={session!.user.id} profile={profile} fallbackName={session!.user.email || 'Student'} />}</PortalFrame>;
}
