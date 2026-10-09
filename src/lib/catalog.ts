// Everything that can be paid for online. The server only ever trusts these amounts.
export type PayItem = { id: string; label: string; amountCents: number | null; needs: 'student' | 'program' | 'name' };

export const CATALOG: PayItem[] = [
  { id: 'application', label: 'Application Fee, $50.00', amountCents: 5000, needs: 'program' },
  { id: 'completion_full', label: 'Adult Diploma Completion Program, paid in full, $1,250.00', amountCents: 125000, needs: 'program' },
  { id: 'completion_half', label: 'Adult Diploma Completion Program, 50% payment, $625.00', amountCents: 62500, needs: 'student' },
  { id: 'testout', label: 'Adult Test Out Diploma Program, $750.00', amountCents: 75000, needs: 'program' },
  { id: 'hs_annual_9_10', label: 'High School Grades 9 and 10, annual tuition, $5,000.00', amountCents: 500000, needs: 'student' },
  { id: 'hs_annual_11_12', label: 'High School Grades 11 and 12, annual tuition, $5,500.00', amountCents: 550000, needs: 'student' },
  { id: 'hs_annual_13', label: '13th Year Postgraduate, annual tuition, $6,000.00', amountCents: 600000, needs: 'student' },
  { id: 'hs_monthly_9_10', label: 'High School Grades 9 and 10, monthly payment, $500.00', amountCents: 50000, needs: 'student' },
  { id: 'hs_monthly_11_12', label: 'High School Grades 11 and 12, monthly payment, $550.00', amountCents: 55000, needs: 'student' },
  { id: 'hs_monthly_13', label: '13th Year Postgraduate, monthly payment, $600.00', amountCents: 60000, needs: 'student' },
  { id: 'athletic_entry', label: 'Athletic Entry Fee, $2,500.00', amountCents: 250000, needs: 'student' },
  { id: 'donation', label: 'Donation, you choose the amount', amountCents: null, needs: 'name' },
];
