-- New Life Preparatory Academy: portal database
-- Run this whole file once in Supabase: SQL Editor, New query, paste, Run.

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  full_name text,
  student_id text unique,          -- format NLPA-20XX-XXX
  role text not null default 'student' check (role in ('student','admin')),
  created_at timestamptz not null default now()
);

create table if not exists public.courses (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  subject text,
  credits numeric(3,1) not null default 1,
  focus text,                       -- the Focus of the course
  video_url text,                   -- optional introduction video (YouTube, Vimeo or .mp4 link)
  active boolean not null default true,
  created_at timestamptz not null default now()
);

-- Every course carries Topics, Assessments, Discussions and Quizzes (Focus lives on the course)
create table if not exists public.course_items (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  kind text not null check (kind in ('topic','assessment','discussion','quiz')),
  position int not null default 0,
  title text not null,
  content jsonb not null default '{}'::jsonb,
  -- topic: {"body": "..."}  assessment/discussion: {"prompt": "...", "rubric": "..."}
  -- quiz: {"questions":[{"q":"...","options":["..",".."]}]}   (answers live in quiz_keys, never sent to students)
  created_at timestamptz not null default now()
);
create index if not exists course_items_course_idx on public.course_items(course_id, kind, position);

create table if not exists public.enrollments (
  user_id uuid not null references public.profiles(id) on delete cascade,
  course_id uuid not null references public.courses(id) on delete cascade,
  status text not null default 'active' check (status in ('active','completed','withdrawn')),
  enrolled_at timestamptz not null default now(),
  primary key (user_id, course_id)
);

create table if not exists public.quiz_attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  item_id uuid not null references public.course_items(id) on delete cascade,
  score int not null check (score between 0 and 100),
  passed boolean not null,         -- 70 percent or better
  answers jsonb,
  created_at timestamptz not null default now()
);
create index if not exists quiz_attempts_user_idx on public.quiz_attempts(user_id, item_id);

-- Written work for assessments and discussions
create table if not exists public.submissions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  item_id uuid not null references public.course_items(id) on delete cascade,
  body text not null,
  score int check (score between 0 and 100),
  feedback text,
  status text not null default 'submitted' check (status in ('submitted','graded')),
  created_at timestamptz not null default now(),
  graded_at timestamptz
);
create index if not exists submissions_user_idx on public.submissions(user_id, item_id);

-- Helper: is the current user an administrator
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;

-- Create a profile automatically when a user is created
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, full_name)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'full_name', ''))
  on conflict (id) do nothing;
  return new;
end; $$;
drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- Row level security
alter table public.profiles enable row level security;
alter table public.courses enable row level security;
alter table public.course_items enable row level security;
alter table public.enrollments enable row level security;
alter table public.quiz_attempts enable row level security;
alter table public.submissions enable row level security;

-- profiles: read own or admin; students can edit only their name, never their role or ID
create policy "profiles read" on public.profiles for select using (id = auth.uid() or public.is_admin());
create policy "profiles admin write" on public.profiles for update using (public.is_admin()) with check (public.is_admin());
create or replace function public.update_my_name(new_name text) returns void
language sql security definer set search_path = public as $$
  update public.profiles set full_name = new_name where id = auth.uid();
$$;

-- courses and items: signed in students see courses they are enrolled in; admins see all and manage
create policy "courses read" on public.courses for select using (
  public.is_admin() or exists (select 1 from public.enrollments e where e.course_id = courses.id and e.user_id = auth.uid()));
create policy "courses admin" on public.courses for all using (public.is_admin()) with check (public.is_admin());
create policy "items read" on public.course_items for select using (
  public.is_admin() or exists (select 1 from public.enrollments e where e.course_id = course_items.course_id and e.user_id = auth.uid()));
create policy "items admin" on public.course_items for all using (public.is_admin()) with check (public.is_admin());

create policy "enroll read" on public.enrollments for select using (user_id = auth.uid() or public.is_admin());
create policy "enroll admin" on public.enrollments for all using (public.is_admin()) with check (public.is_admin());

