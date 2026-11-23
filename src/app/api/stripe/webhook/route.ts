import { NextResponse } from 'next/server';
import { createHmac, timingSafeEqual } from 'crypto';
import { CATALOG } from '@/lib/catalog';
import { emailOffice } from '@/lib/notify';

export const runtime = 'nodejs';

// Stripe signs every webhook. We refuse anything whose signature does not match our secret.
function verify(raw: string, header: string, secret: string): boolean {
  const parts = header.split(',').map((p) => p.split('='));
  const t = parts.find((p) => p[0] === 't')?.[1];
  const sigs = parts.filter((p) => p[0] === 'v1').map((p) => p[1]);
  if (!t || !sigs.length) return false;
  if (Math.abs(Date.now() / 1000 - Number(t)) > 300) return false;
  const expected = createHmac('sha256', secret).update(`${t}.${raw}`).digest('hex');
  const e = Buffer.from(expected, 'hex');
  return sigs.some((s) => { const b = Buffer.from(s, 'hex'); return b.length === e.length && timingSafeEqual(b, e); });
}

export async function POST(req: Request) {
  const secret = process.env.STRIPE_WEBHOOK_SECRET;
  const sbUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!secret || !svc || !sbUrl) return NextResponse.json({ error: 'Not configured.' }, { status: 503 });

  const raw = await req.text();
  if (!verify(raw, req.headers.get('stripe-signature') || '', secret)) return NextResponse.json({ error: 'Bad signature.' }, { status: 400 });

  let ev: any; try { ev = JSON.parse(raw); } catch { return NextResponse.json({ error: 'Bad body.' }, { status: 400 }); }
  const obj = ev?.data?.object || {};
  const headers = { apikey: svc, Authorization: `Bearer ${svc}`, 'Content-Type': 'application/json' };

  try {
    if (ev.type === 'checkout.session.completed') {
      // Only record payments that came from this website. Other apps on the same Stripe account are ignored.
      if (obj.metadata?.source !== 'nlpa' || obj.payment_status !== 'paid') return NextResponse.json({ ok: true, ignored: true });
      const item = CATALOG.find((c) => c.id === obj.metadata?.item);
      const r = await fetch(`${sbUrl}/rest/v1/payments?on_conflict=stripe_session_id`, {
        method: 'POST',
        headers: { ...headers, Prefer: 'resolution=ignore-duplicates,return=minimal' },
        body: JSON.stringify({
          stripe_session_id: obj.id,
          payment_intent: obj.payment_intent || null,
          item: String(obj.metadata?.item || 'unknown').slice(0, 60),
          label: item?.label || String(obj.metadata?.label || '').slice(0, 120) || null,
          amount_cents: Number(obj.amount_total || 0),
          currency: obj.currency || 'usd',
          payer_name: String(obj.metadata?.payer_name || obj.customer_details?.name || '').slice(0, 120) || null,
          payer_email: obj.customer_details?.email || obj.customer_email || null,
          reference: String(obj.metadata?.reference || '').slice(0, 80) || null,
        }),
      });
      if (!r.ok) return NextResponse.json({ error: 'Could not save.' }, { status: 500 });

      // A paid transcript or verification request from the landing page: mark it paid and email the office.
      const inqId = String(obj.metadata?.inquiry_id || '');
      if (/^[0-9a-f-]{36}$/i.test(inqId)) {
        const up = await fetch(`${sbUrl}/rest/v1/inquiries?id=eq.${inqId}`, {
          method: 'PATCH',
          headers: { ...headers, Prefer: 'return=representation' },
          body: JSON.stringify({ paid: true, paid_at: new Date().toISOString(), status: 'new', stripe_session_id: obj.id }),
        });
        const q = up.ok ? (await up.json().catch(() => []))?.[0] : null;
        if (q) {
          const sent = await emailOffice({ ...q, paid: true });
          if (sent) await fetch(`${sbUrl}/rest/v1/inquiries?id=eq.${inqId}`, { method: 'PATCH', headers: { ...headers, Prefer: 'return=minimal' }, body: JSON.stringify({ emailed: true }) }).catch(() => {});
        }
      }
    } else if (ev.type === 'charge.refunded') {
      if (!obj.payment_intent) return NextResponse.json({ ok: true });
      const full = Number(obj.amount_refunded || 0) >= Number(obj.amount || 0);
      const r = await fetch(`${sbUrl}/rest/v1/payments?payment_intent=eq.${encodeURIComponent(obj.payment_intent)}`, {
        method: 'PATCH',
        headers: { ...headers, Prefer: 'return=minimal' },
        body: JSON.stringify({ refunded_cents: Number(obj.amount_refunded || 0), status: full ? 'refunded' : 'partially_refunded' }),
      });
      if (!r.ok) return NextResponse.json({ error: 'Could not save.' }, { status: 500 });
    }
  } catch { return NextResponse.json({ error: 'Could not save.' }, { status: 500 }); }
  return NextResponse.json({ ok: true });
}
