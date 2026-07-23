/* ═══════════════════════════════════════════════
   GRAMLINGO — AppProvider (Core State Management)
   ═══════════════════════════════════════════════ */

import { useState, useCallback, useEffect, type ReactNode } from 'react';
import { AppContext } from './app-state';
import type { AppState, UserProfile, PhaseProgress, ErrorEntry, Screen, Language } from '../game/types';
import { GAME_DATA } from '../game/data';

const STORAGE_KEY = 'gramlingo_state';

function loadState(): Partial<AppState> | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    // Basic validation
    if (typeof parsed !== 'object') return null;
    return parsed;
  } catch {
    return null;
  }
}

function saveState(state: Partial<AppState>) {
  try {
    const existing = loadState() || {};
    const merged = { ...existing, ...state };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(merged));
  } catch {
    // Storage full or unavailable — fail silently
  }
}

export function AppProvider({ children }: { children: ReactNode }) {
  const saved = loadState();
  // Never restore transient screens (lesson, loading state requires live context)
  // First visit: show loading screen. Returning visitor with saved state: restore.
  const restoredScreen = saved?.screen === 'module' ? 'learning-path' : saved?.screen;
  const initialScreen: Screen = saved === null
    ? 'loading'
    : (restoredScreen && restoredScreen !== 'lesson' && restoredScreen !== 'loading') ? restoredScreen : 'welcome';

  const [screen, setScreen] = useState<Screen>(initialScreen);
  const [language, setLanguage] = useState<Language>(saved?.language || 'en');
  const [currentUser, setCurrentUser] = useState<UserProfile | null>(saved?.currentUser || null);
  const [activeModuleId, setActiveModuleId] = useState<string | null>(saved?.activeModuleId || null);
  const [activePhaseId, setActivePhaseId] = useState<string | null>(saved?.activePhaseId || null);
  const [activeQuestionIndex, setActiveQuestionIndex] = useState<number>(saved?.activeQuestionIndex || 0);
  const [progress, setProgress] = useState<PhaseProgress[]>(saved?.progress || []);
  const [errorLog, setWrongBook] = useState<ErrorEntry[]>(saved?.errorLog || []);
  const [isAdmin, setIsAdmin] = useState<boolean>(saved?.isAdmin || false);
  const [moduleLocks, setModuleLocks] = useState<Record<string, string[]>>(saved?.moduleLocks || {});

  // Persist state on changes (but never persist transient screens)
  useEffect(() => {
    const safeScreen = screen === 'lesson' ? 'learning-path' : screen;
    saveState({
      screen: safeScreen, language, currentUser, activeModuleId, activePhaseId,
      activeQuestionIndex, progress, errorLog, isAdmin, moduleLocks,
    });
  }, [screen, language, currentUser, activeModuleId, activePhaseId, activeQuestionIndex, progress, errorLog, isAdmin, moduleLocks]);

  // ── Navigation ──
  const navigateTo = useCallback((s: Screen) => {
    setScreen(s);
  }, []);

  // ── Auth ──
  const getUsers = useCallback((): UserProfile[] => {
    try {
      const raw = localStorage.getItem('gramlingo_users');
      return raw ? JSON.parse(raw) : [];
    } catch { return []; }
  }, []);

  const login = useCallback((username: string, pin?: string): boolean => {
    const users = getUsers();
    let user = users.find((u: UserProfile) => u.username === username);

    if (!user) {
      // New user
      user = { username, pin: pin || null, createdAt: new Date().toISOString() };
      localStorage.setItem('gramlingo_users', JSON.stringify([...users, user]));
    } else if (user.pin && user.pin !== pin) {
      return false; // Wrong PIN
    }

    setCurrentUser(user);
    setIsAdmin(username === 'admin' && pin === 'gramlin');
    setScreen('learning-path');
    return true;
  }, [getUsers]);

  const logout = useCallback(() => {
    setCurrentUser(null);
    setIsAdmin(false);
    setActiveModuleId(null);
    setActivePhaseId(null);
    setActiveQuestionIndex(0);
    setScreen('welcome');
  }, []);

  // ── User Lock ──
  const isUserLocked = useCallback((username: string): boolean => {
    try {
      const locked = localStorage.getItem('gramlingo_locked');
      if (!locked) return false;
      return JSON.parse(locked).includes(username);
    } catch { return false; }
  }, []);

  const toggleUserLock = useCallback((username: string) => {
    try {
      const lockedRaw = localStorage.getItem('gramlingo_locked');
      const locked: string[] = lockedRaw ? JSON.parse(lockedRaw) : [];
      const idx = locked.indexOf(username);
      if (idx >= 0) locked.splice(idx, 1);
      else locked.push(username);
      localStorage.setItem('gramlingo_locked', JSON.stringify(locked));
    } catch { /* ignore */ }
  }, []);

  // ── Module-level Locking ──
  const isModuleLocked = useCallback((username: string, moduleId: string): boolean => {
    return !!moduleLocks[username]?.includes(moduleId);
  }, [moduleLocks]);

  const toggleModuleLock = useCallback((username: string, moduleId: string) => {
    setModuleLocks((prev: Record<string, string[]>) => {
      const userLocks = prev[username] || [];
      const idx = userLocks.indexOf(moduleId);
      const next = { ...prev };
      if (idx >= 0) {
        next[username] = userLocks.filter((m: string) => m !== moduleId);
        if (next[username].length === 0) delete next[username];
      } else {
        next[username] = [...userLocks, moduleId];
      }
      localStorage.setItem('gramlingo_module_locks', JSON.stringify(next));
      return next;
    });
  }, []);

  // ── Progress ──
  const getPhaseProgress = useCallback((phaseId: string): PhaseProgress | undefined => {
    return progress.find((p: PhaseProgress) => p.phaseId === phaseId);
  }, [progress]);

  const getModuleProgress = useCallback((moduleId: string): number => {
    const order = GAME_DATA.phaseLockOrder[moduleId];
    if (!order || order.length === 0) return 0;
    const completed = order.filter((pid: string) => {
      const p = progress.find((pp: PhaseProgress) => pp.phaseId === pid);
      return p?.completed;
    }).length;
    return Math.round((completed / order.length) * 100);
  }, [progress]);
  const getModuleAttempted = useCallback((moduleId: string) => {
    const order = GAME_DATA.phaseLockOrder[moduleId];
    if (!order || order.length === 0) return { attempted: 0, total: 0 };
    const attempted = order.filter((pid) => {
      const p = progress.find((pp) => pp.phaseId === pid);
      return p && p.attempts > 0;
    }).length;
    return { attempted, total: order.length };
  }, [progress]);


  const updateProgress = useCallback((phaseId: string, moduleId: string, score: number) => {
    setProgress((prev: PhaseProgress[]) => {
      const existing = prev.find((p: PhaseProgress) => p.phaseId === phaseId);
      if (existing) {
        return prev.map((p: PhaseProgress) =>
          p.phaseId === phaseId
            ? {
                ...p,
                bestScore: Math.max(p.bestScore, score),
                attempts: p.attempts + 1,
                completed: score >= 70 || p.completed,
                lastAttempt: new Date().toISOString(),
              }
            : p,
        );
      }
      return [
        ...prev,
        {
          phaseId,
          moduleId,
          bestScore: score,
          attempts: 1,
          completed: score >= 70,
          lastAttempt: new Date().toISOString(),
        },
      ];
    });
  }, []);

  // ── Error Log ──
  const addError = useCallback((entry: Omit<ErrorEntry, 'timestamp' | 'attemptCount'>) => {
    setWrongBook((prev: ErrorEntry[]) => {
      const existing = prev.find(
        (w: ErrorEntry) =>
          w.moduleId === entry.moduleId &&
          w.phaseId === entry.phaseId &&
          w.questionIndex === entry.questionIndex,
      );
      if (existing) {
        return prev.map((w: ErrorEntry) =>
          w === existing
            ? { ...w, attemptCount: w.attemptCount + 1, timestamp: new Date().toISOString() }
            : w,
        );
      }
      return [
        { ...entry, timestamp: new Date().toISOString(), attemptCount: 1 },
        ...prev,
      ];
    });
  }, []);

  const removeError = useCallback((moduleId: string, phaseId: string, questionIndex: number) => {
    setWrongBook((prev: ErrorEntry[]) =>
      prev.filter(
        (w: ErrorEntry) =>
          !(w.moduleId === moduleId && w.phaseId === phaseId && w.questionIndex === questionIndex),
      ),
    );
  }, []);

  const getErrorsByModule = useCallback((moduleId: string): ErrorEntry[] => {
    return errorLog.filter((w: ErrorEntry) => w.moduleId === moduleId);
  }, [errorLog]);

  const getErrorsByPhase = useCallback((phaseId: string): ErrorEntry[] => {
    return errorLog.filter((w: ErrorEntry) => w.phaseId === phaseId);
  }, [errorLog]);

  // ── Module Navigation ──
  const setActiveModule = useCallback((moduleId: string | null) => {
    setActiveModuleId(moduleId);
  }, []);
  const startPhase = useCallback((moduleId: string, phaseId: string) => {
    const phase = GAME_DATA.phases.find((candidate) => candidate.id === phaseId && candidate.module === moduleId);
    if (!phase?.q.length) return;
    setActiveModuleId(moduleId);
    setActivePhaseId(phaseId);
    setActiveQuestionIndex(0);
    setScreen('lesson');
  }, []);

  const nextQuestion = useCallback(() => {
    setActiveQuestionIndex((prev: number) => prev + 1);
  }, []);

  // ── Completion ──
  const completePhase = useCallback((score: number) => {
    if (activeModuleId && activePhaseId) {
      updateProgress(activePhaseId, activeModuleId, score);
    }
    setScreen('completion');
  }, [activeModuleId, activePhaseId, updateProgress]);

  // ── Backup/Restore ──
  const exportData = useCallback((): string => {
    const data = {
      version: 2,
      exportedAt: new Date().toISOString(),
      users: getUsers(),
      progress,
      errorLog,
      currentUser: currentUser?.username || null,
      moduleLocks,
    };
    return JSON.stringify(data, null, 2);
  }, [getUsers, progress, errorLog, currentUser, moduleLocks]);

  const importData = useCallback((json: string): boolean => {
    try {
      const data = JSON.parse(json);
      if (!data || typeof data !== 'object') return false;
      if (data.version !== 1 && data.version !== 2) return false;

      if (Array.isArray(data.users)) {
        localStorage.setItem('gramlingo_users', JSON.stringify(data.users));
      }
      if (Array.isArray(data.progress)) setProgress(data.progress);
      if (Array.isArray(data.errorLog)) setWrongBook(data.errorLog);
      if (data.moduleLocks && typeof data.moduleLocks === 'object') {
        setModuleLocks(data.moduleLocks);
        localStorage.setItem('gramlingo_module_locks', JSON.stringify(data.moduleLocks));
      }

      return true;
    } catch {
      return false;
    }
  }, []);

  const ctx = {
    // State
    screen, language, currentUser, activeModuleId, activePhaseId,
    activeQuestionIndex, progress, errorLog, isAdmin, moduleLocks,
    // Actions
    navigateTo, setLanguage, login, logout, getUsers,
    updateProgress, getPhaseProgress, getModuleProgress, getModuleAttempted,
    addError, removeError, getErrorsByModule, getErrorsByPhase,
    startPhase, nextQuestion,
    setActiveModule,
    exportData, importData,
    toggleUserLock, isUserLocked,
    toggleModuleLock, isModuleLocked,
    completePhase,
  };

  return <AppContext.Provider value={ctx}>{children}</AppContext.Provider>;
}
