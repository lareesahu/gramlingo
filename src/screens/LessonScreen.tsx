/* ==================================================
   GRAMLINGO — Lesson Screen (orchestration only)
   ================================================== */

import { useState, useCallback } from "react";
import { useAppContext } from "../app/app-state";
import { Gramlin } from "../components/Gramlin/Gramlin";
import { ProgressBar } from "../components/ProgressBar/ProgressBar";
import { getStrings } from "../i18n/i18n";
import { trilingualName } from "./LearningPathScreen";
import { GAME_DATA } from "../game/data";
import { QuestionRenderer } from "../game/questions/QuestionRenderer";
import type { QuestionResult, Question } from "../game/types";
import "./LessonScreen.css";

function isPlayable(q: any): q is Question {
  return q && typeof q.type === "string";
}

export function LessonScreen() {
  const {
    language, activeModuleId, activePhaseId, activeQuestionIndex,
    nextQuestion, prevQuestion, completePhase, navigateTo,
    addError, removeError,
  } = useAppContext();
  const s = getStrings(language);

  const phase = GAME_DATA.phases.find((p) => p.id === activePhaseId);

  const [pointsEarned, setPointsEarned] = useState(0);
  const [gramlinPose, setGramlinPose] = useState("think");

  const questions = (phase?.q || []) as Question[];
  const currentQ = questions[activeQuestionIndex];
  const isLastQuestion = activeQuestionIndex >= questions.length - 1;
  const progressPct = questions.length > 0
    ? Math.round((activeQuestionIndex / questions.length) * 100)
    : 0;

  const phaseName = trilingualName(phase?.name || '', phase?.nameZh, phase?.nameEs);

  const handleFirstResult = useCallback((result: QuestionResult) => {
    setPointsEarned(prev => prev + result.points);
    if (!result.correct && activeModuleId && activePhaseId) {
      addError({
        moduleId: activeModuleId, phaseId: activePhaseId,
        questionId: result.questionId, questionIndex: activeQuestionIndex,
        userAnswer: result.userAnswer, correctAnswer: result.correctAnswer,
      });
    } else if (result.correct && activeModuleId && activePhaseId) {
      removeError(activeModuleId, activePhaseId, activeQuestionIndex);
    }
  }, [activeModuleId, activePhaseId, activeQuestionIndex, addError, removeError]);

  const handleReadyForNext = useCallback(() => {
    if (isLastQuestion) {
      const finalPct = questions.length > 0 ? Math.round((pointsEarned / questions.length) * 100) : 0;
      completePhase(finalPct);
    } else {
      nextQuestion();
      setGramlinPose("think");
    }
  }, [isLastQuestion, questions.length, pointsEarned, completePhase, nextQuestion]);

  if (!phase || !currentQ || !isPlayable(currentQ)) {
    navigateTo("learning-path");
    return null;
  }

  return (
    <div className="lesson-screen animate-fade-in">
      <div className="lesson-progress-header">
        <span className="lesson-phase-label">{s.phase} {phase.sort}: {phaseName}</span>
        <span className="lesson-question-count">{s.question} {activeQuestionIndex + 1} {s.of} {questions.length}</span>
      </div>
      <ProgressBar value={progressPct} size="sm" />
      <div className="lesson-nav-bar">
        <button
          className="btn btn--ghost btn--sm lesson-back-btn"
          onClick={prevQuestion}
          disabled={activeQuestionIndex === 0}
          aria-label="Previous question"
        >
          ← {s.back || "Back"}
        </button>
        <span className="lesson-nav-pos">{activeQuestionIndex + 1} / {questions.length}</span>
        <span className="lesson-nav-spacer" />
      </div>
      <div className="lesson-gramlin">
        <Gramlin pose={gramlinPose as any} size="lg" animated={gramlinPose === "celebrate"} />
      </div>
      <QuestionRenderer question={currentQ} language={language} onFirstResult={handleFirstResult} onReadyForNext={handleReadyForNext} onGramlinPose={setGramlinPose} />
    </div>
  );
}
