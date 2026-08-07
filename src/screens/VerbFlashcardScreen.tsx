/* ═══════════════════════════════════════════════
   GRAMLINGO — Verb Flashcard Screen
   ═══════════════════════════════════════════════ */

import { useState, useEffect, useMemo, useCallback } from 'react';
import { useAppContext } from '../app/app-state';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { ProgressBar } from '../components/ProgressBar/ProgressBar';
import type { VerbFlashcard } from '../game/types';
import './VerbFlashcardScreen.css';

interface VerbDeckFile {
  groups: {
    id: string;
    name: string;
    nameZh: string;
    nameEs: string;
    verbs: VerbFlashcard[];
  }[];
}

export function VerbFlashcardScreen() {
  const { language, activePhaseId, activeModuleId, navigateTo, updateProgress } = useAppContext();
  const isZh = language === 'zh';
  const isEs = language === 'es';

  // Load verb deck data
  const [deck, setDeck] = useState<VerbFlashcard[]>([]);
  const [groupName, setGroupName] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const basePath = import.meta.env.BASE_URL || '/';
    fetch(`${basePath}data/verb-deck.json`)
      .then(r => r.json())
      .then((data: VerbDeckFile) => {
        const group = data.groups.find(g => g.id === activePhaseId);
        if (group) {
          const name = isZh ? group.nameZh : (isEs ? group.nameEs : group.name);
          setGroupName(name);
          // Shuffle verbs for varied study order
          const shuffled = [...group.verbs].sort(() => Math.random() - 0.5);
          setDeck(shuffled);
        }
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [activePhaseId, isZh, isEs]);

  // State
  const [currentIdx, setCurrentIdx] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [mastered, setMastered] = useState<Set<number>>(new Set());
  const [reviewSet, setReviewSet] = useState<Set<number>>(new Set());
  const [reviewMode, setReviewMode] = useState(false);
  const [sessionDone, setSessionDone] = useState(false);

  // Derived
  const totalCards = deck.length;
  const masteredCount = mastered.size;

  const currentCard = deck[currentIdx];

  // Get study queue (non-mastered cards, or review set cards)
  const studyQueue = useMemo(() => {
    if (reviewMode) {
      return deck
        .map((_, i) => i)
        .filter(i => reviewSet.has(i));
    }
    return deck
      .map((_, i) => i)
      .filter(i => !mastered.has(i));
  }, [deck, mastered, reviewSet, reviewMode]);

  const currentQueueIdx = studyQueue.indexOf(currentIdx);

  const handleFlip = useCallback(() => {
    setIsFlipped(f => !f);
  }, []);

  const handleGotIt = useCallback(() => {
    if (!currentCard) return;
    const newMastered = new Set(mastered);
    newMastered.add(currentIdx);
    // Remove from review if it was there
    const newReview = new Set(reviewSet);
    newReview.delete(currentIdx);
    setMastered(newMastered);
    setReviewSet(newReview);
    advanceToNext(newMastered, newReview);
  }, [currentIdx, mastered, reviewSet, currentCard]);

  const handleStudyAgain = useCallback(() => {
    if (!currentCard) return;
    const newReview = new Set(reviewSet);
    newReview.add(currentIdx);
    setReviewSet(newReview);
    advanceToNext(mastered, newReview);
  }, [currentIdx, mastered, reviewSet, currentCard]);

  const advanceToNext = useCallback((currentMastered: Set<number>, currentReview: Set<number>) => {
    // Build next queue from non-mastered cards
    const nextQueue = deck
      .map((_, i) => i)
      .filter(i => !currentMastered.has(i));

    if (nextQueue.length === 0) {
      // All mastered — check if review is needed
      if (currentReview.size > 0) {
        setReviewMode(true);
        const reviewCards = deck
          .map((_, i) => i)
          .filter(i => currentReview.has(i));
        setCurrentIdx(reviewCards[0]);
        setSessionDone(false);
      } else {
        setSessionDone(true);
        // Update progress in app state
        if (activePhaseId && activeModuleId) {
          updateProgress(activePhaseId, activeModuleId, 100);
        }
      }
      setIsFlipped(false);
      return;
    }

    // Pick next card from non-mastered
    const currentPos = nextQueue.indexOf(currentIdx);
    const nextPos = (currentPos + 1) % nextQueue.length;
    setCurrentIdx(nextQueue[nextPos]);
    setIsFlipped(false);
  }, [deck, activePhaseId, activeModuleId, updateProgress]);

  const handleRestartSession = useCallback(() => {
    const shuffled = [...deck].sort(() => Math.random() - 0.5);
    setDeck(shuffled);
    setCurrentIdx(0);
    setIsFlipped(false);
    setMastered(new Set());
    setReviewSet(new Set());
    setReviewMode(false);
    setSessionDone(false);
  }, [deck]);

  if (loading) {
    return (
      <div className="verb-flashcard animate-fade-in">
        <div className="vf-loading">Loading flashcards...</div>
      </div>
    );
  }

  if (!deck.length) {
    return (
      <div className="verb-flashcard animate-fade-in">
        <div className="vf-empty">No flashcards found for this group.</div>
      </div>
    );
  }

  // Session complete view
  if (sessionDone) {
    const needsReview = reviewSet.size > 0;
    return (
      <div className="verb-flashcard animate-fade-in">
        <div className="vf-complete">
          <Gramlin pose={needsReview ? 'think' : 'celebrate'} size="lg" animated />
          <h2>{isZh ? '本轮完成！' : (isEs ? '¡Sesión completa!' : 'Session Complete!')}</h2>
          <div className="vf-complete-stats">
            <div className="vf-stat">
              <span className="vf-stat-num">{totalCards}</span>
              <span className="vf-stat-label">{isZh ? '总计' : (isEs ? 'Total' : 'Total')}</span>
            </div>
            <div className="vf-stat vf-stat--mastered">
              <span className="vf-stat-num">{masteredCount}</span>
              <span className="vf-stat-label">{isZh ? '已掌握' : (isEs ? 'Dominado' : 'Mastered')}</span>
            </div>
            {needsReview && (
              <div className="vf-stat vf-stat--review">
                <span className="vf-stat-num">{reviewSet.size}</span>
                <span className="vf-stat-label">{isZh ? '需复习' : (isEs ? 'Repasar' : 'Review')}</span>
              </div>
            )}
          </div>
          <div className="vf-complete-actions">
            {needsReview && (
              <button className="vf-btn vf-btn--review" onClick={() => {
                const reviewCards = deck.map((_, i) => i).filter(i => reviewSet.has(i));
                setCurrentIdx(reviewCards[0]);
                setIsFlipped(false);
                setReviewMode(true);
                setSessionDone(false);
              }}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M1 4v6h6"/><path d="M3.5 15.5A9 9 0 1 0 3 11"/></svg>
                {isZh ? `复习 ${reviewSet.size} 个` : (isEs ? `Repasar ${reviewSet.size}` : `Review ${reviewSet.size}`)}
              </button>
            )}
            <button className="vf-btn vf-btn--restart" onClick={handleRestartSession}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M23 4v6h-6"/><path d="M20.5 8.5A9 9 0 1 0 23 13"/></svg>
              {isZh ? '重新开始' : (isEs ? 'Reiniciar' : 'Restart')}
            </button>
            <button className="vf-btn vf-btn--back" onClick={() => navigateTo('learning-path')}>
              {isZh ? '返回' : (isEs ? 'Volver' : 'Back')}
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (!currentCard) return null;

  return (
    <div className="verb-flashcard animate-fade-in">
      {/* Header */}
      <div className="vf-header">
        <div className="vf-header-top">
          <button className="vf-back-btn" onClick={() => navigateTo('learning-path')} aria-label="Back">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          </button>
          <div className="vf-header-info">
            <span className="vf-group-name">{groupName}</span>
            <span className="vf-progress-text">
              {reviewMode
                ? `${isZh ? '复习' : (isEs ? 'Repaso' : 'Review')} ${currentQueueIdx + 1}/${studyQueue.length}`
                : `${masteredCount}/${totalCards} ${isZh ? '已掌握' : (isEs ? 'dominado' : 'mastered')}`
              }
            </span>
          </div>
        </div>
        <ProgressBar
          value={totalCards > 0 ? Math.round((masteredCount / totalCards) * 100) : 0}
          size="sm"
          color="correct"
        />
      </div>

      {/* Card */}
      <div className="vf-card-wrapper" onClick={handleFlip}>
        <div className={`vf-card ${isFlipped ? 'vf-card--flipped' : ''}`}>
          {/* Front */}
          <div className="vf-card-front">
            <span className="vf-card-pattern-label">{currentCard.group}</span>
            <h1 className="vf-card-verb">{currentCard.base}</h1>
            <p className="vf-card-hint">{isZh ? '点击翻转' : (isEs ? 'Toca para voltear' : 'Tap to flip')}</p>
          </div>
          {/* Back */}
          <div className="vf-card-back">
            <div className="vf-card-forms">
              <div className="vf-form-row">
                <span className="vf-form-label">{isZh ? '过去式' : (isEs ? 'Pasado' : 'Past')}</span>
                <span className="vf-form-value">{currentCard.past}</span>
              </div>
              <div className="vf-form-row">
                <span className="vf-form-label">{isZh ? '过去分词' : (isEs ? 'Participio' : 'Participle')}</span>
                <span className="vf-form-value">{currentCard.participle}</span>
              </div>
            </div>
            <div className="vf-card-example">
              <p className="vf-example-text">{currentCard.example}</p>
              {isZh && currentCard.exampleZh && (
                <p className="vf-example-translation">{currentCard.exampleZh}</p>
              )}
              {isEs && currentCard.exampleEs && (
                <p className="vf-example-translation">{currentCard.exampleEs}</p>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Actions (only show when flipped) */}
      <div className={`vf-actions ${isFlipped ? 'vf-actions--visible' : ''}`}>
        <button className="vf-btn vf-btn--again" onClick={handleStudyAgain}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M1 4v6h6"/><path d="M3.5 15.5A9 9 0 1 0 3 11"/></svg>
          {isZh ? '再学一遍' : (isEs ? 'Estudiar de nuevo' : 'Study again')}
        </button>
        <button className="vf-btn vf-btn--got-it" onClick={handleGotIt}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          {isZh ? '记住了' : (isEs ? 'Lo tengo' : 'Got it')}
        </button>
      </div>

      {/* Review mode indicator */}
      {reviewMode && !sessionDone && (
        <div className="vf-review-banner">
          {isZh ? '正在复习需要加强的词汇' : (isEs ? 'Repasando palabras que necesitan refuerzo' : 'Reviewing words that need more practice')}
        </div>
      )}
    </div>
  );
}
