"""Builds supabase/seed_bib102_unitN.sql from content/b102_units*.py. Run: python3 supabase/build_bib102.py"""
import json, random, re, sys, os, importlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'content'))
UNIT_MODULES = [('b102_units1', 'UNIT1'), ('b102_units2', 'UNIT2'), ('b102_units3', 'UNIT3'), ('b102_units4', 'UNIT4'), ('b102_units5', 'UNIT5')]
PRESENTER = "Dr. Alex L. Jenkins Sr."
def kjv(ref):
    book, ch = ref.rsplit(' ', 1)
    return {"title": ref.replace("Psalms ", "Psalm ") + " (King James Version)", "url": "/portal/bible/" + book.replace(' ', '') + "/" + ch}
# Scripture reading links per lesson, shown as "Read it here" so students do not need a printed Bible.
READINGS = {
  "1.1": ["Matthew 1", "Luke 1", "Luke 2", "John 1"],
  "1.2": ["Matthew 3", "Matthew 4", "Matthew 5", "Matthew 6"],
  "1.3": ["Mark 4", "Mark 5", "Luke 15", "John 11"],
  "1.4": ["Luke 23", "John 3", "John 19", "John 20", "Matthew 28"],
  "2.1": ["Acts 1", "Acts 2"],
  "2.2": ["Acts 3", "Acts 4", "Acts 7", "Acts 9"],
  "2.3": ["Acts 10", "Acts 11", "Acts 13", "Acts 15"],
  "2.4": ["Acts 16", "Acts 17", "Acts 20", "Acts 28"],
  "3.1": ["Romans 3", "Romans 5", "Romans 6"],
  "3.2": ["Romans 8", "Romans 10", "Romans 12"],
  "3.3": ["1 Corinthians 12", "1 Corinthians 13", "1 Corinthians 15", "2 Corinthians 5", "2 Corinthians 12"],
  "3.4": ["Galatians 2", "Galatians 3", "Galatians 5"],
  "4.1": ["Ephesians 2", "Ephesians 4", "Ephesians 6"],
  "4.2": ["Philippians 2", "Philippians 4", "Colossians 1", "Colossians 3"],
  "4.3": ["1 Thessalonians 4", "1 Thessalonians 5", "2 Thessalonians 3"],
  "4.4": ["1 Timothy 4", "2 Timothy 3", "Titus 2", "Philemon 1"],
  "5.1": ["Hebrews 4", "Hebrews 11", "Hebrews 12"],
  "5.2": ["James 1", "James 2", "James 3", "James 4"],
  "5.3": ["1 Peter 1", "1 Peter 2", "1 Peter 5", "2 Peter 3"],
  "5.4": ["1 John 1", "1 John 4", "1 John 5", "3 John 1", "Jude 1"],
}
SLUG, TITLE = 'bib-102', 'BIB 102 New Testament Survey'
FOCUS = ("BIB 102 is a one credit survey of the New Testament in the King James Version. Students read the four Gospels, the book of Acts, "
         "the letters of Paul, the General Epistles and Revelation, learn the setting and message of each section, and trace the story of "
         "Jesus Christ, the birth of the church and the hope of His return. Every lesson includes a reading assignment, a video lesson script, "
         "a check quiz, and unit work in writing and discussion. The course ends with a final assessment and a final exam. Excellence, Faith, Purpose.")
rng = random.Random(1021001)
def shuffle_q(q):
    text, opts, ci, ex = q
    order = list(range(len(opts))); rng.shuffle(order)
    return text, [opts[i] for i in order], order.index(ci), ex
def quiz(title, qs):
    qs = [shuffle_q(q) for q in qs]
    if len(qs) >= 3 and len(set(q[2] for q in qs)) == 1:
        # avoid a quiz where every answer sits in the same position: move the correct option for some questions (no random numbers used)
        fixed = []
        for i, (t, o, ci, ex) in enumerate(qs):
            k = (ci + i) % len(o)
            o = list(o); o[ci], o[k] = o[k], o[ci]
            fixed.append((t, o, k, ex))
        qs = fixed
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

HEAD = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = '%s';\n" % SLUG
def write_parts(tag, stmts, plain):
    """Writes short self contained SQL parts (each under about 6500 characters) so chat copy does not cut them off."""
    outdir = os.path.join(os.path.dirname(__file__), 'bib102_parts'); os.makedirs(outdir, exist_ok=True)
    parts, cur, size = [], [], 0
    for st in stmts:
        if cur and size + len(st) > 6500: parts.append(cur); cur, size = [], 0
        cur.append(st); size += len(st)
    if cur: parts.append(cur)
    for k, p in enumerate(parts, 1):
        open(os.path.join(outdir, '%s_part%d.sql' % (tag, k)), 'w', encoding='utf-8').write(HEAD + "\n".join(p) + "\nend\n$seed$;\n")
    print(tag, "parts", len(parts))
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
    out = "-- BIB 102 New Testament Survey, unit %d. Safe to run more than once.\n\n" % n + pre + head + "\n".join(stmts) + "\nend\n$seed$;\n"
    open(os.path.join(os.path.dirname(__file__), 'seed_bib102_unit%d.sql' % n), 'w', encoding='utf-8').write(out)
    print("unit", n, "topics", len(u['topics']), "quizzes", len(qs), "questions", sum(len(q['answers']) for q in qs), "chars", len(out))
    write_parts('unit%d' % n, stmts, n > 1)

# Final Assessment and Final Exam
try:
    from b102_final import FINAL
except ImportError:
    FINAL = None

if FINAL:
    fin_stmts = [item_stmt('assessment', len(UNIT_MODULES) + 1, dict(title=FINAL['assess']['t'], content=dict(prompt=FINAL['assess']['prompt'], rubric=FINAL['assess']['rubric'])))]
    scan(bad, 'final assess', FINAL['assess']['t'] + FINAL['assess']['prompt'] + FINAL['assess']['rubric'])
    fq = quiz("Final Exam: New Testament Survey", FINAL['quiz'])
    scan(bad, 'final exam', fq['title'] + ' '.join(x['q'] + ' '.join(x['options']) for x in fq['content']['questions']) + ' '.join(fq['explains']))
    fin_stmts.append(item_stmt('quiz', len(UNIT_MODULES) * 5 + 1, fq))
    fin_stmts.append(quiz_key_stmt(fq))
    write_parts('final', fin_stmts, True)
if bad:
    print("HYPHEN OR DASH FOUND IN:", bad); sys.exit(1)

