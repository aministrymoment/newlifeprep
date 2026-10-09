import type { Metadata } from 'next';
import '@/styles/home.css';
import '@/styles/extra.css';
import { SITE } from '@/site';
import SiteNav from '@/components/SiteNav';
import SiteFooter from '@/components/SiteFooter';

export const metadata: Metadata = {
  metadataBase: new URL('https://www.newlifeprep.org'),
  title: `${SITE.name} | Pompano Beach, Florida`,
  description: 'A Christ centered private school in Pompano Beach, Florida. Adult diploma completion, high school grades 9 to 12, 13th Year Postgraduate and the NLPA Camels athletic program.',
  icons: { icon: '/logos/favicon.ico', apple: '/logos/apple-touch-icon.png' },
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
      </head>
      <body>
        <SiteNav />
        <main>{children}</main>
        <SiteFooter />
      </body>
    </html>
  );
}
