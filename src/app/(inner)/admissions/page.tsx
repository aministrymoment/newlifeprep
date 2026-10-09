import type { Metadata } from 'next';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'Admissions', description: 'How to apply to New Life Preparatory Academy, requirements and enrollment steps.' };
export default function Page() { return <RichPage name="admissions" />; }
