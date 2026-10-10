'use client';
import { useState } from 'react';

export default function InquiryForm() {
  const [state, setState] = useState<'idle' | 'sending' | 'ok' | 'err'>('idle');
  const [msg, setMsg] = useState('');

  async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setState('sending');
    const data = Object.fromEntries(new FormData(e.currentTarget).entries());
    try {
      const r = await fetch('/api/inquiry', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
      const j = await r.json().catch(() => ({}));
      if (r.ok) { setState('ok'); setMsg(j.message || 'Thank you. We will respond within one business day.'); }
      else { setState('err'); setMsg(j.error || 'Something went wrong. Please call (954) 851-6608.'); }
    } catch { setState('err'); setMsg('Something went wrong. Please call (954) 851-6608.'); }
  }

  if (state === 'ok') return <div className="form-note ok"><strong>Message received.</strong><br />{msg}</div>;

  return (
    <form className="contact-form" onSubmit={onSubmit}>
      <div className="form-row">
        <div className="form-group"><label htmlFor="f_name">Full Name</label><input id="f_name" name="name" required maxLength={120} /></div>
        <div className="form-group"><label htmlFor="f_email">Email</label><input id="f_email" name="email" type="email" required maxLength={160} /></div>
      </div>
      <div className="form-row">
        <div className="form-group"><label htmlFor="f_phone">Phone</label><input id="f_phone" name="phone" type="tel" maxLength={40} /></div>
        <div className="form-group"><label htmlFor="f_prog">Program of Interest</label>
          <select id="f_prog" name="program" defaultValue="">
            <option value="">Select a program</option>
            <option>Adult Diploma Completion Program</option>
            <option>Adult Test Out Diploma Program</option>
            <option>High School Grades 9 to 12</option>
            <option>13th Year Postgraduate</option>
            <option>Athletic Program</option>
            <option>Scholarships</option>
            <option>Other</option>
          </select>
        </div>
      </div>
      <div className="form-group"><label htmlFor="f_street">Mailing Address (optional, if you would like information mailed to you)</label><input id="f_street" name="street" autoComplete="street-address" maxLength={160} placeholder="Street address" /></div>
      <div className="form-row">
        <div className="form-group"><label htmlFor="f_city">City</label><input id="f_city" name="city" autoComplete="address-level2" maxLength={80} /></div>
        <div className="form-row">
          <div className="form-group"><label htmlFor="f_state">State</label><input id="f_state" name="state" autoComplete="address-level1" maxLength={40} /></div>
          <div className="form-group"><label htmlFor="f_zip">ZIP</label><input id="f_zip" name="zip" autoComplete="postal-code" maxLength={12} /></div>
        </div>
      </div>
      <div className="form-group"><label htmlFor="f_msg">How can we help?</label><textarea id="f_msg" name="message" required maxLength={4000} /></div>
      <input name="website" tabIndex={-1} autoComplete="off" aria-hidden="true" style={{ position: 'absolute', left: '-9999px', height: 0, width: 0, opacity: 0 }} />
      {state === 'err' && <div className="form-note err">{msg}</div>}
      <button className="btn-primary form-submit" disabled={state === 'sending'}>{state === 'sending' ? 'Sending...' : 'Send Message'}</button>
    </form>
  );
}
