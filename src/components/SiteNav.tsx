'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';

const LINKS = [
  ['/about', 'About'], ['/programs', 'Programs'], ['/admissions', 'Admissions'],
  ['/athletics', 'Athletics'], ['/scholarships', 'Scholarships'], ['/payment', 'Payment'],
  ['/faqs', 'FAQs'], ['/contact', 'Contact'],
];

export default function SiteNav() {
  const path = usePathname();
  const [open, setOpen] = useState(false);
  const [portal, setPortal] = useState<{ href: string; label: string }>({ href: '/portal/login', label: 'Student Login' });

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const sb = supabase();
        const { data } = await sb.auth.getSession();
        if (!data.session) return;
        const { data: p } = await sb.from('profiles').select('role').eq('id', data.session.user.id).maybeSingle();
        if (alive) setPortal(p?.role === 'admin' ? { href: '/portal/admin', label: 'Administration' } : { href: '/portal', label: 'My Portal' });
      } catch { /* stay on the default link */ }
    })();
    return () => { alive = false; };
  }, []);
  return (
    <nav className={open ? 'nav-open' : ''}>
      <Link href="/" className="nav-logo" onClick={() => setOpen(false)}>
        <span className="logo-chip"><img src="/logos/NLPA_Block_Logo_400.png" alt="New Life Preparatory Academy" /></span>
        <span className="nav-logo-text">
          <span className="nav-logo-name">New Life Preparatory Academy</span>
          <span className="nav-logo-tagline">Excellence · Faith · Purpose</span>
        </span>
      </Link>
      <button className="nav-toggle" aria-label="Menu" aria-expanded={open} onClick={() => setOpen(!open)}>
        <span /><span /><span />
      </button>
      <ul className="nav-links">
        {LINKS.map(([href, label]) => (
          <li key={href}><Link href={href} className={path === href ? 'active' : ''} onClick={() => setOpen(false)}>{label}</Link></li>
        ))}
        <li className="nav-portal-li"><Link href={portal.href} className="nav-portal" onClick={() => setOpen(false)}>{portal.label}</Link></li>
        <li className="nav-cta-li"><Link href="/contact" className="nav-cta" onClick={() => setOpen(false)}>Apply Now</Link></li>
      </ul>
    </nav>
  );
}
