'use client';
import Link from 'next/link';
import { useParams, useRouter } from 'next/navigation';
import { useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';
import Video from '@/components/portal/Video';
import { Written, Quiz, Help } from '@/components/portal/CourseParts';
import { useCourse } from '@/components/portal/useCourse';
import { buildPath, flat, stepStatus } from '@/lib/coursePath';

function StepView({ userId, slug, itemId }: { userId: string; slug: string; itemId: string }) {
  const { course, items, subs, atts, prog, state, reload } = useCourse(userId, slug);
  const [teach, setTeach] = useState<{ id: string; title: string } | null>(null);
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  if (state === 'loading') return <p className="p-muted">Loading...</p>;
  if (state === 'none' || !course) return <div className="p-card"><p>That course was not found, or you are not enrolled in it.</p><Link className="p-btn" href="/portal">Back to Dashboard</Link></div>;

  const mods = buildPath(items);
  const steps = flat(mods);
  const idx = steps.findIndex((s) => s.item.id === itemId);
  if (idx < 0) return <div className="p-card"><p>That step was not found.</p><Link className="p-btn" href={`/portal/courses/${slug}`}>Back to Course Home</Link></div>;
  const step = steps[idx]; const item = step.item;
  const mod = mods.find((m) => m.steps.some((s) => s.item.id === itemId));
  const modPos = mod ? mod.steps.findIndex((s) => s.item.id === itemId) + 1 : 0;
  const sv = stepStatus(item, prog, atts, subs);
  const prev = idx > 0 ? steps[idx - 1] : null;
  const next = idx < steps.length - 1 ? steps[idx + 1] : null;
  const to = (id: string) => `/portal/courses/${slug}/step/${id}`;

  async function complete() {
    setBusy(true); setErr('');
    const { error } = await supabase().from('item_progress').upsert({ user_id: userId, item_id: item.id }, { onConflict: 'user_id,item_id', ignoreDuplicates: true });
    if (error) setErr('Could not save your progress. Please try again.'); else { await reload(); if (next) router.push(to(next.item.id)); }
    setBusy(false);
  }

  return (
    <>
      <Link href={`/portal/courses/${slug}`} className="p-link">← {course.title} course home</Link>
      <p className="p-tag" style={{ marginTop: 14 }}>{mod?.title} · Step {modPos} of {mod?.steps.length}</p>
      <h1 className="p-h1">{step.label}: {item.title}</h1>
      {sv.done && <p className="p-pass-line">✓ {sv.note}</p>}
      <div className="p-two">
        <section>
          {item.kind === 'topic' && (
            <div className="p-card">
              <Video url={item.content?.video} title={item.title} />
              {item.content?.presenter && item.content?.video ? <p className="p-muted">Presented by {item.content.presenter}</p> : null}
              {Array.isArray(item.content?.readings) && item.content.readings.length ? <div className="p-readings"><strong>Read it here</strong><ul>{item.content.readings.map((r: { title: string; url: string }) => <li key={r.url + r.title}><a href={r.url} target="_blank" rel="noopener noreferrer">{r.title}</a></li>)}</ul></div> : null}
              <p className="p-pre">{item.content?.body}</p>
              <div className="p-row">
                <button className="p-btn" onClick={() => setTeach({ id: item.id, title: item.title })}>Teach Me</button>
                {!sv.done && <button className="p-btn" onClick={complete} disabled={busy}>{busy ? 'Saving...' : 'Mark Lesson Complete'}</button>}
              </div>
              {err && <p className="p-note">{err}</p>}
              {!sv.done && <p className="p-small">When you have finished the lesson and your task, mark it complete, then take the Check Quiz.</p>}
            </div>
          )}
          {item.kind === 'quiz' && <Quiz item={item} atts={atts} onDone={reload} />}
          {(item.kind === 'assessment' || item.kind === 'discussion') && <Written item={item} subs={subs} userId={userId} onSaved={reload} />}

          <div className="p-stepnav">
            {prev ? <Link className="p-btn ghost" href={to(prev.item.id)}>← Previous</Link> : <span />}
            {next ? <Link className={sv.done ? 'p-btn' : 'p-btn ghost'} href={to(next.item.id)}>{sv.done ? 'Next step →' : 'Skip to next →'}</Link> : <Link className="p-btn" href={`/portal/courses/${slug}/grades`}>View grade report</Link>}
          </div>
        </section>
        <Help slug={slug} topic={teach} onClear={() => setTeach(null)} />
      </div>
    </>
  );
}

export default function Page() {
  const { slug, itemId } = useParams<{ slug: string; itemId: string }>();
  return <PortalFrame>{({ session }) => <StepView userId={session!.user.id} slug={slug} itemId={itemId} />}</PortalFrame>;
}
