'use client';
import { Suspense, useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import { supabase } from '@/lib/supabase';
import { useAuth } from '@/components/portal/useAuth';
import { AVERY, perSheet } from '@/lib/avery';

type Q = { id: string; name: string; street: string | null; city: string | null; state: string | null; zip: string | null };

function Labels() {
  const { profile, loading } = useAuth();
  const params = useSearchParams();
  const num = (params.get('avery') || '5160').trim();
  const start = Math.max(1, Number(params.get('start')) || 1);
  const ids = (params.get('ids') || '').split(',').filter(Boolean);
  const sheet = AVERY[num];
  const [rows, setRows] = useState<Q[] | null>(null);

  useEffect(() => {
    if (!profile || profile.role !== 'admin' || !ids.length) return;
    supabase().from('inquiries').select('id,name,street,city,state,zip').in('id', ids).then(({ data }) => {
      const byId = new Map((data || []).map((r: any) => [r.id, r as Q]));
      setRows(ids.map((i) => byId.get(i)).filter(Boolean) as Q[]);
    });
  }, [profile, params]); // eslint-disable-line react-hooks/exhaustive-deps

  if (loading) return <p style={{ padding: 24 }}>One moment...</p>;
  if (!profile || profile.role !== 'admin') return <p style={{ padding: 24 }}>Administrators only. Please sign in.</p>;
  if (!sheet) return <p style={{ padding: 24 }}>Avery {num} is not on the list yet. Supported numbers: 5160, 5161, 5162, 5163, 5164 (and the matching 5260, 8160, 5261, 8161, 8162, 5263, 8163, 8164).</p>;
  if (!rows) return <p style={{ padding: 24 }}>Loading labels...</p>;

  const n = perSheet(sheet);
  const cells: (Q | null)[] = [...Array(start - 1).fill(null), ...rows];
  const sheets: (Q | null)[][] = [];
  for (let i = 0; i < cells.length; i += n) sheets.push(cells.slice(i, i + n));

  return (
    <div>
      <style>{`
        @page { size: 8.5in 11in; margin: 0; }
        body { background: #e9e6df; }
        .lb-bar { position: sticky; top: 0; z-index: 5; background: #0D1F3C; color: #fff; padding: 12px 20px; display: flex; gap: 16px; align-items: center; flex-wrap: wrap; font-family: Georgia, serif; font-size: 14px; }
        .lb-bar button { background: #C9A84C; color: #0D1F3C; border: 0; padding: 8px 18px; font-weight: bold; cursor: pointer; font-size: 14px; }
        .lb-sheet { position: relative; width: 8.5in; height: 11in; margin: 16px auto; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,.2); page-break-after: always; break-after: page; overflow: hidden; }
        .lb-cell { position: absolute; box-sizing: border-box; padding: 0.08in 0.12in; overflow: hidden; font-family: Arial, Helvetica, sans-serif; color: #000; line-height: 1.2; display: flex; flex-direction: column; justify-content: center; }
        .lb-cell b { font-weight: bold; }
        @media print { body { background: #fff; } .lb-bar { display: none; } .lb-sheet { margin: 0; box-shadow: none; } }
      `}</style>
      <div className="lb-bar">
        <button onClick={() => window.print()}>Print labels</button>
        <span>Avery {num} · {rows.length} label{rows.length === 1 ? '' : 's'} · starting at label {start} · {sheets.length} sheet{sheets.length === 1 ? '' : 's'}</span>
        <span>In the print window: Paper Letter, Scale 100 percent (not Fit to page), Margins None, Headers and footers off.</span>
      </div>
      {sheets.map((sh, si) => (
        <div key={si} className="lb-sheet">
          {sh.map((q, i) => q && (
            <div key={i} className="lb-cell" style={{ width: `${sheet.w}in`, height: `${sheet.h}in`, left: `${sheet.left + (i % sheet.cols) * sheet.pitchX}in`, top: `${sheet.top + Math.floor(i / sheet.cols) * sheet.pitchY}in`, fontSize: `${sheet.fontPt}pt` }}>
              <b>{q.name}</b>
              {q.street && <span>{q.street}</span>}
              <span>{[q.city, [q.state, q.zip].filter(Boolean).join(' ')].filter(Boolean).join(', ')}</span>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default function Page() { return <Suspense fallback={null}><Labels /></Suspense>; }
