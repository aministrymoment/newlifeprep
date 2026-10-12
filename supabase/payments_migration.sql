-- Records every NLPA Stripe payment (and refunds) so the office can see them in Administration.
-- Only the server webhook writes to this table. Only administrators can read it. Safe to run more than once.
create table if not exists public.payments (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  stripe_session_id text not null unique,
  payment_intent text,
  item text not null,
  label text,
  amount_cents integer not null,
  currency text not null default 'usd',
  payer_name text,
  payer_email text,
  reference text,
  status text not null default 'paid' check (status in ('paid', 'partially_refunded', 'refunded')),
  refunded_cents integer not null default 0,
  receipt_no text unique
);
create index if not exists payments_created_idx on public.payments(created_at desc);
create index if not exists payments_intent_idx on public.payments(payment_intent);

-- Receipt numbers follow NLPA-RCP-YYYY-NNN, counting up each year.
create or replace function public.set_receipt_no() returns trigger language plpgsql as $$
declare n int; y text := to_char(coalesce(new.created_at, now()), 'YYYY');
begin
  if new.receipt_no is null then
    perform pg_advisory_xact_lock(7413);
    select coalesce(max(substring(receipt_no from '[0-9]+$')::int), 0) + 1 into n
      from public.payments where receipt_no like 'NLPA-RCP-' || y || '-%';
    new.receipt_no := 'NLPA-RCP-' || y || '-' || lpad(n::text, 3, '0');
  end if;
  return new;
end; $$;
drop trigger if exists payments_receipt_no on public.payments;
create trigger payments_receipt_no before insert on public.payments for each row execute function public.set_receipt_no();

alter table public.payments enable row level security;
drop policy if exists "payments admin read" on public.payments;
create policy "payments admin read" on public.payments for select using (public.is_admin());
grant select on public.payments to authenticated;
