/* ═══════════════════════════════════════════════
   GRAMLINGO — App Router (home + module pages)
   ═══════════════════════════════════════════════ */

import { useEffect } from 'react';
import { useAppContext } from './app-state';
import { AppShell } from '../components/AppShell/AppShell';
import { LoadingScreen } from '../screens/LoadingScreen';
import { WelcomeScreen } from '../screens/WelcomeScreen';
import { HomeScreen } from '../screens/HomeScreen';
import { ModuleScreen } from '../screens/ModuleScreen';
import { LessonScreen } from '../screens/LessonScreen';
import { CompletionScreen } from '../screens/CompletionScreen';
import { WrongBookScreen } from '../screens/WrongBookScreen';
import { AdminScreen } from '../screens/AdminScreen';

const LOADED_FLAG = 'gramlingo_loaded_before';
const LOAD_DURATION = 1500;

export function App() {
  const { screen, currentUser, navigateTo } = useAppContext();

  // Loading screen mount: show 1.5s on first visit, then route to welcome
  useEffect(() => {
    if (screen === 'loading') {
      const alreadyLoaded = localStorage.getItem(LOADED_FLAG);
      if (alreadyLoaded) {
        navigateTo('welcome');
        return;
      }
      const timer = setTimeout(() => {
        localStorage.setItem(LOADED_FLAG, 'true');
        navigateTo('welcome');
      }, LOAD_DURATION);
      return () => clearTimeout(timer);
    }
  }, [screen, navigateTo]);

  // Show loading screen
  if (screen === 'loading') {
    return <LoadingScreen />;
  }

  if (!currentUser && screen !== 'welcome') {
    return <AppShell showNav={false}><WelcomeScreen /></AppShell>;
  }

  switch (screen) {
    case 'welcome':
      return <AppShell showNav={false}><WelcomeScreen /></AppShell>;

    case 'learning-path':
      return <AppShell><HomeScreen /></AppShell>;

    case 'module':
      return <AppShell backTo={() => navigateTo('learning-path')}><ModuleScreen /></AppShell>;

    case 'lesson':
      return <AppShell backTo={() => navigateTo('module')}><LessonScreen /></AppShell>;

    case 'completion':
      return <AppShell backTo={() => navigateTo('module')}><CompletionScreen /></AppShell>;

    case 'wrong-book':
      return <AppShell backTo={() => navigateTo('learning-path')}><WrongBookScreen /></AppShell>;

    case 'admin':
      return <AppShell backTo={() => navigateTo('learning-path')}><AdminScreen /></AppShell>;

    default:
      return <AppShell showNav={false}><WelcomeScreen /></AppShell>;
  }
}
