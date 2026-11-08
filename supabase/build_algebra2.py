"""Builds supabase/seed_algebra2_course.sql and seed_algebra2_unitN.sql (plus short parts) from content/a2_units*.py. Run: python3 supabase/build_algebra2.py"""
import json, random, re, sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))
UNIT_MODULES = [('a2_units1', 'UNIT1'), ('a2_units2', 'UNIT2'), ('a2_units3', 'UNIT3'), ('a2_units4', 'UNIT4'), ('a2_units5', 'UNIT5'), ('a2_units6', 'UNIT6')]
PRESENTER = "Dr. Alex L. Jenkins Sr."
SLUG, TITLE = 'algebra-2', 'Algebra 2'
FOCUS = ("Algebra 2 extends the algebra of Algebra 1 and Geometry to functions of every major family. Students study function operations, transformations and inverses, quadratic and complex numbers, polynomial and rational functions, radicals and absolute value, exponential and logarithmic functions with financial applications, and systems of equations and inequalities. Students model real situations, fit functions to data, and justify solutions. The course aligns to the Florida B.E.S.T. Mathematics standards for Algebra 2 and ends with a final project and a final exam. Excellence, Faith, Purpose.")
def kjv(ref):
    book, ch = ref.rsplit(' ', 1)
    return {"title": ref.replace("Psalms ", "Psalm ") + " (King James Version)", "url": "/portal/bible/" + book.replace(' ', '') + "/" + ch}
READINGS = {}
rng = random.Random(2002340)
def shuffle_q(q):
    text, opts, ci, ex = q
    order = list(range(len(opts))); rng.shuffle(order)
    return text, [opts[i] for i in order], order.index(ci), ex
def quiz(title, qs):
    qs = [shuffle_q(q) for q in qs]
    return dict(title=title, content={"questions": [{"q": q[0], "options": q[1]} for q in qs]}, answers=[q[2] for q in qs], explains=[q[3] for q in qs])
def lit(s): return "$j$" + s + "$j$"
bad = []
def scan(bad_list, label, s):
    if re.search(r'[-\u2010-\u2015]', s): bad_list.append(label)
def item_stmt(kind, pos, it):
    t = lit(it['title'])
    return (f"  insert into public.course_items (course_id, kind, position, title, content) select cid, '{kind}', {pos}, {t}, {lit(json.dumps(it['content'], ensure_ascii=False))}::jsonb "
            f"where not exists (select 1 from public.course_items where course_id = cid and kind = '{kind}' and title = {t});")
def quiz_key_stmt(it):
    ans = "{" + ",".join(map(str, it['answers'])) + "}"
    ex = "array[" + ",".join(lit(e) for e in it['explains']) + "]"
    return (f"  insert into public.quiz_keys (item_id, answers, explains) select id, '{ans}'::int[], {ex} from public.course_items where course_id = cid and kind = 'quiz' and title = {lit(it['title'])} on conflict (item_id) do nothing;")
HEAD = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = '%s';\n  if cid is null then raise exception 'Run the course file first'; end if;\n" % SLUG
def write_parts(tag, stmts):
    outdir = os.path.join(HERE, 'algebra2_parts'); os.makedirs(outdir, exist_ok=True)
    parts, cur, size = [], [], 0
    for st in stmts:
        if cur and size + len(st) > 6500: parts.append(cur); cur, size = [], 0
        cur.append(st); size += len(st)
    if cur: parts.append(cur)
    for k, p in enumerate(parts, 1):
        open(os.path.join(outdir, '%s_part%d.sql' % (tag, k)), 'w', encoding='utf-8').write(HEAD + "\n".join(p) + "\nend\n$seed$;\n")
    print(tag, "parts", len(parts))
scan(bad, 'focus', FOCUS)
course_sql = ("-- Algebra 2 course record. Safe to run more than once.\nalter table public.courses add column if not exists video_url text;\n\n"
              "insert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', 'Mathematics', 1.0, %s)\non conflict (slug) do nothing;\n" % (SLUG, TITLE, lit(FOCUS)))
open(os.path.join(HERE, 'seed_algebra2_course.sql'), 'w', encoding='utf-8').write(course_sql)
total_q = 0
for n, (mod, name) in enumerate(UNIT_MODULES, 1):
    try: u = getattr(importlib.import_module(mod), name)
    except ModuleNotFoundError: continue
    stmts = []
    for i, t in enumerate(u['topics'], 1):
        body = t['body'].strip() + "\n\nFlorida standards: " + t['std'] + "."
        it = dict(title=t['t'], content=dict(readings=[kjv(r) for r in READINGS.get(t['t'].split(' ')[0], [])], body=body, video="", presenter=PRESENTER, standards=t['std'], script=t['script'].strip()))
        scan(bad, t['t'], t['t'] + body + t['script'])
        stmts.append(item_stmt('topic', (n - 1) * 4 + i, it))
    a = u['assess']; d = u['disc']
    for lab, s in (('assess', a['t'] + a['prompt'] + a['rubric']), ('disc', d['t'] + d['prompt']), ('unit', u['title'])): scan(bad, lab, s)
    stmts.append(item_stmt('assessment', n, dict(title=a['t'], content=dict(prompt=a['prompt'], rubric=a['rubric']))))
    stmts.append(item_stmt('discussion', n, dict(title=d['t'], content=dict(prompt=d['prompt']))))
    qpos = (n - 1) * 5
    qs = [quiz("Check " + t['t'].split(' ')[0] + ": " + t['t'].split(' ', 1)[1], t['quiz']) for t in u['topics']]
    qs.append(quiz(u['title'].replace('Unit ', 'Unit Quiz ', 1), u['unit_quiz']))
    for j, q in enumerate(qs, 1):
        scan(bad, q['title'], q['title'] + ' '.join(x['q'] + ' '.join(x['options']) for x in q['content']['questions']) + ' '.join(q['explains']))
        stmts.append(item_stmt('quiz', qpos + j, q)); stmts.append(quiz_key_stmt(q))
    out = "-- Algebra 2, unit %d. Run seed_algebra2_course.sql first. Safe to run more than once.\n\n" % n + HEAD + "\n".join(stmts) + "\nend\n$seed$;\n"
    open(os.path.join(HERE, 'seed_algebra2_unit%d.sql' % n), 'w', encoding='utf-8').write(out)
    nq = sum(len(q['answers']) for q in qs); total_q += nq
    print("unit", n, "topics", len(u['topics']), "quizzes", len(qs), "questions", nq, "chars", len(out))
    write_parts('unit%d' % n, stmts)
if bad:
    print("HYPHEN OR DASH FOUND IN:", bad); sys.exit(1)
print("clean: no hyphens or dashes")
