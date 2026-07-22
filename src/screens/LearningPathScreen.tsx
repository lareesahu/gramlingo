/* ═══════════════════════════════════════════════
   GRAMLINGO — Homepage (module overview cards)
   ═══════════════════════════════════════════════ */

import { useAppContext } from '../app/app-state';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import { Button } from '../components/Button/Button';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import type { GramlinPose } from '../game/types';
import './LearningPathScreen.css';

export function LearningPathScreen() {
  const { language, navigateTo, getModuleProgress, getPhaseProgress, setActiveModule } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const openModule = (moduleId: string) => {
    setActiveModule(moduleId);
    navigateTo('module');
  };

  return (
    <div className="homepage animate-fade-in">
      <h1 className="homepage-title">{s.learningPath}</h1>

      <div className="module-cards stagger">
        {GAME_DATA.modules.map((mod) => {
          const pct = getModuleProgress(mod.id);
          const order = GAME_DATA.phaseLockOrder[mod.id] || [];
          const completed = order.filter((pid) => getPhaseProgress(pid)?.completed).length;
          const pose = (mod.gramlin?.replace('.png', '') || 'book') as GramlinPose;
          const name = isZh ? mod.nameZh : mod.name;
          const desc = isZh ? mod.descZh : mod.desc;

          return (
            <div key={mod.id} className="module-card" onClick={() => openModule(mod.id)}>
              <Gramlin pose={pose} size="lg" />
              <div className="module-card-body">
                <h2>{mod.icon} {name}</h2>
                <p>{desc}</p>
                <ProgressBar value={pct} label={`${completed}/${order.length}`} showPercent color={pct >= 70 ? 'correct' : 'primary'} />
                <div className="module-card-footer">
                  <span className="module-card-stat">{completed} {s.completed}</span>
                  <Button variant="secondary" size="sm">View →</Button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
