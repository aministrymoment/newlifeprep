import type { Metadata } from 'next';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'Scholarships', description: 'Florida scholarship programs and internal scholarships at New Life Preparatory Academy.' };
export default function Page() { return <RichPage name="scholarships" />; }