create policy "attempts read" on public.quiz_attempts for select using (user_id = auth.uid() or public.is_admin());

create policy "subs read" on public.submissions for select using (user_id = auth.uid() or public.is_admin());
create policy "subs insert" on public.submissions for insert with check (user_id = auth.uid() and status = 'submitted' and score is null);
create policy "subs admin update" on public.submissions for update using (public.is_admin()) with check (public.is_admin());


-- Answer keys: administrators only. Students are graded by grade_quiz(), so answers never reach the browser.
create table if not exists public.quiz_keys (
  item_id uuid primary key references public.course_items(id) on delete cascade,
  answers int[] not null,           -- index of the correct option for each question, in order
  explains text[]                   -- optional explanation for each question
);
alter table public.quiz_keys enable row level security;
create policy "keys admin" on public.quiz_keys for all using (public.is_admin()) with check (public.is_admin());

create or replace function public.grade_quiz(p_item uuid, p_answers int[]) returns json
language plpgsql security definer set search_path = public as $$
declare k public.quiz_keys; v_course uuid; n int; right_n int := 0; i int; flags boolean[] := '{}'; pct int; ok boolean;
begin
  select course_id into v_course from public.course_items where id = p_item and kind = 'quiz';
  if v_course is null then raise exception 'Quiz not found'; end if;
  if not (public.is_admin() or exists (select 1 from public.enrollments where user_id = auth.uid() and course_id = v_course and status <> 'withdrawn')) then
    raise exception 'Not enrolled';
  end if;
  select * into k from public.quiz_keys where item_id = p_item;
  if k.item_id is null then raise exception 'Quiz has no answer key yet'; end if;
  n := array_length(k.answers, 1);
  for i in 1..n loop
    flags := flags || (p_answers[i] is not null and p_answers[i] = k.answers[i]);
    if flags[i] then right_n := right_n + 1; end if;
  end loop;
  pct := round(100.0 * right_n / n); ok := pct >= 70;
  insert into public.quiz_attempts(user_id, item_id, score, passed, answers) values (auth.uid(), p_item, pct, ok, to_jsonb(p_answers));
  return json_build_object('score', pct, 'passed', ok, 'correct', flags, 'explains', case when ok then to_json(k.explains) else null end);
end; $$;

-- Sample course so you can test the portal. Delete it later from the admin page or SQL editor.
insert into public.courses (slug, title, subject, credits, focus)
values ('sample-course', 'Sample Course (delete later)', 'Sample', 0.5,
  'This sample course shows how every NLPA course is organized: a Focus, Topics, Assessments, Discussions and Quizzes.')
on conflict (slug) do nothing;

insert into public.course_items (course_id, kind, position, title, content)
select c.id, v.kind, v.position, v.title, v.content::jsonb
from public.courses c,
(values
 ('topic', 1, 'Topic 1: Welcome', '{"body":"Welcome to New Life Preparatory Academy. This is a sample topic. Real lessons will follow the Florida State Standards."}'),
 ('topic', 2, 'Topic 2: How lessons work', '{"body":"Each lesson ends with a quiz. You need 70 percent or better to pass, and you may retake it until you pass."}'),
 ('assessment', 1, 'Assessment 1: Short response', '{"prompt":"In 3 to 5 sentences, tell us what you hope to accomplish at NLPA.","rubric":"Clear, complete, in your own words."}'),
 ('discussion', 1, 'Discussion 1: Purpose', '{"prompt":"Share one goal you have for the next year and why it matters to you."}'),
 ('quiz', 1, 'Quiz 1: Getting started', '{"questions":[{"q":"What score do you need to pass a quiz?","options":["50 percent","60 percent","70 percent or better","100 percent"]},{"q":"Can you retake a quiz you did not pass?","options":["No","Yes, until you pass","Only once","Only with a fee"]}]}')
) as v(kind, position, title, content)
where c.slug = 'sample-course'
  and not exists (select 1 from public.course_items i where i.course_id = c.id);

