/* ═══════════════════════════════════════════════
   GRAMLINGO — IntroScreen (first-launch journey)
   Full-screen swipe slideshow of the 4 journey posters.
   Shown ONCE per device (localStorage flag), then straight into the app.
   ═══════════════════════════════════════════════ */

import { useCallback, useRef, useState } from 'react';
import './IntroScreen.css';

export const INTRO_SEEN_FLAG = 'gramlingo_intro_seen_v1';

const SLIDES = [
  {
    poster: 1,
    en: 'Learn English by playing',
    cn: '边玩边学英语',
    sub: 'Bite-sized grammar & vocabulary quests — built for exam prep and everyday confidence.',
  },
  {
    poster: 2,
    en: 'Answer. Learn. Level up.',
    cn: '作答 · 讲解 · 升级',
    sub: 'Instant feedback and clear explanations on every single question.',
  },
  {
    poster: 3,
    en: 'Worlds to explore',
    cn: '探索你的世界',
    sub: 'Grammar worlds, plus flashcard decks for verbs, word pairs and word families.',
  },
  {
    poster: 4,
    en: 'Your progress, everywhere',
    cn: '进度随身带',
    sub: 'Create an account to sync across devices — or stay local with a PIN.',
  },
];

const BASE_URL = import.meta.env.BASE_URL;

export function introAlreadySeen(): boolean {
  try {
    return localStorage.getItem(INTRO_SEEN_FLAG) === '1';
  } catch {
    return true; // storage unavailable — never trap the user behind the intro
  }
}

export function markIntroSeen(): void {
  try {
    localStorage.setItem(INTRO_SEEN_FLAG, '1');
  } catch {
    /* ignore */
  }
}

export function IntroScreen({ onDone }: { onDone: () => void }) {
  const [index, setIndex] = useState(0);
  const [dragging, setDragging] = useState(false);
  const startX = useRef(0);
  const lastX = useRef(0);
  const moved = useRef(0);
  const offset = useRef(0);

  const count = SLIDES.length;
  const isLast = index === count - 1;

  const goTo = useCallback(
    (n: number) => {
      setIndex(Math.max(0, Math.min(count - 1, n)));
    },
    [count],
  );

  const finish = useCallback(() => {
    markIntroSeen();
    onDone();
  }, [onDone]);

  // ── Pointer/touch drag (direction-locked horizontal, like the app's swipe pattern) ──
  const onPointerDown = (e: React.PointerEvent) => {
    // Never hijack drag from interactive controls (Skip / Next buttons).
    const target = e.target as HTMLElement;
    if (target.closest('button')) return;
    startX.current = e.clientX;
    lastX.current = e.clientX;
    moved.current = 0;
    setDragging(true);
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  };
  const onPointerMove = (e: React.PointerEvent) => {
    if (!dragging) return;
    const dx = e.clientX - lastX.current;
    lastX.current = e.clientX;
    moved.current += dx;
    offset.current = Math.max(-count * 100, Math.min(0, moved.current));
  };
  const onPointerUp = () => {
    if (!dragging) return;
    setDragging(false);
    const total = lastX.current - startX.current;
    if (Math.abs(total) > 48) {
      goTo(index + (total < 0 ? 1 : -1));
    }
    moved.current = 0;
    offset.current = 0;
  };

  const translate = dragging
    ? `translateX(calc(${-index * 100}% + ${moved.current}px))`
    : `translateX(-${index * 100}%)`;

  return (
    <div
      className={`intro-stage${dragging ? ' dragging' : ''}`}
      onPointerDown={onPointerDown}
      onPointerMove={onPointerMove}
      onPointerUp={onPointerUp}
      onPointerCancel={onPointerUp}
    >
      {/* progress bar */}
      <div className="intro-progress" aria-hidden="true">
        <i style={{ width: `${(100 / count) * (index + 1)}%` }} />
      </div>

      {/* skip */}
      <button type="button" className="intro-skip" onClick={finish}>
        Skip
      </button>

      {/* slides */}
      <div className="intro-slides" style={{ transform: translate }}>
        {SLIDES.map((s) => (
          <section className="intro-slide" key={s.poster}>
            <img
              src={`${BASE_URL}assets/intro/poster-${s.poster}.jpg`}
              alt=""
              draggable={false}
            />
            <div className="intro-shade" aria-hidden="true" />
            <div className="intro-copy">
              <div className="intro-en">{s.en}</div>
              <div className="intro-cn">{s.cn}</div>
              <div className="intro-sub">{s.sub}</div>
            </div>
          </section>
        ))}
      </div>

      {/* dots */}
      <div className="intro-dots" aria-hidden="true">
        {SLIDES.map((s, i) => (
          <span key={s.poster} className={`intro-dot${i === index ? ' on' : ''}`} />
        ))}
      </div>

      {/* next / let's go */}
      <button
        type="button"
        className={`intro-next${isLast ? ' glow' : ''}`}
        onClick={() => (isLast ? finish() : goTo(index + 1))}
      >
        {isLast ? "Let's Go!" : 'Next'}
      </button>
    </div>
  );
}
