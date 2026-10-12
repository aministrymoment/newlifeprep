'use client';
import Link from 'next/link';
import { useParams, useSearchParams } from 'next/navigation';
import { Suspense, useEffect, useState } from 'react';
import PortalFrame from '@/components/portal/PortalFrame';

type Book = { slug: string; name: string; chapters: number };

function Reader({ slug, ch, back }: { slug: string; ch: number; back: string }) {
  const [books, setBooks] = useState<Book[] | null>(null);
  const [verses, setVerses] = useState<string[] | null>(null);
  const [bad, setBad] = useState(false);

  useEffect(() => { fetch('/kjv/books.json').then((r) => r.json()).then(setBooks).catch(() => setBad(true)); }, []);
  const book = books?.find((b) => b.slug === slug);
  useEffect(() => {
    if (!book) return;
    setVerses(null);
    fetch(`/kjv/${book.slug}.json`).then((r) => r.json()).then((d: string[][]) => { const c = d[ch - 1]; if (c) setVerses(c); else setBad(true); }).catch(() => setBad(true));
  }, [book, ch]);

  const q = back ? `?back=${encodeURIComponent(back)}` : '';
  const href = (b: string, c: number) => `/portal/bible/${b}/${c}${q}`;
  const idx = books && book ? books.findIndex((b) => b.slug === book.slug) : -1;
  const prev = !book ? null : ch > 1 ? href(book.slug, ch - 1) : idx > 0 ? href(books![idx - 1].slug, books![idx - 1].chapters) : null;
  const next = !book ? null : ch < book.chapters ? href(book.slug, ch + 1) : idx >= 0 && idx < books!.length - 1 ? href(books![idx + 1].slug, 1) : null;

  if (bad || (books && !book) || !(ch >= 1)) return <div className="p-card"><p>That chapter was not found.</p>{back ? <Link className="p-btn" href={back}>Back to your lesson</Link> : <Link className="p-btn" href="/portal">Back to Dashboard</Link>}</div>;
  if (!book || !verses) return <p className="p-muted">Loading...</p>;

  const top = back ? <Link className="p-btn" href={back}>← Back to your lesson</Link> : <Link className="p-link" href="/portal">← Dashboard</Link>;
  return (
    <>
      {top}
      <p className="p-tag" style={{ marginTop: 14 }}>King James Version</p>
      <h1 className="p-h1">{book.name} {ch}</h1>
      <div className="p-card" style={{ lineHeight: 1.8, fontSize: '1.05rem' }}>
        {verses.map((v, i) => <p key={i} style={{ margin: '0 0 8px' }}><sup style={{ color: '#C9A84C', fontWeight: 700, marginRight: 6 }}>{i + 1}</sup>{v}</p>)}
      </div>
      <div className="p-stepnav">
        {prev ? <Link className="p-btn ghost" href={prev}>← Previous chapter</Link> : <span />}
        {next ? <Link className="p-btn ghost" href={next}>Next chapter →</Link> : <span />}
      </div>
      {back && <p style={{ marginTop: 18 }}>{top}</p>}
    </>
  );
}

function Inner() {
  const params = useParams<{ book: string; chapter: string }>();
  const sp = useSearchParams();
  const raw = sp.get('back') || '';
  const back = raw.startsWith('/portal/') && !raw.startsWith('//') ? raw : '';
  return <PortalFrame>{() => <Reader slug={decodeURIComponent(params.book)} ch={parseInt(params.chapter, 10)} back={back} />}</PortalFrame>;
}

export default function Page() {
  return <Suspense fallback={null}><Inner /></Suspense>;
}
