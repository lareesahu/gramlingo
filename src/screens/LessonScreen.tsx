/* ==================================================
   GRAMLINGO — Lesson Screen
   States: idle → selected → submitted(+revealed) → next
   ================================================== */

import { useState, useCallback, useEffect } from "react";
import { useAppContext } from "../app/app-state";
import { Button } from "../components/Button/Button";
import { Gramlin } from "../components/Gramlin/Gramlin";
import { ProgressBar } from "../components/ProgressBar/ProgressBar";
import { getStrings } from "../i18n/i18n";
import { GAME_DATA } from "../game/data";
import "./LessonScreen.css";

export function LessonScreen() {
  const {
    language, activeModuleId, activePhaseId, activeQuestionIndex,
    nextQuestion, completePhase, navigateTo,
    addWrong, removeWrong, wrongBook,
  } = useAppContext();
  const s = getStrings(language);

  const phase = GAME_DATA.phases.find((p) => p.id === activePhaseId);

  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [revealedOption, setRevealedOption] = useState<number | null>(null);
  const [score, setScore] = useState(0);
  const [wrongStreak, setWrongStreak] = useState(0);

  const questions = phase?.q || [];
  const currentQ = questions[activeQuestionIndex];
  const isLastQuestion = activeQuestionIndex >= questions.length - 1;
  const progressPct = questions.length > 0
    ? Math.round(((activeQuestionIndex) / questions.length) * 100)
    : 0;

  const isZh = language === "zh";
  const phaseName = isZh ? phase?.nameZh : phase?.name;
  const options = currentQ?.o || [];
  const selectedText = selectedOption !== null ? options[selectedOption] : "";
  const correctAnswers = Array.isArray(currentQ?.a) ? currentQ.a : [currentQ?.a || ""];
  const isCorrect = correctAnswers.some(
    (a: string) => selectedText.includes(a) || a.includes(selectedText)
  );

  const gramlinPose = submitted
    ? (isCorrect ? "celebrate" : wrongStreak >= 2 ? "sad" : "think")
    : "think";

  const getExplanation = (optIndex: number): string => {
    if (!currentQ) return "";
    const tip = isZh ? currentQ.tZh : language === "es" ? (currentQ as any).tEs : currentQ.t;
    const exArr = isZh ? currentQ.exZh : language === "es" ? (currentQ as any).exEs : currentQ.ex;
    const perOpt = exArr?.[optIndex];
    return perOpt || tip || "";
  };

  const handleOptionClick = useCallback((index: number) => {
    if (submitted) {
      setRevealedOption(revealedOption === index ? null : index);
    } else {
      setSelectedOption(index);
    }
  }, [submitted, revealedOption]);

  const handleSubmit = useCallback(() => {
    if (selectedOption === null || !currentQ) return;

    setSubmitted(true);
    setRevealedOption(selectedOption);

    if (isCorrect) {
      setScore(prev => prev + 1);
      setWrongStreak(0);
      if (activeModuleId && activePhaseId) {
        removeWrong(activeModuleId, activePhaseId, activeQuestionIndex);
      }
    } else {
      const streak = wrongBook.filter(
        w => w.phaseId === activePhaseId && w.questionIndex === activeQuestionIndex
      ).length;
      setWrongStreak(streak + 1);
      if (activeModuleId && activePhaseId) {
        addWrong({
          moduleId: activeModuleId,
          phaseId: activePhaseId,
          questionIndex: activeQuestionIndex,
          userAnswer: selectedText,
          correctAnswer: correctAnswers.join(", "),
        });
      }
    }
  }, [selectedOption, currentQ, isCorrect, activeModuleId, activePhaseId,
      activeQuestionIndex, addWrong, removeWrong, wrongBook, selectedText, correctAnswers]);

  const handleNext = useCallback(() => {
    if (isLastQuestion) {
      const finalScore = questions.length > 0
        ? Math.round((score / questions.length) * 100)
        : 0;
      completePhase(finalScore);
    } else {
      nextQuestion();
      setSelectedOption(null);
      setSubmitted(false);
      setRevealedOption(null);
      setWrongStreak(0);
    }
  }, [isLastQuestion, questions.length, score, completePhase, nextQuestion]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Enter") {
        if (!submitted && selectedOption !== null) {
          e.preventDefault();
          handleSubmit();
        } else if (submitted) {
          e.preventDefault();
          handleNext();
        }
      } else if (e.key === "ArrowRight" && submitted) {
        e.preventDefault();
        handleNext();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [submitted, selectedOption, handleSubmit, handleNext]);

  if (!phase || !currentQ) {
    navigateTo("learning-path");
    return null;
  }

  return (
    <div className="lesson-screen animate-fade-in">
      <div className="lesson-progress-header">
        <span className="lesson-phase-label">
          {s.phase} {phase.sort}: {phaseName}
        </span>
        <span className="lesson-question-count">
          {s.question} {activeQuestionIndex + 1} {s.of} {questions.length}
        </span>
      </div>
      <ProgressBar value={progressPct} size="sm" />

      <div className="lesson-gramlin">
        <Gramlin pose={gramlinPose} size="lg" animated={submitted && isCorrect} />
      </div>

      <div className={`lesson-question-card ${submitted ? (isCorrect ? "card--correct" : "card--wrong") : ""}`}>
        <p className="question-text" dangerouslySetInnerHTML={{ __html: currentQ.q }} />

        <div className="options-grid">
          {options.map((opt: string, i: number) => {
            let cls = "option-btn";
            if (!submitted) {
              if (i === selectedOption) cls += " option-btn--selected";
            } else {
              if (correctAnswers.some((a: string) => opt.includes(a) || a.includes(opt))) {
                cls += " option-btn--correct";
              } else if (i === selectedOption) {
                cls += " option-btn--wrong";
              } else {
                cls += " option-btn--dimmed";
              }
            }

            return (
              <button
                key={i}
                className={cls}
                onClick={() => handleOptionClick(i)}
                disabled={false}
                aria-pressed={i === selectedOption || i === revealedOption}
              >
                <span className="option-letter">{"ABCD"[i]}</span>
                <span className="option-text" dangerouslySetInnerHTML={{ __html: opt }} />
              </button>
            );
          })}
        </div>

        {submitted && revealedOption !== null && (
          <div className={`feedback ${correctAnswers.some((a: string) => options[revealedOption]?.includes(a) || a.includes(options[revealedOption])) ? "feedback--correct" : "feedback--wrong"} animate-slide-up`}>
            <div className="feedback-label">
              {revealedOption === selectedOption
                ? s.yourAnswer
                : `${isZh ? s.optionLabel : "Option"} ${revealedOption + 1}`}
            </div>
            <div className="feedback-body">
              {getExplanation(revealedOption) || s.tapExplanation}
            </div>
          </div>
        )}

        {submitted && revealedOption === null && (
          <div className={`feedback ${isCorrect ? "feedback--correct" : "feedback--wrong"} animate-slide-up`}>
            <div className="feedback-body">{s.tapExplanation}</div>
          </div>
        )}
      </div>

      <div className="lesson-next animate-slide-up">
        {submitted ? (
          <Button onClick={handleNext} size="lg">
            {isLastQuestion ? s.completion : s.next} →
          </Button>
        ) : (
          <Button onClick={handleSubmit} size="lg" disabled={selectedOption === null}>
            {s.submit}
          </Button>
        )}
      </div>
    </div>
  );
}
