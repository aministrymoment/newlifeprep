import type { Metadata } from 'next';
import '@/styles/portal.css';

export const metadata: Metadata = {
  title: 'Student Portal | New Life Preparatory Academy',
  robots: { index: false, follow: false },
  icons: { icon: '/logos/favicon.ico', apple: '/logos/apple-touch-icon.png' },
};

export default function PortalLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  );
}
