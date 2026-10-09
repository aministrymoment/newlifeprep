import type { Metadata } from 'next';
import '@/styles/payment.css';
import RichPage from '@/components/RichPage';
export const metadata: Metadata = { title: 'Tuition and Payment', description: 'Tuition, fees and secure online payment for New Life Preparatory Academy.' };
export default function Page() { return <RichPage name="payment" />; }
