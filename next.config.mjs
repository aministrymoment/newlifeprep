// Security headers applied to every page and API route.
const isDev = process.env.NODE_ENV !== 'production';
const supa = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const supaWs = supa.replace(/^https:/, 'wss:');

function buildCsp(frameAncestors) {
  return [
    "default-src 'self'",
    // Next.js writes small inline scripts; dev mode also needs eval.
    `script-src 'self' 'unsafe-inline'${isDev ? " 'unsafe-eval'" : ''}`,
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com data:",
    "img-src 'self' data: blob: https:",
    "media-src 'self' https:",
    `connect-src 'self' ${supa} ${supaWs}`.trim(),
    "frame-src 'self' https://www.youtube-nocookie.com https://player.vimeo.com",
    `frame-ancestors ${frameAncestors}`,
    "base-uri 'self'",
    "form-action 'self'",
    "object-src 'none'",
  ].join('; ');
}

const csp = buildCsp("'none'");
// The admin only generators in /tools may be shown inside our own admin pages.
const toolsCsp = buildCsp("'self'");

const common = [
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), payment=()' },
  { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' },
];

/** @type {import('next').NextConfig} */
const nextConfig = {
  poweredByHeader: false,
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'Content-Security-Policy', value: csp },
          { key: 'X-Frame-Options', value: 'DENY' },
          ...common,
        ],
      },
      {
        source: '/tools/:path*',
        headers: [
          { key: 'Content-Security-Policy', value: toolsCsp },
          { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
          ...common,
        ],
      },
    ];
  },
};
export default nextConfig;
