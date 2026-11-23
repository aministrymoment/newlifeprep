// Fees for website requests. The server only ever trusts these amounts.
// To start charging for student verification, change verification below (cents). 1000 means $10.00.
export const FEES = { transcript: 2500, verification: 0 } as const;
export type RequestType = 'information' | 'verification' | 'transcript' | 'other';

export const REQUEST_LABEL: Record<RequestType, string> = {
  information: 'Information about the school',
  verification: 'Verification of a student',
  transcript: 'Official transcript request',
  other: 'Other question',
};

export const money = (cents: number) => `$${(cents / 100).toFixed(2)}`;

// Fields collected for each request type. Key, label, required.
export const DETAIL_FIELDS: Record<'transcript' | 'verification', { key: string; label: string; required?: boolean; max: number }[]> = {
  transcript: [
    { key: 'student_name', label: 'Student full name (as used while attending)', required: true, max: 120 },
    { key: 'student_id', label: 'Student ID, if known (NLPA-20XX-XXX)', max: 40 },
    { key: 'dob', label: 'Student date of birth', required: true, max: 40 },
    { key: 'attended', label: 'Years attended or graduation year', required: true, max: 80 },
    { key: 'relationship', label: 'Requested by', required: true, max: 60 },
    { key: 'recipient_name', label: 'Send the transcript to (school, employer or person)', required: true, max: 160 },
    { key: 'recipient_email', label: 'Recipient email address', max: 160 },
    { key: 'recipient_address', label: 'Recipient mailing address, if it should be mailed', max: 300 },
  ],
  verification: [
    { key: 'student_name', label: 'Student full name (as used while attending)', required: true, max: 120 },
    { key: 'student_id', label: 'Student ID, if known (NLPA-20XX-XXX)', max: 40 },
    { key: 'dob', label: 'Student date of birth', required: true, max: 40 },
    { key: 'attended', label: 'Years attended or graduation year', required: true, max: 80 },
    { key: 'verify_what', label: 'What needs to be verified', required: true, max: 80 },
    { key: 'requester_org', label: 'Your organization (employer, school or agency)', required: true, max: 160 },
  ],
};
