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

  // Save first, so the message is never lost even if email fails.
  const sbUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  let savedId: string | null = null;
  if (svc && sbUrl) {
    try {
      const ins = await fetch(`${sbUrl}/rest/v1/inquiries`, {
        method: 'POST',
        headers: { apikey: svc, Authorization: `Bearer ${svc}`, 'Content-Type': 'application/json', Prefer: 'return=representation' },
        body: JSON.stringify({ name, email, phone: phone || null, program: program || null, message }),
      });
      if (ins.ok) savedId = (await ins.json().catch(() => []))?.[0]?.id ?? null;
    } catch { /* fall through to email */ }
  }

  let emailed = false;
  const key = process.env.RESEND_API_KEY;
  if (key) {
    try {
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
      emailed = r.ok;
    } catch { /* keep going */ }
  }

  if (savedId && svc && sbUrl && emailed) {
    fetch(`${sbUrl}/rest/v1/inquiries?id=eq.${savedId}`, { method: 'PATCH', headers: { apikey: svc, Authorization: `Bearer ${svc}`, 'Content-Type': 'application/json', Prefer: 'return=minimal' }, body: JSON.stringify({ emailed: true }) }).catch(() => {});
  }

  // The visitor sees success if the message was saved or emailed. Only if both failed do we ask them to call.
  if (!savedId && !emailed) return NextResponse.json({ error: FALLBACK }, { status: 502 });
  return NextResponse.json({ message: 'Thank you. Dr. Jenkins and the NLPA office will respond within one business day.' });
}
