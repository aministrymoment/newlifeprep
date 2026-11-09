'use client';
import { useCallback, useEffect, useRef, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { plainText } from '@/lib/plainText';
import { MAX_ATTEMPTS, type Item, type Sub, type Att } from '@/lib/coursePath';

export function Written({ item, subs, userId, onSaved }: { item: Item; subs: Sub[]; userId: string; onSaved: () => void }) {
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

export function Quiz({ item, atts, onDone }: { item: Item; atts: Att[]; onDone: () => void }) {
  const qs: { q: string; options: string[] }[] = item.content?.questions || [];
  const [ans, setAns] = useState<(number | null)[]>(qs.map(() => null));
  const [res, setRes] = useState<{ score: number; passed: boolean; correct: boolean[]; explains: string[] | null; left?: number } | null>(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const mine = atts.filter((a) => a.item_id === item.id);
  const best = mine.reduce((m, a) => Math.max(m, a.score), 0);
  const passed = mine.some((a) => a.passed);
  const left = Math.max(0, MAX_ATTEMPTS - mine.length);
  const locked = !passed && left === 0;

  async function submit() {
    setBusy(true); setErr('');
    const { data, error } = await supabase().rpc('grade_quiz', { p_item: item.id, p_answers: ans.map((a) => (a === null ? -1 : a)) });
    if (error) setErr(error.message.includes('answer key') ? 'This quiz is not ready yet.' : error.message.includes('No attempts left') ? 'You have used all 3 attempts. Please contact the office.' : error.message.includes('already passed') ? 'You already passed this quiz.' : 'Could not grade the quiz. Please try again.');
    else { setRes(data); onDone(); }
    setBusy(false);
  }
  function retake() { setRes(null); setAns(qs.map(() => null)); }

  return (
    <div className="p-card">
      <h3>{item.title} {passed && <span className="p-pass">Passed</span>}</h3>
      <p className="p-small">{mine.length ? `Attempt${mine.length > 1 ? 's' : ''} used ${mine.length} of ${MAX_ATTEMPTS} · best score ${best}` : `You need 70 percent or better. You have ${MAX_ATTEMPTS} attempts.`}</p>
      {locked && !res && <p className="p-note">You have used all 3 attempts. Please contact the office.</p>}
      {!res && !locked && !passed && qs.map((q, i) => (
        <fieldset key={i} className="p-q">
          <legend>{i + 1}. {q.q}</legend>
          {q.options.map((o, j) => (
            <label key={j}><input type="radio" name={`${item.id}-${i}`} checked={ans[i] === j} onChange={() => setAns(ans.map((a, k) => (k === i ? j : a)))} /> {o}</label>
          ))}
        </fieldset>
      ))}
      {!res && !locked && !passed && <button className="p-btn" onClick={submit} disabled={busy || ans.some((a) => a === null)}>{busy ? 'Grading...' : 'Submit Quiz'}</button>}
      {err && <p className="p-note">{err}</p>}
      {res && (
        <div className={res.passed ? 'p-result ok' : 'p-result no'}>
          <p><b>{res.score} percent.</b> {res.passed ? 'You passed. Well done.' : 'Not yet 70 percent. Review the topics and try again.'}</p>
          {qs.map((q, i) => <p key={i} className="p-small">{i + 1}. {res.correct[i] ? 'Correct' : 'Incorrect'}{res.explains && res.explains[i] ? `. ${res.explains[i]}` : ''}</p>)}
          {!res.passed && left > 0 && <button className="p-btn" onClick={retake}>Retake Quiz ({left} left)</button>}
          {!res.passed && left === 0 && <p className="p-note">You have used all 3 attempts. Please contact the office.</p>}
        </div>
      )}
    </div>
  );
}

export function Help({ slug, topic, onClear }: { slug: string; topic: { id: string; title: string } | null; onClear: () => void }) {
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
      <div className="p-log">{log.map((m, i) => <p key={i} className={m.role === 'user' ? 'me' : 'bot'} style={{ whiteSpace: 'pre-wrap' }}>{m.role === 'user' ? m.content : plainText(m.content)}</p>)}{busy && <p className="bot p-muted">Thinking...</p>}</div>
      <textarea rows={3} value={text} onChange={(e) => setText(e.target.value)} placeholder={topic ? 'Type your answer or question' : 'Type your question'} onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); ask(); } }} />
      <button className="p-btn" onClick={ask} disabled={busy || !text.trim()}>Send</button>
    </aside>
  );
}

