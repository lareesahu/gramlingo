/* ═══════════════════════════════════════════════
   GRAMLINGO — Homepage (Module Overview Cards)
   ═══════════════════════════════════════════════ */

import { useAppContext } from '../app/app-state';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import { Badge } from '../components/Badge/Badge';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import type { GramlinPose } from '../game/types';
import './HomeScreen.css';

function toPose(gramlin: string): GramlinPose {
  return (gramlin?.replace('gramlin-', '').replace('.png', '') || 'book') as GramlinPose;
}

export function HomeScreen() {
  const { language, currentUser, getModuleProgress, navigateTo, setActiveModule, isModuleLocked, isUserLocked } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const userBlocked = currentUser && isUserLocked(currentUser.username);

  return (
    <div className="home-screen animate-fade-in">
      <h1 className="home-title">{s.learningPath}</h1>

      <div className="module-cards stagger">
        {GAME_DATA.modules.map((mod) => {
          const pct = getModuleProgress(mod.id);
          const name = isZh ? mod.nameZh : mod.name;
          const desc = isZh ? mod.descZh : mod.desc;
          const modLocked = currentUser && isModuleLocked(currentUser.username, mod.id);
          const isDisabled = userBlocked || modLocked;

          return (
            <div
              key={mod.id}
              className={`module-overview-card${isDisabled ? ' moc-locked' : ''}`}
              onClick={() => { if (!isDisabled) { setActiveModule(mod.id); navigateTo('module'); } }}
              title={isDisabled ? s.moduleLocked : ''}
            >
              <div className="moc-gramlin">
                <Gramlin pose={toPose(mod.gramlin)} size="md" />
              </div>
              <div className="moc-body">
                <h3>{name}</h3>
                <p className="moc-desc">{desc}</p>
                <ProgressBar value={pct} size="sm" showPercent color={pct >= 70 ? 'correct' : 'primary'} />
              </div>
              <div className="moc-action">
                {isDisabled ? (
                  <Badge variant="danger" size="sm">🔒</Badge>
                ) : (
                  <span className="moc-arrow">→</span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
