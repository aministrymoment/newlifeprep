-- Economics course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('economics', 'Economics', 'Social Studies', 0.5, $j$Economics is a one semester course on how people, businesses and nations make choices with limited resources, and how a person manages money wisely. Students study scarcity and opportunity cost, economic systems, supply and demand, competition, business and entrepreneurship, labor and wages, money, banking and the Federal Reserve, the role of government and taxes, GDP, unemployment and inflation, fiscal and monetary policy, international trade, and personal finance including budgeting, saving, interest, credit and giving. Students read real data, compare viewpoints with respect, and see what Scripture teaches about work, wealth and stewardship. The course aligns to the Florida economics and financial literacy standards and ends with a final economic choices report and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
