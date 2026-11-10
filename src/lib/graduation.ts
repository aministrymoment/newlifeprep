// Graduation plan data and the planner used by Administration, Virtual Counselor.
// Follows the Florida 24 credit diploma structure. Dr. Jenkins confirms NLPA's own requirements.
export type Area = 'English' | 'Mathematics' | 'Science' | 'Social Studies' | 'Physical Education' | 'Fine Arts' | 'Electives';
export const AREAS: Area[] = ['English', 'Mathematics', 'Science', 'Social Studies', 'Physical Education', 'Fine Arts', 'Electives'];
export const REQUIRED: { area: Area; need: number }[] = [
  { area: 'English', need: 4 }, { area: 'Mathematics', need: 4 }, { area: 'Science', need: 3 }, { area: 'Social Studies', need: 3 },
  { area: 'Physical Education', need: 1 }, { area: 'Fine Arts', need: 1 }, { area: 'Electives', need: 8 },
];
export const TOTAL_NEEDED = 24;
export const MAX_PER_YEAR = 7;

// Recommended four year plan. Titles match the course titles in the database.
export const PLAN: Record<number, string[]> = {
  9: ['English 1', 'Algebra 1', 'Physical Science', 'Physical Education with Personal Fitness', 'BIB 101 Old Testament Survey', 'Digital Technology and Computer Applications', 'Public Speaking and Communication'],
  10: ['English 2', 'Geometry', 'Biology 1', 'World History 1', 'BIB 102 New Testament Survey', 'Health Education', 'Spanish 1'],
  11: ['English 3', 'Algebra 2', 'Chemistry', 'United States History 1', 'Music Appreciation and Worship Arts', 'Personal Finance and Stewardship'],
  12: ['English 4', 'Probability and Statistics', 'United States Government', 'Economics', 'Christian Ethics', 'Entrepreneurship and Business Stewardship', 'Spanish 2'],
};
export const ALTERNATES: { title: string; use: string }[] = [
  { title: 'Earth and Space Science', use: 'Swap for Physical Science, or add as a fourth science for college bound students.' },
];
export const AREA: Record<string, Area> = {
  'English 1': 'English', 'English 2': 'English', 'English 3': 'English', 'English 4': 'English',
  'Algebra 1': 'Mathematics', 'Geometry': 'Mathematics', 'Algebra 2': 'Mathematics', 'Probability and Statistics': 'Mathematics',
  'Physical Science': 'Science', 'Biology 1': 'Science', 'Chemistry': 'Science', 'Earth and Space Science': 'Science',
  'World History 1': 'Social Studies', 'United States History 1': 'Social Studies', 'United States Government': 'Social Studies', 'Economics': 'Social Studies',
  'Physical Education with Personal Fitness': 'Physical Education',
  'Music Appreciation and Worship Arts': 'Fine Arts',
};
export const areaOf = (t: string): Area => AREA[t] || 'Electives';
export const ALL_NLPA_TITLES: string[] = [...Object.values(PLAN).flat(), ...ALTERNATES.map((a) => a.title)];
const planGradeOf = (t: string) => { for (const g of [9, 10, 11, 12]) if (PLAN[g].includes(t)) return g; return t === 'Earth and Space Science' ? 11 : 12; };

// Courses that must be taken by name, not only by credit count.
const MANDATORY: Partial<Record<Area, string[]>> = {
  Mathematics: ['Algebra 1', 'Geometry'],
  Science: ['Biology 1'],
  'Social Studies': ['World History 1', 'United States History 1', 'United States Government', 'Economics'],
};
// Order in which NLPA courses are offered to fill an area.
const SEQ: Record<Exclude<Area, 'Electives'>, string[]> = {
  English: ['English 1', 'English 2', 'English 3', 'English 4'],
  Mathematics: ['Algebra 1', 'Geometry', 'Algebra 2', 'Probability and Statistics'],
  Science: ['Biology 1', 'Physical Science', 'Chemistry', 'Earth and Space Science'],
  'Social Studies': ['World History 1', 'United States History 1', 'United States Government', 'Economics'],
  'Physical Education': ['Physical Education with Personal Fitness'],
  'Fine Arts': ['Music Appreciation and Worship Arts'],
};
const ELECTIVE_ORDER = ['BIB 101 Old Testament Survey', 'BIB 102 New Testament Survey', 'Christian Ethics', 'Health Education', 'Digital Technology and Computer Applications', 'Public Speaking and Communication', 'Spanish 1', 'Spanish 2', 'Personal Finance and Stewardship', 'Entrepreneurship and Business Stewardship', 'Earth and Space Science'];
// A course in a chain must come in a later year than the one before it, when both are still needed.
const CHAINS: string[][] = [
  ['English 1', 'English 2', 'English 3', 'English 4'],
  ['Algebra 1', 'Geometry', 'Algebra 2', 'Probability and Statistics'],
];

export type TStatus = 'completed' | 'in_progress' | 'failed';
export type TCourse = { id: string; title: string; credits: number; area: Area; match: string | null; status: TStatus; grade?: string; year?: string };
export type Item = { title: string; credits: number; area: Area; reason: string; year: number; doubled?: boolean };
export type Result = {
  counted: Record<Area, number>;       // credits counted per area, with extra core credits moved to electives
  rawEarned: number;
  remaining: Item[];
  years: { grade: number; items: Item[]; credits: number }[];
  flags: string[];
  finalTotal: number;
};

