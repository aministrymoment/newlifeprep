do $seed$
declare cid uuid;
begin
  select id into cid from public.courses where slug = 'bib-102';
  insert into public.quiz_keys (item_id, answers, explains) select id, '{2,1,3,3,3,0}'::int[], array[$j$Romans is the longest and explains grace and faith in detail.$j$,$j$The wages of sin is death, but the gift of God is eternal life.$j$,$j$Faith cometh by hearing, and hearing by the word of God.$j$,$j$First Corinthians 13 teaches that love is greater than every gift.$j$,$j$Paul wrote that old things are passed away and all things are become new.$j$,$j$Paul taught that a person is justified by faith in Jesus Christ.$j$] from public.course_items where course_id = cid and kind = 'quiz' and title = $j$Unit Quiz 3: Paul's Letters, Part One, Romans to Galatians$j$ on conflict (item_id) do nothing;
end
$seed$;
