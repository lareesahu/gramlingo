import type { Question, Language, QuestionResult } from "../types";
import { MultipleChoiceQuestionComponent } from "./MultipleChoiceQuestion";
import { ClozeMemorization } from "./BlockBuilderQuestion";

interface Props {
  question: Question;
  language: Language;
  onFirstResult: (result: QuestionResult) => void;
  onReadyForNext: () => void;
  onGramlinPose?: (pose: string) => void;
}

export function QuestionRenderer({ question, language, onFirstResult, onReadyForNext, onGramlinPose }: Props) {
  switch (question.type) {
    case "multiple_choice_single":
      return <MultipleChoiceQuestionComponent question={question} language={language} onFirstResult={onFirstResult} onReadyForNext={onReadyForNext} />;
    case "cloze":
      return <ClozeMemorization question={question} language={language} onFirstResult={onFirstResult} onReadyForNext={onReadyForNext} onGramlinPose={onGramlinPose} />;
    default: { const _exhaustive: never = question; throw new Error("Unknown question type: " + (_exhaustive as any).type); }
  }
}
