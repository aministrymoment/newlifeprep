import { NextResponse } from 'next/server';
import { tooMany } from '@/lib/rateLimit';

export const runtime = 'nodejs';
export const maxDuration = 30;
const URL_ = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const ANON = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Emails a stored transcript (PDF, optionally the Word copy) to a school, employer or other requester.
// Administrators only. A release authorization is required and every send is logged.
export async function POST(req: Request) {
  const auth = req.headers.get('authorization') || '';
  if (!auth.startsWith('Bearer ')) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const me = await fetch(`${URL_}/auth/v1/user`, { headers: { apikey: ANON, Authorization: auth } });
  if (!me.ok) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const uid = (await me.json()).id;
  const pr = await fetch(`${URL_}/rest/v1/profiles?id=eq.${uid}&select=role`, { headers: { apikey: ANON, Authorization: auth } });
  if ((await pr.json().catch(() => []))?.[0]?.role !== 'admin') return NextResponse.json({ error: 'Administrators only.' }, { status: 403 });
  if (tooMany(`tsend:${uid}`, 40, 60 * 60 * 1000)) return NextResponse.json({ error: 'Too many emails this hour. Please try again later.' }, { status: 429 });

  let b: any; try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const id = String(b.transcriptId || '');
  const to = String(b.to || '').trim();
  const toName = String(b.toName || '').trim().slice(0, 120);
  const authorizedBy = String(b.authorizedBy || '').trim().slice(0, 200);
  const message = String(b.message || '').trim().slice(0, 2000);
  if (!/^[0-9a-f-]{36}$/i.test(id)) return NextResponse.json({ error: 'Choose a transcript.' }, { status: 400 });
  if (!EMAIL_RE.test(to)) return NextResponse.json({ error: 'Enter a valid email address for the recipient.' }, { status: 400 });
  const list = (v: any) => String(v || '').split(/[,;\s]+/).map((x) => x.trim()).filter(Boolean).slice(0, 10);
  const cc = list(b.cc), bcc = list(b.bcc);
  if ([...cc, ...bcc].some((x) => !EMAIL_RE.test(x))) return NextResponse.json({ error: 'One of the CC or BCC addresses is not a valid email address.' }, { status: 400 });
  if (!authorizedBy) return NextResponse.json({ error: 'Confirm the release authorization and say who gave it.' }, { status: 400 });

  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const key = process.env.RESEND_API_KEY;
  if (!svc) return NextResponse.json({ error: 'Sending is not switched on yet. The SUPABASE_SERVICE_ROLE_KEY setting is missing.' }, { status: 503 });
  if (!key) return NextResponse.json({ error: 'Sending is not switched on yet. The RESEND_API_KEY setting is missing from the site settings.' }, { status: 503 });

  const sh = { apikey: svc, Authorization: `Bearer ${svc}` };
  const tr = await fetch(`${URL_}/rest/v1/transcripts?id=eq.${id}&select=student_name,pdf_path,docx_path,original_path,original_name`, { headers: sh });
  const t = (await tr.json().catch(() => []))?.[0];
  if (!t) return NextResponse.json({ error: 'That transcript was not found.' }, { status: 404 });
  if (!t.pdf_path && !t.original_path) return NextResponse.json({ error: 'This record has no file to send.' }, { status: 400 });

  const files: { path: string; name: string }[] = [];
  if (t.pdf_path) files.push({ path: t.pdf_path, name: `NLPA_Transcript_${String(t.student_name).replace(/[^A-Za-z0-9]+/g, '_')}.pdf` });
  else files.push({ path: t.original_path, name: t.original_name || 'transcript.pdf' });
  if (b.includeWord && t.docx_path) files.push({ path: t.docx_path, name: `NLPA_Transcript_${String(t.student_name).replace(/[^A-Za-z0-9]+/g, '_')}.docx` });

  const attachments: { filename: string; content: string }[] = [];
  for (const f of files) {
    const r = await fetch(`${URL_}/storage/v1/object/transcripts/${f.path.split('/').map(encodeURIComponent).join('/')}`, { headers: sh });
    if (!r.ok) return NextResponse.json({ error: 'The transcript file could not be read from storage.' }, { status: 502 });
    attachments.push({ filename: f.name, content: Buffer.from(await r.arrayBuffer()).toString('base64') });
  }

  const subject = String(b.subject || '').trim().slice(0, 160) || `Official transcript for ${t.student_name}, New Life Preparatory Academy`;
  const body = message || `Please find attached the transcript for ${t.student_name}, sent at the request and with the authorization of the student or parent or guardian.`;
  const html = `<div style="font-family:Georgia,serif;color:#0D1F3C;max-width:620px">
<p>${toName ? `Dear ${esc(toName)},` : 'Hello,'}</p>
<p>${esc(body).replace(/\n/g, '<br>')}</p>
<p>If you have questions or need verification, please contact the school office at (954) 851-6608 or newlifeprep@gmail.com.</p>
<p>Sincerely,<br><b>New Life Preparatory Academy</b><br>131 NE 9th Street, Pompano Beach, FL 33060<br>Florida DOE Private School ID 06-1840 | NCES ID A1300838<br><i>Excellence · Faith · Purpose</i></p></div>`;

  let ok = false, err = '';
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: process.env.TRANSCRIPT_FROM || process.env.INQUIRY_FROM || 'NLPA Registrar <onboarding@resend.dev>',
        to: [to],
        ...(cc.length ? { cc } : {}),
        ...(bcc.length ? { bcc } : {}),
        reply_to: process.env.TRANSCRIPT_REPLY_TO || 'newlifeprep@gmail.com',
        subject, html, attachments,
      }),
    });
    ok = r.ok;
    if (!r.ok) err = (await r.text().catch(() => '')).slice(0, 300);
  } catch (e: any) { err = String(e?.message || e).slice(0, 300); }

  await fetch(`${URL_}/rest/v1/transcript_sends`, {
    method: 'POST',
    headers: { ...sh, 'Content-Type': 'application/json', Prefer: 'return=minimal' },
    body: JSON.stringify({ transcript_id: id, to_email: to, cc: cc.join(', ') || null, bcc: bcc.join(', ') || null, to_name: toName || null, subject, message: body, authorized_by: authorizedBy, sent_by: uid, status: ok ? 'sent' : 'failed', error: ok ? null : err || 'Send failed' }),
  }).catch(() => {});

  if (!ok) return NextResponse.json({ error: 'The email could not be sent. The school office can check the sending address setup. Nothing was delivered.' }, { status: 502 });
  return NextResponse.json({ message: `Sent to ${to}.` });
}
