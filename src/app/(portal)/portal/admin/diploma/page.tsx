'use client';
import PortalFrame from '@/components/portal/PortalFrame';

export default function Page() {
  return (
    <PortalFrame adminOnly>
      {() => (
        <>
          <h1 className="p-h1">Diploma Generator</h1>
          <p className="p-small"><a href="/portal/admin">Back to Administration</a></p>
          <iframe src="/tools/NLPA_Diploma_Generator.html" title="Diploma Generator" style={{ width: '100%', height: '1500px', border: 0 }} />
        </>
      )}
    </PortalFrame>
  );
}
