import { NextResponse } from 'next/server';

export const runtime = 'nodejs';
const URL_ = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const ANON = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

// Creates a student login. Only a signed in administrator may call this.
export async function POST(req: Request) {
  const auth = req.headers.get('authorization') || '';
  if (!auth.startsWith('Bearer ')) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const me = await fetch(`${URL_}/auth/v1/user`, { headers: { apikey: ANON, Authorization: auth } });
  if (!me.ok) return NextResponse.json({ error: 'Please sign in again.' }, { status: 401 });
  const uid = (await me.json()).id;
  const pr = await fetch(`${URL_}/rest/v1/profiles?id=eq.${uid}&select=role`, { headers: { apikey: ANON, Authorization: auth } });
  if ((await pr.json().catch(() => []))?.[0]?.role !== 'admin') return NextResponse.json({ error: 'Administrators only.' }, { status: 403 });

  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!key) return NextResponse.json({ error: 'Adding students here is not switched on yet. The office key has not been added to the site settings.' }, { status: 503 });

  let b: any; try { b = await req.json(); } catch { return NextResponse.json({ error: 'Invalid request.' }, { status: 400 }); }
  const email = String(b.email || '').trim().toLowerCase();
  const name = String(b.name || '').trim().slice(0, 120);
  const password = String(b.password || '');
  const sid = String(b.studentId || '').trim().toUpperCase();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || !name) return NextResponse.json({ error: 'Enter the student name and a valid email.' }, { status: 400 });
  if (password.length < 8) return NextResponse.json({ error: 'The temporary password must be at least 8 characters.' }, { status: 400 });
  if (sid && !/^NLPA-\d{4}-\d{3}$/.test(sid)) return NextResponse.json({ error: 'Student ID must look like NLPA-2026-001.' }, { status: 400 });

  const cr = await fetch(`${URL_}/auth/v1/admin/users`, {
    method: 'POST',
    headers: { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, email_confirm: true, user_metadata: { full_name: name } }),
  });
  const created = await cr.json().catch(() => ({}));
  if (!cr.ok) return NextResponse.json({ error: /already|registered/i.test(JSON.stringify(created)) ? 'That email already has an account.' : 'Could not create the account.' }, { status: 400 });

  const up = await fetch(`${URL_}/rest/v1/profiles?id=eq.${created.id}`, {
    method: 'PATCH',
    headers: { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json', Prefer: 'return=minimal' },
    body: JSON.stringify({ full_name: name, student_id: sid || null }),
  });
  if (!up.ok) return NextResponse.json({ ok: true, warning: 'Account created, but the Student ID was not saved. It may already be in use. Set it below.' });
  return NextResponse.json({ ok: true });
}
