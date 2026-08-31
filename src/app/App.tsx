/* ═══════════════════════════════════════════════
   GRAMLINGO — App Router (home + module pages)
   ═══════════════════════════════════════════════ */

import { useEffect, useState } from 'react';
import { useAppContext } from './app-state';
import { useUrlSync } from './router';
import { AppShell } from '../components/AppShell/AppShell';
import { LoadingScreen } from '../screens/LoadingScreen';
import { IntroScreen, introAlreadySeen } from '../screens/IntroScreen';
import { WelcomeScreen } from '../screens/WelcomeScreen';
import { LearningPathScreen } from '../screens/LearningPathScreen';
import { ModuleScreen } from '../screens/ModuleScreen';
import { LessonScreen } from '../screens/LessonScreen';
import { CompletionScreen } from '../screens/CompletionScreen';
import { ErrorLogScreen } from '../screens/ErrorLogScreen';
import { AdminScreen } from '../screens/AdminScreen';
import { FlashcardLessonScreen } from '../screens/FlashcardLessonScreen';

const LOADED_FLAG = 'gramlingo_loaded_before';
const LOAD_DURATION = 1500;

export function App() {
  const { screen, currentUser, navigateTo, cloudEnabled } = useAppContext();
  const [introSeen, setIntroSeen] = useState<boolean>(introAlreadySeen);
  // Deep-linked /login skips the intro — the landing CTA promises direct login.
  const [skipIntroOnce] = useState<boolean>(() => typeof window !== 'undefined' && window.location.pathname === '/login');

  // Logged-in users landing on /login go straight to the learning path.
  useEffect(() => {
    if (screen === 'login' && currentUser) navigateTo('learning-path');
  }, [screen, currentUser, navigateTo]);

  // URL ↔ screen sync (subdomain-aware; landing at /, app at /app, lessons at /app/lesson)
  useUrlSync(screen, navigateTo);

  // First-launch journey: full-screen poster slideshow, shown ONCE, then the login screen.
  if (!introSeen && !skipIntroOnce) {
    return <IntroScreen onDone={() => { setIntroSeen(true); navigateTo('login'); }} />;
  }

  // Loading screen mount: show 1.5s on first visit, then route to login
  useEffect(() => {
    if (screen === 'loading' && !cloudEnabled) {
      const alreadyLoaded = localStorage.getItem(LOADED_FLAG);
      if (alreadyLoaded) {
        navigateTo('login');
        return;
      }
      const timer = setTimeout(() => {
        localStorage.setItem(LOADED_FLAG, 'true');
        navigateTo('login');
      }, LOAD_DURATION);
      return () => clearTimeout(timer);
    }
  }, [screen, navigateTo, cloudEnabled]);

  // Show loading screen
  if (screen === 'loading') {
    return <LoadingScreen />;
  }

  if (!currentUser && screen !== 'welcome' && screen !== 'login') {
    return <AppShell showNav={false}><WelcomeScreen /></AppShell>;
  }

  switch (screen) {
    case 'welcome':
      return <AppShell showNav={false}><WelcomeScreen /></AppShell>;

    case 'login':
      return <AppShell showNav={false}><WelcomeScreen autoAuth /></AppShell>;

    case 'learning-path':
          return <AppShell><LearningPathScreen /></AppShell>;

    case 'module':
      return <AppShell backTo={() => navigateTo('learning-path')}><ModuleScreen /></AppShell>;

    case 'lesson':
      return <AppShell backTo={() => navigateTo('learning-path')}><LessonScreen /></AppShell>;

    case 'completion':
      return <AppShell backTo={() => navigateTo('learning-path')}><CompletionScreen /></AppShell>;

    case 'error-log':
      return <AppShell backTo={() => navigateTo('learning-path')}><ErrorLogScreen /></AppShell>;

    case 'admin':
      return <AppShell backTo={() => navigateTo('learning-path')}><AdminScreen /></AppShell>;

    case 'flashcard-lesson':
      return <AppShell backTo={() => navigateTo('learning-path')}><FlashcardLessonScreen /></AppShell>;

    default:
      return <AppShell showNav={false}><WelcomeScreen /></AppShell>;
  }
}
