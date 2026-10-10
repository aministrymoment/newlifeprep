'use client';
import { useCallback, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import type { Course, Item, Sub, Att } from '@/lib/coursePath';

// Loads one course with this student's progress, scores and written work.
export function useCourse(userId: string, slug: string) {
  const [course, setCourse] = useState<Course | null>(null);
  const [items, setItems] = useState<Item[]>([]);
  const [subs, setSubs] = useState<Sub[]>([]);
  const [atts, setAtts] = useState<Att[]>([]);
  const [prog, setProg] = useState<Set<string>>(new Set());
  const [state, setState] = useState<'loading' | 'ok' | 'none'>('loading');

  const loadMine = useCallback(async (courseId: string) => {
    const sb = supabase();
    const { data: its } = await sb.from('course_items').select('*').eq('course_id', courseId).order('position');
    const list = (its || []) as Item[];
    setItems(list);
    const ids = list.map((i) => i.id);
    if (ids.length) {
      const [s, a, p] = await Promise.all([
        sb.from('submissions').select('*').eq('user_id', userId).eq('voided', false).in('item_id', ids).order('created_at', { ascending: false }),
        sb.from('quiz_attempts').select('item_id, score, passed, created_at').eq('user_id', userId).eq('voided', false).in('item_id', ids),
        sb.from('item_progress').select('item_id').eq('user_id', userId).eq('voided', false).in('item_id', ids),
      ]);
      setSubs((s.data || []) as Sub[]); setAtts((a.data || []) as Att[]);
      setProg(new Set((p.data || []).map((r: { item_id: string }) => r.item_id)));
    }
  }, [userId]);

  useEffect(() => {
    (async () => {
      const { data } = await supabase().from('courses').select('*').eq('slug', slug).maybeSingle();
      if (!data) { setState('none'); return; }
      setCourse(data as Course); setState('ok'); loadMine(data.id);
    })();
  }, [slug, loadMine]);

  const reload = useCallback(() => { if (course) return loadMine(course.id); }, [course, loadMine]);
  return { course, items, subs, atts, prog, state, reload };
}
