import { Fragment, useEffect, useMemo, useState } from "react";
import type { ClozeQuestion, Language, QuestionResult } from "../types";
import "./BlockBuilderQuestion.css";

interface Props {
  question: ClozeQuestion;
  language: Language;
  onFirstResult: (result: QuestionResult) => void;
  onReadyForNext: () => void;
  onGramlinPose?: (pose: string) => void;
}

type RoundStage = "study" | "recall" | "result";

const COPY = {
  en: {
    study: "STUDY",
    recall: "RECALL",
    instruction: "Read the whole sentence aloud. Then hide it and rebuild it from memory.",
    start: "Hide words & recall",
    choose: "Choose a word",
    check: "Check recall",
    next: "Next sentence",
    correct: "Perfect recall",
    wrong: "Review the complete sentence",
  },
  zh: {
    study: "学习",
    recall: "回忆",
    instruction: "大声读完整句子，然后隐藏关键词并凭记忆补全。",
    start: "隐藏并回忆",
    choose: "选择单词",
    check: "检查答案",
    next: "下一句",
    correct: "回忆正确",
    wrong: "复习完整句子",
  },
  es: {
    study: "ESTUDIA",
    recall: "RECUERDA",
    instruction: "Lee la frase completa en voz alta. Después oculta las palabras clave y recuérdalas.",
    start: "Ocultar y recordar",
    choose: "Elige una palabra",
    check: "Comprobar",
    next: "Siguiente frase",
    correct: "Recuerdo perfecto",
    wrong: "Repasa la frase completa",
  },
} as const;

export function ClozeMemorization({ question, language, onFirstResult, onReadyForNext, onGramlinPose }: Props) {
  const [stage, setStage] = useState<RoundStage>("study");
  const [selectedBlank, setSelectedBlank] = useState<number | null>(null);
  const [answers, setAnswers] = useState<Record<number, string>>({});
  const [resultSent, setResultSent] = useState(false);

  useEffect(() => {
    setStage("study");
    setSelectedBlank(null);
    setAnswers({});
    setResultSent(false);
    onGramlinPose?.("book");
  }, [question.id, onGramlinPose]);

  const copy = COPY[language];
  const prompt = language === "zh" ? question.qZh : language === "es" ? question.qEs : question.q;
  const fullSentence = language === "zh"
    ? question.fullSentenceZh
    : language === "es"
      ? question.fullSentenceEs
      : question.fullSentence;
  const promptParts = useMemo(() => prompt.split("_____"), [prompt]);
  const allFilled = question.blanks.every((_, index) => answers[index] !== undefined);
  const allCorrect = question.blanks.every((blank, index) => answers[index] === blank.word);

  const startRecall = () => {
    setStage("recall");
    setSelectedBlank(0);
    onGramlinPose?.("think");
  };

  const handleWordPick = (word: string) => {
    if (stage !== "recall" || selectedBlank === null) return;

    const nextAnswers = { ...answers, [selectedBlank]: word };
    setAnswers(nextAnswers);
    const nextBlank = question.blanks.findIndex((_, index) => nextAnswers[index] === undefined);
    setSelectedBlank(nextBlank === -1 ? null : nextBlank);
  };

  const handleSubmit = () => {
    if (!allFilled || stage !== "recall") return;

    setStage("result");
    if (!resultSent) {
      setResultSent(true);
      onFirstResult({
        questionId: question.id,
        correct: allCorrect,
        userAnswer: question.blanks.map((_, index) => answers[index] || "?").join("|"),
        correctAnswer: question.blanks.map((blank) => blank.word).join("|"),
        points: allCorrect ? 1 : 0,
        hintUsed: false,
      });
    }
    onGramlinPose?.(allCorrect ? "celebrate" : "sad");
  };

  return (
    <div className={`bb-question-card ${stage === "result" ? (allCorrect ? "card--correct" : "card--wrong") : ""}`}>
      <div className="bb-memory-progress" aria-label="Memorization steps">
        <span className={stage === "study" ? "is-active" : "is-complete"}>1 {copy.study}</span>
        <span aria-hidden="true">→</span>
        <span className={stage === "recall" ? "is-active" : stage === "result" ? "is-complete" : ""}>2 {copy.recall}</span>
        <span aria-hidden="true">→</span>
        <span className={stage === "result" ? "is-active" : ""}>3 CHECK</span>
      </div>

      {stage === "study" ? (
        <section className="bb-study-panel">
          <div className="bb-scenario-label">{copy.study}</div>
          <p className="bb-study-instruction">{copy.instruction}</p>
          <p className="bb-study-sentence">{fullSentence}</p>
          <div className="bb-actions">
            <button className="btn btn--primary btn--lg" onClick={startRecall}>{copy.start}</button>
          </div>
        </section>
      ) : (
        <>
          <div className="bb-scenario-label">{stage === "recall" ? copy.recall : (allCorrect ? copy.correct : copy.wrong)}</div>
          <p className="bb-scenario">{language === "zh" ? question.scenarioZh : language === "es" ? question.scenarioEs : question.scenario}</p>

          <div className="bb-memorize-sentence">
            {promptParts.map((part, index) => (
              <Fragment key={`${question.id}-${index}`}>
                <span className="bb-mem-text">{part}</span>
                {index < question.blanks.length && (
                  <button
                    type="button"
                    aria-label={`${copy.choose} ${index + 1}`}
                    aria-pressed={selectedBlank === index}
                    className={`bb-mem-blank ${selectedBlank === index ? "bb-mem-blank--active" : ""} ${stage === "result" ? (answers[index] === question.blanks[index].word ? "bb-mem-blank--correct" : "bb-mem-blank--wrong") : ""}`}
                    onClick={() => stage === "recall" && setSelectedBlank(index)}
                    disabled={stage === "result"}
                  >
                    {answers[index] || <span aria-hidden="true">•••</span>}
                  </button>
                )}
              </Fragment>
            ))}
          </div>

          {selectedBlank !== null && stage === "recall" && (
            <div className="bb-choice-panel">
              <div className="bb-bank-label">{copy.choose} {selectedBlank + 1} / {question.blanks.length}</div>
              <div className="bb-bank">
                {question.blanks[selectedBlank].options.map((word) => (
                  <button
                    key={word}
                    type="button"
                    className={`bb-bank-block ${answers[selectedBlank] === word ? "bb-bank-block--chosen" : ""}`}
                    onClick={() => handleWordPick(word)}
                  >
                    {word}
                  </button>
                ))}
              </div>
            </div>
          )}

          {stage === "result" && (
            <div className={`feedback ${allCorrect ? "feedback--correct" : "feedback--wrong"} animate-slide-up`} aria-live="polite">
              <div className="feedback-label">{allCorrect ? copy.correct : copy.wrong}</div>
              <div className="feedback-body">{fullSentence}</div>
            </div>
          )}

          <div className="bb-actions animate-slide-up">
            {stage === "result" ? (
              <button className="btn btn--primary btn--lg" onClick={onReadyForNext}>{copy.next} →</button>
            ) : (
              <button className="btn btn--primary btn--lg" onClick={handleSubmit} disabled={!allFilled}>{copy.check}</button>
            )}
          </div>
        </>
      )}
    </div>
  );
}
