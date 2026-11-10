-- Health Education course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('health-education', 'Health Education', 'Health', 0.5, $j$Health Education is a one semester course on caring for the whole person: body, mind, relationships and spirit. Students study wellness, nutrition and physical activity, sleep, hygiene and stress, mental and emotional health, alcohol, tobacco, vaping and drugs, disease prevention, safety, first aid and CPR awareness, bullying and online safety, healthy relationships, abstinence and respect, decision making, goal setting and reliable health information. Students learn skills for making wise choices and see what Scripture teaches about the body as the temple of the Holy Ghost. The course gives general education and is not medical advice. It aligns to the Florida health education standards for grades 9 to 12 and ends with a final wellness plan and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
