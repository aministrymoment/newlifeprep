"""Verifies quoted KJV verses against public/kjv. Usage: python3 supabase/check_quotes.py <module> <QUOTESVAR> <UNITVAR>"""
import sys, os, json, re, importlib
base = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(base, 'content'))
mod, qv, uv = sys.argv[1:4]
m = importlib.import_module(mod)
def norm(s): return re.sub(r'\s+', ' ', s.replace('’', "'")).strip().lower()
bad = 0
full = ' '.join(t['script'] + ' ' + t['body'] for t in getattr(m, uv)['topics'])
for ref, q in getattr(m, qv):
    book, ch = ref.rsplit(' ', 1)
    d = json.load(open(os.path.join(base, '..', 'public', 'kjv', book.replace(' ', '') + '.json')))
    txt = norm(' '.join(d[int(ch) - 1]))
    if norm(q) not in txt: print('NOT IN KJV:', ref, q[:60]); bad += 1
    if norm(q) not in norm(full): print('NOT IN SCRIPT:', ref, q[:60]); bad += 1
print('quotes checked', len(getattr(m, qv)), 'problems', bad)
