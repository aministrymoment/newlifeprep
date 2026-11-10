"""Builds seed SQL for half credit courses (3 units of 4 lessons plus final) from content modules.
Run: python3 supabase/build_half.py health   (or ethics, econfl)
Writes seed_<key>_course.sql, seed_<key>_unit1..3.sql and seed_<key>_final.sql. Hyphen scan blocks any hyphen or dash."""
import json, random, re, sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))
PRESENTER = "Dr. Alex L. Jenkins Sr."
CFG = {
 'health': dict(prefix='hl', slug='health-education', title='Health Education', subject='Health', seed=2002522,
   exam_title='Final Exam: Health Education', readings={
   "1.1": ["1 Corinthians 6"], "1.2": ["Daniel 1"], "1.3": ["Psalms 127"], "1.4": ["Psalms 34"],
   "2.1": ["Proverbs 20"], "2.2": ["Proverbs 22"], "2.3": ["Proverbs 27"], "2.4": ["Ephesians 4"],
   "3.1": ["Proverbs 13"], "3.2": ["Proverbs 4"], "3.3": ["Proverbs 1"], "3.4": ["1 Thessalonians 5"]}),
 'ethics': dict(prefix='ce', slug='christian-ethics', title='Christian Ethics', subject='Bible', seed=2002524,
   exam_title='Final Exam: Christian Ethics', readings={
   "1.1": ["Micah 6"], "1.2": ["Exodus 20"], "1.3": ["Galatians 5"], "1.4": ["Romans 12"],
   "2.1": ["Ephesians 4"], "2.2": ["Philippians 4"], "2.3": ["Colossians 3"], "2.4": ["James 3"],
   "3.1": ["Psalms 139"], "3.2": ["Proverbs 31"], "3.3": ["Philippians 4"], "3.4": ["1 Peter 3"]}),
 'econfl': dict(prefix='ef', slug='economics-financial-literacy', title='Economics with Financial Literacy', subject='Social Studies', seed=2002526,
   exam_title='Final Exam: Economics with Financial Literacy', readings={
   "1.1": ["Genesis 41"], "1.2": ["Proverbs 11"], "1.3": ["Proverbs 14"], "1.4": ["Proverbs 22"],
   "2.1": ["Ecclesiastes 3"], "2.2": ["Matthew 22"], "2.3": ["2 Thessalonians 3"], "2.4": ["Luke 14"],
   "3.1": ["Proverbs 21"], "3.2": ["Romans 13"], "3.3": ["Ecclesiastes 11"], "3.4": ["Malachi 3"]}),
}
key = sys.argv[1]
c = CFG[key]
mods = [(c['prefix'] + '_units%d' % n, 'UNIT%d' % n) for n in (1, 2, 3)]
FOCUS = importlib.import_module(c['prefix'] + '_final').FOCUS
def kjv(ref):
    book, ch = ref.rsplit(' ', 1)
    return {"title": ref.replace("Psalms ", "Psalm ") + " (King James Version)", "url": "/portal/bible/" + book.replace(' ', '') + "/" + ch}
rng = random.Random(c['seed'])
def shuffle_q(q):
    text, opts, ci, ex = q
    order = list(range(len(opts))); rng.shuffle(order)
    return text, [opts[i] for i in order], order.index(ci), ex
def quiz(title, qs):
    qs = [shuffle_q(q) for q in qs]
    return dict(title=title, content={"questions": [{"q": q[0], "options": q[1]} for q in qs]}, answers=[q[2] for q in qs], explains=[q[3] for q in qs])
def lit(s): return "$j$" + s + "$j$"
bad = []
def scan(label, s):
    if re.search(r'[-‐-―−]', s): bad.append(label)
def item_stmt(kind, pos, it):
    t = lit(it['title'])
    return (f"  insert into public.course_items (course_id, kind, position, title, content) select cid, '{kind}', {pos}, {t}, {lit(json.dumps(it['content'], ensure_ascii=False))}::jsonb "
            f"where not exists (select 1 from public.course_items where course_id = cid and kind = '{kind}' and title = {t});")
def key_stmt(it):
    ans = "{" + ",".join(map(str, it['answers'])) + "}"
    ex = "array[" + ",".join(lit(e) for e in it['explains']) + "]"
    return (f"  insert into public.quiz_keys (item_id, answers, explains) select id, '{ans}'::int[], {ex} from public.course_items where course_id = cid and kind = 'quiz' and title = {lit(it['title'])} on conflict (item_id) do nothing;")
