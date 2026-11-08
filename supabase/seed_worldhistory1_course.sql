-- World History 1 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('world-history-1', 'World History 1', 'Social Studies', 1.0, $j$World History 1 traces the story of the nations from the fall of Rome to the modern world. Students study the Byzantine Empire, medieval Europe and Japan, the rise of Islam, the kingdoms of Africa, the civilizations of the Americas, the Renaissance, the Reformation, the Scientific Revolution, the Age of Exploration, the Enlightenment, revolutions, industrialization, imperialism, the world wars, the Holocaust, the Cold War and global trends today. Students analyze sources, build timelines, compare viewpoints and write evidence based explanations while seeing how God directs the times and seasons of the nations. The course aligns to the Florida Next Generation Sunshine State Standards for World History and ends with a final assessment and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
