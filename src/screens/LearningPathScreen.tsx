import { useState, useRef } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
// types used implicitly in JSX
import './LearningPathScreen.css';

export function LearningPathScreen() {
  const { language, currentUser, getPhaseProgress, navigateTo, startPhase, isModuleLocked, progress, wrongBook } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';
  const [openModule, setOpenModule] = useState<string | null>(null);
  const gridRef = useRef<HTMLDivElement>(null);

  const { modules, phases, phaseLockOrder } = GAME_DATA;
  const totalCompleted = progress.filter(p => p.completed).length;
  const mistakeCount = wrongBook.length;

  const scrollGrid = (dir: number) => { if (gridRef.current) gridRef.current.scrollBy({ left: dir * 300, behavior: 'smooth' }); };

  const isPhaseLockedFn = (moduleId: string, phaseId: string) => {
    const order = phaseLockOrder[moduleId] || [];
    const idx = order.indexOf(phaseId);
    if (idx <= 0) return false;
    return !getPhaseProgress(order[idx - 1])?.completed;
  };

  return (
    <div className="lp">
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
              {mistakeCount} {s.wrongBook}
            </>)}
          </span>
        </div>
      )}
      <div className="lp__grid-wrapper">
        <button className="lp__grid-arrow lp__grid-arrow--left" onClick={() => scrollGrid(-1)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <div className="lp__grid" ref={gridRef}>
          {modules.map(mod => {
            const modPhases = phases.filter(p => p.module === mod.id);
            const completed = modPhases.filter(p => getPhaseProgress(p.id)?.completed).length;
            const isOpen = openModule === mod.id;
            const modLocked = currentUser && isModuleLocked(currentUser.username, mod.id);
            const isInProgress = completed > 0 && completed < modPhases.length;
            const isDone = completed === modPhases.length && modPhases.length > 0;
            const coverSrc = import.meta.env.BASE_URL + 'assets/covers/cover-' + mod.id + '.jpg';
            const firstUnfinished = modPhases.find(ph => !getPhaseProgress(ph.id)?.completed && !isPhaseLockedFn(mod.id, ph.id));
            const cls = 'lp__card' + (isOpen ? ' lp__card--open' : '') + (modLocked ? ' lp__card--locked' : '') + (isDone ? ' lp__card--done' : '') + (isInProgress ? ' lp__card--progress' : '');

            return (
              <article key={mod.id} className={cls} onClick={() => !modLocked && setOpenModule(isOpen ? null : mod.id)}>
                <div className="lp__collapsed">
                  <div className="lp__img-wrap">
                    <img src={coverSrc} alt={isZh ? mod.nameZh : mod.name} className="lp__img" loading="lazy" />
                    {isDone && <span className="lp__badge lp__badge--done">{isZh ? '已完成' : 'Done'}</span>}
                    {isInProgress && <span className="lp__badge lp__badge--progress">{completed}/{modPhases.length}</span>}
                    {modLocked && (<div className="lp__locked-overlay"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>)}
                  </div>
                  <div className="lp__card-body">
                    <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                    <p className="lp__card-desc">{isZh ? mod.descZh : mod.desc}</p>
                  </div>
                </div>
                {isOpen && (
                  <div className="lp__panel" onClick={e => e.stopPropagation()}>
                    <div className="lp__panel-drag" onClick={() => setOpenModule(null)} />
                    <h2 className="lp__panel-title">{isZh ? mod.nameZh : mod.name}</h2>
                    <div className="lp__phases">
                      {modPhases.map((phase, i) => {
                        const locked = isPhaseLockedFn(mod.id, phase.id);
                        const isPhaseDone = getPhaseProgress(phase.id)?.completed;
                        const phaseCls = 'lp__phase' + (locked ? ' lp__phase--locked' : '') + (isPhaseDone ? ' lp__phase--done' : '');
                        return (
                          <button key={phase.id} className={phaseCls} onClick={!locked ? () => startPhase(mod.id, phase.id) : undefined} disabled={locked}>
                            <span className="lp__phase-num">{isPhaseDone ? (<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-correct)" strokeWidth="2.5"><polyline points="20 6 9 17 4 12"/></svg>) : (i + 1)}</span>
                            <span className="lp__phase-name">{isZh ? phase.nameZh : phase.name}</span>
                            {locked && <span className="lp__phase-lock">🔒</span>}
                            {!locked && !isPhaseDone && <span className="lp__phase-arrow">→</span>}
                          </button>
                        );
                      })}
                    </div>
                    <div className="lp__panel-cta">
                      {firstUnfinished ? (
                        <button className="lp__pill-btn" onClick={() => startPhase(mod.id, firstUnfinished.id)}>{isInProgress ? s.continue : s.start} →</button>
                      ) : (
                        <button className="lp__pill-btn" onClick={() => setOpenModule(null)}>{isZh ? '已完成' : 'All Done'} ✓</button>
                      )}
                    </div>
                  </div>
                )}
              </article>
            );
          })}
        </div>
        <button className="lp__grid-arrow lp__grid-arrow--right" onClick={() => scrollGrid(1)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M9 18l6-6-6-6"/></svg>
        </button>
      </div>
      {mistakeCount > 0 && (
        <div className="lp__mistakes-cta">
          <Button variant="ghost" size="sm" onClick={() => navigateTo('wrong-book')}>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{marginRight:4}}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            {isZh ? '复习 ' + mistakeCount + ' 个错误' : 'Review ' + mistakeCount + ' Mistake' + (mistakeCount !== 1 ? 's' : '')}
          </Button>
        </div>
      )}
    </div>
  );
}