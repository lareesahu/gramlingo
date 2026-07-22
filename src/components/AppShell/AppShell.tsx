/* ═══════════════════════════════════════════════
   GRAMLINGO — App Shell with user dropdown
   ═══════════════════════════════════════════════ */

import { useState } from 'react';
import { useAppContext } from '../../app/app-state';
import { getStrings } from '../../i18n/i18n';
import type { Language } from '../../game/types';
import './AppShell.css';

interface AppShellProps {
  children: React.ReactNode;
  showNav?: boolean;
  backTo?: () => void;
}

export function AppShell({ children, showNav = true, backTo }: AppShellProps) {
  const { currentUser, language, setLanguage, screen, navigateTo, logout, isAdmin } = useAppContext();
  const s = getStrings(language);
  const [menuOpen, setMenuOpen] = useState(false);

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
            {!backTo && screen !== 'welcome' && (
              <img
                src={`${import.meta.env.BASE_URL}assets/gramlin/gramlingo-logo.svg`}
                alt="GramLingo"
                className="header-logo"
                onClick={() => navigateTo('learning-path')}
              />
            )}
          </div>
          <div className="header-right">
            {currentUser && (
              <div className="user-menu" onClick={() => setMenuOpen(!menuOpen)}>
                <svg className="user-icon-svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 4-7 8-7s8 3 8 7"/>
                </svg>
                <span className="username">{currentUser.username}</span>
                {menuOpen && (
                  <div className="user-dropdown" onClick={(e) => e.stopPropagation()}>
                    <div className="dropdown-section">
                      <span className="dropdown-label">Language</span>
                      <div className="lang-options">
                        {(['en', 'zh', 'es'] as Language[]).map((l) => (
                          <button
                            key={l}
                            className={`lang-opt ${language === l ? 'lang-opt--active' : ''}`}
                            onClick={() => { setLanguage(l); setMenuOpen(false); }}
                          >
                            {l === 'en' ? 'English' : l === 'zh' ? '中文' : 'Español'}
                          </button>
                        ))}
                      </div>
                    </div>
                    <div className="dropdown-section">
                      <button className="dropdown-btn" onClick={() => { logout(); setMenuOpen(false); }}>
                        Log Out
                      </button>
                    </div>
                    {isAdmin && (
                      <div className="dropdown-section dropdown-admin">
                        <button className="dropdown-btn" onClick={() => { navigateTo('admin'); setMenuOpen(false); }}>
                          Admin Panel
                        </button>
                      </div>
                    )}
                  </div>
                )}
              </div>
            )}
          </div>
        </header>
      )}
      <main className="app-main">{children}</main>
    </div>
  );
}
