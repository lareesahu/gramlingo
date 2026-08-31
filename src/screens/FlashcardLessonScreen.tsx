/* ═══════════════════════════════════════════════
   GRAMLINGO — Flashcard Lesson Screen (card stack + swipeable rows)
   ═══════════════════════════════════════════════ */

import { useState, useCallback, useRef } from 'react';
import { useAppContext } from '../app/app-state';
import { Gramlin } from '../components/Gramlin/Gramlin';
import './FlashcardLessonScreen.css';

export function FlashcardLessonScreen() {
  const {
    language, flashcardModules, activeModuleId, activePhaseId,
    navigateTo, flashcardMarkReviewed, flashcardMarkNeedsWork,
  } = useAppContext();
  const isZh = language === 'zh';

  const mod = flashcardModules.find(m => m.id === activeModuleId);
  const lesson = mod?.lessons.find(l => l.id === activePhaseId);

  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [masteredIds, setMasteredIds] = useState<Set<string>>(new Set());
  const [reviewIds, setReviewIds] = useState<Set<string>>(new Set());

  // Swipe state: per-card horizontal drag offset (px) + drag lifecycle.
  const [swipeOffsets, setSwipeOffsets] = useState<Record<string, number>>({});
  const swipeDrag = useRef<{ id: string; startX: number; startY: number; dx: number; horiz: boolean; moved: boolean } | null>(null);

  const families = lesson?.families || [];
  const totalCards = families.length;
  const reviewedCount = masteredIds.size + reviewIds.size;

  const handleTap = useCallback((familyId: string) => {
    setExpandedId(prev => prev === familyId ? null : familyId);
  }, []);

  const handleMastered = useCallback((familyId: string) => {
    setMasteredIds(prev => new Set(prev).add(familyId));
    setReviewIds(prev => { const n = new Set(prev); n.delete(familyId); return n; });
    flashcardMarkReviewed(familyId);
  }, [flashcardMarkReviewed]);

  const handleReview = useCallback((familyId: string) => {
    setReviewIds(prev => new Set(prev).add(familyId));
    flashcardMarkNeedsWork(familyId);
  }, [flashcardMarkNeedsWork]);

  // ── Swipe handlers (work on both touch and mouse) ──
  const SWIPE_THRESHOLD = 80; // px to commit a swipe

  const onSwipeStart = useCallback((e: React.PointerEvent, familyId: string) => {
    if (masteredIds.has(familyId) || reviewIds.has(familyId)) return; // already done
    swipeDrag.current = { id: familyId, startX: e.clientX, startY: e.clientY, dx: 0, horiz: false, moved: false };
  }, [masteredIds, reviewIds]);

  const onSwipeMove = useCallback((e: React.PointerEvent) => {
    const d = swipeDrag.current;
    if (!d) return;
    const dx = e.clientX - d.startX;
    const dy = e.clientY - d.startY;
    if (!d.horiz && (Math.abs(dx) > 8 || Math.abs(dy) > 8)) {
      // classify gesture: horizontal swipe vs vertical scroll
      d.horiz = Math.abs(dx) > Math.abs(dy);
    }
    if (d.horiz) {
      d.dx = dx;
      d.moved = true;
      setSwipeOffsets(prev => ({ ...prev, [d.id]: dx }));
    }
  }, []);

  const onSwipeEnd = useCallback((e: React.PointerEvent) => {
    const d = swipeDrag.current;
    if (!d) return;
    swipeDrag.current = null;
    const id = d.id;
    const dx = d.dx;
    const committed = d.horiz && d.moved && Math.abs(dx) >= SWIPE_THRESHOLD;
    setSwipeOffsets(prev => {
      const next = { ...prev };
      delete next[id];
      return next;
    });
    if (committed) {
      if (dx < 0) handleReview(id);
      else handleMastered(id);
      // Suppress the click that follows a swipe so the card doesn't also toggle.
      (e.currentTarget as HTMLElement).addEventListener('click', (ev) => {
        ev.preventDefault();
        ev.stopPropagation();
      }, { capture: true, once: true });
    }
  }, [handleReview, handleMastered]);

  const getMemberLevelClass = (level: number) => {
    if (level === 0) return 'fm-l0';
    if (level === 1) return 'fm-l1';
    if (level === 2) return 'fm-l2';
    return 'fm-l3';
  };

  if (!lesson) {
    navigateTo('learning-path');
    return null;
  }

  return (
    <div className="fcls animate-fade-in">
      {/* Header */}
      <div className="fcls-header">
        <button className="fcls-back" onClick={() => navigateTo('learning-path')} aria-label="Back">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        </button>
        <div className="fcls-header-info">
          <span className="fcls-mod-name">{isZh ? mod?.nameZh : mod?.name}</span>
          <span className="fcls-lesson-name">{isZh ? lesson.nameZh : lesson.name}</span>
        </div>
      </div>

      {/* Progress */}
      <div className="fcls-progress">
        <span>{reviewedCount} / {totalCards} {isZh ? '已复习' : 'reviewed'}</span>
        <span className="fcls-mastered">{masteredIds.size} {isZh ? '掌握' : 'mastered'}</span>
      </div>
      <div className="fcls-progress-bar">
        <div className="fcls-progress-fill" style={{width: totalCards > 0 ? `${Math.round(reviewedCount/totalCards*100)}%` : '0%'}} />
      </div>

      {/* Card Stack */}
      <div className="fcls-stack">
        {families.map((family) => {
          const isExpanded = expandedId === family.id;
          const isMastered = masteredIds.has(family.id);
          const isReview = reviewIds.has(family.id);
          const isDone = isMastered || isReview;
          const offset = swipeOffsets[family.id] || 0;

          return (
            <div
              key={family.id}
              className={`fcls-card ${isExpanded ? 'fcls-card--open' : ''} ${isMastered ? 'fcls-card--mastered' : ''} ${isReview ? 'fcls-card--review' : ''} ${offset !== 0 ? 'fcls-card--swiping' : ''}`}
              style={offset !== 0 ? { transform: `translateX(${offset}px) rotate(${offset * 0.02}deg)` } : undefined}
              onPointerDown={(e) => onSwipeStart(e, family.id)}
              onPointerMove={onSwipeMove}
              onPointerUp={onSwipeEnd}
              onPointerCancel={onSwipeEnd}
            >
              {/* Front: clue only */}
              <div className="fcls-front" onClick={() => handleTap(family.id)}>
                <span className="fcls-pos-tag">{family.pos}</span>
                <div className="fcls-clue">{isZh ? family.clueZh : family.clue}</div>
                <span className="fcls-hint">
                  {isMastered ? (isZh ? '✓ 已掌握' : '✓ Mastered') :
                   isReview ? (isZh ? '↻ 需复习' : '↻ Review') :
                   isExpanded ? (isZh ? '▲ 收起' : '▲ Collapse') :
                   (isZh ? '› 点击显示' : '› tap to reveal')}
                </span>
              </div>

              {/* Back: word family accordion */}
              {isExpanded && (
                <div className="fcls-expanded">
                  <div className="fcls-word">{family.root}</div>
                  <div className="fcls-phonetic">{family.phonetic}</div>
                  <div className="fcls-members">
                    {family.members.map((member, mi) => {
                      const levelClass = getMemberLevelClass(member.level);
                      return (
                        <div key={mi} className={`fcls-member ${levelClass}`}>
                          <span className="fcls-member-pos">{isZh ? member.posZh : member.pos}</span>
                          <span className="fcls-member-word">{member.word}</span>
                          <span className="fcls-member-example">{member.example}</span>
                        </div>
                      );
                    })}
                  </div>

                  {/* Swipe actions */}
                  {!isDone && (
                    <div className="fcls-actions">
                      <button className="fcls-btn fcls-btn--review" onClick={() => handleReview(family.id)}>
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M1 4v6h6"/><path d="M3.5 15.5A9 9 0 1 0 3 11"/></svg>
                        {isZh ? '需练习' : 'Review'}
                      </button>
                      <button className="fcls-btn fcls-btn--mastered" onClick={() => handleMastered(family.id)}>
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                        {isZh ? '记住了' : 'Got it'}
                      </button>
                    </div>
                  )}

                  <div className="fcls-swipe-hint">
                    <span>{isZh ? '◄── 需练习' : '◄── Review'}</span>
                    <span>{isZh ? '记住了 ──►' : 'Got it ──►'}</span>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* All done */}
      {totalCards > 0 && reviewedCount === totalCards && (
        <div className="fcls-done">
          <Gramlin pose="celebrate" size="md" animated />
          <p>{isZh ? '本轮完成！' : 'Session complete!'}</p>
          <button className="fcls-btn fcls-btn--restart" onClick={() => {
            setMasteredIds(new Set());
            setReviewIds(new Set());
            setExpandedId(null);
          }}>
            {isZh ? '重新开始' : 'Restart'}
          </button>
        </div>
      )}
    </div>
  );
}
