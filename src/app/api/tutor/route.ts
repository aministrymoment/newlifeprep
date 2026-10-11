import { NextResponse } from 'next/server';
import { tooMany } from '@/lib/rateLimit';

export const runtime = 'nodejs';
const URL_ = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const ANON = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

export async function POST(req: Request) {
  const auth = req.headers.get('authorization') || '';
  if (!auth.startsWith('Bearer ')) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const who = await fetch(`${URL_}/auth/v1/user`, { headers: { apikey: ANON, Authorization: auth } });
  if (!who.ok) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });

  const me = await who.clone().json().catch(() => ({}));
  if (tooMany(`tutor:${me?.id || auth.slice(-24)}`, 40, 60 * 60 * 1000)) return NextResponse.json({ error: 'You have asked a lot of questions this hour. Please take a short break and try again later.' }, { status: 429 });

  let b: any; try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const slug = String(b.slug || '').slice(0, 80);
  const messages = (Array.isArray(b.messages) ? b.messages : []).slice(-12).map((m: any) => ({ role: m.role === 'assistant' ? 'assistant' : 'user', content: String(m.content || '').slice(0, 2000) })).filter((m: any) => m.content);
  if (!messages.length || messages[messages.length - 1].role !== 'user') return NextResponse.json({ error: 'Please type a question.' }, { status: 400 });

  // The student's own token is used, so database rules confirm they are enrolled in this course.
  const cr = await fetch(`${URL_}/rest/v1/courses?slug=eq.${encodeURIComponent(slug)}&select=id,title,subject,focus`, { headers: { apikey: ANON, Authorization: auth } });
  const course = (await cr.json().catch(() => []))?.[0];
  if (!course) return NextResponse.json({ error: 'Course not found.' }, { status: 404 });

  // Lesson material (text and video script). The student's token is used, so only enrolled students get it.
  const topicId = String(b.topicId || '').slice(0, 64);
  const ir = await fetch(`${URL_}/rest/v1/course_items?course_id=eq.${course.id}&kind=eq.topic&select=id,title,content&order=position`, { headers: { apikey: ANON, Authorization: auth } });
  const topics: { id: string; title: string; content: any }[] = (await ir.json().catch(() => [])) || [];
  const pick = topicId ? topics.filter((t) => t.id === topicId) : topics;
  const material = pick.map((t) => `### ${t.title}\n${t.content?.body || ''}${t.content?.script ? `\n[Video script]\n${t.content.script}` : ''}`).join('\n\n').slice(0, 14000);
  const teaching = Boolean(topicId && pick.length);

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return NextResponse.json({ error: 'Help is not available right now. Please contact the office at (954) 851-6608.' }, { status: 503 });

  const system = `You are a patient, encouraging study guide for a high school student at New Life Preparatory Academy, a Christian school in Pompano Beach, Florida. Course: ${course.title}${course.subject ? ` (${course.subject})` : ''}. Course focus: ${course.focus || 'not provided'}.
${material ? `Use ONLY the lesson material below as your source of truth for what this course teaches. If the student asks something outside it, answer briefly and steer back to the lesson.\n\nLESSON MATERIAL\n${material}\n\n` : ''}${teaching ? 'TEACHING MODE: The student pressed Teach Me. Teach this lesson step by step like a patient classroom teacher: give one short idea at a time, then ask one question to check understanding, and wait for the answer before moving on. Praise effort, correct gently, and finish with a brief recap and a pointer to the quiz.\n' : ''}Teach with clear explanations, examples and guiding questions aligned to the Florida State Standards. Never give the answer to a quiz or graded assignment; give hints and check the student's reasoning instead. When quoting Scripture, use the King James Version only. Keep a warm, respectful, faith friendly tone. Keep replies short (under 200 words) and stay on this course. If the student seems distressed or mentions harm, kindly encourage them to speak with a trusted adult or the school office at (954) 851-6608.`;

  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': key, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: process.env.ANTHROPIC_MODEL || 'claude-sonnet-5-5', max_tokens: 700, system, messages }),
  });
  if (!r.ok) return NextResponse.json({ error: 'Help is not available right now. Please try again in a moment.' }, { status: 502 });
  const j = await r.json();
  return NextResponse.json({ reply: (j.content || []).map((c: any) => c.text || '').join('').trim() });
}
