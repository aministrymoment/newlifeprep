import { NextResponse } from 'next/server';

export const runtime = 'nodejs';
const URL_ = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const ANON = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

export async function POST(req: Request) {
  const auth = req.headers.get('authorization') || '';
  if (!auth.startsWith('Bearer ')) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const who = await fetch(`${URL_}/auth/v1/user`, { headers: { apikey: ANON, Authorization: auth } });
  if (!who.ok) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });

  let b: any; try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const slug = String(b.slug || '').slice(0, 80);
  const messages = (Array.isArray(b.messages) ? b.messages : []).slice(-12).map((m: any) => ({ role: m.role === 'assistant' ? 'assistant' : 'user', content: String(m.content || '').slice(0, 2000) })).filter((m: any) => m.content);
  if (!messages.length || messages[messages.length - 1].role !== 'user') return NextResponse.json({ error: 'Please type a question.' }, { status: 400 });

  // The student's own token is used, so database rules confirm they are enrolled in this course.
  const cr = await fetch(`${URL_}/rest/v1/courses?slug=eq.${encodeURIComponent(slug)}&select=title,subject,focus`, { headers: { apikey: ANON, Authorization: auth } });
  const course = (await cr.json().catch(() => []))?.[0];
  if (!course) return NextResponse.json({ error: 'Course not found.' }, { status: 404 });

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return NextResponse.json({ error: 'Help is not available right now. Please contact the office at (954) 851-6608.' }, { status: 503 });

  const system = `You are a patient, encouraging study guide for a high school student at New Life Preparatory Academy, a Christian school in Pompano Beach, Florida. Course: ${course.title}${course.subject ? ` (${course.subject})` : ''}. Course focus: ${course.focus || 'not provided'}.
Teach with clear explanations, examples and guiding questions aligned to the Florida State Standards. Never give the answer to a quiz or graded assignment; give hints and check the student's reasoning instead. When quoting Scripture, use the King James Version only. Keep a warm, respectful, faith friendly tone. Keep replies short (under 200 words) and stay on this course. If the student seems distressed or mentions harm, kindly encourage them to speak with a trusted adult or the school office at (954) 851-6608.`;

  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': key, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: process.env.ANTHROPIC_MODEL || 'claude-sonnet-5-5', max_tokens: 600, system, messages }),
  });
  if (!r.ok) return NextResponse.json({ error: 'Help is not available right now. Please try again in a moment.' }, { status: 502 });
  const j = await r.json();
  return NextResponse.json({ reply: (j.content || []).map((c: any) => c.text || '').join('').trim() });
}
