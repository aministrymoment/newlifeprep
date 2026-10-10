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
