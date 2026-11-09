-- United States Government course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('united-states-government', 'United States Government', 'Social Studies', 0.5, $j$United States Government is a one semester course on how American government works and how a citizen takes part in it. Students study the purposes and forms of government, the Declaration of Independence, the Articles of Confederation, the Constitution and its principles, the Bill of Rights and the amendments, the three branches, federalism, Florida government, elections, civil liberties and civil rights, the media and interest groups, and the rights and duties of citizens. Students read primary sources, compare viewpoints with respect, and see what Scripture teaches about authority, justice and service. The course aligns to the Florida civics standards for United States Government and ends with a final civic action report and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
