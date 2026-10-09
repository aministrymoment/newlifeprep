import { NextResponse } from 'next/server';
import { CATALOG } from '@/lib/catalog';
import { SITE } from '@/site';

export const runtime = 'nodejs';
const FALLBACK = `Online payment is not available right now. Please call ${SITE.phone} or email ${SITE.email}.`;

export async function POST(req: Request) {
  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const item = CATALOG.find((c) => c.id === b.item);
  const name = String(b.name ?? '').trim().slice(0, 120);
  const email = String(b.email ?? '').trim().slice(0, 160);
  const reference = String(b.reference ?? '').trim().slice(0, 80);
  if (!item || !name || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return NextResponse.json({ error: 'Please complete all fields.' }, { status: 400 });
  if (item.needs !== 'name' && !reference) return NextResponse.json({ error: 'Please enter your Student ID or program.' }, { status: 400 });

  let cents = item.amountCents;
  if (cents === null) {
    const dollars = Math.floor(Number(b.amount));
    if (!Number.isFinite(dollars) || dollars < 1 || dollars > 50000) return NextResponse.json({ error: 'Enter a donation between $1 and $50,000.' }, { status: 400 });
    cents = dollars * 100;
  }

  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) return NextResponse.json({ error: FALLBACK }, { status: 503 });
  const origin = process.env.SITE_URL || new URL(req.url).origin;

  const p = new URLSearchParams();
  p.set('mode', 'payment');
  p.set('success_url', `${origin}/payment/thanks`);
  p.set('cancel_url', `${origin}/payment`);
  p.set('customer_email', email);
  p.set('line_items[0][quantity]', '1');
  p.set('line_items[0][price_data][currency]', 'usd');
  p.set('line_items[0][price_data][unit_amount]', String(cents));
  p.set('line_items[0][price_data][product_data][name]', item.id === 'donation' ? 'Donation to New Life Preparatory Academy' : item.label.replace(/,\s*\$[\d,.]+$/, ''));
  p.set('metadata[item]', item.id);
  p.set('metadata[payer_name]', name);
  p.set('metadata[reference]', reference);
  p.set('payment_intent_data[description]', `NLPA ${item.id} | ${name} | ${reference}`);
  p.set('payment_intent_data[receipt_email]', email);

  const r = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/x-www-form-urlencoded' },
    body: p,
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.url) return NextResponse.json({ error: FALLBACK }, { status: 502 });
  return NextResponse.json({ url: j.url });
}
