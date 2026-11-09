"""Builds supabase/seed_ess_course.sql and seed_ess_unitN.sql (plus short parts) from content/ess_units*.py. Run: python3 supabase/build_ess.py"""
import json, random, re, sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))
UNIT_MODULES = [('ess_units1', 'UNIT1'), ('ess_units2', 'UNIT2'), ('ess_units3', 'UNIT3'), ('ess_units4', 'UNIT4'), ('ess_units5', 'UNIT5'), ('ess_units6', 'UNIT6')]
PRESENTER = "Dr. Alex L. Jenkins Sr."
SLUG, TITLE = 'earth-space-science', 'Earth and Space Science'
FOCUS = ("Earth and Space Science is a one credit science course that studies our planet and its place in the universe. Students study Earth, the Moon and the Sun, the solar system, stars and galaxies, Earth's layers and plate tectonics, earthquakes and volcanoes, minerals, rocks and the rock cycle, weathering, erosion and soil, geologic time and fossils, the geology of Florida, the atmosphere, weather and hurricanes, oceans, climate, water resources and wise stewardship of the earth. Every lesson is taught by Dr. Alex L. Jenkins Sr. with Scripture from the King James Version, and every unit includes a Focus, Topics, Assessments, Discussions and Quizzes, with a final investigation and a final exam. The course is aligned at the strand level to Florida NGSSS Earth and Space Science benchmarks.")
def kjv(ref):
    book, ch = ref.rsplit(' ', 1)
    return {"title": ref.replace("Psalms ", "Psalm ") + " (King James Version)", "url": "/portal/bible/" + book.replace(' ', '') + "/" + ch}
READINGS = {
  "1.1": ["Job 38"], "1.2": ["Genesis 1"], "1.3": ["Psalms 8"], "1.4": ["Psalms 19"],
  "2.1": ["Proverbs 8"], "2.2": ["Psalms 104"], "2.3": ["Psalms 46"], "2.4": ["Psalms 90"],
  "3.1": ["Job 28"], "3.2": ["Isaiah 51"], "3.3": ["Matthew 7"], "3.4": ["Job 14"],
  "4.1": ["Ecclesiastes 3"], "4.2": ["Psalms 102"], "4.3": ["Job 12"], "4.4": ["Deuteronomy 8"],
  "5.1": ["Isaiah 40"], "5.2": ["Ecclesiastes 1"], "5.3": ["Job 36"], "5.4": ["Mark 4"],
  "6.1": ["Psalms 107"], "6.2": ["Genesis 8"], "6.3": ["John 4"], "6.4": ["Psalms 24", "Genesis 2"],
}
rng = random.Random(2002450)
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
    outdir = os.path.join(HERE, 'ess_parts'); os.makedirs(outdir, exist_ok=True)
    parts, cur, size = [], [], 0
    for st in stmts:
        if cur and size + len(st) > 6500: parts.append(cur); cur, size = [], 0
        cur.append(st); size += len(st)
    if cur: parts.append(cur)
    for k, p in enumerate(parts, 1):
        open(os.path.join(outdir, '%s_part%d.sql' % (tag, k)), 'w', encoding='utf-8').write(HEAD + "\n".join(p) + "\nend\n$seed$;\n")
    print(tag, "parts", len(parts))
scan(bad, 'focus', FOCUS)
course_sql = ("-- Earth and Space Science course record. Safe to run more than once.\nalter table public.courses add column if not exists video_url text;\n\n"
              "insert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', 'Science', 1.0, %s)\non conflict (slug) do nothing;\n" % (SLUG, TITLE, lit(FOCUS)))
open(os.path.join(HERE, 'seed_ess_course.sql'), 'w', encoding='utf-8').write(course_sql)
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
    out = "-- Earth and Space Science, unit %d. Run seed_ess_course.sql first. Safe to run more than once.\n\n" % n + HEAD + "\n".join(stmts) + "\nend\n$seed$;\n"
    open(os.path.join(HERE, 'seed_ess_unit%d.sql' % n), 'w', encoding='utf-8').write(out)
    nq = sum(len(q['answers']) for q in qs); total_q += nq
    print("unit", n, "topics", len(u['topics']), "quizzes", len(qs), "questions", nq, "chars", len(out))
    write_parts('unit%d' % n, stmts)
if bad:
    print("HYPHEN OR DASH FOUND IN:", bad); sys.exit(1)
print("clean: no hyphens or dashes")
