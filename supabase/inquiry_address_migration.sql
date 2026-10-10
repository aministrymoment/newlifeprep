-- Adds an optional mailing address to website messages so labels can be printed. Safe to run more than once.
alter table public.inquiries add column if not exists street text;
alter table public.inquiries add column if not exists city text;
alter table public.inquiries add column if not exists state text;
alter table public.inquiries add column if not exists zip text;
