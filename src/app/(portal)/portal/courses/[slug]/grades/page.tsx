'use client';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import PortalFrame from '@/components/portal/PortalFrame';
import { useCourse } from '@/components/portal/useCourse';
import { buildPath, flat, stepStatus, computeGrade, letter } from '@/lib/coursePath';

function Report({ userId, slug }: { userId: string; slug: string }) {
  const { course, items, subs, atts, prog, state } = useCourse(userId, slug);
  if (state === 'loading') return <p className="p-muted">Loading...</p>;
  if (state === 'none' || !course) return <div className="p-card"><p>That course was not found.</p><Link className="p-btn" href="/portal">Back to Dashboard</Link></div>;
  const steps = flat(buildPath(items));
  const st = steps.map((s) => stepStatus(s.item, prog, atts, subs));
  const done = st.filter((s) => s.done).length;
  const pct = steps.length ? Math.round((100 * done) / steps.length) : 0;
  const g = computeGrade(items, atts, subs);
  const score = (id: string, kind: string) => {
    if (kind === 'quiz') { const s = atts.filter((a) => a.item_id === id).map((a) => a.score); return s.length ? `${Math.max(...s)}%` : 'Not taken'; }
    if (kind === 'topic') return prog.has(id) ? 'Complete' : 'Not done';
    const m = subs.filter((x) => x.item_id === id); if (!m.length) return 'Not submitted';
    const sc = m.filter((x) => x.score !== null).map((x) => x.score as number);
    return sc.length ? `${Math.max(...sc)}%` : 'Awaiting review';
  };
  return (
    <>
      <Link href={`/portal/courses/${slug}`} className="p-link">← {course.title} course home</Link>
      <h1 className="p-h1">Grade Report: {course.title}</h1>
      <div className="p-stats">
        <div className="p-stat"><span>Course complete</span><b>{pct}%</b><div className="p-bar"><span style={{ width: `${pct}%` }} /></div><small>{done} of {steps.length} steps</small></div>
        <div className="p-stat"><span>Cumulative grade</span><b>{g.percent === null ? 'No grade yet' : `${g.percent}%`}</b><small>{g.percent === null ? 'Waiting for your first scored work' : `${letter(g.percent)}. 70 percent or better passes.`}</small></div>
      </div>
      <div className="p-card">
        <h3>How the grade is built</h3>
        <table className="p-table"><thead><tr><th>Category</th><th>Weight</th><th>Scored</th><th>Average</th></tr></thead>
          <tbody>{g.cats.map((c) => <tr key={c.name}><td>{c.name}</td><td>{c.weight}%</td><td>{c.counted} of {c.total}</td><td>{c.avg === null ? 'None yet' : `${Math.round(c.avg)}%`}</td></tr>)}</tbody></table>
        <p className="p-small">Only scored work is counted. Quizzes use your best attempt. Written work uses your highest score.</p>
      </div>
      <div className="p-card">
        <h3>Every step</h3>
        <table className="p-table"><thead><tr><th>Step</th><th>Result</th></tr></thead>
          <tbody>{steps.map((s) => <tr key={s.item.id}><td><Link href={`/portal/courses/${slug}/step/${s.item.id}`}><em>{s.label}</em> {s.item.title}</Link></td><td>{score(s.item.id, s.item.kind)}</td></tr>)}</tbody></table>
      </div>
    </>
  );
}

export default function Page() {
  const { slug } = useParams<{ slug: string }>();
  return <PortalFrame>{({ session }) => <Report userId={session!.user.id} slug={slug} />}</PortalFrame>;
}
