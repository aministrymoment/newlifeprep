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
