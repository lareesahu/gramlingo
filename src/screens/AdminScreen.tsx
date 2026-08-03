/* ═══════════════════════════════════════════════
   GRAMLINGO — Admin Screen (Local-device-only)
   Honest labeling per spec: no cross-device claims.
   ═══════════════════════════════════════════════ */

import { useEffect, useState } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Badge } from '../components/Badge/Badge';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import './AdminScreen.css';

export function AdminScreen() {
  const {
    language, getUsers, isUserLocked, toggleUserLock, isModuleLocked, toggleModuleLock,
    getUserModuleProgress, exportData, cloudEnabled, getCloudAdminUsers,
  } = useAppContext();
  const s = getStrings(language);
  const [cloudUsers, setCloudUsers] = useState<Awaited<ReturnType<typeof getCloudAdminUsers>>>([]);
  const [cloudLoading, setCloudLoading] = useState(cloudEnabled);
  const [cloudError, setCloudError] = useState(false);
  const [copied, setCopied] = useState(false);
  const isZh = language === 'zh';
  const [expandedUser, setExpandedUser] = useState<string | null>(null);

  useEffect(() => {
    if (!cloudEnabled) return;
    getCloudAdminUsers()
      .then(setCloudUsers)
      .catch(() => setCloudError(true))
      .finally(() => setCloudLoading(false));
  }, [cloudEnabled, getCloudAdminUsers]);

  const users = cloudEnabled
    ? cloudUsers.map((user) => ({ ...user, isCloud: true as const }))
    : getUsers().map((user) => ({ ...user, isCloud: false as const }));

  const cloudModuleProgress = (user: (typeof users)[number], moduleId: string) => {
    if (!user.isCloud) return getUserModuleProgress(user.username, moduleId);
    const order = GAME_DATA.phaseLockOrder[moduleId];
    if (!order?.length) return 0;
    const completed = order.filter((phaseId) =>
      user.state.progress.some((item) => item.phaseId === phaseId && item.completed),
    ).length;
    return Math.round((completed / order.length) * 100);
  };

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
        {cloudEnabled
          ? '☁️ Showing authenticated learner results from all devices.'
          : '⚠️ Progress is saved on this device only — cloud sync is not configured.'}
      </p>

      {cloudLoading ? (
        <p>Loading cloud results…</p>
      ) : cloudError ? (
        <p>Cloud results could not be loaded. Check the admin role and connection.</p>
      ) : users.length === 0 ? (
        <p>{s.noUsers}</p>
      ) : (
        <div className="admin-table">
          <div className="admin-table-header">
            <span>{isZh ? '学员' : 'Learner'}</span>
            <span>{s.status}</span>
            <span>{isZh ? '进度' : 'Progress'}</span>
            <span>Action</span>
          </div>
          {users.map((user: any) => {
            const locked = !user.isCloud && isUserLocked(user.username);
            const modulePercentages = GAME_DATA.modules.map((mod) => cloudModuleProgress(user, mod.id));
            const avgPct = Math.round(modulePercentages.reduce((sum, value) => sum + value, 0) / Math.max(modulePercentages.length, 1));
            const isExpanded = expandedUser === user.username;

            return (
              <div key={user.username}>
                <div className="admin-table-row" onClick={() => setExpandedUser(isExpanded ? null : user.username)} style={{cursor: 'pointer'}}>
                  <span className="admin-user-name">
                    {user.username}
                    {user.username === 'admin' && <Badge variant="warning" size="sm">admin</Badge>}
                  </span>
                  <span>
                    {user.isCloud ? (
                      <Badge variant="info">☁️ Synced</Badge>
                    ) : locked ? (
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
                    {user.isCloud ? (
                      <span>{new Date(user.updatedAt).toLocaleDateString()}</span>
                    ) : (
                      <Button
                        variant={locked ? 'secondary' : 'danger'}
                        size="sm"
                        onClick={(e: React.MouseEvent) => { e.stopPropagation(); toggleUserLock(user.username); }}
                      >
                        {locked ? (isZh ? '解锁' : 'Unlock') : (isZh ? '锁定' : 'Lock')}
                      </Button>
                    )}
                  </span>
                </div>
                {isExpanded && (
                  <div className="admin-module-access">
                    <div className="admin-module-access-header">{s.moduleAccess}</div>
                    <div className="admin-module-chips">
                      {GAME_DATA.modules.map((mod: any) => {
                        const modLocked = !user.isCloud && isModuleLocked(user.username, mod.id);
                        const progressPct = cloudModuleProgress(user, mod.id);
                        return (
                          <button
                            key={mod.id}
                            className={`admin-module-chip${modLocked ? ' chip-locked' : ' chip-unlocked'}`}
                            onClick={() => { if (!user.isCloud) toggleModuleLock(user.username, mod.id); }}
                            title={user.isCloud ? `${progressPct}% complete` : (modLocked ? 'Click to unlock' : 'Click to lock')}
                            disabled={user.isCloud}
                          >
                            {user.isCloud ? `${progressPct}%` : (modLocked ? '🔒' : '🔓')} {mod.name}
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
