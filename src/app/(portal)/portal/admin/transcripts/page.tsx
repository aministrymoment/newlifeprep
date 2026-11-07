'use client';
import { useEffect, useRef, useState } from 'react';
import { useAuth } from '@/components/portal/useAuth';

declare global { interface Window { __nlpaTranscriptLoaded?: boolean } }

function loadScript(src: string) {
  return new Promise<void>((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src; s.onload = () => resolve(); s.onerror = () => reject(new Error(src));
    document.body.appendChild(s);
  });
}

export default function TranscriptGenerator() {
  const { profile, loading } = useAuth();
  const host = useRef<HTMLDivElement>(null);
  const [err, setErr] = useState('');
  const isAdmin = !!profile && profile.role === 'admin';

  useEffect(() => {
    if (!isAdmin) return;
    // The generator wires document level listeners once; a fresh page load keeps that clean.
    if (window.__nlpaTranscriptLoaded) { window.location.reload(); return; }
    let cancelled = false;
    const link = document.createElement('link');
    link.rel = 'stylesheet'; link.href = '/tools/nlpa-transcript.css';
    document.head.appendChild(link);
    (async () => {
      try {
        const html = await (await fetch('/tools/nlpa-transcript.html')).text();
        if (cancelled || !host.current) return;
        host.current.innerHTML = html;
        await loadScript('/tools/jszip.min.js');
        await loadScript('/tools/nlpa-transcript.js');
        window.__nlpaTranscriptLoaded = true;
      } catch (e) { setErr('The generator could not load. Please refresh the page.'); }
    })();
    return () => { cancelled = true; link.remove(); };
  }, [isAdmin]);

  if (loading) return <p style={{ padding: 24 }}>One moment...</p>;
  if (!isAdmin) return <p style={{ padding: 24 }}>Administrators only. Please sign in.</p>;
  return (
    <div>
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      {/* eslint-disable-next-line @next/next/no-page-custom-font */}
      <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
      <div style={{ background: '#0D1F3C', color: '#fff', padding: '10px 20px', fontFamily: 'Georgia, serif', fontSize: 14 }}>
        <a href="/portal/admin" style={{ color: '#C9A84C' }}>&larr; Back to administration</a>
      </div>
      {err && <p style={{ padding: 24 }}>{err}</p>}
      <div ref={host} />
    </div>
  );
}
