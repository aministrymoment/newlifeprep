import InquiryForm from './InquiryForm';
import PayForm from './PayForm';
import { loadContent } from '@/lib/content';

// Renders a legacy HTML fragment, swapping the markers for live React forms.
export default function RichPage({ name }: { name: string }) {
  const html = loadContent(name);
  const parts = html.split(/(<!--FORM-->|<!--PAY-->)/);
  return (
    <>
      {parts.map((p, i) =>
        p === '<!--FORM-->' ? <InquiryForm key={i} /> :
        p === '<!--PAY-->' ? <PayForm key={i} /> :
        <div key={i} style={{ display: 'contents' }} dangerouslySetInnerHTML={{ __html: p }} />
      )}
    </>
  );
}
