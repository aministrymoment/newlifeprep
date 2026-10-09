'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';

type Row = { id: string; slug: string; title: string; subject: string | null; credits: number; quizzes: number; passed: number };

function Dash({ userId, name }: { userId: string; name: string }) {
  const [rows, setRows] = useState<Row[] | null>(null);
  const [err, setErr] = useState('');

  useEffect(() => {
    (async () => {
      const sb = supabase();
      const { data: enr, error } = await sb.from('enrollments').select('course_id, courses(id, slug, title, subject, credits)').eq('user_id', userId).neq('status', 'withdrawn');
      if (error) { setErr('We could not load your courses. Please refresh.'); return; }
      const courses = (enr || []).map((e: any) => e.courses).filter(Boolean);
      if (!courses.length) { setRows([]); return; }
      const ids = courses.map((c: any) => c.id);
      const { data: items } = await sb.from('course_items').select('id, course_id').eq('kind', 'quiz').in('course_id', ids);
      const { data: att } = await sb.from('quiz_attempts').select('item_id, passed').eq('user_id', userId).eq('passed', true);
      const passedSet = new Set((att || []).map((a: any) => a.item_id));
      setRows(courses.map((c: any) => {
        const qs = (items || []).filter((i: any) => i.course_id === c.id);
        return { ...c, quizzes: qs.length, passed: qs.filter((q: any) => passedSet.has(q.id)).length };
      }));
    })();
  }, [userId]);

  return (
    <>
      <h1 className="p-h1">Welcome, {name}</h1>
      <p className="p-muted">Your courses are below. Every quiz needs 70 percent or better, and you may retake it until you pass.</p>
      {err && <p className="p-note">{err}</p>}
      {rows === null && !err && <p className="p-muted">Loading your courses...</p>}
      {rows && rows.length === 0 && <div className="p-card"><p>You are not enrolled in a course yet. The office will add your courses soon. Questions? Call (954) 851-6608.</p></div>}
      <div className="p-grid">
        {rows?.map((r) => {
          const pct = r.quizzes ? Math.round((100 * r.passed) / r.quizzes) : 0;
          return (
            <Link key={r.id} href={`/portal/courses/${r.slug}`} className="p-card p-course">
              <span className="p-tag">{r.subject || 'Course'} · {r.credits} credit</span>
              <h2>{r.title}</h2>
              <div className="p-bar"><span style={{ width: `${pct}%` }} /></div>
              <p className="p-small">{r.passed} of {r.quizzes} quizzes passed</p>
            </Link>
          );
        })}
      </div>
    </>
  );
}

export default function Page() {
  return <PortalFrame>{({ session, profile }) => <Dash userId={session!.user.id} name={profile?.full_name || session!.user.email || 'Student'} />}</PortalFrame>;
}