const eps = 0.001;
export function buildPlan(courses: TCourse[], enteringGrade: number, countInProgress: boolean, credits: (t: string) => number): Result {
  const flags: string[] = [];
  const counted = courses.filter((c) => c.status === 'completed' || (countInProgress && c.status === 'in_progress'));
  const earned = {} as Record<Area, number>;
  AREAS.forEach((a) => { earned[a] = 0; });
  counted.forEach((c) => { earned[c.area] += c.credits; });
  const rawEarned = counted.reduce((a, c) => a + c.credits, 0);
  const satisfied = new Set(counted.map((c) => c.match).filter(Boolean) as string[]);

  const picks: { title: string; area: Area; reason: string }[] = [];
  const have = (t: string) => satisfied.has(t) || picks.some((p) => p.title === t);
  const add = (title: string, area: Area, reason: string) => { picks.push({ title, area, reason }); };

  let surplus = 0;
  (Object.keys(SEQ) as Exclude<Area, 'Electives'>[]).forEach((area) => {
    const req = REQUIRED.find((r) => r.area === area)!.need;
    let need = req - earned[area];
    if (need < 0) { surplus += -need; need = 0; }
    (MANDATORY[area] || []).forEach((t) => { if (!satisfied.has(t)) { add(t, area, 'Required course'); need -= credits(t); } });
    if (area === 'English') {
      const matched = SEQ.English.filter((t) => satisfied.has(t)).length;
      const start = Math.max(matched, Math.floor(earned.English + eps));
      for (let i = start; i < SEQ.English.length && need > eps; i++) { if (!have(SEQ.English[i])) { add(SEQ.English[i], area, 'English credit still needed'); need -= credits(SEQ.English[i]); } }
    } else {
      for (const t of SEQ[area]) { if (need <= eps) break; if (!have(t)) { add(t, area, 'Credit still needed'); need -= credits(t); } }
    }
    if (need > eps) flags.push(`${area} is short by ${need.toFixed(1)} credit even after every NLPA course in that area. Review the transcript or consider transfer credit.`);
  });

  let elecNeed = 8 - earned.Electives - surplus;
  const reasonE = 'Elective credit still needed';
  for (const t of ELECTIVE_ORDER) { if (elecNeed <= eps) break; if (!have(t)) { add(t, 'Electives', reasonE); elecNeed -= credits(t); } }
  const spill = Math.max(0, earned.Electives + surplus - 8);

  // Place the remaining courses into the years left.
  const first = Math.min(12, Math.max(9, enteringGrade));
  const order = picks.map((p, i) => ({ ...p, i, pg: planGradeOf(p.title), chain: CHAINS.some((c) => c.includes(p.title)) })).sort((a, b) => Number(a.area === 'Electives') - Number(b.area === 'Electives') || a.pg - b.pg || Number(b.chain) - Number(a.chain) || a.i - b.i);
  const load: Record<number, number> = { 9: 0, 10: 0, 11: 0, 12: 0 };
  const yearOf: Record<string, number> = {};
  const items: Item[] = [];
  for (const p of order) {
    const cr = credits(p.title);
    let y = Math.max(first, p.pg);
    let doubled = false;
    const chain = CHAINS.find((c) => c.includes(p.title));
    if (chain) {
      const prevIdx = chain.indexOf(p.title) - 1;
      const prev = prevIdx >= 0 ? yearOf[chain[prevIdx]] : undefined;
      if (prev !== undefined && y <= prev) y = prev + 1;
      if (y > 12) { y = 12; doubled = true; }
    }
    while (load[y] + cr > MAX_PER_YEAR + eps && y < 12) y++;
    if (load[y] + cr > MAX_PER_YEAR + eps) doubled = true;
    load[y] += cr; yearOf[p.title] = y;
    items.push({ title: p.title, credits: cr, area: p.area, reason: p.reason, year: y, doubled });
  }
  if (items.some((i) => i.doubled)) flags.push('Some courses cannot fit in the years left without taking two courses of the same sequence in one year or going over 7.0 credits. Options: summer study, a lighter load with the 13th Year Postgraduate, or transfer credit. Those courses are marked.');
  if (first === 12 && items.reduce((a, i) => a + i.credits, 0) > MAX_PER_YEAR) flags.push('This student enters Grade 12 needing more than 7.0 credits. Dr. Jenkins decides whether to allow it.');
  if (courses.some((c) => c.status === 'failed')) flags.push('Failed courses are not counted. The student may repeat them at NLPA.');
  const unmatchedCore = counted.filter((c) => c.area !== 'Electives' && !c.match);
  if (unmatchedCore.length) flags.push(`Check the mapping for: ${unmatchedCore.map((c) => c.title).join(', ')}. They count toward credits but not toward a specific NLPA course, so the plan may ask for a course the student already has.`);
  if (spill > eps) flags.push(`${spill.toFixed(1)} extra elective credit is already earned beyond the 8.0 needed.`);
  if (courses.some((c) => c.status === 'in_progress') && countInProgress) flags.push('Courses in progress are counted as earned. Update the plan when final grades arrive.');

  const counted2 = {} as Record<Area, number>;
  AREAS.forEach((a) => { counted2[a] = earned[a]; });
  counted2.Electives += surplus;
  const remainingCredits = items.reduce((a, i) => a + i.credits, 0);
  const years = [9, 10, 11, 12].filter((g) => g >= first).map((g) => ({ grade: g, items: items.filter((i) => i.year === g), credits: items.filter((i) => i.year === g).reduce((a, i) => a + i.credits, 0) }));
  return { counted: counted2, rawEarned, remaining: items, years, flags, finalTotal: rawEarned + remainingCredits };
}
