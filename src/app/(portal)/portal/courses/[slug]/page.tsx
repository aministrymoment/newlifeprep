'use client';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import PortalFrame from '@/components/portal/PortalFrame';
import Video from '@/components/portal/Video';
import { useCourse } from '@/components/portal/useCourse';
import { buildPath, flat, stepStatus, computeGrade, letter, WEIGHTS } from '@/lib/coursePath';

function Home({ userId, slug }: { userId: string; slug: string }) {
  const { course, items, subs, atts, prog, state } = useCourse(userId, slug);
  if (state === 'loading') return <p className="p-muted">Loading...</p>;
  if (state === 'none' || !course) return <div className="p-card"><p>That course was not found, or you are not enrolled in it.</p><Link className="p-btn" href="/portal">Back to Dashboard</Link></div>;

  const mods = buildPath(items);
  const steps = flat(mods);
  const st = steps.map((s) => stepStatus(s.item, prog, atts, subs));
  const done = st.filter((s) => s.done).length;
  const pct = steps.length ? Math.round((100 * done) / steps.length) : 0;
  const nextIdx = st.findIndex((s) => !s.done);
  const next = nextIdx >= 0 ? steps[nextIdx] : null;
  const g = computeGrade(items, atts, subs);
  const href = (id: string) => `/portal/courses/${slug}/step/${id}`;
  let k = 0;

  return (
    <>
      <Link href="/portal" className="p-link">← All courses</Link>
      <h1 className="p-h1">{course.title}</h1>
      <p className="p-muted">{course.subject} · {course.credits} credit</p>

      <div className="p-stats">
        <div className="p-stat"><span>Course complete</span><b>{pct}%</b><div className="p-bar"><span style={{ width: `${pct}%` }} /></div><small>{done} of {steps.length} steps</small></div>
        <div className="p-stat"><span>Current grade</span><b>{g.percent === null ? 'No grade yet' : `${g.percent}%`}</b><small>{g.percent === null ? 'Your grade appears after your first quiz or graded work' : letter(g.percent)}</small><Link href={`/portal/courses/${slug}/grades`} className="p-link">View grade report</Link></div>
      </div>

      {next
        ? <div className="p-card p-next"><span className="p-tag">Your next step</span><h3>{next.label}: {next.item.title}</h3><Link className="p-btn" href={href(next.item.id)}>{done ? 'Continue' : 'Start the course'}</Link></div>
        : steps.length ? <div className="p-card p-next"><span className="p-tag">Course complete</span><h3>You have finished every step. Well done.</h3><p className="p-muted">Your final grade is shown in the grade report. A score of 70 percent or better passes the course.</p></div> : null}

      <div className="p-card">
        <h3>Start Here: How to Take This Course</h3>
        <Video url={course.video_url} title={`${course.title} introduction`} />
        <p>{course.focus}</p>
        <ol className="p-how">
          <li><b>Work in order, top to bottom.</b> Each unit follows the same path: a Lesson, then its Check Quiz, for every lesson in the unit. Then the Unit Quiz, the Written Assignment and the Discussion. The Final Assessment and Final Exam come last.</li>
          <li><b>Lesson.</b> Watch the video when one is posted, read the notes and any Read it here links, and work the Your Task problems on paper. If you are stuck, press Teach Me and the tutor will walk you through it. When you are finished, press Mark Lesson Complete.</li>
          <li><b>Check Quiz.</b> Take it right after the lesson. You need 70 percent or better to pass, and you may retake it as many times as you need.</li>
          <li><b>Unit Quiz.</b> Take it after all the lessons in the unit. Same rule: 70 percent or better, unlimited retakes.</li>
          <li><b>Written Assignment and Discussion.</b> Type your response in the box and press Submit. The school office reviews it and posts your score and feedback. Show your work and write in complete sentences.</li>
          <li><b>Final Assessment and Final Exam.</b> Finish every unit first. A course grade of 70 percent or better passes the course.</li>
        </ol>
        <p className="p-small"><b>How your grade is figured.</b> Quizzes and the Final Exam count {WEIGHTS.quizzes} percent (your best score on each quiz). Written Assignments and the Final Assessment count {WEIGHTS.written} percent. Discussions count {WEIGHTS.discussions} percent. Your grade is based on the work that has been scored so far, so it can change as you go.</p>
        <p className="p-small"><i>Study to shew thyself approved unto God, a workman that needeth not to be ashamed, rightly dividing the word of truth.</i> 2 Timothy 2:15</p>
      </div>

      {mods.map((m) => (
        <div key={m.key} className="p-card p-module">
          <h3>{m.title}</h3>
          <ol className="p-steps">
            {m.steps.map((s) => {
              const i = k++; const sv = st[i];
              return (
                <li key={s.item.id} className={sv.done ? 'done' : i === nextIdx ? 'now' : ''}>
                  <span className="p-mark">{sv.done ? '✓' : i === nextIdx ? '▶' : ''}</span>
                  <Link href={href(s.item.id)}><em>{s.label}</em> {s.item.title}</Link>
                  {sv.note && <small>{sv.note}</small>}
                </li>
              );
            })}
          </ol>
        </div>
      ))}
    </>
  );
}

export default function Page() {
  const { slug } = useParams<{ slug: string }>();
  return <PortalFrame>{({ session }) => <Home userId={session!.user.id} slug={slug} />}</PortalFrame>;
}
