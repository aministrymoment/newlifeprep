'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PasswordField from '@/components/portal/PasswordField';

// Students arrive here from the reset email, already verified by Supabase, and choose a new password.
export default function Reset() {
  const router = useRouter();
  const [ready, setReady] = useState(false);
  const [checked, setChecked] = useState(false);
  const [pw, setPw] = useState('');
  const [pw2, setPw2] = useState('');
  const [msg, setMsg] = useState('');
  const [busy, setBusy] = useState(false);
  const [done, setDone] = useState(false);

  useEffect(() => {
    const sb = supabase();
    const { data: sub } = sb.auth.onAuthStateChange((e, s) => { if (e === 'PASSWORD_RECOVERY' || s) { setReady(true); setChecked(true); } });
    sb.auth.getSession().then(({ data }) => { if (data.session) setReady(true); });
    const t = setTimeout(() => setChecked(true), 2500);
    return () => { sub.subscription.unsubscribe(); clearTimeout(t); };
  }, []);

  async function submit(e: React.FormEvent) {
    e.preventDefault(); setMsg('');
    if (pw.length < 8) { setMsg('Please use at least 8 characters.'); return; }
    if (pw !== pw2) { setMsg('The two passwords do not match.'); return; }
    setBusy(true);
    const { error } = await supabase().auth.updateUser({ password: pw });
    setBusy(false);
    if (error) { setMsg('We could not save the new password. The link may have expired. Please request a new one.'); return; }
    setDone(true);
    setTimeout(() => router.replace('/portal'), 1800);
  }

  return (
    <div className="p-login">
      <form className="p-card p-loginbox" onSubmit={submit}>
        <span className="p-chip big"><img src="/logos/NLPA_Block_Logo_800.png" alt="New Life Preparatory Academy" /></span>
        <h1>Choose a New Password</h1>
        {done ? <p className="p-note">Your password is saved. Taking you to your dashboard.</p> : ready ? (
          <>
            <PasswordField label="New password" value={pw} onChange={setPw} autoComplete="new-password" minLength={8} />
            <PasswordField label="Type it again" value={pw2} onChange={setPw2} autoComplete="new-password" minLength={8} />
            {msg && <p className="p-note">{msg}</p>}
            <button className="p-btn" disabled={busy}>{busy ? 'Saving...' : 'Save Password'}</button>
          </>
        ) : checked ? <p className="p-note">This reset link is not valid or has expired. Please return to sign in and choose Forgot your password to get a new one.</p> : <p className="p-muted">One moment...</p>}
        <p className="p-small"><Link href="/portal/login">Back to sign in</Link></p>
      </form>
    </div>
  );
}
