import type { Metadata } from 'next';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'FAQs', description: 'Answers to common questions about New Life Preparatory Academy.' };
export default function Page() { return <RichPage name="faqs" />; }
