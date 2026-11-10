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

-- Package 2: Mathematics. Probability and Statistics is provisional: 1210300 is Probability and Statistics Honors in the directory; Mathematics for College Statistics (1210305) is under evaluation.
update public.courses set fl_course_code = v.c, fl_max_credit = 1.0, fl_directory_year = '2026-2027', standards_status = v.s
from (values ('Algebra 1','1200310','code_verified_benchmarks_pending'),('Geometry','1206310','code_verified_benchmarks_pending'),('Algebra 2','1200330','code_verified_benchmarks_pending'),('Probability and Statistics','1210300','provisional_course_selection_pending')) v(t,c,s) where courses.title = v.t;

-- Package 3: Science.
update public.courses set fl_course_code = v.c, fl_max_credit = 1.0, fl_directory_year = '2026-2027', standards_status = 'code_verified_benchmarks_pending'
from (values ('Biology 1','2000310'),('Chemistry','2003340'),('Physical Science','2003310'),('Earth and Space Science','2001310')) v(t,c) where courses.title = v.t;

-- Package 4: Social Studies. Economics with Financial Literacy (2102335) is terminated after 2023-2024 and must not be treated as current.
update public.courses set fl_course_code = v.c, fl_max_credit = v.m, fl_directory_year = '2026-2027', standards_status = v.s
from (values
 ('World History 1','2109310',1.0,'code_pending_current_version_check'),
 ('United States History 1','2100310',1.0,'code_pending_current_version_check'),
 ('United States Government','2106310',0.5,'code_pending_current_version_check'),
 ('Economics','2102310',0.5,'code_pending_current_status_check'),
 ('Economics with Financial Literacy','2102335',0.5,'terminated_after_2023_2024_do_not_use_as_current'),
 ('Personal Finance and Stewardship',NULL,0.5,'candidate_2102372_pending_verification')
) v(t,c,m,s) where courses.title = v.t;

-- Packages 5 and 6: electives, supporting courses, Biblical Studies, Entrepreneurship. No codes assigned without verification.
update public.courses set fl_directory_year = '2026-2027', standards_status = v.s
from (values
 ('Physical Education with Personal Fitness','provisional_match_HOPE_pending'),
 ('Health Education','provisional_match_pending'),
 ('Spanish 1','provisional_match_pending'),
 ('Spanish 2','provisional_match_pending'),
 ('Personal Finance and Stewardship','candidates_2102372_or_8500120_pending'),
 ('Music Appreciation and Worship Arts','provisional_match_pending'),
 ('Public Speaking and Communication','provisional_match_pending'),
 ('Digital Technology and Computer Applications','provisional_match_pending'),
 ('Entrepreneurship and Business Stewardship','pending_cte_course_level_verification')
) v(t,s) where courses.title = v.t;
update public.courses set standards_status = 'school_designed', fl_course_code = null, fl_max_credit = null, fl_directory_year = null
where title in ('Christian Ethics') or title like 'BIB 101%' or title like 'BIB 102%';
