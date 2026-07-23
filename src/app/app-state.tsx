/* ═══════════════════════════════════════════════
   GRAMLINGO — App State Context
   ═══════════════════════════════════════════════ */

import { createContext, useContext } from 'react';
import type { AppState, Language, Screen, UserProfile, ErrorEntry, PhaseProgress } from '../game/types';

export interface AppContextType extends AppState {
  // Navigation
  navigateTo: (screen: Screen) => void;

  // Language
  setLanguage: (lang: Language) => void;

  // Auth
  login: (username: string, pin?: string) => boolean;
  logout: () => void;
  getUsers: () => UserProfile[];

  // Progress
  updateProgress: (phaseId: string, moduleId: string, score: number) => void;
  getPhaseProgress: (phaseId: string) => PhaseProgress | undefined;
  getModuleProgress: (moduleId: string) => number;
  getModuleAttempted: (moduleId: string) => { attempted: number; total: number };

  // Wrong book
  addError: (entry: Omit<ErrorEntry, 'timestamp' | 'attemptCount'>) => void;
  removeError: (moduleId: string, phaseId: string, questionIndex: number) => void;
  getErrorsByModule: (moduleId: string) => ErrorEntry[];
  getErrorsByPhase: (phaseId: string) => ErrorEntry[];

  // Module
  setActiveModule: (moduleId: string | null) => void;

  // Lesson
  startPhase: (moduleId: string, phaseId: string) => void;
  nextQuestion: () => void;

  // Backup
  exportData: () => string;
  importData: (json: string) => boolean;

  // Admin
  toggleUserLock: (username: string) => void;
  isUserLocked: (username: string) => boolean;
  toggleModuleLock: (username: string, moduleId: string) => void;
  isModuleLocked: (username: string, moduleId: string) => boolean;

  // Completion
  completePhase: (score: number) => void;
}

export const AppContext = createContext<AppContextType | null>(null);

export function useAppContext(): AppContextType {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useAppContext must be used within AppProvider');
  return ctx;
}
