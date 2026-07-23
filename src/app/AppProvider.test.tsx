import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from './AppProvider';
import { useAppContext } from './app-state';

function TestHarness() {
  const ctx = useAppContext();
  return (
    <div>
      <div data-testid="screen">{ctx.screen}</div>
      <div data-testid="lang">{ctx.language}</div>
      <div data-testid="user">{ctx.currentUser?.username || 'none'}</div>
      <div data-testid="admin">{ctx.isAdmin ? 'yes' : 'no'}</div>
      <button data-testid="btn-login" onClick={() => ctx.login('testuser')}>Login</button>
      <button data-testid="btn-admin-login" onClick={() => ctx.login('admin', 'gramlin')}>AdminLogin</button>
      <button data-testid="btn-logout" onClick={() => ctx.logout()}>Logout</button>
      <button data-testid="btn-start" onClick={() => ctx.startPhase('clauses', 'rec')}>StartPhase</button>
      <button data-testid="btn-start-empty" onClick={() => ctx.startPhase('tenses', 'tense_present_simple')}>StartEmpty</button>
      <button data-testid="btn-nav" onClick={() => ctx.navigateTo('wrong-book')}>NavWB</button>
    </div>
  );
}

function renderApp() {
  return render(
    <AppProvider>
      <TestHarness />
    </AppProvider>
  );
}

describe('AppProvider', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('starts on loading screen', () => {
    renderApp();
    expect(screen.getByTestId('screen').textContent).toBe('loading');
  });

  it('defaults to English', () => {
    renderApp();
    expect(screen.getByTestId('lang').textContent).toBe('en');
  });

  it('logs in a user', async () => {
    const user = userEvent.setup();
    renderApp();
    await user.click(screen.getByTestId('btn-login'));
    expect(screen.getByTestId('user').textContent).toBe('testuser');
    expect(screen.getByTestId('screen').textContent).toBe('learning-path');
  });

  it('logs out a user', async () => {
    const user = userEvent.setup();
    renderApp();
    await user.click(screen.getByTestId('btn-login'));
    expect(screen.getByTestId('user').textContent).toBe('testuser');
    await user.click(screen.getByTestId('btn-logout'));
    expect(screen.getByTestId('user').textContent).toBe('none');
  });

  it('detects admin login', async () => {
    const user = userEvent.setup();
    renderApp();
    await user.click(screen.getByTestId('btn-admin-login'));
    expect(screen.getByTestId('admin').textContent).toBe('yes');
  });

  it('navigates between screens', async () => {
    const user = userEvent.setup();
    renderApp();
    await user.click(screen.getByTestId('btn-login'));
    await user.click(screen.getByTestId('btn-nav'));
    expect(screen.getByTestId('screen').textContent).toBe('wrong-book');
  });

  it('does not open a planned phase with no questions', async () => {
    const user = userEvent.setup();
    renderApp();
    await user.click(screen.getByTestId('btn-login'));
    await user.click(screen.getByTestId('btn-start-empty'));
    expect(screen.getByTestId('screen').textContent).toBe('learning-path');
  });

  it('persists user across re-renders', async () => {
    const user = userEvent.setup();
    const { unmount } = renderApp();
    await user.click(screen.getByTestId('btn-login'));
    unmount();

    const { getByTestId } = renderApp();
    expect(getByTestId('user').textContent).toBe('testuser');
  });
});
