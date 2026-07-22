/* ═══════════════════════════════════════════════
   GRAMLINGO — Module Screen (Phase List)
   ═══════════════════════════════════════════════ */

import { useAppContext } from '../app/app-state';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import { Button } from '../components/Button/Button';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import { scoreToStars, type GramlinPose } from '../game/types';
import './ModuleScreen.css';

function toPose(g: string): GramlinPose {
  return (g?.replace('.png', '') || 'book') as GramlinPose;
}

export function ModuleScreen() {
  const { language, activeModuleId, getModuleProgress, getPhaseProgress, startPhase, navigateTo } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const mod = GAME_DATA.modules.find((m) => m.id === activeModuleId);
  if (!mod) { navigateTo('learning-path'); return null; }

  const pct = getModuleProgress(mod.id);
  const order = GAME_DATA.phaseLockOrder[mod.id] || [];
  const name = isZh ? mod.nameZh : mod.name;
  const desc = isZh ? mod.descZh : mod.desc;

  return (
    <div className="module-screen animate-fade-in">
      <div className="ms-header">
        <Gramlin pose={toPose(mod.gramlin)} size="lg" />
        <div>
          <h2>{name}</h2>
          <p>{desc}</p>
        </div>
      </div>

      <ProgressBar value={pct} label={s.progress} showPercent size="md" color={pct >= 70 ? 'correct' : 'primary'} />

      <div className="ms-phase-list">
        {order.map((pid, i) => {
          const pp = getPhaseProgress(pid);
          const phase = GAME_DATA.phases.find((ph) => ph.id === pid);
          const isLocked = i > 0 && !getPhaseProgress(order[i - 1])?.completed;
          const stars = pp?.bestScore ? scoreToStars(pp.bestScore) : 0;
          const phaseName = isZh && phase?.nameZh ? phase.nameZh : (phase?.name || pid);

          return (
            <div key={pid} className={`ms-phase-item ${isLocked ? 'locked' : ''} ${pp?.completed ? 'done' : ''}`}>
              <div className="ms-phase-info">
                <span className={`ms-phase-num ${isLocked ? 'ms-phase-num-locked' : ''} ${pp?.completed ? 'ms-phase-num-done' : ''}`}>
                  {isLocked ? '' : pp?.completed ? '' : i + 1}
                </span>
                <div>
                  <strong>{phaseName}</strong>
                  {phase?.sub && <p className="ms-phase-sub">{isZh && phase.subZh ? phase.subZh : phase.sub}</p>}
                </div>
              </div>
              <div className="ms-phase-action">
                {pp?.completed ? (
                  <span className="ms-stars">{'★'.repeat(stars)}{'☆'.repeat(3 - stars)} <small>{pp.bestScore}%</small></span>
                ) : isLocked ? (
                  <span className="ms-locked">{s.locked}</span>
                ) : (
                  <Button size="sm" onClick={() => startPhase(mod.id, pid)}>
                    {pp?.attempts ? s.continue : s.start}
                  </Button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
