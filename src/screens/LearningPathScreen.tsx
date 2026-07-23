/* ==================================================
   GRAMLINGO — Learning Path
   Vertical journey cards with progression states
   ================================================== */

import { useState } from "react";
import { useAppContext } from "../app/app-state";
import { Button } from "../components/Button/Button";
import { ProgressBar } from "../components/ProgressBar/ProgressBar";
import { getStrings } from "../i18n/i18n";
import { GAME_DATA } from "../game/data";
import type { Phase, Module } from "../game/types";
import "./LearningPathScreen.css";

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
  const isZh = language === "zh";
  const [openModule, setOpenModule] = useState<string | null>(null);

  const { modules, phases, phaseLockOrder } = GAME_DATA;

  const totalCompleted = progress.filter((p) => p.completed).length;
  const mistakeCount = wrongBook.length;

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
      {/* Welcome + stats banner */}
      {currentUser && (
        <div className="lp__banner animate-fade-in">
          <div className="lp__banner-text">
            <p className="lp__banner-title">
              {isZh ? `欢迎，{currentUser.username}！` : `Welcome, {currentUser.username}!`}
            </p>
            <p className="lp__banner-sub">
              {isZh ? "选择一个模块开始你的语法冒险吧！" : "Pick a module to start your grammar adventure!"}
            </p>
          </div>
          <div className="lp__stats">
            <span className="lp__stat">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-correct)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
              </svg>
              <span className="lp__stat-value">{totalCompleted}</span> {s.completed}
            </span>
            {mistakeCount > 0 && (
              <span className="lp__stat">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-wrong)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                  <polyline points="14 2 14 8 20 8" />
                </svg>
                <span className="lp__stat-value">{mistakeCount}</span> {s.wrongBook}
              </span>
            )}
          </div>
        </div>
      )}

      {/* Module journey cards */}
      <div className="lp__path">
        {modules.map((mod: Module) => {
          const modPhases = phases.filter((p: Phase) => p.module === mod.id);
          const moduleProgress = getModuleProgress(mod.id);
          const completed = modPhases.filter((p) => {
            const prog = getPhaseProgress(p.id);
            return prog?.completed;
          }).length;
          const isOpen = openModule === mod.id;
          const modLocked = currentUser && isModuleLocked(currentUser.username, mod.id);
          const isInProgress = completed > 0 && completed < modPhases.length;
          const isDone = completed === modPhases.length && modPhases.length > 0;
          const coverSrc = import.meta.env.BASE_URL + "assets/covers/cover-" + mod.id + ".jpg";
          const firstUnfinished = modPhases.find(
            (ph: Phase) => !getPhaseProgress(ph.id)?.completed && !isPhaseLockedFn(mod.id, ph.id)
          );

          return (
            <article
              key={mod.id}
              className={`lp__card ${isOpen ? "lp__card--open" : ""} ${modLocked ? "lp__card--locked" : ""} ${isDone ? "lp__card--done" : ""} ${isInProgress ? "lp__card--progress" : ""}`}
              onClick={() => !modLocked && setOpenModule(isOpen ? null : mod.id)}
            >
              {/* Cover image */}
              <div className="lp__img-wrap">
                <img src={coverSrc} alt={isZh ? mod.nameZh : mod.name} className="lp__img" loading="lazy" />
                {isDone && <span className="lp__done-badge">{isZh ? "已完成" : "Done"}</span>}
                {isInProgress && <span className="lp__progress-badge">{completed}/{modPhases.length}</span>}
                {modLocked && (
                  <div className="lp__locked-overlay">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                    <span>{isZh ? "已锁定" : "Locked"}</span>
                  </div>
                )}
              </div>

              {/* Card body */}
              <div className="lp__card-body">
                <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>
                <p className="lp__card-desc">{isZh ? mod.descZh : mod.desc}</p>
                <div className="lp__card-actions">
                  {modLocked ? (
                    <span className="lp__locked-reason">
                      {isZh ? "请先完成上一个模块" : "Complete the previous module first"}
                    </span>
                  ) : isDone ? (
                    <Button size="sm" variant="secondary" onClick={(e: React.MouseEvent) => { e.stopPropagation(); setOpenModule(isOpen ? null : mod.id); }}>
                      {isZh ? "复习" : "Review"}
                    </Button>
                  ) : firstUnfinished && isInProgress ? (
                    <Button size="sm" onClick={(e: React.MouseEvent) => { e.stopPropagation(); startPhase(mod.id, firstUnfinished.id); }}>
                      {s.continue} →
                    </Button>
                  ) : (
                    <Button size="sm" onClick={(e: React.MouseEvent) => { e.stopPropagation(); setOpenModule(isOpen ? null : mod.id); }}>
                      {isZh ? "开始" : "Start"} →
                    </Button>
                  )}
                </div>
              </div>

              {/* Expanded phase panel */}
              {isOpen && (
                <div className="lp__panel" onClick={(e) => e.stopPropagation()}>
                  <div className="lp__panel-drag" onClick={() => setOpenModule(null)} />
                  <h2 className="lp__card-title">{isZh ? mod.nameZh : mod.name}</h2>

                  <div className="lp__phases">
                    {modPhases.map((phase: Phase, i: number) => {
                      const locked = isPhaseLockedFn(mod.id, phase.id);
                      const prog = getPhaseProgress(phase.id);
                      const isPhaseDone = prog?.completed;
                      const isPhaseCurrent = !isPhaseDone && !locked && phase.id === firstUnfinished?.id;

                      return (
                        <button
                          key={phase.id}
                          className={`lp__phase ${locked ? "lp__phase--locked" : ""} ${isPhaseDone ? "lp__phase--done" : ""} ${isPhaseCurrent ? "lp__phase--current" : ""}`}
                          onClick={locked ? undefined : () => startPhase(mod.id, phase.id)}
                          disabled={locked}
                        >
                          <span className="lp__phase-num">
                            {isPhaseDone ? (
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-correct)" strokeWidth="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                            ) : (
                              i + 1
                            )}
                          </span>
                          <span className="lp__phase-name">{isZh ? phase.nameZh : phase.name}</span>
                          {!locked && !isPhaseDone && <span className="lp__phase-arrow">→</span>}
                          {locked && <span className="lp__phase-lock">🔒</span>}
                        </button>
                      );
                    })}
                  </div>

                  {moduleProgress > 0 && <ProgressBar value={moduleProgress} size="sm" />}

                  <div className="lp__panel-cta">
                    {firstUnfinished ? (
                      <button className="lp__pill-btn" onClick={() => startPhase(mod.id, firstUnfinished.id)}>
                        {isInProgress ? s.continue : s.start} →
                      </button>
                    ) : (
                      <button className="lp__pill-btn" onClick={() => setOpenModule(null)}>
                        {isZh ? "已完成" : "All Done"} ✓
                      </button>
                    )}
                  </div>
                </div>
              )}
            </article>
          );
        })}
      </div>

      {/* Mistakes CTA */}
      {mistakeCount > 0 && (
        <div className="lp__mistakes-cta">
          <Button variant="ghost" onClick={() => navigateTo("wrong-book")}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ verticalAlign: "-3px", marginRight: "6px" }}>
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
              <polyline points="14 2 14 8 20 8" />
            </svg>
            {isZh ? `复习你的 {mistakeCount} 个错误` : `Review Your {mistakeCount} Mistake{mistakeCount !== 1 ? "s" : ""}`}
          </Button>
        </div>
      )}
    </div>
  );
}