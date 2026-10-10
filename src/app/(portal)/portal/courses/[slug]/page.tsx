'use client';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import { useCallback, useEffect, useRef, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';
import Video from '@/components/portal/Video';

type Course = { id: string; slug: string; title: string; subject: string | null; credits: number; focus: string | null; video_url?: string | null };
type Item = { id: string; kind: 'topic' | 'assessment' | 'discussion' | 'quiz'; position: number; title: string; content: any };
type Sub = { id: string; item_id: string; body: string; score: number | null; feedback: string | null; status: string; created_at: string };
type Att = { item_id: string; score: number; passed: boolean; created_at: string };
const TABS = ['Focus', 'Topics', 'Assessments', 'Discussions', 'Quizzes'] as const;

function Written({ item, subs, userId, onSaved }: { item: Item; subs: Sub[]; userId: string; onSaved: () => void }) {
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const mine = subs.filter((s) => s.item_id === item.id);
  async function send() {
    if (!text.trim()) return;
    setBusy(true); setErr('');
    const { error } = await supabase().from('submissions').insert({ user_id: userId, item_id: item.id, body: text.trim() });
    if (error) setErr('Could not save. Please try again.'); else { setText(''); onSaved(); }
    setBusy(false);
  }
  return (
    <div className="p-card">
      <h3>{item.title}</h3>
      <p>{item.content?.prompt}</p>
      {item.content?.rubric && <p className="p-small"><b>What we look for:</b> {item.content.rubric}</p>}
      <textarea value={text} onChange={(e) => setText(e.target.value)} rows={5} placeholder="Type your response here" />
      {err && <p className="p-note">{err}</p>}
      <button className="p-btn" onClick={send} disabled={busy || !text.trim()}>{busy ? 'Saving...' : 'Submit'}</button>
      {mine.map((s) => (
        <div key={s.id} className="p-sub">
          <p className="p-small">{new Date(s.created_at).toLocaleString()} · {s.status === 'graded' ? `Score ${s.score}` : 'Awaiting review'}</p>
          <p>{s.body}</p>
          {s.feedback && <p className="p-feedback"><b>Feedback:</b> {s.feedback}</p>}
        </div>
      ))}
    </div>
  );
}

function Quiz({ item, atts, onDone }: { item: Item; atts: Att[]; onDone: () => void }) {
  const qs: { q: string; options: string[] }[] = item.content?.questions || [];
  const [ans, setAns] = useState<(number | null)[]>(qs.map(() => null));
  const [res, setRes] = useState<{ score: number; passed: boolean; correct: boolean[]; explains: string[] | null } | null>(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const mine = atts.filter((a) => a.item_id === item.id);
  const best = mine.reduce((m, a) => Math.max(m, a.score), 0);
  const passed = mine.some((a) => a.passed);

  async function submit() {
    setBusy(true); setErr('');
    const { data, error } = await supabase().rpc('grade_quiz', { p_item: item.id, p_answers: ans.map((a) => (a === null ? -1 : a)) });
    if (error) setErr(error.message.includes('answer key') ? 'This quiz is not ready yet.' : 'Could not grade the quiz. Please try again.');
    else { setRes(data); onDone(); }
    setBusy(false);
  }
  function retake() { setRes(null); setAns(qs.map(() => null)); }

  return (
    <div className="p-card">
      <h3>{item.title} {passed && <span className="p-pass">Passed</span>}</h3>
      <p className="p-small">{mine.length ? `${mine.length} attempt${mine.length > 1 ? 's' : ''} · best score ${best}` : 'You need 70 percent or better. You may retake until you pass.'}</p>
      {!res && qs.map((q, i) => (
        <fieldset key={i} className="p-q">
          <legend>{i + 1}. {q.q}</legend>
          {q.options.map((o, j) => (
            <label key={j}><input type="radio" name={`${item.id}-${i}`} checked={ans[i] === j} onChange={() => setAns(ans.map((a, k) => (k === i ? j : a)))} /> {o}</label>
          ))}
        </fieldset>
      ))}
      {!res && <button className="p-btn" onClick={submit} disabled={busy || ans.some((a) => a === null)}>{busy ? 'Grading...' : 'Submit Quiz'}</button>}
      {err && <p className="p-note">{err}</p>}
      {res && (
        <div className={res.passed ? 'p-result ok' : 'p-result no'}>
          <p><b>{res.score} percent.</b> {res.passed ? 'You passed. Well done.' : 'Not yet 70 percent. Review the topics and try again.'}</p>
          {qs.map((q, i) => <p key={i} className="p-small">{i + 1}. {res.correct[i] ? 'Correct' : 'Incorrect'}{res.explains && res.explains[i] ? `. ${res.explains[i]}` : ''}</p>)}
          {!res.passed && <button className="p-btn" onClick={retake}>Retake Quiz</button>}
        </div>
      )}
    </div>
  );
}

function Help({ slug, topic, onClear }: { slug: string; topic: { id: string; title: string } | null; onClear: () => void }) {
  const [log, setLog] = useState<{ role: 'user' | 'assistant'; content: string }[]>([]);
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  const box = useRef<HTMLElement | null>(null);

  const send = useCallback(async (next: { role: 'user' | 'assistant'; content: string }[], topicId?: string) => {
    setLog(next); setBusy(true);
    const { data } = await supabase().auth.getSession();
    try {
      const r = await fetch('/api/tutor', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${data.session?.access_token}` }, body: JSON.stringify({ slug, topicId, messages: next.slice(-12) }) });
      const j = await r.json().catch(() => ({}));
      setLog([...next, { role: 'assistant', content: r.ok ? j.reply : j.error || 'Help is not available right now. Please contact the office.' }]);
    } catch { setLog([...next, { role: 'assistant', content: 'Help is not available right now. Please contact the office.' }]); }
    setBusy(false);
  }, [slug]);

  // Pressing Teach Me on a topic starts a guided lesson
  useEffect(() => {
    if (!topic) return;
    box.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    send([{ role: 'user', content: `Please teach me this lesson step by step: ${topic.title}` }], topic.id);
  }, [topic, send]);

  async function ask() {
    const q = text.trim(); if (!q || busy) return;
    setText('');
    send([...log, { role: 'user', content: q }], topic?.id);
  }
  return (
    <aside className="p-card p-help" ref={box as any}>
      <h3>{topic ? 'Teach Me' : 'Ask for Help'}</h3>
      {topic ? <p className="p-small">Lesson: {topic.title} <button className="p-link" onClick={() => { onClear(); setLog([]); }}>End lesson</button></p> : <p className="p-small">Ask about this course. You will get hints and explanations, not quiz answers. Press Teach Me on any topic for a guided lesson.</p>}
      <div className="p-log">{log.map((m, i) => <p key={i} className={m.role === 'user' ? 'me' : 'bot'}>{m.content}</p>)}{busy && <p className="bot p-muted">Thinking...</p>}</div>
      <textarea rows={3} value={text} onChange={(e) => setText(e.target.value)} placeholder={topic ? 'Type your answer or question' : 'Type your question'} onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); ask(); } }} />
      <button className="p-btn" onClick={ask} disabled={busy || !text.trim()}>Send</button>
    </aside>
  );
}

function CourseView({ userId, slug }: { userId: string; slug: string }) {
  const [course, setCourse] = useState<Course | null>(null);
  const [items, setItems] = useState<Item[]>([]);
  const [subs, setSubs] = useState<Sub[]>([]);
  const [atts, setAtts] = useState<Att[]>([]);
  const [tab, setTab] = useState<(typeof TABS)[number]>('Focus');
  const [teach, setTeach] = useState<{ id: string; title: string } | null>(null);
  const [state, setState] = useState<'loading' | 'ok' | 'none'>('loading');

  const loadMine = useCallback(async (courseId: string) => {
    const sb = supabase();
    const { data: its } = await sb.from('course_items').select('*').eq('course_id', courseId).order('position');
    const ids = (its || []).map((i: any) => i.id);
    setItems((its || []) as Item[]);
    if (ids.length) {
      const { data: s } = await sb.from('submissions').select('*').eq('user_id', userId).in('item_id', ids).order('created_at', { ascending: false });
      const { data: a } = await sb.from('quiz_attempts').select('item_id, score, passed, created_at').eq('user_id', userId).in('item_id', ids);
      setSubs((s || []) as Sub[]); setAtts((a || []) as Att[]);
    }
  }, [userId]);

  useEffect(() => {
    (async () => {
      const { data } = await supabase().from('courses').select('*').eq('slug', slug).maybeSingle();
      if (!data) { setState('none'); return; }
      setCourse(data as Course); setState('ok'); loadMine(data.id);
    })();
  }, [slug, loadMine]);

  if (state === 'loading') return <p className="p-muted">Loading...</p>;
  if (state === 'none' || !course) return <div className="p-card"><p>That course was not found, or you are not enrolled in it.</p><Link className="p-btn" href="/portal">Back to Dashboard</Link></div>;

  const of = (k: Item['kind']) => items.filter((i) => i.kind === k);
  const refresh = () => loadMine(course.id);
  return (
    <>
      <Link href="/portal" className="p-link">← All courses</Link>
      <h1 className="p-h1">{course.title}</h1>
      <p className="p-muted">{course.subject} · {course.credits} credit</p>
      <div className="p-tabs">{TABS.map((t) => <button key={t} className={tab === t ? 'on' : ''} onClick={() => setTab(t)}>{t}</button>)}</div>
      <div className="p-two">
        <section>
          {tab === 'Focus' && <div className="p-card"><h3>Focus</h3><Video url={course.video_url} title={`${course.title} introduction`} /><p>{course.focus || 'The focus of this course will appear here.'}</p></div>}
          {tab === 'Topics' && (of('topic').length ? of('topic').map((i) => <div key={i.id} className="p-card"><h3>{i.title}</h3><Video url={i.content?.video} title={i.title} />{i.content?.presenter && i.content?.video ? <p className="p-muted">Presented by {i.content.presenter}</p> : null}{Array.isArray(i.content?.readings) && i.content.readings.length ? <div className="p-readings"><strong>Read it here</strong><ul>{i.content.readings.map((r: { title: string; url: string }) => <li key={r.url + r.title}><a href={r.url} target="_blank" rel="noopener noreferrer">{r.title}</a></li>)}</ul></div> : null}<p className="p-pre">{i.content?.body}</p><button className="p-btn" onClick={() => setTeach({ id: i.id, title: i.title })}>Teach Me</button></div>) : <p className="p-muted">No topics yet.</p>)}
          {tab === 'Assessments' && (of('assessment').length ? of('assessment').map((i) => <Written key={i.id} item={i} subs={subs} userId={userId} onSaved={refresh} />) : <p className="p-muted">No assessments yet.</p>)}
          {tab === 'Discussions' && (of('discussion').length ? of('discussion').map((i) => <Written key={i.id} item={i} subs={subs} userId={userId} onSaved={refresh} />) : <p className="p-muted">No discussions yet.</p>)}
          {tab === 'Quizzes' && (of('quiz').length ? of('quiz').map((i) => <Quiz key={i.id} item={i} atts={atts} onDone={refresh} />) : <p className="p-muted">No quizzes yet.</p>)}
        </section>
        <Help slug={slug} topic={teach} onClear={() => setTeach(null)} />
      </div>
    </>
  );
}

export default function Page() {
  const { slug } = useParams<{ slug: string }>();
  return <PortalFrame>{({ session }) => <CourseView userId={session!.user.id} slug={slug} />}</PortalFrame>;
}
