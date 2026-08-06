/* ═══════════════════════════════════════════════
   GRAMLINGO — Admin Screen (Cloud-synced)
   Merges local + Supabase users for cross-device visibility.
   ═══════════════════════════════════════════════ */

import { useState, useEffect } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Badge } from '../components/Badge/Badge';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import { fetchAllProgress, fetchAllUsers, isSupabaseAvailable } from '../storage/supabase';
import './AdminScreen.css';

interface RemoteUser {
  username: string;
  progress: Record<string, number>;
  moduleLocks: Record<string, string[]>;
  updatedAt: string;
}

export function AdminScreen() {
  const { language, getUsers, isUserLocked, toggleUserLock, isModuleLocked, toggleModuleLock, exportData } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';
  const [copied, setCopied] = useState(false);
  const [expandedUser, setExpandedUser] = useState<string | null>(null);
  const [remoteUsers, setRemoteUsers] = useState<RemoteUser[]>([]);
  const [cloudAvailable, setCloudAvailable] = useState(false);
  const [cloudLoaded, setCloudLoaded] = useState(false);

  // Fetch from Supabase on mount
  useEffect(() => {
    const fetchCloud = async () => {
      if (!isSupabaseAvailable()) {
        setCloudAvailable(false);
        setCloudLoaded(true);
        return;
      }
      setCloudAvailable(true);
      try {
        const [progressRows, userRows] = await Promise.all([
          fetchAllProgress(),
          fetchAllUsers(),
        ]);

        // Convert progress rows to RemoteUser map
        const userMap = new Map<string, RemoteUser>();
        for (const row of progressRows) {
          const data = row.data || {};
          const modProgress: Record<string, number> = {};
          if (data.progress) {
            for (const modId of Object.keys(GAME_DATA.phaseLockOrder)) {
              const order = GAME_DATA.phaseLockOrder[modId];
              if (!order) continue;
              const completed = order.filter((pid: string) => {
                const p = data.progress.find((pp: any) => pp.phaseId === pid);
                return p?.completed;
              }).length;
              modProgress[modId] = order.length > 0 ? Math.round((completed / order.length) * 100) : 0;
            }
          }
          userMap.set(row.username, {
            username: row.username,
            progress: modProgress,
            moduleLocks: data.moduleLocks || {},
            updatedAt: row.updated_at || data.updatedAt || '',
          });
        }

        // Add users from gramlingo_users table who may not have progress yet
        for (const u of userRows) {
          if (!userMap.has(u.username)) {
            userMap.set(u.username, {
              username: u.username,
              progress: {},
              moduleLocks: {},
              updatedAt: u.createdAt || '',
            });
          }
        }

        setRemoteUsers(Array.from(userMap.values()));
      } catch {
        // Supabase fetch failed — will fall back to local only
      }
      setCloudLoaded(true);
    };
    fetchCloud();
  }, []);

  // Merge local + remote users (deduplicate, remote takes priority for progress)
  const localUsers = getUsers();
  const localUsernames = new Set(localUsers.map((u: any) => u.username));
  const remoteUsernames = new Set(remoteUsers.map((u) => u.username));

  // Start with local users, enrich with remote data
  const mergedUsers = localUsers.map((local: any) => {
    const remote = remoteUsers.find((r) => r.username === local.username);
    return {
      username: local.username,
      isLocal: true,
      isRemote: !!remote,
      remoteProgress: remote?.progress || {},
      remoteUpdated: remote?.updatedAt,
    };
  });

  // Add remote-only users (from other devices)
  for (const remote of remoteUsers) {
    if (!localUsernames.has(remote.username)) {
      mergedUsers.push({
        username: remote.username,
        isLocal: false,
        isRemote: true,
        remoteProgress: remote.progress,
        remoteUpdated: remote.updatedAt,
      });
    }
  }

  // Compute progress for a user: use remote data if available, else local
  const getUserProgress = (_username: string, remoteProgress: Record<string, number>) => {
    // For now, use remote if available. In future, could merge.
    const modIds = Object.keys(GAME_DATA.phaseLockOrder);
    if (modIds.length === 0) return 0;
    let total = 0;
    let count = 0;
    for (const modId of modIds) {
      if (remoteProgress[modId] !== undefined) {
        total += remoteProgress[modId];
        count++;
      }
    }
    return count > 0 ? Math.round(total / count) : 0;
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

  const formatDate = (iso: string) => {
    if (!iso) return '—';
    try {
      const d = new Date(iso);
      return d.toLocaleDateString(isZh ? 'zh-CN' : 'en-US', {
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return iso.slice(0, 10);
    }
  };

  return (
    <div className="admin-screen animate-fade-in">
      <div className="admin-header">
        <h2>⚙️ {s.admin}</h2>
        <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
          {cloudAvailable && (
            <Badge variant="success" size="sm">
              ☁️ {cloudLoaded ? `${remoteUsernames.size} synced` : 'Connecting...'}
            </Badge>
          )}
          {!cloudAvailable && (
            <Badge variant="warning" size="sm">📱 Local only</Badge>
          )}
          <Button variant="secondary" size="sm" onClick={handleExport}>
            📥 {copied ? 'Exported!' : (isZh ? '导出备份' : 'Export backup')}
          </Button>
        </div>
      </div>

      <p className="admin-disclaimer">
        {cloudAvailable
          ? '☁️ Progress syncs across devices. Admin can see all students from any device.'
          : '⚠️ Progress is saved on this device only — no cloud sync, no account needed.'}
      </p>

      {mergedUsers.length === 0 ? (
        <p>{s.noUsers}</p>
      ) : (
        <div className="admin-table">
          <div className="admin-table-header">
            <span>{isZh ? '学员' : 'Learner'}</span>
            <span>{s.status}</span>
            <span>{isZh ? '进度' : 'Progress'}</span>
            <span>{isZh ? '来源' : 'Source'}</span>
            <span>Action</span>
          </div>
          {mergedUsers.map((user: any) => {
            const locked = user.isLocal ? isUserLocked(user.username) : false;
            const avgPct = getUserProgress(user.username, user.remoteProgress);
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
                    ) : user.isLocal ? (
                      <Badge variant="success">🟢 Active</Badge>
                    ) : (
                      <Badge variant="info">☁️ Remote</Badge>
                    )}
                  </span>
                  <span className="admin-progress-cell" data-label="Progress">
                    <div className="admin-mini-bar">
                      <div className="admin-mini-fill" style={{ width: `${avgPct}%` }} />
                    </div>
                    <span className="admin-pct">{avgPct}%</span>
                  </span>
                  <span>
                    {user.isRemote && user.isLocal ? (
                      <Badge variant="success" size="sm">Local + Cloud</Badge>
                    ) : user.isRemote ? (
                      <Badge variant="info" size="sm">☁️ Cloud</Badge>
                    ) : (
                      <Badge variant="default" size="sm">📱 Local</Badge>
                    )}
                  </span>
                  <span>
                    {user.isLocal && (
                      <Button
                        variant={locked ? 'secondary' : 'danger'}
                        size="sm"
                        onClick={(e: React.MouseEvent) => { e.stopPropagation(); toggleUserLock(user.username); }}
                      >
                        {locked ? (isZh ? '解锁' : 'Unlock') : (isZh ? '锁定' : 'Lock')}
                      </Button>
                    )}
                    {!user.isLocal && (
                      <span style={{ fontSize: 12, color: '#8c7b6e' }}>
                        {user.remoteUpdated ? formatDate(user.remoteUpdated) : '—'}
                      </span>
                    )}
                  </span>
                </div>
                {isExpanded && user.isLocal && (
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
