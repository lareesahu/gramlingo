/* ═══════════════════════════════════════════════
   GRAMLINGO — Completion Screen
   Stars, score, next phase unlock, retry
   ═══════════════════════════════════════════════ */

import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { StarRating } from '../components/StarRating/StarRating';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import './CompletionScreen.css';

export function CompletionScreen() {
  const { language, navigateTo, activeModuleId, activePhaseId, getPhaseProgress, getModuleProgress, getModuleAttempted, startPhase } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const phaseProgress = activePhaseId ? getPhaseProgress(activePhaseId) : undefined;
  const score = phaseProgress?.bestScore || 0;
  const modulePct = activeModuleId ? getModuleProgress(activeModuleId) : 0;
  const attempted = activeModuleId ? getModuleAttempted(activeModuleId) : { attempted: 0, total: 0 };

  const phase = GAME_DATA.phases.find((p) => p.id === activePhaseId);
  const module = GAME_DATA.modules.find((m) => m.id === activeModuleId);
  const order = activeModuleId ? GAME_DATA.phaseLockOrder[activeModuleId] || [] : [];
  const currentIdx = order.indexOf(activePhaseId || '');
  const nextPhaseId = currentIdx >= 0 && currentIdx < order.length - 1 ? order[currentIdx + 1] : null;
  const nextPhase = nextPhaseId ? GAME_DATA.phases.find((p) => p.id === nextPhaseId) : null;

  const handleRetry = () => {
    if (activeModuleId && activePhaseId) {
      startPhase(activeModuleId, activePhaseId);
    }
  };

  const handleNextPhase = () => {
    if (activeModuleId && nextPhaseId) {
      startPhase(activeModuleId, nextPhaseId);
    }
  };

  return (
    <div className="completion-screen animate-fade-in">
      <div className="completion-card">
        <div className="completion-gramlin">
          {score >= 90 ? (
            <Gramlin pose="grad" size="xl" animated />
          ) : score >= 70 ? (
            <Gramlin pose="grad" size="xl" animated />
          ) : (
            <Gramlin pose="think" size="xl" />
          )}
        </div>

        <h1 className="completion-title">{s.completion}</h1>
        <p className="completion-phase">
          {isZh ? phase?.nameZh : phase?.name}
        </p>

        <div className="completion-score">
          <StarRating score={score} size="lg" animated showScore />
        </div>

        {score >= 70 && nextPhase && (
          <div className="completion-unlock animate-slide-up">
            <p>🔓 {s.unlock}</p>
            <p className="unlock-phase">
              → {isZh ? nextPhase.nameZh : nextPhase.name}
            </p>
          </div>
        )}

        <div className="completion-module-progress">
          <ProgressBar
            value={modulePct}
            label={`${module?.name} ${s.progress}`}
            showPercent
            color={modulePct >= 70 ? 'correct' : 'primary'}
            size="sm"
          />
        </div>

        <div className="completion-module-attempted">
          <span className="attempted-text">{isZh ? `${attempted.attempted} / ${attempted.total} 个阶段已尝试` : `${attempted.attempted} of ${attempted.total} phases attempted`}</span>
        </div>

        <div className="completion-actions">
          <Button variant="secondary" onClick={handleRetry}>
            🔄 {s.retryPhase}
          </Button>
          {score >= 70 && nextPhaseId && (
            <Button onClick={handleNextPhase}>
              {s.nextPhase} →
            </Button>
          )}
          <Button variant="ghost" onClick={() => navigateTo('learning-path')}>
            {s.home}
          </Button>
        </div>
      </div>
    </div>
  );
}
