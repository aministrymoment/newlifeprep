'use client';

// Shows a lesson video from a YouTube link, a Vimeo link, or a direct .mp4 file link.
export function embedUrl(raw: string): { kind: 'iframe' | 'file'; src: string } | null {
  try {
    const u = new URL(raw.trim());
    const h = u.hostname.replace(/^www\./, '');
    if (h === 'youtu.be') return { kind: 'iframe', src: `https://www.youtube-nocookie.com/embed/${u.pathname.slice(1)}` };
    if (h === 'youtube.com' || h === 'm.youtube.com') {
      const id = u.searchParams.get('v') || (u.pathname.startsWith('/embed/') ? u.pathname.split('/')[2] : '');
      return id ? { kind: 'iframe', src: `https://www.youtube-nocookie.com/embed/${id}` } : null;
    }
    if (h === 'vimeo.com') {
      const id = u.pathname.split('/').filter(Boolean)[0];
      const hash = u.pathname.split('/').filter(Boolean)[1];
      return id ? { kind: 'iframe', src: `https://player.vimeo.com/video/${id}${hash ? `?h=${hash}` : ''}` } : null;
    }
    if (h === 'player.vimeo.com') return { kind: 'iframe', src: raw };
    if (/\.(mp4|webm|mov)(\?.*)?$/i.test(u.pathname) && u.protocol === 'https:') return { kind: 'file', src: raw };
  } catch { /* not a link */ }
  return null;
}

export default function Video({ url, title }: { url?: string | null; title: string }) {
  if (!url) return null;
  const v = embedUrl(url);
  if (!v) return null;
  return (
    <div className="p-video">
      {v.kind === 'iframe'
        ? <iframe src={v.src} title={title} allow="accelerometer; encrypted-media; picture-in-picture; fullscreen" allowFullScreen loading="lazy" referrerPolicy="strict-origin-when-cross-origin" />
        : <video src={v.src} controls preload="metadata" title={title} />}
    </div>
  );
}
