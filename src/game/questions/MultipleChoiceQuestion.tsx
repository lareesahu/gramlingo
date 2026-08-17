import { useState, useCallback, useEffect } from "react";
import type { MultipleChoiceQuestion, QuestionResult, Language } from "../types";
import "./MultipleChoiceQuestion.css";

/**
 * Normalize an answer/option string for comparison:
 * strip HTML tags, collapse whitespace, trim, lowercase.
 */
export function normalizeAnswer(s: string): string {
  return s
    .replace(/<[^>]*>/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

/**
 * Exact (normalized) answer match. Never substring matching —
 * substring matching accepted wrong options (D9 defect: 49 MC questions
 * where e.g. "go" passed for "goes" or "a" passed for "an").
 */
export function answerMatches(opt: string, answers: string[]): boolean {
  const n = normalizeAnswer(opt);
  return answers.some((a: string) => normalizeAnswer(a) === n);
}

interface Props {
  question: MultipleChoiceQuestion;
  language: Language;
  onFirstResult: (result: QuestionResult) => void;
  onReadyForNext: () => void;
}

export function MultipleChoiceQuestionComponent({ question, language, onFirstResult, onReadyForNext }: Props) {
  const isZh = language === "zh";
  const isEs = language === "es";
  const options = (isZh && question.oZh) || (isEs && question.oEs) || question.o;
  const questionText = (isZh && question.qZh) || (isEs && question.qEs) || question.q;

  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [revealedOption, setRevealedOption] = useState<number | null>(null);
  const [resultSent, setResultSent] = useState(false);

  const selectedText = selectedOption !== null ? options[selectedOption] : "";
  // Grade by OPTION INDEX derived from the ENGLISH option array, not by the
  // displayed (possibly translated) string. This keeps grading correct in any
  // language: the index is language-independent even when o.zh/o.es differ.
  const correctAnswers = Array.isArray(question.a) ? question.a : [question.a || ""];
  const correctIndices = (question.o || []).map((opt, i) => answerMatches(opt, correctAnswers) ? i : -1).filter(i => i >= 0);
  const isCorrect = selectedOption !== null && correctIndices.includes(selectedOption);

  const getExplanation = (optIndex: number): string => {
    const tip = isZh ? question.tZh : isEs ? (question as any).tEs : question.t;
    const exArr = isZh ? question.exZh : isEs ? (question as any).exEs : question.ex;
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
    if (selectedOption === null) return;
    setSubmitted(true);
    setRevealedOption(selectedOption);

    if (!resultSent) {
      setResultSent(true);
      onFirstResult({
        questionId: question.id,
        correct: isCorrect,
        userAnswer: selectedText,
        correctAnswer: correctAnswers.join(", "),
        points: isCorrect ? 1 : 0,
        hintUsed: false,
      });
    }
  }, [selectedOption, isCorrect, resultSent, question.id, selectedText, correctAnswers, onFirstResult]);

  const handleNext = useCallback(() => {
    onReadyForNext();
  }, [onReadyForNext]);

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

  // Reset on question change
  useEffect(() => {
    setSelectedOption(null);
    setSubmitted(false);
    setRevealedOption(null);
    setResultSent(false);
  }, [question.id]);

  return (
    <div className={`mc-question-card ${submitted ? (isCorrect ? "card--correct" : "card--wrong") : ""}`}>
      <p className="question-text" dangerouslySetInnerHTML={{ __html: questionText }} />

      <div className="options-grid">
        {options.map((opt: string, i: number) => {
          let cls = "option-btn";
          if (!submitted) {
            if (i === selectedOption) cls += " option-btn--selected";
          } else {
            if (correctIndices.includes(i)) {
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
              aria-pressed={i === selectedOption || i === revealedOption}
            >
              <span className="option-letter">{"ABCD"[i]}</span>
              <span className="option-text" dangerouslySetInnerHTML={{ __html: opt }} />
            </button>
          );
        })}
      </div>

      {submitted && revealedOption !== null && (
        <div className={`feedback ${correctIndices.includes(revealedOption) ? "feedback--correct" : "feedback--wrong"} animate-slide-up`}>
          <div className="feedback-label">
            {revealedOption === selectedOption
              ? (isZh ? "你的答案" : isEs ? "Tu respuesta" : "Your answer")
              : `${isZh ? "选项" : isEs ? "Opción" : "Option"} ${revealedOption + 1}`}
          </div>
          <div className="feedback-body">
            {getExplanation(revealedOption) || (isZh ? "点击选项查看解释" : isEs ? "Toca una opción para ver la explicación" : "Tap an option to see its explanation")}
          </div>
        </div>
      )}

      {submitted && revealedOption === null && (
        <div className={`feedback ${isCorrect ? "feedback--correct" : "feedback--wrong"} animate-slide-up`}>
          <div className="feedback-body">{isZh ? "点击选项查看解释" : isEs ? "Toca una opción para ver la explicación" : "Tap an option to see its explanation"}</div>
        </div>
      )}

      <div className="mc-question-actions animate-slide-up">
        {submitted ? (
          <button className="btn btn--primary btn--lg" onClick={handleNext}>
            Next →
          </button>
        ) : (
          <button className="btn btn--primary btn--lg" onClick={handleSubmit} disabled={selectedOption === null}>
            Submit
          </button>
        )}
      </div>
    </div>
  );
}
