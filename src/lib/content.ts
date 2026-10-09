import fs from 'fs';
import path from 'path';
import { SITE } from '@/site';

export function loadContent(name: string): string {
  const raw = fs.readFileSync(path.join(process.cwd(), 'src', 'content', `${name}.html`), 'utf8');
  const einFooter = SITE.showEin ? `<span class="footer-id">Federal EIN: ${SITE.ein}</span>` : '';
  const einContact = SITE.showEin
    ? `<div style="display:flex;gap:16px;align-items:flex-start;"><span style="font-size:24px;min-width:36px;">🔢</span><div><p style="font-family:Cinzel,serif;font-size:10px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:4px;">Federal EIN</p><p style="font-size:16px;color:var(--text);">${SITE.ein}</p></div></div>`
    : '';
  return raw
    .replaceAll('{{SCHOOL}}', SITE.name)
    .replaceAll('{{MINISTRY_LINE}}', SITE.ministryLine)
    .replaceAll('{{EIN_FOOTER}}', einFooter)
    .replaceAll('{{EIN_CONTACT}}', einContact);
}
