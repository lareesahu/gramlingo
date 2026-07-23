/* ═══════════════════════════════════════════════
   GRAMLINGO — Learning Path (Journey Cards with Swipe Navigation)
   ═══════════════════════════════════════════════ */

import { useState, useRef } from 'react';
import { useAppContext } from '../app/app-state';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import { Button } from '../components/Button/Button';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import type { Phase, Module, PhaseProgress } from '../game/types';
import './LearningPathScreen.css';

const arrowLeft = '<path d="M15 18l-6-6 6-6"/>';
const arrowRight = '<path d="M9 18l6-6-6-6"/>';

export function LearningPathScreen() {
  const {
    language,
    currentUser,
    getModuleProgress,
    getPhaseProgress,
    navigateTo,
    startPhase,
    isModuleLocked,
    progress,
    wrongBook,
  } = useAppContext();

  const s = getStrings(language);
  const isZh = language === 'zh';
  const [openModule, setOpenModule] = useState<string | null>(null);
  const gridRef = useRef<HTMLDivElement>(null);

  const { modules, phases, phaseLockOrder } = GAME_DATA;

  // Calculate stats from available progress data
  const totalCompleted = progress.filter((p: PhaseProgress) => p.completed).length;
  const totalAttempted = progress.length;
  const mistakeCount = wrongBook.length;

  const scrollGrid = (dir: number) => {
    if (gridRef.current) gridRef.current.scrollBy({ left: dir * 320, behavior: 'smooth' });
  };

  // Check if a phase is locked (previous phase not completed)
  const isPhaseLockedFn = (moduleId: string, phaseId: string) => {
    const order = phaseLockOrder[moduleId] || [];
    const idx = order.indexOf(phaseId);
    if (idx <= 0) return false;
    const prevPhaseId = order[idx - 1];
    const prevProg = getPhaseProgress(prevPhaseId);
    return !prevProg?.completed;
  };

  return (
    <div className="lp">
      {/* Welcome banner */}
      {currentUser && totalAttempted === 0 ? (
        <div className="lp__banner animate-fade-in">
          <img
            src={`${import.meta.env.BASE_URL}assets/gramlin/neutral-gramlin.png`}
            alt="Gramlin"
            className="lp__banner-gramlin"
            width={48}
            height={48}
          />
          <div className="lp__banner-text">
            <p className="lp__banner-title">
              {isZh ? `欢迎，${currentUser.username}！` : `Welcome, ${currentUser.username}!`}
            </p>
            <p className="lp__banner-sub">
              {isZh ? '选择一个模块开始你的语法冒险吧！' : 'Pick a module to start your grammar adventure!'}
            </p>
          </div>
        </div>
      ) : currentUser ? (
        <div className="lp__stats">
          <span className="lp__stat">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--gl-primary)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
            </svg>
            <span className="lp__stat-value">{totalCompleted}</span> {s.completed}
          </span>
          <span className="lp__stat">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--gl-text-secondary)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="16" y1="13" x2="8" y2="13" />
              <line x1="16" y1="17" x2="8" y2="17" />
            </svg>
            <span className="lp__stat-value">{mistakeCount}</span> {s.wrongBook}
          </span>
          <Button size="sm" variant="ghost" onClick={() => navigateTo('admin')}>{s.admin}</Button>
        </div>
      ) : null}

      {/* Module cards with arrow nav */}
      <div className="lp__grid-wrapper">
        <button className="lp__grid-arrow lp__grid-arrow--left" onClick={() => scrollGrid(-1)} aria-label="Scroll left">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: arrowLeft }} />
        </button>
        <div className="lp__grid" ref={gridRef}>
          {modules.map((mod: Module) => {
            const modPhases = phases.filter((p: Phase) => p.module === mod.id);
            const moduleProgress = getModuleProgress(mod.id);
            const completed = Object.values(moduleProgress).filter((p: PhaseProgress) => p.completed).length;
            const isOpen = openModule === mod.id;
            const modLocked = currentUser && isModuleLocked(currentUser.username, mod.id);
            const coverSrc = `${import.meta.env.BASE_URL}assets/covers/cover-${mod.id}.jpg`;
            const firstUnfinished = modPhases.find(
              (ph: Phase) => !getPhaseProgress(ph.id)?.completed && !isPhaseLockedFn(mod.id, ph.id)
            );

            return (
              <article
                key={mod.id}
                className={`lp__card ${isOpen ? 'lp__card--open' : ''} ${modLocked ? 'lp__card--locked' : ''}`}
                onClick={() => !modLocked && setOpenModule(isOpen ? null : mod.id)}
              >
                {/* ====== COLLAPSED FACE: Storybook ====== */}
                <div className="lp__collapsed">
                  <div className="lp__img-wrap">
                    <img src={coverSrc} alt={isZh ? mod.nameZh : mod.name} className="lp__img" loading="lazy" />
                    <span className="lp__spark lp__spark--1">✨</span>
                    <span className="lp__spark lp__spark--2">⭐</span>
                    <span className="lp__spark lp__spark--3">💫</span>
                  </div>
                  <div className="lp__card-body">
                    <span className="lp__card-emoji">{String(mod.icon || '📖')}</span>
                    <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                    <p className="lp__card-desc">{isZh ? mod.descZh : mod.desc}</p>
                    <span className="lp__pill">
                      {completed === modPhases.length ? s.retry : completed > 0 ? s.continue : s.start} →
                    </span>
                  </div>
                </div>

                {/* ====== EXPANDED PANEL: slides up ====== */}
                <div className="lp__panel" onClick={(e) => e.stopPropagation()}>
                  <div className="lp__panel-drag" onClick={() => setOpenModule(null)} />
                  <span className="lp__card-emoji">{String(mod.icon || '📖')}</span>
                  <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                  <p className="lp__panel-sub">{isZh ? mod.descZh : mod.desc}</p>

                  <div className="lp__phases">
                    {modPhases.map((phase: Phase, i: number) => {
                      const locked = isPhaseLockedFn(mod.id, phase.id);
                      const prog = getPhaseProgress(phase.id);
                      return (
                        <button
                          key={phase.id}
                          className={`lp__phase ${locked ? 'lp__phase--locked' : ''} ${prog?.completed ? 'lp__phase--done' : ''}`}
                          onClick={locked ? undefined : () => startPhase(mod.id, phase.id)}
                          disabled={locked}
                        >
                          <span className="lp__phase-num">{i + 1}</span>
                          <span className="lp__phase-dot" />
                          <span className="lp__phase-name">{isZh ? phase.nameZh : phase.name}</span>
                          {!locked && <span className="lp__phase-arrow">→</span>}
                        </button>
                      );
                    })}
                  </div>

                  {moduleProgress > 0 && <ProgressBar value={moduleProgress} size="sm" />}

                  <div className="lp__panel-cta">
                    <button className="lp__pill-btn" onClick={() => {
                      if (firstUnfinished) startPhase(mod.id, firstUnfinished.id);
                      else setOpenModule(null);
                    }}>
                      {completed === modPhases.length ? s.retry : completed > 0 ? s.continue : s.start} →
                    </button>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
        <button className="lp__grid-arrow lp__grid-arrow--right" onClick={() => scrollGrid(1)} aria-label="Scroll right">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: arrowRight }} />
        </button>
      </div>

      {/* Past Mistakes CTA */}
      {mistakeCount > 0 && (
        <div className="lp__mistakes-cta">
          <Button size="md" variant="ghost" onClick={() => navigateTo('wrong-book')}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ verticalAlign: '-3px', marginRight: 'var(--gl-space-2)' }}>
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="16" y1="13" x2="8" y2="13" />
              <line x1="16" y1="17" x2="8" y2="17" />
            </svg>
            {isZh ? `改写你的 ${mistakeCount} 个错误` : `Rewrite Your ${mistakeCount} Mistake${mistakeCount !== 1 ? 's' : ''}`}
          </Button>
        </div>
      )}
    </div>
  );
}