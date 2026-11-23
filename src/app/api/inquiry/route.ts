import { NextResponse } from 'next/server';
import { SITE } from '@/site';
import { tooMany, clientIp } from '@/lib/rateLimit';
import { DETAIL_FIELDS, FEES, REQUEST_LABEL, money, type RequestType } from '@/lib/fees';
import { emailOffice, type InquiryRow } from '@/lib/notify';

export const runtime = 'nodejs';
const FALLBACK = `Our online form is not available right now. Please call ${SITE.phone} or email ${SITE.email}.`;
const TYPES: RequestType[] = ['information', 'verification', 'transcript', 'other'];

export async function POST(req: Request) {
  if (tooMany(`inq:${clientIp(req)}`, 5, 60 * 60 * 1000)) return NextResponse.json({ error: 'Too many messages from this connection. Please call the office at ' + SITE.phone + '.' }, { status: 429 });
  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  if (typeof b.website === 'string' && b.website) return NextResponse.json({ message: 'Thank you.' }); // honeypot
  const s = (k: string, max: number) => String(b[k] ?? '').trim().slice(0, max);
  const type: RequestType = TYPES.includes(b.request_type as RequestType) ? (b.request_type as RequestType) : 'information';
  const isRecord = type === 'transcript' || type === 'verification';
  const name = s('name', 120), email = s('email', 160), phone = s('phone', 40), program = s('program', 80);
  let message = s('message', 4000);
  const street = s('street', 160), city = s('city', 80), state = s('state', 40), zip = s('zip', 12);
  if (!name || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return NextResponse.json({ error: 'Please enter your name and a valid email.' }, { status: 400 });
  if (!isRecord && !message) return NextResponse.json({ error: 'Please enter your name, a valid email and a message.' }, { status: 400 });

  // Details for transcript and verification requests. Only the listed fields are kept.
  let details: Record<string, string> | null = null;
  if (isRecord) {
    details = {};
    for (const f of DETAIL_FIELDS[type]) {
      const v = s(`d_${f.key}`, f.max);
      if (f.required && !v) return NextResponse.json({ error: `Please complete: ${f.label}.` }, { status: 400 });
      if (v) details[f.key] = v;
    }
    if (b.auth !== 'yes') return NextResponse.json({ error: 'Please confirm the release authorization box.' }, { status: 400 });
    details.auth = 'yes';
    if (type === 'transcript') {
      if (!details.recipient_email && !details.recipient_address) return NextResponse.json({ error: 'Enter the recipient email address or a mailing address.' }, { status: 400 });
      if (details.recipient_email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(details.recipient_email)) return NextResponse.json({ error: 'The recipient email address is not valid.' }, { status: 400 });
    }
    if (!message) message = `${REQUEST_LABEL[type]} for ${details.student_name}.`;
  }
  const fee = type === 'transcript' ? FEES.transcript : type === 'verification' ? FEES.verification : 0;

  // Save first, so the request is never lost even if email or payment fails.
  const sbUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const sh = svc ? { apikey: svc, Authorization: `Bearer ${svc}`, 'Content-Type': 'application/json' } : null;
  let savedId: string | null = null;
  if (sh && sbUrl) {
    try {
      const ins = await fetch(`${sbUrl}/rest/v1/inquiries`, {
        method: 'POST',
        headers: { ...sh, Prefer: 'return=representation' },
        body: JSON.stringify({
          name, email, phone: phone || null, program: program || null, message, street: street || null, city: city || null, state: state || null, zip: zip || null,
          request_type: type, details, fee_cents: fee, status: fee ? 'awaiting_payment' : 'new',
        }),
      });
      if (ins.ok) savedId = (await ins.json().catch(() => []))?.[0]?.id ?? null;
    } catch { /* fall through to email */ }
  }

  // A paid request goes to Stripe first. The office is emailed when Stripe confirms payment (see the webhook).
  if (fee) {
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    const origin = process.env.SITE_URL || new URL(req.url).origin;
    if (!savedId || !stripeKey) return NextResponse.json({ error: `Online requests are not available right now. Please call ${SITE.phone} or email ${SITE.email}.` }, { status: 503 });
    const p = new URLSearchParams();
    p.set('mode', 'payment');
    p.set('success_url', `${origin}/payment/thanks?for=${type}`);
    p.set('cancel_url', `${origin}/#contact`);
    p.set('customer_email', email);
    p.set('line_items[0][quantity]', '1');
    p.set('line_items[0][price_data][currency]', 'usd');
    p.set('line_items[0][price_data][unit_amount]', String(fee));
    p.set('line_items[0][price_data][product_data][name]', `${REQUEST_LABEL[type]}, New Life Preparatory Academy`);
    p.set('metadata[source]', 'nlpa');
    p.set('metadata[item]', type);
    p.set('metadata[label]', `${REQUEST_LABEL[type]}, ${money(fee)}`);
    p.set('metadata[payer_name]', name);
    p.set('metadata[reference]', details?.student_id || details?.student_name || '');
    p.set('metadata[inquiry_id]', savedId);
    p.set('payment_intent_data[description]', `NLPA ${type} | ${details?.student_name || name}`);
    p.set('payment_intent_data[receipt_email]', email);
    const r = await fetch('https://api.stripe.com/v1/checkout/sessions', { method: 'POST', headers: { Authorization: `Bearer ${stripeKey}`, 'Content-Type': 'application/x-www-form-urlencoded' }, body: p });
    const j = await r.json().catch(() => ({}));
    if (!r.ok || !j.url) return NextResponse.json({ error: `Online payment is not available right now. Please call ${SITE.phone} or email ${SITE.email}.` }, { status: 502 });
    if (sh) fetch(`${sbUrl}/rest/v1/inquiries?id=eq.${savedId}`, { method: 'PATCH', headers: { ...sh, Prefer: 'return=minimal' }, body: JSON.stringify({ stripe_session_id: j.id }) }).catch(() => {});
    return NextResponse.json({ url: j.url });
  }

  const row: InquiryRow = { id: savedId || undefined, request_type: type, name, email, phone, program, message, street, city, state, zip, details };
  const emailed = await emailOffice(row);
  if (savedId && sh && sbUrl && emailed) {
    fetch(`${sbUrl}/rest/v1/inquiries?id=eq.${savedId}`, { method: 'PATCH', headers: { ...sh, Prefer: 'return=minimal' }, body: JSON.stringify({ emailed: true }) }).catch(() => {});
  }

  // The visitor sees success if the message was saved or emailed. Only if both failed do we ask them to call.
  if (!savedId && !emailed) return NextResponse.json({ error: FALLBACK }, { status: 502 });
  return NextResponse.json({ message: type === 'verification' ? 'Thank you. The registrar will review your verification request and confirm the authorization before anything is released. We will respond by email.' : 'Thank you. Dr. Jenkins and the NLPA office will respond within one business day.' });
}
