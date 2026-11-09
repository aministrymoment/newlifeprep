-- English 4 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('english-4', 'English 4', 'English Language Arts', 1.0, $j$English 4 is a survey of British and world literature from Beowulf to the modern age, joined to practical writing and speaking for college, career and ministry. Students read and analyze epic, medieval, Renaissance, Enlightenment, Romantic, Victorian and modern works, study the King James Bible as literature, learn to judge arguments and spot logical fallacies, and practice research, synthesis, personal narrative, professional writing and public speaking. Students write literary analyses and a final essay with a presentation plan. The course aligns to the Florida B.E.S.T. ELA standards for grade 12 and ends with a final literary analysis essay and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
