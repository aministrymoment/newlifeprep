-- Algebra 2 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('algebra-2', 'Algebra 2', 'Mathematics', 1.0, $j$Algebra 2 extends the algebra of Algebra 1 and Geometry to functions of every major family. Students study function operations, transformations and inverses, quadratic and complex numbers, polynomial and rational functions, radicals and absolute value, exponential and logarithmic functions with financial applications, and systems of equations and inequalities. Students model real situations, fit functions to data, and justify solutions. The course aligns to the Florida B.E.S.T. Mathematics standards for Algebra 2 and ends with a final project and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
