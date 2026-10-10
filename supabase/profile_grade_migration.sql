-- Adds the student's grade level (9, 10, 11 or 12). Only administrators can change it. Safe to run more than once.
alter table public.profiles add column if not exists grade_level int check (grade_level between 9 and 12);
