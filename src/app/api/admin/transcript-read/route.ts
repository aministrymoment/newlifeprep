import { NextResponse } from 'next/server';
import { tooMany } from '@/lib/rateLimit';
import { ALL_NLPA_TITLES, AREAS } from '@/lib/graduation';

export const runtime = 'nodejs';
export const maxDuration = 60;
const URL_ = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const ANON = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';
const MAX_BYTES = 4 * 1024 * 1024;

// Reads an incoming transcript (PDF, image or pasted text) and returns a course list.
// Administrators only. Nothing from the transcript is stored by this route.
export async function POST(req: Request) {
  const auth = req.headers.get('authorization') || '';
  if (!auth.startsWith('Bearer ')) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const me = await fetch(`${URL_}/auth/v1/user`, { headers: { apikey: ANON, Authorization: auth } });
  if (!me.ok) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const uid = (await me.json()).id;
  const pr = await fetch(`${URL_}/rest/v1/profiles?id=eq.${uid}&select=role`, { headers: { apikey: ANON, Authorization: auth } });
  if ((await pr.json().catch(() => []))?.[0]?.role !== 'admin') return NextResponse.json({ error: 'Administrators only.' }, { status: 403 });
  if (tooMany(`transcript:${uid}`, 30, 60 * 60 * 1000)) return NextResponse.json({ error: 'Too many transcripts this hour. Please try again later.' }, { status: 429 });

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return NextResponse.json({ error: 'Reading transcripts is not switched on yet. The ANTHROPIC_API_KEY setting is missing from the site settings.' }, { status: 503 });

  let b: any; try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const text = String(b.text || '').slice(0, 30000).trim();
  const data = String(b.data || '');
  const mime = String(b.mime || '');
  const content: any[] = [];
  if (data) {
    if (data.length * 0.75 > MAX_BYTES) return NextResponse.json({ error: 'That file is larger than 4 MB. Please use a smaller file or paste the text.' }, { status: 413 });
    if (mime === 'application/pdf') content.push({ type: 'document', source: { type: 'base64', media_type: 'application/pdf', data } });
    else if (['image/png', 'image/jpeg', 'image/webp', 'image/gif'].includes(mime)) content.push({ type: 'image', source: { type: 'base64', media_type: mime, data } });
    else return NextResponse.json({ error: 'Please upload a PDF, PNG or JPG file, or paste the text.' }, { status: 400 });
  }
  if (text) content.push({ type: 'text', text: `Transcript text:\n\n${text}` });
  if (!content.length) return NextResponse.json({ error: 'Add a transcript file or paste its text.' }, { status: 400 });
  content.push({ type: 'text', text: 'Read this transcript and record every high school course using the record_transcript tool.' });

  const tool = {
    name: 'record_transcript',
    description: 'Record the courses found on a high school transcript.',
    input_schema: {
      type: 'object',
      properties: {
        student_name: { type: 'string', description: 'Student name as printed, or empty.' },
        school: { type: 'string', description: 'Previous school name, or empty.' },
        notes: { type: 'string', description: 'Anything unclear, unreadable, estimated or worth a person double checking. Keep short.' },
        courses: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              title: { type: 'string', description: 'Course title as printed.' },
              credits: { type: 'number', description: 'Credits earned or attempted. One year course is 1.0, one semester is 0.5. If not printed, estimate and say so in notes.' },
              grade: { type: 'string', description: 'Final grade as printed, or empty.' },
              year: { type: 'string', description: 'School year or term as printed, or empty.' },
              status: { type: 'string', enum: ['completed', 'in_progress', 'failed'], description: 'failed for F or no credit earned; in_progress only when the transcript shows the course is currently being taken.' },
              area: { type: 'string', enum: AREAS, description: 'Graduation area. Art, music, band, chorus, drama, theater and dance are Fine Arts. Personal finance, financial literacy and money management courses are Personal Financial Literacy. Health, foreign language, JROTC, technology, business and everything else not core are Electives.' },
              nlpa_match: { type: ['string', 'null'], enum: [...ALL_NLPA_TITLES, null], description: 'The single NLPA course that this course clearly covers at the same level, or null. Honors and AP versions match the standard course. Do not guess when unsure.' },
            },
            required: ['title', 'credits', 'status', 'area', 'nlpa_match'],
          },
        },
      },
      required: ['courses'],
    },
  };
  const system = `You read high school transcripts for New Life Preparatory Academy, a Christian school in Pompano Beach, Florida. Extract only what is printed. Never invent courses, grades or credits. Skip GPA lines, test scores and totals. If a course appears in two terms, list it once with its total credit. Use the NLPA course list only for nlpa_match: English 9 to 12 map to English 1 to 4; Algebra I, Geometry, Algebra II, Biology, Chemistry, World History, US History, American Government and Economics map to the NLPA course of the same level when it is clearly the same. When a transcript lists a combined or unclear course, use null and explain in notes.`;

  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': key, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: process.env.ANTHROPIC_MODEL || 'claude-sonnet-5-5', max_tokens: 6000, system, tools: [tool], tool_choice: { type: 'tool', name: 'record_transcript' }, messages: [{ role: 'user', content }] }),
  });
  if (!r.ok) return NextResponse.json({ error: 'The transcript could not be read right now. Please try again, or paste the text instead.' }, { status: 502 });
  const j = await r.json();
  const out = (j.content || []).find((c: any) => c.type === 'tool_use')?.input;
  if (!out || !Array.isArray(out.courses)) return NextResponse.json({ error: 'No courses were found. Try a clearer file or paste the text.' }, { status: 422 });
  const courses = out.courses.slice(0, 80).map((c: any) => ({
    title: String(c.title || '').slice(0, 120),
    credits: Math.max(0, Math.min(4, Number(c.credits) || 0)),
    grade: String(c.grade || '').slice(0, 10),
    year: String(c.year || '').slice(0, 20),
    status: ['completed', 'in_progress', 'failed'].includes(c.status) ? c.status : 'completed',
    area: AREAS.includes(c.area) ? c.area : 'Electives',
    match: ALL_NLPA_TITLES.includes(c.nlpa_match) ? c.nlpa_match : null,
  })).filter((c: any) => c.title);
  return NextResponse.json({ studentName: String(out.student_name || '').slice(0, 120), school: String(out.school || '').slice(0, 160), notes: String(out.notes || '').slice(0, 800), courses });
}
