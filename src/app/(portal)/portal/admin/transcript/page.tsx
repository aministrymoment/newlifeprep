'use client';
import PortalFrame from '@/components/portal/PortalFrame';

export default function Page() {
  return (
    <PortalFrame adminOnly>
      {() => (
        <>
          <h1 className="p-h1">Transcript Generator</h1>
          <p className="p-small"><a href="/portal/admin">Back to Administration</a></p>
          <iframe src="/tools/NLPA_Transcript_Generator.html" title="Transcript Generator" style={{ width: '100%', height: '2700px', border: 0 }} />
        </>
      )}
    </PortalFrame>
  );
}
