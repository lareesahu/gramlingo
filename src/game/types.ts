export type Language = 'en' | 'zh' | 'es';

export interface Module {
  id: string;
  name: string;
  nameZh: string;
  desc: string;
  descZh: string;
  gramlin: string;
  icon: string;
  sort: number;
}

export interface Question {
  q: string;
  a: string | string[];
  o: string[];
  t: string;
  tZh: string;
  tEs: string;
  ex?: string[];
  exZh?: string[];
  exEs?: string[];
}

export interface Phase {
  module: string;
  id: string;
  name: string;
  nameZh: string;
  sub: string;
  subZh: string;
  sort: number;
  q: Question[];
}

export interface GameData {
  title: string;
  modules: Module[];
  phaseLockOrder: Record<string, string[]>;
  phases: Phase[];
}

export interface UserProfile {
  username: string;
  pin: string | null;
  createdAt: string;
}

export interface PhaseProgress {
  phaseId: string;
  moduleId: string;
  bestScore: number;
  attempts: number;
  completed: boolean;
  lastAttempt: string;
}

export interface WrongEntry {
  moduleId: string;
  phaseId: string;
  questionIndex: number;
  userAnswer: string;
  correctAnswer: string;
  timestamp: string;
  attemptCount: number;
}

export type Screen = 'loading' | 'welcome' | 'learning-path' | 'module' | 'lesson' | 'completion' | 'wrong-book' | 'admin';

export type GramlinPose = 'neutral' | 'graduate' | 'book' | 'celebrate' | 'sad' | 'think' | 'sleeper' | 'pencil' | 'hearts' | 'trophy' | 'power' | 'peeking' | 'confused' | 'party' | 'grad' | 'angry' | 'crying' | 'laptop' | 'sleep-ground' | 'juggler';

export interface AppState {
  screen: Screen;
  language: Language;
  currentUser: UserProfile | null;
  activeModuleId: string | null;
  activePhaseId: string | null;
  activeQuestionIndex: number;
  progress: PhaseProgress[];
  wrongBook: WrongEntry[];
  isAdmin: boolean;
  moduleLocks: Record<string, string[]>;
}

export type StarCount = 0 | 1 | 2 | 3;

export function scoreToStars(score: number): StarCount {
  if (score >= 90) return 3;
  if (score >= 70) return 2;
  if (score >= 50) return 1;
  return 0;
}