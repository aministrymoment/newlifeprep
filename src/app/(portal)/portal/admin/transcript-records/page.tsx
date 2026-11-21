'use client';
import { useCallback, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import PortalFrame from '@/components/portal/PortalFrame';

type Rec = { id: string; student_name: string; student_id: string | null; kind: string; school_from: string | null; docx_path: string | null; pdf_path: string | null; original_path: string | null; original_name: string | null; created_at: string; updated_at: string };
type Send = { id: string; transcript_id: string; to_email: string; cc: string | null; bcc: string | null; to_name: string | null; authorized_by: string; sent_at: string; status: string };

function Library() {
  const [recs, setRecs] = useState<Rec[]>([]);
  const [sends, setSends] = useState<Send[]>([]);
  const [q, setQ] = useState('');
  const [msg, setMsg] = useState('');
  const [open, setOpen] = useState<string | null>(null);
  const [to, setTo] = useState(''); const [toName, setToName] = useState(''); const [subject, setSubject] = useState('');
  const [cc, setCc] = useState(''); const [bcc, setBcc] = useState(''); const [copyMe, setCopyMe] = useState(true);
  const [note, setNote] = useState(''); const [by, setBy] = useState(''); const [ok, setOk] = useState(false); const [word, setWord] = useState(false);
  const [busy, setBusy] = useState(false);

  const load = useCallback(async () => {
    const sb = supabase();
    const [r, s] = await Promise.all([
      sb.from('transcripts').select('id,student_name,student_id,kind,school_from,docx_path,pdf_path,original_path,original_name,created_at,updated_at').order('updated_at', { ascending: false }),
      sb.from('transcript_sends').select('id,transcript_id,to_email,cc,bcc,to_name,authorized_by,sent_at,status').order('sent_at', { ascending: false }),
    ]);
    setRecs((r.data || []) as Rec[]); setSends((s.data || []) as Send[]);
  }, []);
  useEffect(() => { load(); }, [load]);

  async function download(path: string, name: string) {
    const { data, error } = await supabase().storage.from('transcripts').createSignedUrl(path, 60, { download: name });
    if (error || !data) { setMsg('That file could not be opened.'); return; }
    window.location.href = data.signedUrl;
  }
  async function remove(r: Rec) {
    if (!confirm(`Delete the stored record for ${r.student_name}? The files and send history are removed. This cannot be undone.`)) return;
    const paths = [r.docx_path, r.pdf_path, r.original_path].filter(Boolean) as string[];
    if (paths.length) await supabase().storage.from('transcripts').remove(paths);
    const { error } = await supabase().from('transcripts').delete().eq('id', r.id);
    setMsg(error ? `Could not delete: ${error.message}` : 'Deleted.'); load();
  }
  async function send(r: Rec) {
    setMsg('');
    if (!ok || !by.trim()) { setMsg('Confirm the release authorization and enter who gave it.'); return; }
    setBusy(true);
    try {
      const { data: s } = await supabase().auth.getSession();
      const res = await fetch('/api/admin/transcript-send', { method: 'POST', headers: { 'content-type': 'application/json', authorization: `Bearer ${s.session?.access_token}` }, body: JSON.stringify({ transcriptId: r.id, to, toName, subject, cc, bcc: [bcc, copyMe ? 'newlifeprep@gmail.com' : ''].filter(Boolean).join(','), message: note, authorizedBy: by, includeWord: word }) });
      const j = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(j.error || 'The email could not be sent.');
      setMsg(j.message || 'Sent.'); setOpen(null); setTo(''); setToName(''); setSubject(''); setCc(''); setBcc(''); setNote(''); setBy(''); setOk(false); setWord(false); load();
    } catch (e: any) { setMsg(e.message || 'The email could not be sent.'); }
    setBusy(false);
  }
  const shown = recs.filter((r) => !q.trim() || `${r.student_name} ${r.student_id || ''} ${r.school_from || ''}`.toLowerCase().includes(q.toLowerCase()));
  const fmt = (d: string) => new Date(d).toLocaleDateString();

  return (
    <>
      <h1 className="p-h1">Transcript Library</h1>
      <p className="p-small"><a href="/portal/admin">Back to Administration</a> | <a href="/portal/admin/transcripts">Open the Transcript Generator</a></p>
      <p className="p-muted">Every saved NLPA transcript and every stored original from a former school. Files are private and visible to administrators only.</p>
      <input className="p-input" placeholder="Search by student name, ID or former school" value={q} onChange={(e) => setQ(e.target.value)} style={{ maxWidth: 420 }} />
      {msg && <p className="p-note">{msg}</p>}
      {shown.length === 0 && <p className="p-muted">No stored transcripts yet. Make one in the Transcript Generator and press Save to transcript library.</p>}
      {shown.map((r) => {
        const mine = sends.filter((x) => x.transcript_id === r.id);
        return (
          <div key={r.id} className="p-card" style={{ margin: '12px 0' }}>
            <h2 className="p-h2" style={{ marginTop: 0 }}>{r.student_name}</h2>
            <p className="p-small">{r.kind === 'nlpa' ? 'NLPA transcript' : 'Original from a former school'}{r.student_id ? ` | ${r.student_id}` : ''}{r.school_from ? ` | From ${r.school_from}` : ''} | Updated {fmt(r.updated_at)}</p>
            <div className="p-row">
              {r.pdf_path && <button className="p-btn" onClick={() => download(r.pdf_path!, `NLPA_Transcript_${r.student_name.replace(/\W+/g, '_')}.pdf`)}>PDF</button>}
              {r.docx_path && <button className="p-btn" onClick={() => download(r.docx_path!, `NLPA_Transcript_${r.student_name.replace(/\W+/g, '_')}.docx`)}>Word</button>}
              {r.original_path && <button className="p-btn" onClick={() => download(r.original_path!, r.original_name || 'original')}>Original file</button>}
              {r.kind === 'nlpa' && <a className="p-btn" href={`/portal/admin/transcripts?record=${r.id}`}>Open to correct</a>}
              <button className="p-btn" onClick={() => setOpen(open === r.id ? null : r.id)}>Email this transcript</button>
              <button className="p-btn" onClick={() => remove(r)}>Delete</button>
            </div>
            {open === r.id && (
              <div style={{ marginTop: 12, display: 'grid', gap: 8, maxWidth: 560 }}>
                <input className="p-input" placeholder="Recipient email" value={to} onChange={(e) => setTo(e.target.value)} />
                <input className="p-input" placeholder="Recipient name or office (optional)" value={toName} onChange={(e) => setToName(e.target.value)} />
                <input className="p-input" placeholder="CC (optional, separate several with commas)" value={cc} onChange={(e) => setCc(e.target.value)} />
                <input className="p-input" placeholder="BCC (optional, hidden from the recipient)" value={bcc} onChange={(e) => setBcc(e.target.value)} />
                <label><input type="checkbox" checked={copyMe} onChange={(e) => setCopyMe(e.target.checked)} /> Send a copy to the school office (newlifeprep@gmail.com, hidden)</label>
                <input className="p-input" placeholder="Subject (optional)" value={subject} onChange={(e) => setSubject(e.target.value)} />
                <textarea className="p-input" rows={3} placeholder="Message (optional)" value={note} onChange={(e) => setNote(e.target.value)} />
                {r.docx_path && <label><input type="checkbox" checked={word} onChange={(e) => setWord(e.target.checked)} /> Also attach the Word copy</label>}
                <input className="p-input" placeholder="Who authorized this release? (student, parent or guardian name)" value={by} onChange={(e) => setBy(e.target.value)} />
                <label><input type="checkbox" checked={ok} onChange={(e) => setOk(e.target.checked)} /> The student, or a parent or guardian if the student is a minor, has authorized this release.</label>
                <div><button className="p-btn" disabled={busy} onClick={() => send(r)}>{busy ? 'Sending…' : 'Send'}</button></div>
              </div>
            )}
            {mine.length > 0 && (
              <details style={{ marginTop: 10 }}>
                <summary>Sent {mine.length} time{mine.length === 1 ? '' : 's'}</summary>
                <ul>{mine.map((x) => <li key={x.id} className="p-small">{fmt(x.sent_at)}: {x.to_name ? `${x.to_name}, ` : ''}{x.to_email}{x.cc ? `, CC ${x.cc}` : ''}{x.bcc ? `, BCC ${x.bcc}` : ''} ({x.status}). Authorized by {x.authorized_by}.</li>)}</ul>
              </details>
            )}
          </div>
        );
      })}
    </>
  );
}

export default function Page() {
  return <PortalFrame adminOnly>{() => <Library />}</PortalFrame>;
}
