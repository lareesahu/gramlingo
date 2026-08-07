/* ═══════════════════════════════════════════════════════════
   GRAMLINGO — Landing Page
   ═══════════════════════════════════════════════════════════ */

import { useState, useEffect, useRef } from "react";
import { useAppContext } from "../app/app-state";
import { Button } from "../components/Button/Button";
import { Gramlin } from "../components/Gramlin/Gramlin";
import { AuthScreen } from "../components/AuthScreen/AuthScreen";
import { useDragScroll } from "../hooks/useDragScroll";
import { GAME_DATA } from "../game/data";
import { getStrings } from "../i18n/i18n";
import "./WelcomeScreen.css";

const BASE_URL = import.meta.env.BASE_URL;

const CATCHPHRASES = [
  "Grammar Quest — Learn by playing",
  "Your friendly grammar gremlin is ready!",
  `${GAME_DATA.phases.filter(p => p.q.length > 0).length} phases. ${GAME_DATA.phases.reduce((t, p) => t + p.q.length, 0)} questions. Endless confidence.`,
];

const CATCHPHRASE_INTERVAL = 3000;

const STEPS = [
  { pose: "think" as const, title: "Pick a Module", desc: "Choose from 12 grammar worlds, each with hand-crafted lessons." },
  { pose: "pencil" as const, title: "Answer & Learn", desc: "Solve questions with instant feedback and clear explanations." },
  { pose: "celebrate" as const, title: "Level Up", desc: "Earn stars, unlock phases, and watch your grammar confidence grow." },
];

export function WelcomeScreen() {
  const { language, cloudRecoveryPending } = useAppContext();
  const s = getStrings(language);

  const [showAuth, setShowAuth] = useState(false);
  const [catchIdx, setCatchIdx] = useState(0);
  const galleryRef = useRef<HTMLDivElement>(null);
  const dragScroll = useDragScroll<HTMLDivElement>();

  useEffect(() => {
    const timer = setInterval(() => {
      setCatchIdx((prev) => (prev + 1) % CATCHPHRASES.length);
    }, CATCHPHRASE_INTERVAL);
    return () => clearInterval(timer);
  }, []);

  const orderedModules = [...GAME_DATA.modules].sort((a, b) => a.sort - b.sort);

  return (
    <div className="welcome-screen">
      {/* ── Hero ── */}
      <section className="landing-hero">
        <div className="hero-gramlin">
          <Gramlin pose="peeking" size="xl" animated />
        </div>
        <h1 className="hero-title">{s.appName}</h1>
        <div className="catchphrase-carousel" aria-live="polite">
          {CATCHPHRASES.map((phrase, i) => (
            <span key={phrase} className={`catchphrase-text ${i === catchIdx ? "visible" : "hidden"}`}>
              {phrase}
            </span>
          ))}
        </div>
        <Button size="lg" onClick={() => setShowAuth(true)} className="hero-cta">
          {s.startLearning}
        </Button>
      </section>

      {/* ── Module Gallery ── */}
      <section className="module-gallery-section">
        <h2 className="section-heading">12 Grammar Worlds</h2>
        <p className="section-sub">From relative clauses to advanced expressions — every module is a new adventure.</p>
        <div className="gallery-wrap">
          <button className="gallery-arrow gallery-arrow--left" onClick={() => galleryRef.current?.scrollBy({ left: -320, behavior: "smooth" })} aria-label="Scroll left">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <div className="module-gallery" ref={galleryRef} {...dragScroll}>
            {orderedModules.map((mod) => (
              <article key={mod.id} className="module-card">
                <div className="module-card-cover">
                  <img src={`${BASE_URL}assets/covers/cover-${mod.id}.jpg`} alt={mod.name} loading="lazy" draggable={false} />
                </div>
                <div className="module-card-body">
                  <h3>{mod.name}</h3>
                  <p>{mod.desc}</p>
                </div>
              </article>
            ))}
          </div>
          <button className="gallery-arrow gallery-arrow--right" onClick={() => galleryRef.current?.scrollBy({ left: 320, behavior: "smooth" })} aria-label="Scroll right">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </div>
      </section>

      {/* ── How It Works ── */}
      <section className="how-it-works">
        <h2 className="section-heading">How It Works</h2>
        <div className="steps-grid">
          {STEPS.map((step, i) => (
            <div key={step.title} className="step-card">
              <Gramlin pose={step.pose} size="md" />
              <div className="step-number">{i + 1}</div>
              <h3>{step.title}</h3>
              <p>{step.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ── Bottom CTA ── */}
      <section className="bottom-cta">
        <h2>Ready to master grammar?</h2>
        <p>{GAME_DATA.phases.filter(p => p.q.length > 0).length} phases. {GAME_DATA.phases.reduce((t, p) => t + p.q.length, 0)} hand-crafted questions.</p>
        <Button size="lg" onClick={() => setShowAuth(true)}>
          {s.startLearning}
        </Button>
      </section>

      {/* ── Auth module (log in / create account / forgot password) ── */}
      {(showAuth || cloudRecoveryPending) && (
        <AuthScreen open={showAuth || cloudRecoveryPending} onClose={() => setShowAuth(false)} />
      )}
    </div>
  );
}
