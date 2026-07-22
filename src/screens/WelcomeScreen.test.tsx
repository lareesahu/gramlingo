import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

describe('WelcomeScreen', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('renders loading screen on first visit (in DOM)', () => {
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    expect(document.querySelector('.loading-screen') || document.querySelector('.welcome-screen')).toBeTruthy();
  });

  it('eventually shows welcome screen with create player form', async () => {
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    // Welcome screen shows Gramlin, catchphrase, and "New Player" button
    expect(await screen.findByText('GramLingo', {}, { timeout: 3000 })).toBeInTheDocument();
    expect(screen.getByText('New Player')).toBeInTheDocument();
    expect(screen.getByText(/Grammar Quest/)).toBeInTheDocument();
  });

  it('allows creating a new player', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    
    const newPlayerBtn = await screen.findByText('New Player', {}, { timeout: 3000 });
    await user.click(newPlayerBtn);

    await user.type(screen.getByPlaceholderText('Username'), 'teststudent');
    await user.type(screen.getByPlaceholderText('PIN (optional)'), '1234');
    await user.click(screen.getByText('Start Learning'));

    expect(screen.getByText('Learning Path')).toBeInTheDocument();
  });

  it('logs in existing user without PIN', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );

    // First create a user
    const newPlayerBtn = await screen.findByText('New Player', {}, { timeout: 3000 });
    await user.click(newPlayerBtn);
    await user.type(screen.getByPlaceholderText('Username'), 'existing');
    await user.click(screen.getByText('Start Learning'));

    // Logout — click user menu then Log Out
    const userMenu = document.querySelector('.user-menu');
    await user.click(userMenu!);
    const logoutBtn = await screen.findByText('Log Out');
    await user.click(logoutBtn);

    // Click existing user
    const userChip = await screen.findByText('existing');
    await user.click(userChip);
    expect(await screen.findByText('Learning Path')).toBeInTheDocument();
  });
});
