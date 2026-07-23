/* ══════════════════════════════════════════════�?
   GRAMLINGO �?Welcome / Login Screen
   ══════════════════════════════════════════════�?*/

import { useState, useEffect, useCallback } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { getStrings } from '../i18n/i18n';
import './WelcomeScreen.css';

const CATCHPHRASES = [
  'Grammar Quest — Learn by playing',
  'Your friendly grammar gremlin is ready!',
  '12 phases. 87 questions. Endless confidence.',
];

const CATCHPHRASE_INTERVAL = 3000;

export function WelcomeScreen() {
  const { language, login, getUsers } = useAppContext();
  const s = getStrings(language);

  const [users, setUsers] = useState<ReturnType<typeof getUsers>>([]);
  const [username, setUsername] = useState('');
  const [pin, setPin] = useState('');
  const [isNewUser, setIsNewUser] = useState(false);
  const [error, setError] = useState('');
  const [catchIdx, setCatchIdx] = useState(0);

  useEffect(() => {
    setUsers(getUsers());
  }, [getUsers]);

  // Catchphrase carousel
  useEffect(() => {
    const timer = setInterval(() => {
      setCatchIdx((prev) => (prev + 1) % CATCHPHRASES.length);
    }, CATCHPHRASE_INTERVAL);
    return () => clearInterval(timer);
  }, []);

  const handleSelectUser = useCallback((username: string) => {
    const user = users.find((u: any) => u.username === username);
    if (user?.pin) {
      setUsername(username);
      setIsNewUser(false);
    } else {
      const result = login(username);
      if (!result) setError('Login failed.');
    }
  }, [users, login]);

  const handleLogin = useCallback(() => {
    setError('');
    if (!username.trim()) {
      setError('Please enter a username.');
      return;
    }
    const result = login(username.trim(), pin || undefined);
    if (!result) setError('Incorrect PIN.');
  }, [username, pin, login]);

  const handleNewUser = useCallback(() => {
    setIsNewUser(true);
    setUsername('');
    setPin('');
    setError('');
  }, []);

  return (
    <div className="welcome-screen animate-fade-in">
      <div className="welcome-hero">
        <div className="welcome-gramlin-wrap">
          <Gramlin pose="peeking" size="lg" animated />
        </div>
        <h1 className="welcome-title">{s.appName}</h1>
        <div className="catchphrase-carousel" aria-live="polite">
          {CATCHPHRASES.map((phrase, i) => (
            <span
              key={phrase}
              className={`catchphrase-text ${i === catchIdx ? 'visible' : 'hidden'}`}
            >
              {phrase}
            </span>
          ))}
        </div>
      </div>

      <div className="welcome-login">
        {isNewUser ? (
          <div className="login-form animate-slide-up">
            <h2>{s.newPlayer}</h2>
            <input
              className="input"
              type="text"
              placeholder={s.username}
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              autoFocus
            />
            <input
              className="input"
              type="password"
              placeholder={s.pin}
              value={pin}
              onChange={(e) => setPin(e.target.value)}
            />
            {error && <p className="login-error">{error}</p>}
            <Button fullWidth onClick={handleLogin}>{s.startLearning}</Button>
            <Button variant="ghost" fullWidth onClick={() => setIsNewUser(false)}>{s.back}</Button>
          </div>
        ) : (
          <div className="login-form animate-slide-up">
            <h2>{s.welcome}</h2>
            {users.length > 0 && (
              <div className="user-list">
                {users.map((u: any) => (
                  <button
                    key={u.username}
                    className="user-chip"
                    onClick={() => handleSelectUser(u.username)}
                  >
                    <span className="user-avatar">{u.username[0].toUpperCase()}</span>
                    <span className="user-name">{u.username}</span>
                  </button>
                ))}
              </div>
            )}
            {/* PIN entry for pre-selected user */}
            {username && !isNewUser && users.find((u: any) => u.username === username)?.pin && (
              <div className="pin-form animate-slide-up">
                <p className="pin-label">Enter PIN for <strong>{username}</strong></p>
                <input
                  className="input"
                  type="password"
                  placeholder="PIN"
                  value={pin}
                  onChange={(e) => setPin(e.target.value)}
                  autoFocus
                  onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
                />
                {error && <p className="login-error">{error}</p>}
                <Button fullWidth onClick={handleLogin}>{s.login}</Button>
              </div>
            )}
            <Button variant="secondary" fullWidth onClick={handleNewUser}>{s.newPlayer}</Button>
          </div>
        )}
      </div>
    </div>
  );
}
