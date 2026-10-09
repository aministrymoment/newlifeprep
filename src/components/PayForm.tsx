'use client';
import { useState } from 'react';
import { CATALOG } from '@/lib/catalog';

export default function PayForm() {
  const [item, setItem] = useState('');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const sel = CATALOG.find((c) => c.id === item);

  async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBusy(true); setErr('');
    const data = Object.fromEntries(new FormData(e.currentTarget).entries());
    try {
      const r = await fetch('/api/checkout', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
      const j = await r.json().catch(() => ({}));
      if (r.ok && j.url) { window.location.href = j.url; return; }
      setErr(j.error || 'Online payment is not available right now. Please call (954) 851-6608.');
    } catch { setErr('Online payment is not available right now. Please call (954) 851-6608.'); }
    setBusy(false);
  }

  return (
    <section style={{ background: 'var(--gold-pale)' }} id="pay">
      <div className="container">
        <span className="section-eyebrow">Secure Online Payment</span>
        <h2 className="section-title">Make a Payment</h2>
        <div className="section-divider" />
        <p className="section-body" style={{ marginBottom: 30 }}>Payments are processed securely by Stripe. You will be taken to Stripe to enter your card details, and Stripe emails your receipt right away.</p>
        <form className="pay-form" onSubmit={onSubmit}>
          <div className="form-group"><label htmlFor="p_item">What are you paying for?</label>
            <select id="p_item" name="item" required value={item} onChange={(e) => setItem(e.target.value)}>
              <option value="">Select a payment</option>
              {CATALOG.map((c) => <option key={c.id} value={c.id}>{c.label}</option>)}
            </select>
          </div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="p_name">Full Name</label><input id="p_name" name="name" required maxLength={120} /></div>
            <div className="form-group"><label htmlFor="p_email">Email for Receipt</label><input id="p_email" name="email" type="email" required maxLength={160} /></div>
          </div>
          {sel?.needs === 'student' && <div className="form-group"><label htmlFor="p_ref">Student ID (format NLPA-20XX-XXX)</label><input id="p_ref" name="reference" required maxLength={40} placeholder="NLPA-2026-001" /></div>}
          {sel?.needs === 'program' && <div className="form-group"><label htmlFor="p_ref">Program or Track</label><input id="p_ref" name="reference" required maxLength={80} /></div>}
          {sel && sel.amountCents === null && <div className="form-group"><label htmlFor="p_amt">Donation Amount (USD)</label><input id="p_amt" name="amount" type="number" min="1" max="50000" step="1" required placeholder="100" /></div>}
          {err && <div className="form-note err">{err}</div>}
          <button className="btn-primary form-submit" disabled={busy || !item}>{busy ? 'Connecting to Stripe...' : 'Continue to Secure Checkout'}</button>
        </form>
      </div>
    </section>
  );
}
