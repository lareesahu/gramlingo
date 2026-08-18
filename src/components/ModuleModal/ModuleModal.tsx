/* ═══════════════════════════════════════════════
   GRAMLINGO — Module Lesson Modal
   Clicking a module card opens a modal/popup of its
   lesson page (grammar phases or flashcard lessons).
   ═══════════════════════════════════════════════ */

import { useEffect, useRef } from 'react';
import { useAppContext } from '../../app/app-state';
import { Gramlin } from '../Gramlin/Gramlin';
import { GAME_DATA } from '../../game/data';
import { getStrings } from '../../i18n/i18n';
import { langName } from '../../screens/LearningPathScreen';
import './ModuleModal.css';

interface ModuleModalProps {
  moduleId: string | null;
  onClose: () => void;
}

const FOCUSABLE = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';

export function ModuleModal({ moduleId, onClose }: ModuleModalProps) {
  const {
    language, activePanel, getModuleProgress, getPhaseProgress,
    startPhase, isModuleLocked, flashcardModules, enterFlashcardLesson, currentUser,
  } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';
  const panelRef = useRef<HTMLDivElement>(null);
  const lastFocused = useRef<Element | null>(null);

  const titleId = moduleId ? `mm-title-${moduleId}` : undefined;

  // Close on Escape + focus trap + scroll lock while open.
  useEffect(() => {
    if (!moduleId) return;
    // Remember what had focus so we can restore it on close.
    lastFocused.current = document.activeElement;
    // Lock body scroll.
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') { onClose(); return; }
      if (e.key !== 'Tab' || !panelRef.current) return;
      // Focus trap: keep Tab cycling within the modal.
      const els = Array.from(panelRef.current.querySelectorAll<HTMLElement>(FOCUSABLE));
      if (els.length === 0) return;
      const first = els[0];
      const last = els[els.length - 1];
      const active = document.activeElement;
      if (e.shiftKey && (active === first || active === panelRef.current)) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && active === last) {
        e.preventDefault();
        first.focus();
      }
    };
    // Move focus into the modal after mount.
    const t = window.setTimeout(() => {
      const first = panelRef.current?.querySelector<HTMLElement>(FOCUSABLE);
      first?.focus();
    }, 10);

    window.addEventListener('keydown', onKey);
    return () => {
      window.removeEventListener('keydown', onKey);
      window.clearTimeout(t);
      document.body.style.overflow = prevOverflow;
      // Restore focus to whatever opened the modal.
      (lastFocused.current as HTMLElement | null)?.focus?.();
    };
  }, [moduleId, onClose]);

  if (!moduleId) return null;

  // ── Grammar module content ──
  if (activePanel === 'grammar') {
    const mod = GAME_DATA.modules.find((m: { id: string }) => m.id === moduleId);
    if (!mod) return null;
    const order: string[] = GAME_DATA.phaseLockOrder[mod.id] || [];
    const pct = getModuleProgress(mod.id);
    const modLocked = currentUser ? isModuleLocked(currentUser.username, mod.id) : false;

    return (
      <div className="mm-overlay" onClick={onClose} role="dialog" aria-modal="true" aria-labelledby={titleId}>
        <div className="mm-modal" onClick={(e) => e.stopPropagation()} ref={panelRef}>
          <button className="mm-close" onClick={onClose} aria-label={isZh ? '关闭' : 'Close'}>×</button>
          <div className="mm-header">
            <Gramlin pose={(mod.gramlin?.replace('.png', '') || 'book') as any} size="lg" />
            <div>
              <h2 id={titleId}>{isZh ? mod.nameZh : mod.name}</h2>
              <p>{isZh ? mod.descZh : mod.desc}</p>
            </div>
          </div>

          <div className="mm-progress">
            <span>{isZh ? '进度' : 'Progress'}: {Math.round(pct)}%</span>
            <div className="mm-progress-bar"><div className="mm-progress-fill" style={{ width: `${pct}%` }} /></div>
          </div>

          <div className="mm-lessons">
            {order.map((pid: string, i: number) => {
              const phase = GAME_DATA.phases.find((ph: { id: string }) => ph.id === pid);
              const hasQuestions = (phase?.q?.length || 0) > 0;
              const locked = modLocked || !hasQuestions || (
                i > 0 && !getPhaseProgress(order[i - 1])?.completed
              );
              const done = getPhaseProgress(pid)?.completed;
              return (
                <button
                  key={pid}
                  className={`mm-lesson ${locked ? 'mm-lesson--locked' : ''} ${!hasQuestions ? 'mm-lesson--planned' : ''} ${done ? 'mm-lesson--done' : ''}`}
                  onClick={!locked ? () => startPhase(mod.id, pid) : undefined}
                  disabled={locked}
                >
                  <span className="mm-lesson-num">{done ? '✓' : i + 1}</span>
                  <span className="mm-lesson-name">{langName(phase?.name || pid, phase?.nameZh, phase?.nameEs, language)}</span>
                  {!hasQuestions && <span className="mm-lesson-status">{s.comingSoon}</span>}
                  {locked && hasQuestions && <span className="mm-lesson-status">{modLocked ? s.lockedByTeacher : s.locked}</span>}
                  {!locked && !done && <span className="mm-lesson-arrow">→</span>}
                </button>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  // ── Flashcards module content ──
  const fmod = flashcardModules.find((m: { id: string }) => m.id === moduleId);
  if (!fmod) return null;

  return (
    <div className="mm-overlay" onClick={onClose} role="dialog" aria-modal="true" aria-labelledby={titleId}>
      <div className="mm-modal" onClick={(e) => e.stopPropagation()} ref={panelRef}>
        <button className="mm-close" onClick={onClose} aria-label={isZh ? '关闭' : 'Close'}>×</button>
        <div className="mm-header">
          <Gramlin pose={(fmod.gramlin?.replace('.png', '') || 'book') as any} size="lg" />
          <div>
            <h2 id={titleId}>{isZh ? fmod.nameZh : fmod.name}</h2>
            <p>{isZh ? fmod.descZh : fmod.desc}</p>
          </div>
        </div>

        <div className="mm-lessons">
          {fmod.lessons.map((lesson: { id: string; name: string; nameZh?: string }, i: number) => (
            <button
              key={lesson.id}
              className="mm-lesson"
              onClick={() => enterFlashcardLesson(fmod.id, lesson.id)}
            >
              <span className="mm-lesson-num">{i + 1}</span>
              <span className="mm-lesson-name">{isZh ? lesson.nameZh : lesson.name}</span>
              <span className="mm-lesson-arrow">→</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
