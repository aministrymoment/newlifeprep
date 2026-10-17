// Everything that can be paid for online. The server only ever trusts these amounts.
export type PayItem = { id: string; label: string; amountCents: number | null; needs: 'student' | 'program' | 'name' };

export const CATALOG: PayItem[] = [
  { id: 'application', label: 'Application Fee, $50.00', amountCents: 5000, needs: 'program' },
  { id: 'completion_full', label: 'Adult Diploma Completion Program, paid in full, $1,250.00', amountCents: 125000, needs: 'program' },
  { id: 'completion_half', label: 'Adult Diploma Completion Program, 50% payment, $625.00', amountCents: 62500, needs: 'student' },
  { id: 'assessment', label: 'Adult Diploma Assessment Program, $750.00', amountCents: 75000, needs: 'program' },
  { id: 'hs_application', label: 'High School Application Fee, $150.00', amountCents: 15000, needs: 'program' },
  { id: 'hs_enrollment', label: 'High School Enrollment Fee, $150.00', amountCents: 15000, needs: 'student' },
  { id: 'hs_annual_9_12', label: 'High School Grades 9 to 12, annual tuition, $8,510.00', amountCents: 851000, needs: 'student' },
  { id: 'hs_annual_13', label: '13th Year Postgraduate, annual tuition, $7,500.00', amountCents: 750000, needs: 'student' },
  { id: 'hs_monthly_9_12', label: 'High School Grades 9 to 12, monthly payment, $851.00', amountCents: 85100, needs: 'student' },
  { id: 'hs_monthly_13', label: '13th Year Postgraduate, monthly payment, $750.00', amountCents: 75000, needs: 'student' },
  { id: 'athletic_entry', label: 'Athletic Entry Fee, $2,500.00', amountCents: 250000, needs: 'student' },
  { id: 'donation', label: 'Donation, you choose the amount', amountCents: null, needs: 'name' },
];
