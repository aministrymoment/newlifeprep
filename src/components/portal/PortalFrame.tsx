'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import { supabase } from '@/lib/supabase';
import { useAuth } from './useAuth';

export default function PortalFrame({ children, adminOnly = false }: { children: (ctx: ReturnType<typeof useAuth>) => React.ReactNode; adminOnly?: boolean }) {
  const auth = useAuth();
  const router = useRouter();
  const { session, profile, loading } = auth;

  useEffect(() => { if (!loading && !session) router.replace('/portal/login'); }, [loading, session, router]);

  if (loading || !session) return <div className="p-center"><p className="p-muted">Loading...</p></div>;
  if (adminOnly && profile?.role !== 'admin') return <div className="p-center"><p>This page is for administrators.</p><Link href="/portal" className="p-btn">Back to Dashboard</Link></div>;

  return (
    <>
      <header className="p-head">
        <Link href="/portal" className="p-brand"><span className="p-chip"><img src="/logos/NLPA_Block_Logo_400.png" alt="NLPA" /></span><span><b>New Life Preparatory Academy</b><i>Student Portal</i></span></Link>
        <nav className="p-nav">
          <Link href="/portal">Dashboard</Link>
          {profile?.role === 'admin' && <Link href="/portal/admin">Administration</Link>}
          <span className="p-who">{profile?.full_name || session.user.email}{profile?.student_id ? ` · ${profile.student_id}` : ''}</span>
          <button className="p-link" onClick={async () => { await supabase().auth.signOut(); router.replace('/portal/login'); }}>Sign Out</button>
        </nav>
      </header>
      <main className="p-main">{children(auth)}</main>
      <footer className="p-foot">Excellence · Faith · Purpose · FL DOE Private School ID 06-1840</footer>
    </>
  );
}
