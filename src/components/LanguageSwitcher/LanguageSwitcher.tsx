/* ═══════════════════════════════════════════════
   GRAMLINGO — Language Switcher (compact dropdown)
   ═══════════════════════════════════════════════ */

import { useAppContext } from '../../app/app-state';
import type { Language } from '../../game/types';
import './LanguageSwitcher.css';

const FLAGS: Record<Language, string> = { en: '🇬🇧', zh: '🇨🇳', es: '🇪🇸' };
const LABELS: Record<Language, string> = { en: 'EN', zh: '中文', es: 'ES' };

export function LanguageSwitcher() {
  const { language, setLanguage } = useAppContext();

  return (
    <select
      className="lang-select"
      value={language}
      onChange={(e) => setLanguage(e.target.value as Language)}
      aria-label="Select language"
    >
      {(['en', 'zh', 'es'] as Language[]).map((l) => (
        <option key={l} value={l}>
          {FLAGS[l]} {LABELS[l]}
        </option>
      ))}
    </select>
  );
}
