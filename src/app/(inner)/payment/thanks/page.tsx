import type { Metadata } from 'next';
import Link from 'next/link';
export const metadata: Metadata = { title: 'Thank You', robots: { index: false } };

export default async function Thanks({ searchParams }: { searchParams: Promise<{ for?: string }> }) {
  const { for: kind } = await searchParams;
  const body = kind === 'transcript'
    ? 'Your payment and transcript request were received. Stripe is emailing your receipt now. The registrar will review the request, confirm the details and send the transcript to the recipient you named. We will contact you by email if anything more is needed.'
    : kind === 'verification'
    ? 'Your payment and verification request were received. Stripe is emailing your receipt now. The registrar will review the request and confirm the student’s authorization before anything is released.'
    : 'Your payment was received. Stripe is emailing your receipt now, and NLPA will record the payment to your account.';
  return (
    <>
      <div className="page-hero"><div className="page-hero-bg" /><div className="page-hero-grid" />
        <div className="page-hero-content"><span className="page-eyebrow">{kind === 'transcript' || kind === 'verification' ? 'Request Received' : 'Payment Received'}</span><h1 className="page-title">Thank <span>You</span></h1></div></div>
      <section style={{ background: 'var(--off-white)' }}>
        <div className="container thanks">
          <p className="section-body">{body} If you have any question, email registrar@newlifeprep.org or call (954) 851-6608.</p>
          <p className="section-body" style={{ fontStyle: 'italic' }}>&ldquo;The Lord bless thee, and keep thee.&rdquo; Numbers 6:24</p>
          <p style={{ marginTop: 30 }}><Link href="/" className="btn-primary">Return Home</Link></p>
        </div>
      </section>
    </>
  );
}
