-- Christian Ethics course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('christian-ethics', 'Christian Ethics', 'Bible', 0.5, $j$Christian Ethics is a one semester course on how followers of Jesus decide what is right and live it out. Students study why ethics matters, the character of God, conscience, the Ten Commandments and the two great commandments, the fruit of the Spirit, and fair summaries of other ways of thinking about right and wrong. Students then apply Scripture to honesty and integrity, purity and self control, money and work, words, anger and forgiveness, the dignity of human life, justice and care for the poor, technology and artificial intelligence, and citizenship and conscience. Students practice respectful discussion and writing with evidence from the King James Version. The course ends with a final ethics portfolio and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