insert into public.quiz_keys (item_id, answers, explains)
select i.id, '{2,1}'::int[], array['Every quiz requires 70 percent or better.','You may retake each quiz until you pass.']
from public.course_items i join public.courses c on c.id = i.course_id
where c.slug = 'sample-course' and i.kind = 'quiz'
on conflict (item_id) do nothing;
-- Lesson progress: records which lessons a student has marked complete. Safe to run more than once.
create table if not exists public.item_progress (
  user_id uuid not null references public.profiles(id) on delete cascade,
  item_id uuid not null references public.course_items(id) on delete cascade,
  completed_at timestamptz not null default now(),
  primary key (user_id, item_id)
);
alter table public.item_progress enable row level security;
drop policy if exists "progress read" on public.item_progress;
drop policy if exists "progress insert" on public.item_progress;
create policy "progress read" on public.item_progress for select using (user_id = auth.uid() or public.is_admin());
create policy "progress insert" on public.item_progress for insert with check (user_id = auth.uid());
grant select, insert on public.item_progress to authenticated;
-- Adds the student's grade level (9, 10, 11 or 12). Only administrators can change it. Safe to run more than once.
alter table public.profiles add column if not exists grade_level int check (grade_level between 9 and 12);
-- Limits each quiz to 3 attempts to reach 70 percent. Administrators can unlock more. Safe to run more than once.
alter table public.quiz_attempts add column if not exists voided boolean not null default false;

create or replace function public.grade_quiz(p_item uuid, p_answers int[]) returns json
language plpgsql security definer set search_path = public as $$
declare k public.quiz_keys; v_course uuid; n int; right_n int := 0; i int; flags boolean[] := '{}'; pct int; ok boolean; used int;
begin
  select course_id into v_course from public.course_items where id = p_item and kind = 'quiz';
  if v_course is null then raise exception 'Quiz not found'; end if;
  if not (public.is_admin() or exists (select 1 from public.enrollments where user_id = auth.uid() and course_id = v_course and status <> 'withdrawn')) then
    raise exception 'Not enrolled';
  end if;
  if exists (select 1 from public.quiz_attempts where user_id = auth.uid() and item_id = p_item and voided = false and passed) then
    raise exception 'Quiz already passed';
  end if;
  select count(*) into used from public.quiz_attempts where user_id = auth.uid() and item_id = p_item and voided = false;
  if used >= 3 then raise exception 'No attempts left'; end if;
  select * into k from public.quiz_keys where item_id = p_item;
  if k.item_id is null then raise exception 'Quiz has no answer key yet'; end if;
  n := array_length(k.answers, 1);
  for i in 1..n loop
    flags := flags || (p_answers[i] is not null and p_answers[i] = k.answers[i]);
    if flags[i] then right_n := right_n + 1; end if;
  end loop;
  pct := round(100.0 * right_n / n); ok := pct >= 70;
  insert into public.quiz_attempts(user_id, item_id, score, passed, answers) values (auth.uid(), p_item, pct, ok, to_jsonb(p_answers));
  return json_build_object('score', pct, 'passed', ok, 'correct', flags, 'explains', case when ok then to_json(k.explains) else null end, 'attempts', used + 1, 'left', 3 - (used + 1));
end; $$;

-- Administrators can give a student a fresh set of 3 attempts. Old attempts are kept but no longer count.
create or replace function public.admin_reset_attempts(p_user uuid, p_item uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'Administrators only'; end if;
  update public.quiz_attempts set voided = true where user_id = p_user and item_id = p_item and voided = false;
end; $$;

-- Saves every website contact form message so none can be lost. Only administrators can read or manage them. Safe to run more than once.
create table if not exists public.inquiries (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text not null,
  email text not null,
  phone text,
  program text,
  message text not null,
  status text not null default 'new' check (status in ('new', 'handled')),
  emailed boolean not null default false
);
create index if not exists inquiries_status_idx on public.inquiries(status, created_at desc);
alter table public.inquiries enable row level security;
drop policy if exists "inquiries admin" on public.inquiries;
create policy "inquiries admin" on public.inquiries for all using (public.is_admin()) with check (public.is_admin());
grant select, update, delete on public.inquiries to authenticated;
