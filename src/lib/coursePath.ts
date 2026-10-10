// Builds the ordered path through a course and works out progress and grades.
export type Kind = 'topic' | 'assessment' | 'discussion' | 'quiz';
export type Course = { id: string; slug: string; title: string; subject: string | null; credits: number; focus: string | null; video_url?: string | null };
export type Item = { id: string; kind: Kind; position: number; title: string; content: any };
export type Sub = { id: string; item_id: string; body: string; score: number | null; feedback: string | null; status: string; created_at: string };
export type Att = { item_id: string; score: number; passed: boolean; created_at: string };
export type Step = { item: Item; label: string };
export type Module = { key: string; title: string; steps: Step[] };

const LABEL = { lesson: 'Lesson', check: 'Check Quiz', unit: 'Unit Quiz', written: 'Written Assignment', disc: 'Discussion', finalW: 'Final Assessment', finalQ: 'Final Exam', other: 'Activity' };

// Titles follow one pattern: "1.1 Name", "Check 1.1: Name", "Unit Quiz 1: Name", "Assessment 1: Name", "Discussion 1: Name".
export function buildPath(items: Item[]): Module[] {
  const sorted = [...items].sort((a, b) => a.position - b.position);
  type U = { n: number; lessons: Map<string, { topic?: Item; check?: Item }>; unitQuiz?: Item; assess?: Item; disc?: Item };
  const units = new Map<number, U>();
  const get = (n: number) => { let u = units.get(n); if (!u) { u = { n, lessons: new Map() }; units.set(n, u); } return u; };
  let finalW: Item | undefined, finalQ: Item | undefined;
  const loose: Item[] = [];
  for (const it of sorted) {
    const t = it.title; let m: RegExpMatchArray | null;
    if (it.kind === 'topic' && (m = t.match(/^(\d+)\.(\d+)\s/))) { const l = get(+m[1]).lessons; const k = `${m[1]}.${m[2]}`; l.set(k, { ...(l.get(k) || {}), topic: it }); }
    else if (it.kind === 'quiz' && (m = t.match(/^Check (\d+)\.(\d+)/))) { const l = get(+m[1]).lessons; const k = `${m[1]}.${m[2]}`; l.set(k, { ...(l.get(k) || {}), check: it }); }
    else if (it.kind === 'quiz' && (m = t.match(/^Unit Quiz (\d+)/))) get(+m[1]).unitQuiz = it;
    else if (it.kind === 'quiz' && /^Final Exam/.test(t)) finalQ = it;
    else if (it.kind === 'assessment' && /^Final Assessment/.test(t)) finalW = it;
    else if (it.kind === 'assessment' && (m = t.match(/^Assessment (\d+)/))) get(+m[1]).assess = it;
    else if (it.kind === 'discussion' && (m = t.match(/^Discussion (\d+)/))) get(+m[1]).disc = it;
    else loose.push(it);
  }
  const mods: Module[] = [];
  [...units.values()].sort((a, b) => a.n - b.n).forEach((u) => {
    const steps: Step[] = [];
    [...u.lessons.entries()].sort((a, b) => a[0].localeCompare(b[0], undefined, { numeric: true })).forEach(([, l]) => {
      if (l.topic) steps.push({ item: l.topic, label: LABEL.lesson });
      if (l.check) steps.push({ item: l.check, label: LABEL.check });
    });
    if (u.unitQuiz) steps.push({ item: u.unitQuiz, label: LABEL.unit });
    if (u.assess) steps.push({ item: u.assess, label: LABEL.written });
    if (u.disc) steps.push({ item: u.disc, label: LABEL.disc });
    const name = u.unitQuiz ? u.unitQuiz.title.replace(/^Unit Quiz (\d+):\s*/, 'Unit $1: ') : `Unit ${u.n}`;
    mods.push({ key: `u${u.n}`, title: name, steps });
  });
  const fin: Step[] = [];
  if (finalW) fin.push({ item: finalW, label: LABEL.finalW });
  if (finalQ) fin.push({ item: finalQ, label: LABEL.finalQ });
  if (fin.length) mods.push({ key: 'final', title: 'Final Assessment and Final Exam', steps: fin });
  if (loose.length) mods.push({ key: 'more', title: 'Course Activities', steps: loose.map((it) => ({ item: it, label: LABEL.other })) });
  return mods;
}

export const flat = (mods: Module[]) => mods.flatMap((m) => m.steps);

export const MAX_ATTEMPTS = 3;
export type Status = { done: boolean; note: string };
export function stepStatus(item: Item, prog: Set<string>, atts: Att[], subs: Sub[]): Status {
  if (item.kind === 'topic') return prog.has(item.id) ? { done: true, note: 'Complete' } : { done: false, note: '' };
  if (item.kind === 'quiz') {
    const mine = atts.filter((a) => a.item_id === item.id);
    if (!mine.length) return { done: false, note: '' };
    const best = Math.max(...mine.map((a) => a.score));
    return mine.some((a) => a.passed) ? { done: true, note: `Passed, ${best} percent` } : { done: false, note: mine.length >= MAX_ATTEMPTS ? `Best ${best} percent, no attempts left` : `Best ${best} percent, ${MAX_ATTEMPTS - mine.length} attempt${MAX_ATTEMPTS - mine.length > 1 ? 's' : ''} left` };
  }
  const mine = subs.filter((s) => s.item_id === item.id);
  if (!mine.length) return { done: false, note: '' };
  const graded = mine.filter((s) => s.score !== null);
  if (graded.length) return { done: true, note: `Scored ${Math.max(...graded.map((s) => s.score as number))}` };
  return { done: true, note: 'Submitted, awaiting review' };
}

export const WEIGHTS = { quizzes: 40, written: 50, discussions: 10 };
export function letter(p: number) { return p >= 90 ? 'A' : p >= 80 ? 'B' : p >= 70 ? 'C' : 'Not yet passing'; }

export function computeGrade(items: Item[], atts: Att[], subs: Sub[]) {
  const best = (id: string) => { const s = atts.filter((a) => a.item_id === id).map((a) => a.score); return s.length ? Math.max(...s) : null; };
  const bestSub = (id: string) => { const s = subs.filter((x) => x.item_id === id && x.score !== null).map((x) => x.score as number); return s.length ? Math.max(...s) : null; };
  const cats = [
    { name: 'Quizzes and Final Exam', weight: WEIGHTS.quizzes, kind: 'quiz' as Kind, get: best },
    { name: 'Written Assignments and Final Assessment', weight: WEIGHTS.written, kind: 'assessment' as Kind, get: bestSub },
    { name: 'Discussions', weight: WEIGHTS.discussions, kind: 'discussion' as Kind, get: bestSub },
  ].map((c) => {
    const all = items.filter((i) => i.kind === c.kind);
    const scores = all.map((i) => c.get(i.id)).filter((s): s is number => s !== null);
    return { name: c.name, weight: c.weight, total: all.length, counted: scores.length, avg: scores.length ? scores.reduce((a, b) => a + b, 0) / scores.length : null };
  });
  const used = cats.filter((c) => c.avg !== null);
  const w = used.reduce((a, c) => a + c.weight, 0);
  const percent = w ? Math.round(used.reduce((a, c) => a + (c.avg as number) * c.weight, 0) / w) : null;
  return { cats, percent };
}
