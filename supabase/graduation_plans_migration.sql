-- Saved graduation plans built in Administration, Virtual Counselor. Administrators only.
create table if not exists public.graduation_plans (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  user_id uuid references public.profiles(id) on delete set null,
  applicant_name text,
  entering_grade int check (entering_grade between 9 and 12),
  count_in_progress boolean not null default true,
  courses jsonb not null default '[]'::jsonb,
  notes text
);
alter table public.graduation_plans enable row level security;
drop policy if exists "graduation plans admin" on public.graduation_plans;
create policy "graduation plans admin" on public.graduation_plans for all using (public.is_admin()) with check (public.is_admin());
