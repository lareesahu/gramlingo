/* ═══════════════════════════════════════════════
   GRAMLINGO — Admin Screen (Local-device-only)
   Honest labeling per spec: no cross-device claims.
   ═══════════════════════════════════════════════ */

import { useState } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Badge } from '../components/Badge/Badge';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import './AdminScreen.css';

export function AdminScreen() {
  const { language, getUsers, isUserLocked, toggleUserLock, isModuleLocked, toggleModuleLock, getModuleProgress, exportData } = useAppContext();
  const s = getStrings(language);
    const [users] = useState(() => getUsers());
  const [copied, setCopied] = useState(false);
  const isZh = language === 'zh';
  const [expandedUser, setExpandedUser] = useState<string | null>(null);

  const handleExport = () => {
    const json = exportData();
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `gramlingo_users_backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="admin-screen animate-fade-in">
      <div className="admin-header">
        <h2>⚙️ {s.admin}</h2>
        <Button variant="secondary" size="sm" onClick={handleExport}>
          📥 {copied ? 'Exported!' : (isZh ? '导出备份' : 'Export backup')}
        </Button>
      </div>

      <p className="admin-disclaimer">
        ⚠️ Progress is saved on this device only — no cloud sync, no account needed.
      </p>

      {users.length === 0 ? (
        <p>{s.noUsers}</p>
      ) : (
        <div className="admin-table">
          <div className="admin-table-header">
            <span>{isZh ? '学员' : 'Learner'}</span>
            <span>{s.status}</span>
            <span>{isZh ? '上次活动' : 'Last active'}</span>
            <span>Action</span>
          </div>
          {users.map((user: any) => {
            const locked = isUserLocked(user.username);
            const clausesPct = getModuleProgress('clauses');
            const prepPct = getModuleProgress('prepositions');
            const avgPct = Math.round((clausesPct + prepPct) / 2);
            const isExpanded = expandedUser === user.username;

            return (
              <div key={user.username}>
                <div className="admin-table-row" onClick={() => setExpandedUser(isExpanded ? null : user.username)} style={{cursor: 'pointer'}}>
                  <span className="admin-user-name">
                    {user.username}
                    {user.username === 'admin' && <Badge variant="warning" size="sm">admin</Badge>}
                  </span>
                  <span>
                    {locked ? (
                      <Badge variant="danger">🔒 Locked</Badge>
                    ) : (
                      <Badge variant="success">🟢 Active</Badge>
                    )}
                  </span>
                  <span className="admin-progress-cell" data-label="Progress">
                    <div className="admin-mini-bar">
                      <div className="admin-mini-fill" style={{ width: `${avgPct}%` }} />
                    </div>
                    <span className="admin-pct">{avgPct}%</span>
                  </span>
                  <span>
                    <Button
                      variant={locked ? 'secondary' : 'danger'}
                      size="sm"
                      onClick={(e: React.MouseEvent) => { e.stopPropagation(); toggleUserLock(user.username); }}
                    >
                      {locked ? (isZh ? '解锁' : 'Unlock') : (isZh ? '锁定' : 'Lock')}
                    </Button>
                  </span>
                </div>
                {isExpanded && (
                  <div className="admin-module-access">
                    <div className="admin-module-access-header">{s.moduleAccess}</div>
                    <div className="admin-module-chips">
                      {GAME_DATA.modules.map((mod: any) => {
                        const modLocked = isModuleLocked(user.username, mod.id);
                        return (
                          <button
                            key={mod.id}
                            className={`admin-module-chip${modLocked ? ' chip-locked' : ' chip-unlocked'}`}
                            onClick={() => toggleModuleLock(user.username, mod.id)}
                            title={modLocked ? 'Click to unlock' : 'Click to lock'}
                          >
                            {modLocked ? '🔒' : '🔓'} {mod.name}
                          </button>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
