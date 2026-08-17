/* ═══════════════════════════════════════════════
   GRAMLINGO — URL Router
   One codebase served across subdomains:
     gramlingo.online        → /          → landing (WelcomeScreen)
     app.gramlingo.online    → /app       → app dashboard (LearningPathScreen)
     lesson.gramlingo.online → /app/lesson/:id → lesson surface
   Falls back gracefully on any host (github.io, localhost).
   ═══════════════════════════════════════════════ */

import { useEffect, useMemo, useState } from 'react';
import type { Screen } from '../game/types';

/** Path → screen map for the URL router. */
export const PATH_SCREENS: Record<string, Screen> = {
  '/': 'welcome',
  '/app': 'learning-path',
  '/app/module': 'module',
  '/app/lesson': 'lesson',
  '/app/completion': 'completion',
  '/app/error-log': 'error-log',
  '/app/admin': 'admin',
  '/app/flashcard-lesson': 'flashcard-lesson',
};

/** Subdomain prefix → default path when the host carries a known prefix. */
const HOST_DEFAULTS: Array<[string, string]> = [
  ['lesson.', '/app/lesson'],
  ['app.', '/app'],
  ['www.', '/'],
];

export function detectHostDefault(): string {
  const host = typeof window !== 'undefined' ? window.location.hostname : '';
  for (const [prefix, path] of HOST_DEFAULTS) {
    if (host.startsWith(prefix)) return path;
  }
  return '/';
}

function normalizePath(path: string): string {
  if (!path || path === '/') return '/';
  // Allow /app/lessons/xxx style and strip trailing slash
  let p = path.replace(/\/+$/, '');
  if (p === '/app/lesson') return '/app/lesson';
  return p;
}

export function pathToScreen(path: string): Screen {
  const p = normalizePath(path);
  if (p === '/app/lesson' || p.startsWith('/app/lesson/')) return 'lesson';
  return PATH_SCREENS[p] || (p.startsWith('/app') ? 'learning-path' : 'welcome');
}

export function screenToPath(screen: Screen): string {
  switch (screen) {
    case 'welcome': return '/';
    case 'learning-path': return '/app';
    case 'module': return '/app/module';
    case 'lesson': return '/app/lesson';
    case 'completion': return '/app/completion';
    case 'error-log': return '/app/error-log';
    case 'admin': return '/app/admin';
    case 'flashcard-lesson': return '/app/flashcard-lesson';
    default: return '/';
  }
}

/**
 * Keeps the URL in sync with the in-memory screen and vice-versa.
 * Uses history.replaceState for programmatic nav (no history spam on modal-ish moves)
 * and listens to popstate for back/forward.
 */
export function useUrlSync(screen: Screen, navigateTo: (s: Screen) => void) {
  const [initialized, setInitialized] = useState(false);

  // One-time: apply host default + URL-derived screen AFTER first render (never during).
  // Respect the app's own boot flow: while screen is 'loading', let the loading
  // timer (or cloud restore) decide; don't hijack it.
  useEffect(() => {
    if (initialized) return;
    if (screen === 'loading') return; // wait for boot; the screen→URL effect will sync later
    const hostDefault = detectHostDefault();
    const want = pathToScreen(window.location.pathname);
    if (hostDefault !== '/' && window.location.pathname === '/') {
      navigateTo(pathToScreen(hostDefault));
    } else if (want !== screen) {
      navigateTo(want);
    }
    setInitialized(true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialized, screen]);

  // URL → screen on back/forward.
  useEffect(() => {
    const onPop = () => navigateTo(pathToScreen(window.location.pathname));
    window.addEventListener('popstate', onPop);
    return () => window.removeEventListener('popstate', onPop);
  }, [navigateTo]);

  // Screen → URL (push a real history entry so Back/Forward works; dedupe same-path).
  useEffect(() => {
    if (!initialized) return;
    const target = screenToPath(screen);
    if (window.location.pathname !== target) {
      window.history.pushState(null, '', target);
    }
  }, [screen, initialized]);

  return useMemo(() => ({ initialized }), [initialized]);
}

/** Whether we're on the app subdomain (or any host with an /app path). */
export function useIsAppSurface(): boolean {
  return useMemo(() => {
    const host = typeof window !== 'undefined' ? window.location.hostname : '';
    const p = typeof window !== 'undefined' ? window.location.pathname : '';
    return host.startsWith('app.') || host.startsWith('lesson.') || p.startsWith('/app');
  }, []);
}

export type { Screen };
