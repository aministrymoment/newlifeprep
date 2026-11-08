-- United States History 1 course record. Safe to run more than once.
alter table public.courses add column if not exists video_url text;

insert into public.courses (slug, title, subject, credits, focus)
values ('united-states-history-1', 'United States History 1', 'Social Studies', 1.0, $j$United States History 1 tells the story of the American people from the Civil War and Reconstruction to the modern nation. Students study the Civil War, Reconstruction, the Gilded Age, industrialization, immigration, westward expansion, the Progressive Era, imperialism, World War I, the Roaring Twenties, the Great Depression and the New Deal, World War II, the Cold War, the Civil Rights movement, Vietnam, and modern America. Students analyze primary sources, build timelines, compare viewpoints and write evidence based explanations, honoring the sacrifices of those who built and defended the nation and telling the hard parts of the story with truth and dignity. The course aligns to the Florida Next Generation Sunshine State Standards for United States History and ends with a final assessment and a final exam. Excellence, Faith, Purpose.$j$)
on conflict (slug) do nothing;
