import type { Metadata } from 'next';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'Athletics', description: 'The NLPA Camels athletic program, planned launch for the 2027 to 2028 academic year.' };
export default function Page() { return <RichPage name="athletics" />; }
