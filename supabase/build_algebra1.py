"""Rebuilds Algebra 1 seed SQL from the database export in content/algebra1_export/part*.jsonl.
Writes seed_algebra1_course.sql, seed_algebra1_unit1..6.sql and seed_algebra1_final.sql.
Run: python3 supabase/build_algebra1.py   (export taken from the live database on November 9, 2026)"""
import json, glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for f in sorted(glob.glob(os.path.join(HERE, 'content', 'algebra1_export', 'part*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        if line.strip(): rows.append(json.loads(line))
course = [r for r in rows if r['kind'] == 'course'][0]['content']
items = {(r['kind'], r['position']): r for r in rows if r['kind'] != 'course'}
SLUG = course['slug']
def lit(s):
    assert '$j$' not in s
    return '$j$' + s + '$j$'
def item_stmt(kind, pos, r):
    t = lit(r['title'])
    return ("  insert into public.course_items (course_id, kind, position, title, content) select cid, '%s', %d, %s, %s::jsonb "
            "where not exists (select 1 from public.course_items where course_id = cid and kind = '%s' and title = %s);" % (kind, pos, t, lit(json.dumps(r['content'], ensure_ascii=False)), kind, t))
def key_stmt(r):
    ans = '{' + ','.join(map(str, r['answers'])) + '}'
    ex = 'array[' + ','.join(lit(e) for e in r['explains']) + ']'
    return ("  insert into public.quiz_keys (item_id, answers, explains) select id, '%s'::int[], %s from public.course_items where course_id = cid and kind = 'quiz' and title = %s on conflict (item_id) do nothing;" % (ans, ex, lit(r['title'])))
HEAD = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = '%s';\n  if cid is null then raise exception 'Run the course file first'; end if;\n" % SLUG
def write(name, stmts):
    open(os.path.join(HERE, name), 'w', encoding='utf-8').write(HEAD + '\n'.join(stmts) + '\nend\n$seed$;\n')
open(os.path.join(HERE, 'seed_algebra1_course.sql'), 'w', encoding='utf-8').write(
    "-- Algebra 1 course record. Safe to run more than once.\nalter table public.courses add column if not exists video_url text;\n\n"
    "insert into public.courses (slug, title, subject, credits, focus)\nvalues ('%s', '%s', '%s', %s, %s)\non conflict (slug) do nothing;\n" % (SLUG, course['title'], course['subject'], course['credits'], lit(course['focus'])))
for u in range(1, 7):
    st = []
    for p in range(4 * u - 3, 4 * u + 1): st.append(item_stmt('topic', p, items[('topic', p)]))
    st.append(item_stmt('assessment', u, items[('assessment', u)]))
    st.append(item_stmt('discussion', u, items[('discussion', u)]))
    for p in range(5 * u - 4, 5 * u + 1):
        r = items[('quiz', p)]; st.append(item_stmt('quiz', p, r)); st.append(key_stmt(r))
    write('seed_algebra1_unit%d.sql' % u, st)
fin = [item_stmt('assessment', 7, items[('assessment', 7)]), item_stmt('quiz', 31, items[('quiz', 31)]), key_stmt(items[('quiz', 31)])]
write('seed_algebra1_final.sql', fin)
print('topics', sum(1 for k in items if k[0]=='topic'), 'assessments', sum(1 for k in items if k[0]=='assessment'), 'discussions', sum(1 for k in items if k[0]=='discussion'), 'quizzes', sum(1 for k in items if k[0]=='quiz'))
