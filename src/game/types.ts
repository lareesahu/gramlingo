/* ═══════════════════════════════════════════════
   GRAMLINGO — Game Types (multilingual support)
   ═══════════════════════════════════════════════ */

export type Language = 'en' | 'zh' | 'es';

// ── Module ──
export interface Module {
  id: string;
  name: string;     nameZh: string;
  desc: string;     descZh: string;
  gramlin: string;  icon: string;
  sort: number;
}

// ── Question ──
export interface Question {
  q: string;                              // prompt (en, HTML allowed)
  a: string | string[];                   // correct answer(s)
  o: string[];                            // options
  t: string;                              // tip (en)
  tZh: string;                            // tip (zh)
  tEs: string;                            // tip (es)
  ex?: string[];                          // per-option explanation (en)
  exZh?: string[];                        // per-option explanation (zh)
  exEs?: string[];                        // per-option explanation (es)
}

// ── Phase ──
export interface Phase {
  module: string;
  id: string;
  name: string;     nameZh: string;
  sub: string;      subZh: string;
  sort: number;
  q: Question[];
}

// ── Data ──
export interface GameData {
  title: string;
  modules: Module[];
  phaseLockOrder: Record<string, string[]>;
  phases: Phase[];
}

// ── User ──
export interface UserProfile {
  username: string;
  pin: string | null;
  createdAt: string;
}

// ── Progress ──
export interface PhaseProgress {
  phaseId: string;  moduleId: string;
  bestScore: number; attempts: number;
  completed: boolean; lastAttempt: string;
}

// ── Wrong Entry ──
export interface WrongEntry {
  moduleId: string;  phaseId: string;
  questionIndex: number;
  userAnswer: string;  correctAnswer: string;
  timestamp: string;   attemptCount: number;
}

// ── Screen ──
export type Screen = 'loading' | 'welcome' | 'learning-path' | 'module' | 'lesson' | 'completion' | 'wrong-book' | 'admin';

// ── Gramlin ──
export type GramlinPose = 'neutral' | 'graduate' | 'book' | 'celebrate' | 'sad' | 'think' | 'sleeper' | 'pencil' | 'hearts' | 'trophy' | 'power' | 'peeking' | 'confused' | 'party' | 'grad' | 'angry' | 'crying' | 'laptop' | 'sleep-ground';

// ── App State ──
export interface AppState {
  screen: Screen;        language: Language;
  currentUser: UserProfile | null;
  activeModuleId: string | null;  activePhaseId: string | null;
  activeQuestionIndex: number;
  progress: PhaseProgress[];      wrongBook: WrongEntry[];
  isAdmin: boolean;
  moduleLocks: Record<string, string[]>;  // username → locked moduleIds[]
}

// ── Stars ──
export type StarCount = 0 | 1 | 2 | 3;
export function scoreToStars(score: number): StarCount {
  if (score >= 90) return 3; if (score >= 70) return 2; if (score >= 50) return 1; return 0;
}
