import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

async function login(user: ReturnType<typeof userEvent.setup>) {
  const newPlayerBtn = await screen.findByText('New Player', {}, { timeout: 3000 });
  await user.click(newPlayerBtn);
  await user.type(screen.getByPlaceholderText('Username'), 'test');
  await user.click(screen.getByText('Start Learning'));
}

describe('HomeScreen (Learning Path)', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('renders module cards after login', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    await login(user);

    expect(screen.getByText('Learning Path')).toBeInTheDocument();
    const moduleCards = document.querySelectorAll('.module-overview-card');
    expect(moduleCards.length).toBeGreaterThan(0);
  });

  it('allows navigating to a module', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    await login(user);

    // Click first module card — it should navigate to module screen
    const firstCard = document.querySelector('.module-overview-card');
    expect(firstCard).toBeInTheDocument();
    await user.click(firstCard!);

    // Module screen should show phase items
    await screen.findByText('Identify Relative Clauses', {}, { timeout: 2000 });
    expect(document.querySelector('.ms-phase-list')).toBeInTheDocument();
  });
});
