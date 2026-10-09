import type { Metadata } from 'next';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'About', description: 'The story, mission and leadership of New Life Preparatory Academy in Pompano Beach, Florida.' };
export default function Page() { return <RichPage name="about" />; }
