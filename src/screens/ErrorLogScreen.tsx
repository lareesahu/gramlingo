/* ═══════════════════════════════════════════════
   GRAMLINGO — WrongBook Screen
   Filterable review of missed questions
   ═══════════════════════════════════════════════ */

import { useState } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { Badge } from '../components/Badge/Badge';
import { Card } from '../components/Card/Card';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import './ErrorLogScreen.css';

export function ErrorLogScreen() {
  const { language, navigateTo, errorLog, getErrorsByModule, startPhase } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const [filterModule, setFilterModule] = useState<string | null>(null);

  const filtered = filterModule ? getErrorsByModule(filterModule) : errorLog;
  const sorted = [...filtered].sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

  const handleRetryQuestion = (entry: typeof sorted[0]) => {
    startPhase(entry.moduleId, entry.phaseId);
  };

  if (errorLog.length === 0) {
    return (
      <div className="errorlog-empty">
        <Gramlin pose="sleeper" size="xl" />
        <h2>{s.errorLogEmpty}</h2>
        <Button onClick={() => navigateTo('learning-path')}>{s.home}</Button>
      </div>
    );
  }

  return (
    <div className="errorlog-screen animate-fade-in">
      <div className="errorlog-header">
        <h2>📝 {s.errorLog} ({errorLog.length})</h2>
        <Button variant="ghost" size="sm" onClick={() => navigateTo('learning-path')}>
          ← {s.home}
        </Button>
      </div>

      {/* Filter chips */}
      <div className="errorlog-filters">
        <button
          className={`filter-chip ${!filterModule ? 'filter-chip--active' : ''}`}
          onClick={() => setFilterModule(null)}
        >
          All
        </button>
        {GAME_DATA.modules.map((mod) => (
          <button
            key={mod.id}
            className={`filter-chip ${filterModule === mod.id ? 'filter-chip--active' : ''}`}
            onClick={() => setFilterModule(filterModule === mod.id ? null : mod.id)}
          >
            {getErrorsByModule(mod.id).length > 0 && (
              <Badge variant="danger" size="sm">{getErrorsByModule(mod.id).length}</Badge>
            )}
            {isZh ? mod.nameZh : mod.name}
          </button>
        ))}
      </div>

      {/* Wrong entries */}
      <div className="errorlog-list">
        {sorted.map((entry, i) => {
          const phase = GAME_DATA.phases.find((p) => p.id === entry.phaseId);
          const question = phase?.q[entry.questionIndex];
          const module = GAME_DATA.modules.find((m) => m.id === entry.moduleId);
          const date = new Date(entry.timestamp).toLocaleDateString();

          return (
            <Card key={`${entry.moduleId}-${entry.phaseId}-${entry.questionIndex}-${i}`} className="error-entry">
              <div className="error-entry-header">
                <Badge variant="default">{isZh ? module?.nameZh : module?.name}</Badge>
                <Badge variant="info">{isZh ? phase?.nameZh : phase?.name}</Badge>
                <span className="error-date">{date}</span>
              </div>

              {question && (
                <div className="error-entry-question">
                  <p dangerouslySetInnerHTML={{ __html: question.q }} />
                </div>
              )}

              <div className="error-entry-answers">
                <div className="error-answer-bubble error-answer-bubble--user">
                  <span className="answer-label">Your answer:</span>
                  <span dangerouslySetInnerHTML={{ __html: entry.userAnswer }} />
                </div>
                <div className="error-answer-bubble error-answer-bubble--correct">
                  <span className="answer-label">Correct:</span>
                  <span>{entry.correctAnswer}</span>
                </div>
              </div>

              <Button size="sm" variant="secondary" onClick={() => handleRetryQuestion(entry)}>
                🔄 {s.retryQuestion}
              </Button>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
