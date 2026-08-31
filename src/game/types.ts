export type Language = "en" | "zh" | "es";

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

export type QuestionType = "multiple_choice_single" | "cloze";

export interface ClozeBlank {
  position: number;
  word: string;
  options: string[];
}

interface QuestionBase {
  id: string;
  type: QuestionType;
  q: string;
  qZh: string;
  qEs: string;
  t: string;
  tZh: string;
  tEs: string;
}

export interface MultipleChoiceQuestion extends QuestionBase {
  type: "multiple_choice_single";
  a: string | string[];
  o: string[];
  oZh?: string[];
  oEs?: string[];
  ex?: string[];
  exZh?: string[];
  exEs?: string[];
}

export interface ClozeQuestion extends QuestionBase {
  type: "cloze";
  scenario: string;
  scenarioZh: string;
  scenarioEs: string;
  blanks: ClozeBlank[];
  fullSentence: string;
  fullSentenceZh: string;
  fullSentenceEs: string;
}

export type Question = MultipleChoiceQuestion | ClozeQuestion;

export interface LegacyQuestion {
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
  nameEs?: string;
  sub: string;
  subZh: string;
  sort: number;
  q: (LegacyQuestion | Question)[];
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
  id?: string;
  email?: string;
}

export interface UserProgressState {
  activeModuleId: string | null;
  activePhaseId: string | null;
  activeQuestionIndex: number;
  progress: PhaseProgress[];
  errorLog: ErrorEntry[];
}

export interface CloudAdminUser {
  id: string;
  username: string;
  createdAt: string;
  updatedAt: string;
  state: UserProgressState;
}

export interface PhaseProgress {
  phaseId: string;
  moduleId: string;
  bestScore: number;
  attempts: number;
  completed: boolean;
  lastAttempt: string;
}

export interface ErrorEntry {
  moduleId: string;
  phaseId: string;
  questionId?: string;
  questionIndex: number;
  userAnswer: string;
  correctAnswer: string;
  timestamp: string;
  attemptCount: number;
}

export type Panel = "grammar" | "flashcards" | "context";

export type Screen =
  | "loading"
  | "welcome"
  | "login"
  | "learning-path"
  | "module"
  | "lesson"
  | "completion"
  | "error-log"
  | "admin"
  | "flashcard-lesson";

/* ── Flashcard data types ── */
export interface WordFamilyMember {
  pos: string;
  posZh: string;
  word: string;
  example: string;
  exampleZh: string;
  level: number; // 0 = root, 1 = +1 affix, 2 = +2 affixes
}

export interface WordFamily {
  id: string;
  root: string;
  phonetic: string;
  pos: string; // "v." | "n." | "v. · n." etc
  clue: string;     // EN: definition; ZH: Chinese word
  clueZh: string;
  members: WordFamilyMember[];
}

export interface FlashcardLesson {
  id: string;
  name: string;
  nameZh: string;
  sort: number;
  families: WordFamily[];
}

export interface FlashcardModule {
  id: string;
  name: string;
  nameZh: string;
  desc: string;
  descZh: string;
  gramlin: string;
  icon: string;
  sort: number;
  deckType: "wordfamily" | "irregular" | "wordpair";
  lessons: FlashcardLesson[];
}

export interface FlashcardData {
  modules: FlashcardModule[];
}

export type GramlinPose = "neutral" | "graduate" | "book" | "celebrate" | "sad" | "think" | "sleeper" | "pencil" | "hearts" | "trophy" | "power" | "peeking" | "confused" | "party" | "grad" | "angry" | "crying" | "laptop" | "sleep-ground" | "juggler";

export interface AppState {
  screen: Screen;
  activePanel: Panel;
  language: Language;
  currentUser: UserProfile | null;
  activeModuleId: string | null;
  activePhaseId: string | null;
  activeQuestionIndex: number;
  progress: PhaseProgress[];
  errorLog: ErrorEntry[];
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

export interface QuestionResult {
  questionId: string;
  correct: boolean;
  userAnswer: string;
  correctAnswer: string;
  points: number;
  hintUsed: boolean;
}
