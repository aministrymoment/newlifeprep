-- English 2 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('english-2', 'English 2', 'English Language Arts', 1.0, $j$English 2 deepens the reading, writing and speaking skills of English 1. Students analyze literature, poetry and Scripture in the King James Version, study how authors use rhetoric and structure in historical American speeches and essays, practice narrative, informative and argumentative writing, and complete a research project with a presentation. The course aligns to the Florida B.E.S.T. ELA standards for grade 10 and ends with a final argumentative essay and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
