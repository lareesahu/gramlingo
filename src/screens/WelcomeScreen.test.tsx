import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

describe('WelcomeScreen', () => {
  beforeEach(() => localStorage.clear());

  it('renders a first-visit screen immediately', () => {
    render(<AppProvider><App /></AppProvider>);
    expect(document.querySelector('.loading-screen') || document.querySelector('.welcome-screen')).toBeTruthy();
  });

  it('shows the welcome screen', async () => {
    render(<AppProvider><App /></AppProvider>);
    expect(await screen.findByText('GramLingo', {}, { timeout: 3000 })).toBeInTheDocument();
    expect(screen.getByText('New Player')).toBeInTheDocument();
    expect(screen.getByText(/Grammar Quest/)).toBeInTheDocument();
  });

  it('creates a new player', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    await user.click(await screen.findByText('New Player', {}, { timeout: 3000 }));
    await user.type(screen.getByPlaceholderText('Username'), 'teststudent');
    await user.type(screen.getByPlaceholderText('PIN (optional)'), '1234');
    await user.click(screen.getByText('Start Learning'));

    expect(await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ })).toBeInTheDocument();
  });

  it('logs in an existing user without a PIN', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    await user.click(await screen.findByText('New Player', {}, { timeout: 3000 }));
    await user.type(screen.getByPlaceholderText('Username'), 'existing');
    await user.click(screen.getByText('Start Learning'));
    await user.click(screen.getByRole('button', { name: 'Profile' }));
    await user.click(await screen.findByText('Log Out'));
    await user.click(await screen.findByText('existing'));

    expect(await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ })).toBeInTheDocument();
  });
});
