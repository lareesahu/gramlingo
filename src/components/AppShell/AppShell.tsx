/* ==================================================
   GRAMLINGO — App Shell
   Roles separated: Admin, Language, Profile
   ================================================== */

import { useState, useEffect, useRef, useCallback } from "react";
import { useAppContext } from "../../app/app-state";
import { getStrings } from "../../i18n/i18n";
import type { Language } from "../../game/types";
import "./AppShell.css";

const LANG_LABELS: Record<string, string> = { en: "EN", zh: "中文", es: "ES" };

interface AppShellProps {
  children: React.ReactNode;
  showNav?: boolean;
  backTo?: () => void;
}

export function AppShell({ children, showNav = true, backTo }: AppShellProps) {
  const { currentUser, language, setLanguage, screen, navigateTo, logout, isAdmin } = useAppContext();
  const s = getStrings(language);
  const [profileOpen, setProfileOpen] = useState(false);
  const [langOpen, setLangOpen] = useState(false);
  const profileRef = useRef<HTMLDivElement>(null);
  const langRef = useRef<HTMLDivElement>(null);

  // Close dropdowns on outside click
  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (profileRef.current && !profileRef.current.contains(e.target as Node)) setProfileOpen(false);
      if (langRef.current && !langRef.current.contains(e.target as Node)) setLangOpen(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, []);

  // Close dropdowns on Escape
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape") { setProfileOpen(false); setLangOpen(false); }
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, []);

  const closeAll = useCallback(() => { setProfileOpen(false); setLangOpen(false); }, []);

  return (
    <div className="app-shell">
      {showNav && (
        <header className="app-header">
          <div className="header-left">
            {backTo && (
              <button className="btn-back" onClick={backTo} aria-label={s.back}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
              </button>
            )}
            {!backTo && screen !== "welcome" && (
              <img src={import.meta.env.BASE_URL + "assets/gramlin/gramlingo-logo.png"} alt="GramLingo" className="header-logo" onClick={() => { closeAll(); navigateTo("learning-path"); }} />
            )}
          </div>

          <nav className="header-right">
            {currentUser && (
              <>
                {/* Admin button — visible as primary action when admin */}
                {isAdmin && (
                  <button className="header-btn header-btn--admin" onClick={() => { closeAll(); navigateTo("admin"); }} aria-label={s.admin}>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
                    <span className="header-btn-label">{s.admin}</span>
                  </button>
                )}

                {/* Language selector — globe icon */}
                <div className="header-dropdown-wrap" ref={langRef}>
                  <button className="header-btn header-btn--lang" onClick={() => { setLangOpen(!langOpen); setProfileOpen(false); }} aria-label="Language">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    <span className="header-btn-label">{LANG_LABELS[language]}</span>
                  </button>
                  {langOpen && (
                    <div className="header-dropdown">
                      {(["en", "zh", "es"] as Language[]).map((l) => (
                        <button key={l} className={"dropdown-option" + (language === l ? " dropdown-option--active" : "")} onClick={() => { setLanguage(l); setLangOpen(false); }}>
                          {l === "en" ? "English" : l === "zh" ? "中文" : "Español"}
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                {/* Profile — switching and logout */}
                <div className="header-dropdown-wrap" ref={profileRef}>
                  <button className="header-btn header-btn--profile" onClick={() => { setProfileOpen(!profileOpen); setLangOpen(false); }} aria-label="Profile">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 4-7 8-7s8 3 8 7"/></svg>
                    <span className="header-btn-label">{currentUser.username}</span>
                  </button>
                  {profileOpen && (
                    <div className="header-dropdown">
                      <button className="dropdown-option" onClick={() => { logout(); setProfileOpen(false); }}>Switch User</button>
                      <button className="dropdown-option" onClick={() => { logout(); setProfileOpen(false); }}>Log Out</button>
                    </div>
                  )}
                </div>
              </>
            )}
          </nav>
        </header>
      )}
      <main className="app-main">{children}</main>
    </div>
  );
}
