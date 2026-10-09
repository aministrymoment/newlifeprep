import Link from 'next/link';
import { SITE } from '@/site';

export default function SiteFooter() {
  return (
    <footer>
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand">
            <div className="footer-seal"><span className="logo-chip"><img src="/logos/NLPA_Block_Logo_400.png" alt={SITE.name} /></span></div>
            <p className="footer-brand-name">{SITE.name}</p>
            <p className="footer-brand-tagline">Opening Doors for the Kingdom, One Student at a Time</p>
            <div className="footer-ids">
              <span className="footer-id">FL DOE Private School ID: {SITE.fldoeId}</span>
              {SITE.showEin && <span className="footer-id">Federal EIN: {SITE.ein}</span>}
              <span className="footer-id">{SITE.ministryLine}</span>
            </div>
          </div>
          <div>
            <p className="footer-col-title">Programs</p>
            <ul className="footer-links">
              <li><Link href="/programs">Adult Diploma Program</Link></li>
              <li><Link href="/programs">High School 9 to 12</Link></li>
              <li><Link href="/programs">13th Year Postgraduate</Link></li>
              <li><Link href="/athletics">Athletic Program</Link></li>
              <li><Link href="/scholarships">Scholarships</Link></li>
            </ul>
          </div>
          <div>
            <p className="footer-col-title">Institution</p>
            <ul className="footer-links">
              <li><Link href="/about">Our Story</Link></li>
              <li><Link href="/admissions">Admissions</Link></li>
              <li><Link href="/payment">Tuition and Payment</Link></li>
              <li><Link href="/faqs">FAQs</Link></li>
              <li><Link href="/contact">Contact</Link></li>
              <li><Link href="/portal/login">Student Login</Link></li>
            </ul>
          </div>
          <div>
            <p className="footer-col-title">Contact</p>
            <ul className="footer-links">
              <li><a href={SITE.phoneHref}>{SITE.phone}</a></li>
              <li><a href={`mailto:${SITE.email}`}>{SITE.email}</a></li>
              <li><span style={{ fontSize: 14, color: 'rgba(255,255,255,0.5)' }}>{SITE.address1}</span></li>
              <li><span style={{ fontSize: 14, color: 'rgba(255,255,255,0.5)' }}>{SITE.address2}</span></li>
              <li><Link href="/contact">Apply Now</Link></li>
            </ul>
          </div>
        </div>
        <div className="footer-bottom">
          <p className="footer-bottom-text">© {new Date().getFullYear()} {SITE.name}. All Rights Reserved.</p>
          <p className="footer-motto">{SITE.motto}</p>
        </div>
      </div>
    </footer>
  );
}
