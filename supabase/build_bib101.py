"""Builds supabase/seed_bib101_unitN.sql from content/b101_units*.py. Run: python3 supabase/build_bib101.py"""
import json, random, re, sys, os, importlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'content'))
UNIT_MODULES = [('b101_units1', 'UNIT1')]          # add ('b101_units2', 'UNIT2') ... as units are written
PRESENTER = "Dr. Alex L. Jenkins Sr."
def kjv(ref):
    from urllib.parse import quote
    return {"title": ref + " (King James Version)", "url": "https://www.biblegateway.com/passage/?search=" + quote(ref) + "&version=KJV"}
# Scripture reading links per lesson, shown as "Read it here" so students do not need a printed Bible.
READINGS = {
  "1.1": ["Genesis 1", "Genesis 2", "Genesis 3"],
  "1.2": ["Genesis 12", "Genesis 15", "Genesis 22", "Genesis 50"],
  "1.3": ["Exodus 3", "Exodus 12", "Exodus 14", "Exodus 20"],
  "1.4": ["Leviticus 19", "Numbers 6", "Deuteronomy 6"],
}
SLUG, TITLE = 'bib-101', 'BIB 101 Old Testament Survey'
FOCUS = ("BIB 101 is a one credit survey of the Old Testament in the King James Version. Students read the Law, the historical books, "
         "the books of poetry and wisdom, and the prophets, learn the setting and message of each section, and trace God's promise of a "
         "deliverer from Genesis to Malachi. Every lesson includes a reading assignment, a video lesson script, a check quiz, and unit "
         "work in writing and discussion. The course ends with a final assessment and a final exam. Excellence, Faith, Purpose.")
rng = random.Random(1011001)
def shuffle_q(q):
    text, opts, ci, ex = q
    order = list(range(len(opts))); rng.shuffle(order)
    return text, [opts[i] for i in order], order.index(ci), ex
def quiz(title, qs):
    qs = [shuffle_q(q) for q in qs]
    return dict(title=title, content={"questions": [{"q": q[0], "options": q[1]} for q in qs]}, answers=[q[2] for q in qs], explains=[q[3] for q in qs])
def lit(s): return "$j$" + s + "$j$"
def scan(bad, label, s):
    if re.search(r'[-‐-―]', s): bad.append(label)

def item_stmt(kind, pos, it):
    t = lit(it['title'])
    return (f"  insert into public.course_items (course_id, kind, position, title, content) select cid, '{kind}', {pos}, {t}, {lit(json.dumps(it['content'], ensure_ascii=False))}::jsonb "
            f"where not exists (select 1 from public.course_items where course_id = cid and kind = '{kind}' and title = {t});")
def quiz_key_stmt(it):
    ans = "{" + ",".join(map(str, it['answers'])) + "}"
    ex = "array[" + ",".join(lit(e) for e in it['explains']) + "]"
    return (f"  insert into public.quiz_keys (item_id, answers, explains) select id, '{ans}'::int[], {ex} from public.course_items where course_id = cid and kind = 'quiz' and title = {lit(it['title'])} on conflict (item_id) do nothing;")

bad = []
scan(bad, 'focus', FOCUS)
for n, (mod, name) in enumerate(UNIT_MODULES, 1):
    u = getattr(importlib.import_module(mod), name)
    stmts = []
    for i, t in enumerate(u['topics'], 1):
        body = t['body'].strip() + "\n\nCourse area: Bible elective. Scripture is read from the King James Version."
        it = dict(title=t['t'], content=dict(readings=[kjv(r) for r in READINGS.get(t['t'].split(' ')[0], [])], body=body, video="", presenter=PRESENTER, standards="Bible elective", script=t['script'].strip()))
        scan(bad, t['t'], t['t'] + body + t['script'])
        stmts.append(item_stmt('topic', (n - 1) * 4 + i, it))
    a = u['assess']; d = u['disc']
    for lab, s in (('assess', a['t'] + a['prompt'] + a['rubric']), ('disc', d['t'] + d['prompt']), ('unit', u['title'])): scan(bad, lab, s)
    stmts.append(item_stmt('assessment', n, dict(title=a['t'], content=dict(prompt=a['prompt'], rubric=a['rubric']))))
    stmts.append(item_stmt('discussion', n, dict(title=d['t'], content=dict(prompt=d['prompt']))))
    qpos = (n - 1) * 5
    qs = []
    for t in u['topics']:
        qs.append(quiz("Check " + t['t'].split(' ')[0] + ": " + t['t'].split(' ', 1)[1], t['quiz']))
    qs.append(quiz(u['title'].replace('Unit ', 'Unit Quiz ', 1), u['unit_quiz']))
    for j, q in enumerate(qs, 1):
        scan(bad, q['title'], q['title'] + ' '.join(x['q'] + ' '.join(x['options']) for x in q['content']['questions']) + ' '.join(q['explains']))
        stmts.append(item_stmt('quiz', qpos + j, q))
        stmts.append(quiz_key_stmt(q))
    head = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = '%s';\n  if cid is null then raise exception 'Run unit 1 first'; end if;\n" % SLUG
    pre = ""
    if n == 1:
        pre = ("alter table public.courses add column if not exists video_url text;\n\n"
               "insert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', 'Bible', 1.0, %s)\non conflict (slug) do nothing;\n\n" % (SLUG, TITLE, lit(FOCUS)))
    out = "-- BIB 101 Old Testament Survey, unit %d. Safe to run more than once.\n\n" % n + pre + head + "\n".join(stmts) + "\nend\n$seed$;\n"
    open(os.path.join(os.path.dirname(__file__), 'seed_bib101_unit%d.sql' % n), 'w', encoding='utf-8').write(out)
    print("unit", n, "topics", len(u['topics']), "quizzes", len(qs), "questions", sum(len(q['answers']) for q in qs), "chars", len(out))
if bad: print("HYPHENS FOUND IN:", bad); sys.exit(1)
