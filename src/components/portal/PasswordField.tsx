'use client';
import { useState } from 'react';

// Password box with a Show / Hide button so people can see what they type.
export default function PasswordField({ label, value, onChange, autoComplete, minLength }: { label: string; value: string; onChange: (v: string) => void; autoComplete: string; minLength?: number }) {
  const [show, setShow] = useState(false);
  return (
    <label>{label}
      <span className="p-pw">
        <input type={show ? 'text' : 'password'} required minLength={minLength} value={value} onChange={(e) => onChange(e.target.value)} autoComplete={autoComplete} />
        <button type="button" className="p-pwbtn" onClick={() => setShow(!show)} aria-label={show ? 'Hide password' : 'Show password'}>{show ? 'Hide' : 'Show'}</button>
      </span>
    </label>
  );
}
