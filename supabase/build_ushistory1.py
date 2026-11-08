"""Builds supabase/seed_ushistory1_course.sql and seed_ushistory1_unitN.sql (plus short parts) from content/ush1_units*.py. Run: python3 supabase/build_ushistory1.py"""
import json, random, re, sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))
UNIT_MODULES = [('ush1_units1', 'UNIT1'), ('ush1_units2', 'UNIT2'), ('ush1_units3', 'UNIT3'), ('ush1_units4', 'UNIT4'), ('ush1_units5', 'UNIT5'), ('ush1_units6', 'UNIT6')]
PRESENTER = "Dr. Alex L. Jenkins Sr."
SLUG, TITLE = 'united-states-history-1', 'United States History 1'
FOCUS = ("United States History 1 tells the story of the American people from the Civil War and Reconstruction to the modern nation. Students study the Civil War, Reconstruction, the Gilded Age, industrialization, immigration, westward expansion, the Progressive Era, imperialism, World War I, the Roaring Twenties, the Great Depression and the New Deal, World War II, the Cold War, the Civil Rights movement, Vietnam, and modern America. Students analyze primary sources, build timelines, compare viewpoints and write evidence based explanations, honoring the sacrifices of those who built and defended the nation and telling the hard parts of the story with truth and dignity. The course aligns to the Florida Next Generation Sunshine State Standards for United States History and ends with a final assessment and a final exam. Excellence, Faith, Purpose.")
def kjv(ref):
    book, ch = ref.rsplit(' ', 1)
    return {"title": ref.replace("Psalms ", "Psalm ") + " (King James Version)", "url": "/portal/bible/" + book.replace(' ', '') + "/" + ch}
READINGS = {
  "1.1": ["Matthew 12"], "1.2": ["Psalms 133"], "1.3": ["Isaiah 61"], "1.4": ["Amos 5"],
  "2.1": ["Proverbs 10"], "2.2": ["Leviticus 19"], "2.3": ["Exodus 22"], "2.4": ["Psalms 24"],
  "3.1": ["Micah 6"], "3.2": ["Galatians 3"], "3.3": ["Proverbs 16"], "3.4": ["John 15"],
  "4.1": ["1 John 2"], "4.2": ["Psalms 37"], "4.3": ["Galatians 6"], "4.4": ["Proverbs 22"],
  "5.1": ["Nehemiah 4"], "5.2": ["Psalms 144"], "5.3": ["Deuteronomy 16"], "5.4": ["Isaiah 2"],
  "6.1": ["Psalms 20"], "6.2": ["Proverbs 31"], "6.3": ["Proverbs 11"], "6.4": ["2 Chronicles 7"],
}
rng = random.Random(2002370)
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
    outdir = os.path.join(HERE, 'ushistory1_parts'); os.makedirs(outdir, exist_ok=True)
    parts, cur, size = [], [], 0
    for st in stmts:
        if cur and size + len(st) > 6500: parts.append(cur); cur, size = [], 0
        cur.append(st); size += len(st)
    if cur: parts.append(cur)
    for k, p in enumerate(parts, 1):
        open(os.path.join(outdir, '%s_part%d.sql' % (tag, k)), 'w', encoding='utf-8').write(HEAD + "\n".join(p) + "\nend\n$seed$;\n")
    print(tag, "parts", len(parts))
scan(bad, 'focus', FOCUS)
course_sql = ("-- United States History 1 course record. Safe to run more than once.\nalter table public.courses add column if not exists video_url text;\n\n"
              "insert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', 'Social Studies', 1.0, %s)\non conflict (slug) do nothing;\n" % (SLUG, TITLE, lit(FOCUS)))
open(os.path.join(HERE, 'seed_ushistory1_course.sql'), 'w', encoding='utf-8').write(course_sql)
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
    out = "-- United States History 1, unit %d. Run seed_ushistory1_course.sql first. Safe to run more than once.\n\n" % n + HEAD + "\n".join(stmts) + "\nend\n$seed$;\n"
    open(os.path.join(HERE, 'seed_ushistory1_unit%d.sql' % n), 'w', encoding='utf-8').write(out)
    nq = sum(len(q['answers']) for q in qs); total_q += nq
    print("unit", n, "topics", len(u['topics']), "quizzes", len(qs), "questions", nq, "chars", len(out))
    write_parts('unit%d' % n, stmts)
if bad:
    print("HYPHEN OR DASH FOUND IN:", bad); sys.exit(1)
print("clean: no hyphens or dashes")
