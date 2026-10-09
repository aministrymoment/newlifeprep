import type { Metadata } from 'next';
import Link from 'next/link';
export const metadata: Metadata = { title: 'Thank You', robots: { index: false } };
export default function Thanks() {
  return (
    <>
      <div className="page-hero"><div className="page-hero-bg" /><div className="page-hero-grid" />
        <div className="page-hero-content"><span className="page-eyebrow">Payment Received</span><h1 className="page-title">Thank <span>You</span></h1></div></div>
      <section style={{ background: 'var(--off-white)' }}>
        <div className="container thanks">
          <p className="section-body">Your payment was received. Stripe is emailing your receipt now, and NLPA will record the payment to your account. If you have any question, email newlifeprep@gmail.com or call (954) 851-6608.</p>
          <p className="section-body" style={{ fontStyle: 'italic' }}>&ldquo;The Lord bless thee, and keep thee.&rdquo; Numbers 6:24</p>
          <p style={{ marginTop: 30 }}><Link href="/" className="btn-primary">Return Home</Link></p>
        </div>
      </section>
    </>
  );
}
