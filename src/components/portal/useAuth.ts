'use client';
import { useEffect, useState } from 'react';
import type { Session } from '@supabase/supabase-js';
import { supabase } from '@/lib/supabase';

export type Profile = { id: string; email: string | null; full_name: string | null; student_id: string | null; role: 'student' | 'admin' };

export function useAuth() {
  const [session, setSession] = useState<Session | null>(null);
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const sb = supabase();
    let alive = true;
    async function load(s: Session | null) {
      if (!alive) return;
      setSession(s);
      if (s) {
        const { data } = await sb.from('profiles').select('*').eq('id', s.user.id).maybeSingle();
        if (alive) setProfile((data as Profile) || null);
      } else setProfile(null);
      if (alive) setLoading(false);
    }
    sb.auth.getSession().then(({ data }) => load(data.session));
    const { data: sub } = sb.auth.onAuthStateChange((_e, s) => { load(s); });
    return () => { alive = false; sub.subscription.unsubscribe(); };
  }, []);

  return { session, profile, loading };
}
