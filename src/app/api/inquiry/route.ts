import { NextResponse } from 'next/server';
import { SITE } from '@/site';

export const runtime = 'nodejs';
const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] as string));
const FALLBACK = `Our online form is not available right now. Please call ${SITE.phone} or email ${SITE.email}.`;

export async function POST(req: Request) {
  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  if (typeof b.website === 'string' && b.website) return NextResponse.json({ message: 'Thank you.' }); // honeypot
  const s = (k: string, max: number) => String(b[k] ?? '').trim().slice(0, max);
  const name = s('name', 120), email = s('email', 160), phone = s('phone', 40), program = s('program', 80), message = s('message', 4000);
  if (!name || !message || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return NextResponse.json({ error: 'Please enter your name, a valid email and a message.' }, { status: 400 });

  const key = process.env.RESEND_API_KEY;
  if (!key) return NextResponse.json({ error: FALLBACK }, { status: 503 });

  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: process.env.INQUIRY_FROM || 'NLPA Website <onboarding@resend.dev>',
      to: [process.env.INQUIRY_TO || SITE.email],
      reply_to: email,
      subject: `Website inquiry from ${name}${program ? ` (${program})` : ''}`,
      html: `<p><b>Name:</b> ${esc(name)}</p><p><b>Email:</b> ${esc(email)}</p><p><b>Phone:</b> ${esc(phone)}</p><p><b>Program:</b> ${esc(program)}</p><p><b>Message:</b><br>${esc(message).replace(/\n/g, '<br>')}</p>`,
    }),
  });
  if (!r.ok) return NextResponse.json({ error: FALLBACK }, { status: 502 });
  return NextResponse.json({ message: 'Thank you. Dr. Jenkins and the NLPA office will respond within one business day.' });
}
