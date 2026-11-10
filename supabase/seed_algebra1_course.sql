-- Algebra 1 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('algebra-1', 'Algebra 1', 'Mathematics', 1, $j$Algebra 1 teaches students to read, write and solve the language of mathematics. Students work with expressions, exponents, radicals and polynomials, solve equations and inequalities, build and graph linear functions and systems, factor and solve quadratics, model growth and decay with exponentials, and analyze data. The course aligns to the Florida B.E.S.T. Mathematics standards for Algebra 1 and ends with a cumulative problem set and a 15 question final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
