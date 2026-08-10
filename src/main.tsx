import React from 'react';
import ReactDOM from 'react-dom/client';
import { App } from './app/App';
import { AppProvider } from './app/AppProvider';
import './styles/global.css';

// Register service worker for offline support
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register(
    import.meta.env.BASE_URL + 'sw.js',
    { scope: import.meta.env.BASE_URL }
  ).catch(() => {
    // Fail silently — app works online without SW
  });
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <AppProvider>
      <App />
    </AppProvider>
  </React.StrictMode>,
);
