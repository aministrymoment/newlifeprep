-- Biology 1 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('biology-1', 'Biology 1', 'Science', 1.0, $j$Biology 1 is the study of life from molecules to ecosystems. Students investigate how scientists ask and test questions, the chemistry of living things, cell structure and function, energy in cells through photosynthesis and respiration, heredity and DNA, evolution and classification, the human body, and ecology and stewardship of creation. Students design investigations, analyze data and write evidence based explanations. The course aligns to the Florida Next Generation Sunshine State Standards for Biology 1 and ends with a final assessment and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
