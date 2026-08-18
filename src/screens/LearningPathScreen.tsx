import { useState, useRef } from 'react';
import { useAppContext } from '../app/app-state';
import { useDragScroll } from '../hooks/useDragScroll';
import { getStrings } from '../i18n/i18n';
import { ModuleModal } from '../components/ModuleModal/ModuleModal';
import { assetUrl } from '../app/router';

/** Display name in the ACTIVE language only (fallback to primary). */
export function langName(primary: string, zh?: string, es?: string, lang: string = 'en'): string {
  const pick = lang === 'zh' ? zh : lang === 'es' ? es : primary;
  return (pick && pick.trim()) ? pick.trim() : primary;
}
import { GAME_DATA } from '../game/data';
import './LearningPathScreen.css';

export function LearningPathScreen() {
  const { language, currentUser, activePanel, setActivePanel,
    getPhaseProgress, navigateTo, isModuleLocked, progress, errorLog,
    flashcardModules, flashcardReviewStack,
  } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';
  const [modalModule, setModalModule] = useState<string | null>(null);
  const gridRef = useRef<HTMLDivElement>(null);
  const dragScroll = useDragScroll<HTMLDivElement>();

  const { modules, phases } = GAME_DATA;
  const totalCompleted = progress.filter(p => p.completed).length;
  const mistakeCount = errorLog.length;

  const scrollGrid = (dir: number) => { if (gridRef.current) gridRef.current.scrollBy({ left: dir * 300, behavior: 'smooth' }); };

  return (
    <div className="lp">
      {/* ── Panel Tabs ── */}
      <div className="lp__tabs">
        <button
          className={`lp__tab ${activePanel === 'grammar' ? 'lp__tab--active' : ''}`}
          onClick={() => setActivePanel('grammar')}
        >
          {isZh ? '📝 语法' : '📝 Grammar'}
        </button>
        <button
          className={`lp__tab ${activePanel === 'flashcards' ? 'lp__tab--active' : ''}`}
          onClick={() => setActivePanel('flashcards')}
        >
          {isZh ? '🃏 闪卡' : '🃏 Flashcards'}
        </button>
      </div>

      {currentUser && (
        <div className="lp__banner">
          <span className="lp__banner-greeting">{isZh ? '欢迎，' + currentUser.username : 'Hi, ' + currentUser.username}</span>
          <span className="lp__banner-sub">{isZh ? '挑一个模块开始吧' : 'Pick a module to start'}</span>
          <span className="lp__banner-stats">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-correct)" strokeWidth="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            {totalCompleted} {s.completed}
            {mistakeCount > 0 && (<>
              <span style={{margin: '0 4px', color: 'var(--color-border)'}}>|</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-wrong)" strokeWidth="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg>
              <a href="#" onClick={(e) => { e.preventDefault(); navigateTo('error-log'); }} style={{color: 'inherit', textDecoration: 'underline', cursor: 'pointer'}}>{mistakeCount} {s.errorLog}</a>
            </>)}
          </span>
        </div>
      )}

      {/* ═══════════════════════════ GRAMMAR PANEL — LOCKED ═══════════════════════════ */}
      {activePanel === 'grammar' && (
        <div className="lp__grid-wrapper">
          <button type="button" className="lp__grid-arrow lp__grid-arrow--left" onClick={() => scrollGrid(-1)} aria-label="Previous modules">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <div className="lp__grid" ref={gridRef} {...dragScroll}>
            {modules.map(mod => {
              const modPhases = phases.filter(p => p.module === mod.id);
              const playablePhases = modPhases.filter(p => p.q.length > 0);
              const completed = playablePhases.filter(p => getPhaseProgress(p.id)?.completed).length;
              const modLocked = currentUser && isModuleLocked(currentUser.username, mod.id);
              const hasLessons = playablePhases.length > 0;
              const isInProgress = completed > 0 && completed < playablePhases.length;
              const isDone = completed === playablePhases.length && hasLessons;
              const coverSrc = assetUrl('assets/covers/cover-' + mod.id + '.jpg');
              const cls = 'lp__card' + (modLocked ? ' lp__card--locked' : '') + (!hasLessons ? ' lp__card--planned' : '') + (isDone ? ' lp__card--done' : '') + (isInProgress ? ' lp__card--progress' : '');
              const toggleCard = () => {
                if (modLocked) return;
                setModalModule(mod.id);   // open lesson page as a modal/popup
              };

              return (
                <article
                  key={mod.id}
                  className={cls}
                  onClick={toggleCard}
                  onKeyDown={event => {
                    if (event.target === event.currentTarget && (event.key === 'Enter' || event.key === ' ')) { event.preventDefault(); toggleCard(); }
                  }}
                  role="button" tabIndex={0}
                  aria-label={`${isZh ? mod.nameZh : mod.name}: ${s.lessonPlan}`}
                >
                  <div className="lp__collapsed">
                    <div className="lp__img-wrap">
                      <img src={coverSrc} alt={isZh ? mod.nameZh : mod.name} className="lp__img" loading="lazy" draggable={false} />
                      {isDone && <span className="lp__badge lp__badge--done">{isZh ? '已完成' : 'Done'}</span>}
                      {isInProgress && <span className="lp__badge lp__badge--progress">{completed}/{playablePhases.length}</span>}
                      {!hasLessons && <span className="lp__badge lp__badge--planned">{s.comingSoon}</span>}
                      {modLocked && (<div className="lp__locked-overlay"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>)}
                    </div>
                    <div className="lp__card-body">
                      <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                      <p className="lp__card-desc">{isZh ? mod.descZh : mod.desc}</p>
                    </div>
                  </div>
                </article>
              );
            })}
          </div>
          <button type="button" className="lp__grid-arrow lp__grid-arrow--right" onClick={() => scrollGrid(1)} aria-label="Next modules">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </div>
      )}

      {/* ═══════════════════════════ FLASHCARDS PANEL ═══════════════════════════ */}
      {activePanel === 'flashcards' && (
        <div className="lp__grid-wrapper">
          <div className="lp__grid" ref={gridRef} {...dragScroll}>
            {flashcardModules.map(mod => {
              const coverSrc = assetUrl('assets/covers/cover-' + mod.id + '.jpg');
              const cls = 'lp__card';
              const toggleCard = () => {
                setModalModule(mod.id);   // open lesson page as a modal/popup
              };

              return (
                <article
                  key={mod.id}
                  className={cls}
                  onClick={toggleCard}
                  onKeyDown={event => {
                    if (event.target === event.currentTarget && (event.key === 'Enter' || event.key === ' ')) { event.preventDefault(); toggleCard(); }
                  }}
                  role="button" tabIndex={0}
                  aria-label={`${isZh ? mod.nameZh : mod.name}: ${s.lessonPlan}`}
                >
                  <div className="lp__collapsed">
                    <div className="lp__img-wrap">
                      <img src={coverSrc} alt={isZh ? mod.nameZh : mod.name} className="lp__img" loading="lazy" draggable={false} />
                    </div>
                    <div className="lp__card-body">
                      <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                      <p className="lp__card-desc">{isZh ? mod.descZh : mod.desc}</p>
                    </div>
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      )}

      {/* ═══════════════════════════ REVIEW STACK ═══════════════════════════ */}
      {activePanel === 'flashcards' && flashcardReviewStack.length > 0 && (
        <div className="lp__review-stack" onClick={() => navigateTo('flashcard-lesson')}>
          <span>{isZh ? '📋 复习堆' : '📋 Review Stack'}</span>
          <span className="lp__review-count">{flashcardReviewStack.length}</span>
        </div>
      )}

      {/* ═══════════════════════════ MODULE LESSON MODAL ═══════════════════════════ */}
      <ModuleModal moduleId={modalModule} onClose={() => setModalModule(null)} />
    </div>
  );
}
