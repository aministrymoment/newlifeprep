-- English 3 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('english-3', 'English 3', 'English Language Arts', 1.0, $j$English 3 is a survey of American literature and rhetoric from early colonial voices to the modern era. Students read and analyze essays, speeches, stories and poems from each period, study how authors use rhetoric, symbol, allegory and contrast, compare writers who treat related subjects, and read Scripture in the King James Version alongside the literature. Students write literary analyses, complex narratives and argumentative essays, complete a literary research project with a presentation, and practice grammar and vocabulary. The course aligns to the Florida B.E.S.T. ELA standards for grade 11 and ends with a final literary analysis essay and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
