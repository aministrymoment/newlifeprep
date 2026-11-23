import { SITE } from '@/site';
import { DETAIL_FIELDS, REQUEST_LABEL, money, type RequestType } from '@/lib/fees';

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] as string));

export type InquiryRow = {
  id?: string; request_type: RequestType; name: string; email: string; phone?: string | null; program?: string | null;
  message?: string | null; street?: string | null; city?: string | null; state?: string | null; zip?: string | null;
  details?: Record<string, string> | null; fee_cents?: number; paid?: boolean;
};

// Emails the school office about a website request. Returns true when Resend accepted it.
export async function emailOffice(q: InquiryRow): Promise<boolean> {
  const key = process.env.RESEND_API_KEY;
  if (!key) return false;
  const kind = REQUEST_LABEL[q.request_type] || 'Website inquiry';
  const rows: string[] = [
    `<p><b>Request:</b> ${esc(kind)}${q.fee_cents ? ` (${money(q.fee_cents)}${q.paid ? ' PAID' : ' not yet paid'})` : ''}</p>`,
    `<p><b>Name:</b> ${esc(q.name)}</p><p><b>Email:</b> ${esc(q.email)}</p><p><b>Phone:</b> ${esc(q.phone || '')}</p>`,
  ];
  if (q.program) rows.push(`<p><b>Program:</b> ${esc(q.program)}</p>`);
  if (q.request_type === 'transcript' || q.request_type === 'verification') {
    const f = DETAIL_FIELDS[q.request_type];
    for (const d of f) if (q.details?.[d.key]) rows.push(`<p><b>${esc(d.label)}:</b> ${esc(String(q.details[d.key]))}</p>`);
    rows.push(`<p><b>Release authorization confirmed on the form:</b> ${q.details?.auth === 'yes' ? 'Yes' : 'No'}</p>`);
  } else {
    const addr = [q.street, [q.city, q.state, q.zip].filter(Boolean).join(' ')].filter(Boolean).join(', ');
    rows.push(`<p><b>Mailing address:</b> ${esc(addr)}</p>`);
  }
  if (q.message) rows.push(`<p><b>Message:</b><br>${esc(q.message).replace(/\n/g, '<br>')}</p>`);
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: process.env.INQUIRY_FROM || 'NLPA Website <onboarding@resend.dev>',
        to: [process.env.INQUIRY_TO || SITE.email],
        reply_to: q.email,
        subject: `${kind}${q.fee_cents && q.paid ? ' (paid)' : ''}: ${q.name}${q.program ? ` (${q.program})` : ''}`,
        html: rows.join(''),
      }),
    });
    return r.ok;
  } catch { return false; }
}
