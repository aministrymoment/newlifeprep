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
