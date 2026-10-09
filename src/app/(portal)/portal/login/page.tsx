'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');
  const [mode, setMode] = useState<'in' | 'reset'>('in');
  const [busy, setBusy] = useState(false);

  useEffect(() => { supabase().auth.getSession().then(({ data }) => { if (data.session) router.replace('/portal'); }); }, [router]);

  async function submit(e: React.FormEvent) {
    e.preventDefault(); setBusy(true); setMsg('');
    if (mode === 'in') {
      const { error } = await supabase().auth.signInWithPassword({ email: email.trim(), password });
      if (error) { setMsg('That email or password did not work. Please try again or ask the office for help.'); setBusy(false); return; }
      router.replace('/portal');
    } else {
      const { error } = await supabase().auth.resetPasswordForEmail(email.trim(), { redirectTo: `${window.location.origin}/portal/login` });
      setMsg(error ? 'We could not send that email. Please contact the office.' : 'If that email has an account, a reset link is on its way.');
      setBusy(false);
    }
  }

  return (
    <div className="p-login">
      <form className="p-card p-loginbox" onSubmit={submit}>
        <span className="p-chip big"><img src="/logos/NLPA_Block_Logo_800.png" alt="New Life Preparatory Academy" /></span>
        <h1>Student Portal</h1>
        <p className="p-muted">{mode === 'in' ? 'Sign in to continue your coursework.' : 'Enter your email and we will send a reset link.'}</p>
        <label>Email<input type="email" required value={email} onChange={(e) => setEmail(e.target.value)} autoComplete="email" /></label>
        {mode === 'in' && <label>Password<input type="password" required value={password} onChange={(e) => setPassword(e.target.value)} autoComplete="current-password" /></label>}
        {msg && <p className="p-note">{msg}</p>}
        <button className="p-btn" disabled={busy}>{busy ? 'Please wait...' : mode === 'in' ? 'Sign In' : 'Send Reset Link'}</button>
        <button type="button" className="p-link" onClick={() => { setMode(mode === 'in' ? 'reset' : 'in'); setMsg(''); }}>{mode === 'in' ? 'Forgot your password?' : 'Back to sign in'}</button>
        <p className="p-small">New student? Contact the office at (954) 851-6608 or newlifeprep@gmail.com. <Link href="/">Return to the school website</Link></p>
      </form>
    </div>
  );
}
