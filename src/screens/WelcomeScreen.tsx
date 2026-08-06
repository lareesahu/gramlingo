/* ═══════════════════════════════════════════════════════════
   GRAMLINGO — Landing Page
   ═══════════════════════════════════════════════════════════ */

import { useState, useEffect, useCallback, useRef } from "react";
import { useAppContext } from "../app/app-state";
import { Button } from "../components/Button/Button";
import { Gramlin } from "../components/Gramlin/Gramlin";
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
  const { language, login, getUsers } = useAppContext();
  const s = getStrings(language);

  const [users, setUsers] = useState<ReturnType<typeof getUsers>>([]);
  const [showLogin, setShowLogin] = useState(false);
  const [username, setUsername] = useState("");
  const [pin, setPin] = useState("");
  const [isNewUser, setIsNewUser] = useState(false);
  const [error, setError] = useState("");
  const [catchIdx, setCatchIdx] = useState(0);
  const galleryRef = useRef<HTMLDivElement>(null);

  useEffect(() => { setUsers(getUsers()); }, [getUsers]);

  useEffect(() => {
    const timer = setInterval(() => {
      setCatchIdx((prev) => (prev + 1) % CATCHPHRASES.length);
    }, CATCHPHRASE_INTERVAL);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    if (!showLogin) return;
    const handler = (e: KeyboardEvent) => { if (e.key === "Escape") setShowLogin(false); };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [showLogin]);

  const handleSelectUser = useCallback((name: string) => {
    const user = users.find((u: any) => u.username === name);
    if (user?.pin) { setUsername(name); setIsNewUser(false); }
    else { login(name); }
  }, [users, login]);

  const handleLogin = useCallback(() => {
    setError("");
    if (!username.trim()) { setError("Please enter a username."); return; }
    const result = login(username.trim(), pin || undefined);
    if (!result) setError("Incorrect PIN.");
  }, [username, pin, login]);

  const handleNewUser = useCallback(() => {
    setIsNewUser(true); setUsername(""); setPin(""); setError("");
  }, []);

  const scrollGallery = useCallback((dir: "left" | "right") => {
    galleryRef.current?.scrollBy({ left: dir === "left" ? -320 : 320, behavior: "smooth" });
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
        <Button size="lg" onClick={() => setShowLogin(true)} className="hero-cta">
          {s.startLearning}
        </Button>
        {users.length > 0 && (
          <p className="returning-hint">Welcome back! Choose your profile or start fresh.</p>
        )}
      </section>

      {/* ── Module Gallery ── */}
      <section className="module-gallery-section">
        <h2 className="section-heading">12 Grammar Worlds</h2>
        <p className="section-sub">From relative clauses to advanced expressions — every module is a new adventure.</p>
        <div className="gallery-wrap">
          <button className="gallery-arrow gallery-arrow--left" onClick={() => scrollGallery("left")} aria-label="Scroll left">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <div className="module-gallery" ref={galleryRef}>
            {orderedModules.map((mod) => (
              <article key={mod.id} className="module-card">
                <div className="module-card-cover">
                  <img src={`${BASE_URL}assets/covers/cover-${mod.id}.jpg`} alt={mod.name} loading="lazy" />
                </div>
                <div className="module-card-body">
                  <h3>{mod.name}</h3>
                  <p>{mod.desc}</p>
                </div>
              </article>
            ))}
          </div>
          <button className="gallery-arrow gallery-arrow--right" onClick={() => scrollGallery("right")} aria-label="Scroll right">
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
        <Button size="lg" onClick={() => setShowLogin(true)}>
          {s.startLearning}
        </Button>
      </section>

      {/* ── Login Modal ── */}
      {showLogin && (
        <div className="login-overlay" onClick={(e) => { if (e.target === e.currentTarget) setShowLogin(false); }}>
          <div className="login-modal" role="dialog" aria-modal="true">
            <button className="modal-close" onClick={() => setShowLogin(false)} aria-label="Close">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
            {isNewUser ? (
              <>
                <h2>{s.newPlayer}</h2>
                <input className="input" type="text" placeholder={s.username} value={username} onChange={(e) => setUsername(e.target.value)} autoFocus />
                <input className="input" type="password" placeholder={s.pin} value={pin} onChange={(e) => setPin(e.target.value)} />
                {error && <p className="login-error">{error}</p>}
                <Button fullWidth onClick={handleLogin}>{s.login}</Button>
                <Button variant="ghost" fullWidth onClick={() => setIsNewUser(false)}>{s.back}</Button>
              </>
            ) : (
              <>
                <h2>{s.welcome}</h2>
                {users.length > 0 && (
                  <div className="user-list">
                    {users.map((u: any) => (
                      <button key={u.username} className="user-chip" onClick={() => handleSelectUser(u.username)}>
                        <span className="user-avatar">{u.username[0].toUpperCase()}</span>
                        <span className="user-name">{u.username}</span>
                      </button>
                    ))}
                  </div>
                )}
                {username && !isNewUser && users.find((u: any) => u.username === username)?.pin && (
                  <div className="pin-form animate-slide-up">
                    <p className="pin-label">Enter PIN for <strong>{username}</strong></p>
                    <input className="input" type="password" placeholder="PIN" value={pin} onChange={(e) => setPin(e.target.value)} autoFocus onKeyDown={(e) => e.key === "Enter" && handleLogin()} />
                    {error && <p className="login-error">{error}</p>}
                    <Button fullWidth onClick={handleLogin}>{s.login}</Button>
                  </div>
                )}
                <Button variant="secondary" fullWidth onClick={handleNewUser}>{s.newPlayer}</Button>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
