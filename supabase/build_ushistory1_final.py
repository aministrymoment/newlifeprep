import json, random, re, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content'))
from ush1_final import FINAL_ASSESS, FINAL_EXAM
HERE = os.path.dirname(os.path.abspath(__file__))
def lit(s): return "$j$" + s + "$j$"
rng = random.Random(2002371)
bad = re.compile(r'[-‐-―−]')
qs = []
for text, opts, ci, ex in FINAL_EXAM:
    order = list(range(len(opts))); rng.shuffle(order)
    qs.append((text, [opts[i] for i in order], order.index(ci), ex))
alltext = FINAL_ASSESS['t'] + FINAL_ASSESS['prompt'] + FINAL_ASSESS['rubric'] + ' '.join(q[0] + ' '.join(q[1]) + q[3] for q in qs)
assert not bad.search(alltext), "hyphen found"
title = "Final Exam: United States History 1"
HEAD = "do $seed$\ndeclare cid uuid;\nbegin\n  select id into cid from public.courses where slug = 'united-states-history-1';\n  if cid is null then raise exception 'Run the course file first'; end if;\n"
def item(kind, pos, t, content):
    return (f"  insert into public.course_items (course_id, kind, position, title, content) select cid, '{kind}', {pos}, {lit(t)}, {lit(json.dumps(content, ensure_ascii=False))}::jsonb "
            f"where not exists (select 1 from public.course_items where course_id = cid and kind = '{kind}' and title = {lit(t)});")
a = item('assessment', 7, FINAL_ASSESS['t'], dict(prompt=FINAL_ASSESS['prompt'], rubric=FINAL_ASSESS['rubric']))
q = item('quiz', 31, title, {"questions": [{"q": x[0], "options": x[1]} for x in qs]})
k = (f"  insert into public.quiz_keys (item_id, answers, explains) select id, '{{{','.join(str(x[2]) for x in qs)}}}'::int[], array[{','.join(lit(x[3]) for x in qs)}] "
     f"from public.course_items where course_id = cid and kind = 'quiz' and title = {lit(title)} on conflict (item_id) do nothing;")
os.makedirs(os.path.join(HERE, 'ushistory1_parts'), exist_ok=True)
open(os.path.join(HERE, 'ushistory1_parts', 'final_part1.sql'), 'w', encoding='utf-8').write(HEAD + a + "\nend\n$seed$;\n")
open(os.path.join(HERE, 'ushistory1_parts', 'final_part2.sql'), 'w', encoding='utf-8').write(HEAD + q + "\n" + k + "\nend\n$seed$;\n")
open(os.path.join(HERE, 'seed_ushistory1_final.sql'), 'w', encoding='utf-8').write("-- United States History 1 final module. Run seed_ushistory1_course.sql first. Safe to run more than once.\n\n" + HEAD + a + "\n" + q + "\n" + k + "\nend\n$seed$;\n")
print("clean; answers", [x[2] for x in qs])
