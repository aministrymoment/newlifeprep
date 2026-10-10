# English 1 Recording Guide

24 videos, one per topic. Scripts are in the Supabase seed (content.script) and in supabase/content/*.py.
Each script runs about 370 to 420 words, which is roughly 3 minutes read aloud. With a pause for on screen examples it reaches 3 to 5 minutes.

Workflow:
1. Print or open the script for one topic (see list in seed_english1.sql, or ask Claude for a printable PDF).
2. Record on camera. Upload to the school YouTube channel as Unlisted.
3. Paste the link into that topic: Supabase, Table editor, course_items, content, field "video".
   Or run:  update public.course_items set content = jsonb_set(content, '{video}', '"https://youtu.be/XXXX"') where title like '1.1 %' and kind = 'topic';
