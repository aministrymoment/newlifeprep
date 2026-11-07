// Simple sliding window limiter kept in server memory. It resets when the server instance restarts
// and is per instance, so it is a speed bump against abuse, not a hard guarantee.
const hits = new Map<string, number[]>();

export function tooMany(key: string, max: number, windowMs: number): boolean {
  const now = Date.now();
  const recent = (hits.get(key) || []).filter((t) => now - t < windowMs);
  if (recent.length >= max) { hits.set(key, recent); return true; }
  recent.push(now);
  hits.set(key, recent);
  if (hits.size > 5000) { for (const [k, v] of hits) if (!v.some((t) => now - t < windowMs)) hits.delete(k); }
  return false;
}

export function clientIp(req: Request): string {
  return (req.headers.get('x-nf-client-connection-ip') || req.headers.get('x-forwarded-for') || 'unknown').split(',')[0].trim();
}
