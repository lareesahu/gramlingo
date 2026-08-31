/* ═══════════════════════════════════════════════════════════
   GRAMLINGO — Auth Screen (Log in / Create account / Forgot password)
   A proper account module: distinct flows, honest errors, calm design.
   ═══════════════════════════════════════════════════════════ */

import { useState, useEffect } from "react";
import { useAppContext } from "../../app/app-state";
import { Button } from "../Button/Button";
import { Gramlin } from "../Gramlin/Gramlin";
import { getStrings } from "../../i18n/i18n";
import "./AuthScreen.css";

type AuthMode = "login" | "signup" | "forgot" | "check-email" | "recovery";

interface AuthScreenProps {
  open: boolean;
  onClose: () => void;
}

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/** Returns an error message if invalid, or null when valid. */
function validateEmail(email: string): string | null {
  return EMAIL_RE.test(email) ? null : "Enter a valid email address.";
}
function validatePassword(password: string): string | null {
  return password.length >= 6 ? null : "Password must be at least 6 characters.";
}

export function AuthScreen({ open, onClose }: AuthScreenProps) {
  const {
    language, cloudEnabled, getUsers, login, createAccount,
    cloudRecoveryPending, requestPasswordReset, resendConfirmation, completePasswordReset,
  } = useAppContext();
  const s = getStrings(language);

  const [mode, setMode] = useState<AuthMode>(cloudRecoveryPending ? "recovery" : "login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [name, setName] = useState("");
  const [localName, setLocalName] = useState("");
  const [localPin, setLocalPin] = useState("");
  const [users, setUsers] = useState<ReturnType<typeof getUsers>>([]);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [submitting, setSubmitting] = useState(false);

  // Recovery links force the recovery mode; otherwise default to login.
  useEffect(() => {
    if (cloudRecoveryPending) setMode("recovery");
  }, [cloudRecoveryPending]);

  // Fresh state each time the screen opens.
  useEffect(() => {
    if (!open) return;
    setUsers(getUsers());
    setError("");
    setNotice("");
    if (!cloudRecoveryPending) setMode("login");
  }, [open, cloudRecoveryPending, getUsers]);

  // Escape closes (unless a recovery flow is active — keep them in it).
  useEffect(() => {
    if (!open) return;
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape" && !cloudRecoveryPending) onClose();
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [open, onClose, cloudRecoveryPending]);

  if (!open) return null;

  const switchMode = (next: AuthMode) => {
    setMode(next);
    setError("");
    setNotice("");
  };

  const pickUser = (u: { username: string; pin: string | null }) => {
    setLocalName(u.username);
    setError("");
    setNotice("");
    if (!u.pin) void submitLocalLogin(u.username, "");
  };

  const submitLocalLogin = async (username: string, pin: string) => {
    setSubmitting(true);
    setError("");
    setNotice("");
    const err = await login(username.trim(), pin || undefined);
    setSubmitting(false);
    if (err) setError(err.message);
  };

  const handleLogin = async () => {
    setError("");
    setNotice("");
    if (!cloudEnabled) {
      const exists = users.some((u: any) => u.username === localName.trim());
      if (!localName.trim()) { setError(s.username + " is required."); return; }
      if (!exists) { setError(`No account named "${localName.trim()}" yet — create one instead.`); return; }
      await submitLocalLogin(localName, localPin);
      return;
    }
    const emailErr = validateEmail(email);
    if (emailErr) { setError(emailErr); return; }
    const passErr = validatePassword(password);
    if (passErr) { setError(passErr); return; }
    setSubmitting(true);
    const err = await login(email.trim(), password);
    setSubmitting(false);
    if (err) setError(err.message);
  };

  const handleSignup = async () => {
    setError("");
    setNotice("");
    if (!cloudEnabled) {
      if (!localName.trim()) { setError(s.username + " is required."); return; }
      if (localPin && localPin.length < 4) { setError("PIN needs at least 4 characters."); return; }
      if (localPin !== confirm) { setError("PINs do not match."); return; }
      await submitLocalLogin(localName, localPin); // local: creates the profile on first use
      return;
    }
    if (name.trim().length > 30) { setError("Name is too long (30 characters max)."); return; }
    const emailErr = validateEmail(email);
    if (emailErr) { setError(emailErr); return; }
    const passErr = validatePassword(password);
    if (passErr) { setError(passErr); return; }
    if (password !== confirm) { setError("Passwords do not match."); return; }
    setSubmitting(true);
    const err = await createAccount(email.trim(), password, name.trim() || undefined);
    setSubmitting(false);
    if (!err) return; // logged in (confirmation off) — context navigates
    if (err.code === "confirmation_required") {
      switchMode("check-email");
      return;
    }
    setError(err.message);
  };

  const handleForgot = async () => {
    setError("");
    setNotice("");
    const emailErr = validateEmail(email);
    if (emailErr) { setError(emailErr); return; }
    setSubmitting(true);
    const err = await requestPasswordReset(email.trim());
    setSubmitting(false);
    if (err) setError(err.message);
    else setNotice("Reset link sent — check your email (and spam).");
  };

  const handleResend = async () => {
    setError("");
    setNotice("");
    setSubmitting(true);
    const err = await resendConfirmation(email.trim());
    setSubmitting(false);
    if (err) setError(err.message);
    else setNotice("Confirmation email sent — check your inbox.");
  };

  const handleRecovery = async () => {
    setError("");
    setNotice("");
    if (password.length < 6) { setError("Password must be at least 6 characters."); return; }
    if (password !== confirm) { setError("Passwords do not match."); return; }
    setSubmitting(true);
    const err = await completePasswordReset(password);
    setSubmitting(false);
    if (err) setError(err.message);
  };

  const showTabs = mode === "login" || mode === "signup";

  return (
    <div className="auth-overlay" role="dialog" aria-modal="true">
      <div className="auth-card">
        <button className="auth-close" onClick={onClose} aria-label="Close" disabled={cloudRecoveryPending}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>

        <div className="auth-head">
          <Gramlin pose={mode === "check-email" || mode === "forgot" ? "think" : "peeking"} size="md" />
          {mode === "login" && (
            <>
              <h2>{cloudEnabled ? "Log in" : s.welcome}</h2>
              <p className="auth-sub">{cloudEnabled ? "Welcome back — pick up where you left off." : "Choose your profile or log in."}</p>
            </>
          )}
          {mode === "signup" && (
            <>
              <h2>{cloudEnabled ? "Create account" : s.newPlayer}</h2>
              <p className="auth-sub">{cloudEnabled ? "Your progress saves to the cloud. Takes 10 seconds." : "Pick a name so we remember you."}</p>
            </>
          )}
          {mode === "forgot" && (
            <>
              <h2>Forgot password?</h2>
              <p className="auth-sub">Enter your email and we'll send a reset link.</p>
            </>
          )}
          {mode === "check-email" && (
            <>
              <h2>Check your email</h2>
              <p className="auth-sub">
                We sent a confirmation link to <strong>{email}</strong>. Click it to activate your account — it will log you in.
              </p>
            </>
          )}
          {mode === "recovery" && (
            <>
              <h2>Set a new password</h2>
              <p className="auth-sub">Choose a new password for your account.</p>
            </>
          )}
        </div>

        {showTabs && (
          <div className="auth-tabs" role="tablist">
            <button type="button" role="tab" aria-selected={mode === "login"} className={`auth-tab${mode === "login" ? " is-active" : ""}`} onClick={() => switchMode("login")}>
              {cloudEnabled ? "Log in" : s.login}
            </button>
            <button type="button" role="tab" aria-selected={mode === "signup"} className={`auth-tab${mode === "signup" ? " is-active" : ""}`} onClick={() => switchMode("signup")}>
              {cloudEnabled ? "Create account" : s.newPlayer}
            </button>
          </div>
        )}

        <form
          className="auth-form"
          onSubmit={(e) => {
            e.preventDefault();
            if (mode === "login") void handleLogin();
            else if (mode === "signup") void handleSignup();
            else if (mode === "forgot") void handleForgot();
            else if (mode === "check-email") void handleResend();
            else if (mode === "recovery") void handleRecovery();
          }}
        >
          {mode === "login" && !cloudEnabled && users.length > 0 && (
            <div className="auth-users">
              {users.map((u: any) => (
                <button type="button" key={u.username} className="auth-user-chip" onClick={() => pickUser(u)}>
                  <span className="auth-user-avatar">{u.username[0].toUpperCase()}</span>
                  <span>{u.username}</span>
                </button>
              ))}
            </div>
          )}

          {(mode === "login" || mode === "signup") && !cloudEnabled && (
            <>
              <label className="auth-label">{s.username}</label>
              <input className="auth-input" value={localName} onChange={(e) => setLocalName(e.target.value)} placeholder={s.username} autoComplete="username" autoFocus />
              {mode === "signup" ? (
                <>
                  <label className="auth-label">PIN (optional)</label>
                  <input className="auth-input" type="password" value={localPin} onChange={(e) => setLocalPin(e.target.value)} placeholder="PIN (optional)" autoComplete="new-password" />
                  <label className="auth-label">Confirm PIN</label>
                  <input className="auth-input" type="password" value={confirm} onChange={(e) => setConfirm(e.target.value)} placeholder="Confirm PIN" autoComplete="new-password" />
                </>
              ) : (
                <>
                  <label className="auth-label">PIN</label>
                  <input className="auth-input" type="password" value={localPin} onChange={(e) => setLocalPin(e.target.value)} placeholder="PIN" autoComplete="current-password" />
                </>
              )}
            </>
          )}

          {(mode === "login" || mode === "signup" || mode === "forgot") && cloudEnabled && (
            <>
              {mode === "signup" && (
                <>
                  <label className="auth-label">Name (optional)</label>
                  <input className="auth-input" value={name} onChange={(e) => setName(e.target.value)} placeholder="What should we call you?" autoComplete="name" maxLength={30} />
                </>
              )}
              <label className="auth-label">Email</label>
              <input className="auth-input" type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com" autoComplete="email" autoFocus />
              <label className="auth-label">Password</label>
              <input
                className="auth-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder={mode === "signup" ? "6+ characters" : "Your password"}
                autoComplete={mode === "signup" ? "new-password" : "current-password"}
              />
              {mode === "signup" && (
                <>
                  <label className="auth-label">Confirm password</label>
                  <input className="auth-input" type="password" value={confirm} onChange={(e) => setConfirm(e.target.value)} placeholder="Repeat your password" autoComplete="new-password" />
                </>
              )}
            </>
          )}

          {mode === "check-email" && (
            <p className="auth-hint">
              Didn't get it? Check spam, or resend below. Your account activates the moment you click the link.
            </p>
          )}

          {mode === "recovery" && (
            <>
              <label className="auth-label">New password</label>
              <input className="auth-input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="6+ characters" autoComplete="new-password" autoFocus />
              <label className="auth-label">Confirm new password</label>
              <input className="auth-input" type="password" value={confirm} onChange={(e) => setConfirm(e.target.value)} placeholder="Repeat your password" autoComplete="new-password" />
            </>
          )}

          {error && <p className="auth-error" role="alert">{error}</p>}
          {notice && <p className="auth-notice" role="status">{notice}</p>}

          <Button fullWidth loading={submitting} type="submit" size="lg">
            {mode === "login" && (cloudEnabled ? "Log in" : s.login)}
            {mode === "signup" && (cloudEnabled ? "Create account" : s.login)}
            {mode === "forgot" && "Send reset link"}
            {mode === "check-email" && "Resend email"}
            {mode === "recovery" && "Update password"}
          </Button>
        </form>

        <div className="auth-links">
          {mode === "login" && cloudEnabled && (
            <button type="button" className="auth-link" onClick={() => switchMode("forgot")}>Forgot password?</button>
          )}
          {(mode === "forgot" || mode === "check-email") && (
            <button type="button" className="auth-link" onClick={() => switchMode("login")}>Back to log in</button>
          )}
        </div>

        <p className="auth-legal">
          By continuing, you agree to our{" "}
          <a href={import.meta.env.BASE_URL + "privacy.html"} target="_blank" rel="noopener noreferrer">Privacy Policy</a>.
        </p>
      </div>
    </div>
  );
}
