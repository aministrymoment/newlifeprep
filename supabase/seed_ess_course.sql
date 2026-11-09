-- Earth and Space Science course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('earth-space-science', 'Earth and Space Science', 'Science', 1.0, $j$Earth and Space Science is a one credit science course that studies our planet and its place in the universe. Students study Earth, the Moon and the Sun, the solar system, stars and galaxies, Earth's layers and plate tectonics, earthquakes and volcanoes, minerals, rocks and the rock cycle, weathering, erosion and soil, geologic time and fossils, the geology of Florida, the atmosphere, weather and hurricanes, oceans, climate, water resources and wise stewardship of the earth. Every lesson is taught by Dr. Alex L. Jenkins Sr. with Scripture from the King James Version, and every unit includes a Focus, Topics, Assessments, Discussions and Quizzes, with a final investigation and a final exam. The course is aligned at the strand level to Florida NGSSS Earth and Space Science benchmarks.$j$)
on conflict (slug) do nothing;
