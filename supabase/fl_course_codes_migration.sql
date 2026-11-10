-- Florida course code registration and benchmark verification tracking (2026-2027 Course Directory).
alter table public.courses add column if not exists fl_course_code text, add column if not exists fl_max_credit numeric(3,1), add column if not exists fl_directory_year text, add column if not exists standards_status text not null default 'not_checked';
create table if not exists public.course_benchmarks (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  code text not null,
  benchmark_text text,
  clarifications text,
  source text not null default 'unverified' check (source in ('cpalms','unverified')),
  verified boolean not null default false,
  unit_title text,
  created_at timestamptz not null default now(),
  unique (course_id, code)
);
alter table public.course_benchmarks enable row level security;
drop policy if exists "benchmarks admin" on public.course_benchmarks;
create policy "benchmarks admin" on public.course_benchmarks for all using (public.is_admin()) with check (public.is_admin());
update public.courses set fl_course_code = v.c, fl_max_credit = 1.0, fl_directory_year = '2026-2027', standards_status = 'code_verified_benchmarks_pending'
from (values ('English 1','1001310'),('English 2','1001340'),('English 3','1001370'),('English 4','1001400')) v(t,c) where courses.title = v.t;