HEAD = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = '%s';\n  if cid is null then raise exception 'Run the course file first'; end if;\n" % c['slug']
scan('focus', FOCUS)
open(os.path.join(HERE, 'seed_%s_course.sql' % key), 'w', encoding='utf-8').write(
  "-- %s course record. Safe to run more than once.\nalter table public.courses add column if not exists video_url text;\n\ninsert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', '%s', 0.5, %s)\non conflict (slug) do nothing;\n" % (c['title'], c['slug'], c['title'], c['subject'], lit(FOCUS)))
tq = 0
for n, (mod, name) in enumerate(mods, 1):
    u = getattr(importlib.import_module(mod), name)
    stmts = []
    assert len(u['topics']) == 4
    for i, t in enumerate(u['topics'], 1):
        body = t['body'].strip() + "\n\nFlorida standards: " + t['std'] + "."
        num = t['t'].split(' ')[0]
        it = dict(title=t['t'], content=dict(readings=[kjv(r) for r in c['readings'].get(num, [])], body=body, video="", presenter=PRESENTER, standards=t['std'], script=t['script'].strip()))
        scan(t['t'], t['t'] + body + t['script'])
        assert len(t['quiz']) == 4, t['t']
        stmts.append(item_stmt('topic', (n - 1) * 4 + i, it))
    a = u['assess']; d = u['disc']
    scan('assess%d' % n, a['t'] + a['prompt'] + a['rubric']); scan('disc%d' % n, d['t'] + d['prompt']); scan('unit%d' % n, u['title'])
    stmts.append(item_stmt('assessment', n, dict(title=a['t'], content=dict(prompt=a['prompt'], rubric=a['rubric']))))
    stmts.append(item_stmt('discussion', n, dict(title=d['t'], content=dict(prompt=d['prompt']))))
    qs = [quiz("Check " + t['t'].split(' ')[0] + ": " + t['t'].split(' ', 1)[1], t['quiz']) for t in u['topics']]
    assert len(u['unit_quiz']) == 8
    qs.append(quiz(u['title'].replace('Unit ', 'Unit Quiz ', 1), u['unit_quiz']))
    for j, q in enumerate(qs, 1):
        scan(q['title'], q['title'] + ' '.join(x['q'] + ' '.join(x['options']) for x in q['content']['questions']) + ' '.join(q['explains']))
        for qq in q['content']['questions']: assert len(set(qq['options'])) == len(qq['options']) == 4, qq
        stmts.append(item_stmt('quiz', (n - 1) * 5 + j, q)); stmts.append(key_stmt(q))
    open(os.path.join(HERE, 'seed_%s_unit%d.sql' % (key, n)), 'w', encoding='utf-8').write(
      "-- %s, unit %d. Run seed_%s_course.sql first. Safe to run more than once.\n\n" % (c['title'], n, key) + HEAD + "\n".join(stmts) + "\nend\n$seed$;\n")
    nq = sum(len(q['answers']) for q in qs); tq += nq
    print("unit", n, "quizzes", len(qs), "questions", nq)
# final module
F = importlib.import_module(c['prefix'] + '_final')
rng2 = random.Random(c['seed'] + 1)
fq = []
for text, opts, ci, ex in F.FINAL_EXAM:
    order = list(range(len(opts))); rng2.shuffle(order)
    fq.append((text, [opts[i] for i in order], order.index(ci), ex))
assert len(fq) == 15
scan('final', F.FINAL_ASSESS['t'] + F.FINAL_ASSESS['prompt'] + F.FINAL_ASSESS['rubric'] + ' '.join(q[0] + ' '.join(q[1]) + q[3] for q in fq))
for q in fq: assert len(set(q[1])) == 4
a = item_stmt('assessment', 4, dict(title=F.FINAL_ASSESS['t'], content=dict(prompt=F.FINAL_ASSESS['prompt'], rubric=F.FINAL_ASSESS['rubric'])))
fqd = dict(title=c['exam_title'], answers=[q[2] for q in fq], explains=[q[3] for q in fq], content={"questions": [{"q": q[0], "options": q[1]} for q in fq]})
q = item_stmt('quiz', 16, fqd); k = key_stmt(fqd)
open(os.path.join(HERE, 'seed_%s_final.sql' % key), 'w', encoding='utf-8').write(
  "-- %s final module. Run seed_%s_course.sql first. Safe to run more than once.\n\n" % (c['title'], key) + HEAD + a + "\n" + q + "\n" + k + "\nend\n$seed$;\n")
print("total questions", tq + 15)
if bad:
    print("HYPHEN OR DASH FOUND IN:", bad); sys.exit(1)
print("clean: no hyphens or dashes")
