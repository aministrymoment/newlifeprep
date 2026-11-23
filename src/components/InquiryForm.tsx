'use client';
import { useState } from 'react';
import { FEES, REQUEST_LABEL, money, type RequestType } from '@/lib/fees';

const RELATIONSHIPS = ['The student or graduate', 'Parent or guardian of the student'];
const VERIFY_WHAT = ['Enrollment and dates attended', 'Diploma and graduation', 'Both enrollment and graduation'];

export default function InquiryForm() {
  const [state, setState] = useState<'idle' | 'sending' | 'ok' | 'err'>('idle');
  const [msg, setMsg] = useState('');
  const [type, setType] = useState<RequestType>('information');
  const fee = type === 'transcript' ? FEES.transcript : type === 'verification' ? FEES.verification : 0;
  const isRecord = type === 'transcript' || type === 'verification';

  async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setState('sending');
    const data = Object.fromEntries(new FormData(e.currentTarget).entries());
    try {
      const r = await fetch('/api/inquiry', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...data, request_type: type }) });
      const j = await r.json().catch(() => ({}));
      if (r.ok && j.url) { window.location.href = j.url; return; }
      if (r.ok) { setState('ok'); setMsg(j.message || 'Thank you. We will respond within one business day.'); }
      else { setState('err'); setMsg(j.error || 'Something went wrong. Please call (954) 851-6608.'); }
    } catch { setState('err'); setMsg('Something went wrong. Please call (954) 851-6608.'); }
  }

  if (state === 'ok') return <div className="form-note ok"><strong>Message received.</strong><br />{msg}</div>;

  return (
    <form className="contact-form" onSubmit={onSubmit}>
      <div className="form-group"><label htmlFor="f_type">What are you requesting?</label>
        <select id="f_type" value={type} onChange={(e) => setType(e.target.value as RequestType)}>
          <option value="information">{REQUEST_LABEL.information}</option>
          <option value="verification">{REQUEST_LABEL.verification}{FEES.verification ? `, ${money(FEES.verification)}` : ''}</option>
          <option value="transcript">{REQUEST_LABEL.transcript}, {money(FEES.transcript)}</option>
          <option value="other">{REQUEST_LABEL.other}</option>
        </select>
      </div>
      {type === 'transcript' && <div className="form-note">Official transcripts are {money(FEES.transcript)} per request. After you submit this form you will go to secure Stripe checkout. The registrar begins your request once payment is received.</div>}
      {type === 'verification' && <div className="form-note">{fee ? `Student verification is ${money(fee)} per request and is paid at secure Stripe checkout after you submit this form. ` : ''}Verification is released only with the student&rsquo;s written authorization, which the office may ask you to provide.</div>}

      <div className="form-row">
        <div className="form-group"><label htmlFor="f_name">{isRecord ? 'Your Full Name' : 'Full Name'}</label><input id="f_name" name="name" required maxLength={120} /></div>
        <div className="form-group"><label htmlFor="f_email">{isRecord ? 'Your Email' : 'Email'}</label><input id="f_email" name="email" type="email" required maxLength={160} /></div>
      </div>
      <div className="form-row">
        <div className="form-group"><label htmlFor="f_phone">Phone</label><input id="f_phone" name="phone" type="tel" maxLength={40} /></div>
        {!isRecord && (
          <div className="form-group"><label htmlFor="f_prog">Program of Interest</label>
            <select id="f_prog" name="program" defaultValue="">
              <option value="">Select a program</option>
              <option>Adult Diploma Completion Program</option>
              <option>Adult Diploma Assessment Program</option>
              <option>High School Grades 9 to 12</option>
              <option>13th Year Postgraduate</option>
              <option>Athletic Program</option>
              <option>Scholarships</option>
              <option>Other</option>
            </select>
          </div>
        )}
      </div>

      {type === 'transcript' && (
        <>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_student_name">Student full name (as used while attending)</label><input id="d_student_name" name="d_student_name" required maxLength={120} /></div>
            <div className="form-group"><label htmlFor="d_student_id">Student ID, if known (NLPA-20XX-XXX)</label><input id="d_student_id" name="d_student_id" maxLength={40} /></div>
          </div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_dob">Student date of birth</label><input id="d_dob" name="d_dob" required maxLength={40} placeholder="MM/DD/YYYY" /></div>
            <div className="form-group"><label htmlFor="d_attended">Years attended or graduation year</label><input id="d_attended" name="d_attended" required maxLength={80} placeholder="2008 to 2012" /></div>
          </div>
          <div className="form-group"><label htmlFor="d_relationship">I am</label>
            <select id="d_relationship" name="d_relationship" required defaultValue="">
              <option value="" disabled>Select one</option>
              {RELATIONSHIPS.map((r) => <option key={r}>{r}</option>)}
            </select>
          </div>
          <div className="form-group"><label htmlFor="d_recipient_name">Send the transcript to (school, employer or person)</label><input id="d_recipient_name" name="d_recipient_name" required maxLength={160} /></div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_recipient_email">Recipient email address</label><input id="d_recipient_email" name="d_recipient_email" type="email" maxLength={160} /></div>
            <div className="form-group"><label htmlFor="d_recipient_address">Or mailing address, if it should be mailed</label><input id="d_recipient_address" name="d_recipient_address" maxLength={300} /></div>
          </div>
          <label className="form-check"><input type="checkbox" name="auth" value="yes" required /> I am the student, or the parent or guardian of a minor student, and I authorize New Life Preparatory Academy to release this transcript to the recipient named above.</label>
        </>
      )}

      {type === 'verification' && (
        <>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_student_name">Student full name (as used while attending)</label><input id="d_student_name" name="d_student_name" required maxLength={120} /></div>
            <div className="form-group"><label htmlFor="d_student_id">Student ID, if known (NLPA-20XX-XXX)</label><input id="d_student_id" name="d_student_id" maxLength={40} /></div>
          </div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_dob">Student date of birth</label><input id="d_dob" name="d_dob" required maxLength={40} placeholder="MM/DD/YYYY" /></div>
            <div className="form-group"><label htmlFor="d_attended">Years attended or graduation year</label><input id="d_attended" name="d_attended" required maxLength={80} placeholder="2008 to 2012" /></div>
          </div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="d_verify_what">What needs to be verified</label>
              <select id="d_verify_what" name="d_verify_what" required defaultValue="">
                <option value="" disabled>Select one</option>
                {VERIFY_WHAT.map((r) => <option key={r}>{r}</option>)}
              </select>
            </div>
            <div className="form-group"><label htmlFor="d_requester_org">Your organization (employer, school or agency)</label><input id="d_requester_org" name="d_requester_org" required maxLength={160} /></div>
          </div>
          <label className="form-check"><input type="checkbox" name="auth" value="yes" required /> The student has given written authorization for this verification. I understand NLPA may ask for a copy and will confirm the request before releasing anything.</label>
        </>
      )}

      {(type === 'information' || type === 'other') && (
        <div className="form-group"><label htmlFor="f_street">Mailing Address (optional, if you would like information mailed to you)</label><input id="f_street" name="street" autoComplete="street-address" maxLength={160} placeholder="Street address" /></div>
      )}
      {(type === 'information' || type === 'other') && (
        <div className="form-row">
          <div className="form-group"><label htmlFor="f_city">City</label><input id="f_city" name="city" autoComplete="address-level2" maxLength={80} /></div>
          <div className="form-row">
            <div className="form-group"><label htmlFor="f_state">State</label><input id="f_state" name="state" autoComplete="address-level1" maxLength={40} /></div>
            <div className="form-group"><label htmlFor="f_zip">ZIP</label><input id="f_zip" name="zip" autoComplete="postal-code" maxLength={12} /></div>
          </div>
        </div>
      )}
      <div className="form-group"><label htmlFor="f_msg">{isRecord ? 'Anything else the office should know (optional)' : 'How can we help?'}</label><textarea id="f_msg" name="message" required={!isRecord} maxLength={4000} /></div>
      <input name="website" tabIndex={-1} autoComplete="off" aria-hidden="true" style={{ position: 'absolute', left: '-9999px', height: 0, width: 0, opacity: 0 }} />
      {state === 'err' && <div className="form-note err">{msg}</div>}
      <button className="btn-primary form-submit" disabled={state === 'sending'}>
        {state === 'sending' ? (fee ? 'Connecting to Stripe...' : 'Sending...') : fee ? `Continue to Secure Checkout, ${money(fee)}` : isRecord ? 'Submit Request' : 'Send Message'}
      </button>
    </form>
  );
}
