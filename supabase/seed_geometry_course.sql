-- Geometry course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('geometry', 'Geometry', 'Mathematics', 1.0, $j$Geometry teaches students to reason, prove and measure. Students build a foundation of logic and constructions, study parallel lines, triangles and congruence, explore similarity and right triangle trigonometry, apply transformations and coordinate geometry, work with polygons and area, and finish with circles and solids. The course aligns to the Florida B.E.S.T. Mathematics standards for Geometry and ends with a cumulative problem set and a 15 question final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
