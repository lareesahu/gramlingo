import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

describe('Lesson flow', () => {
  beforeEach(() => { localStorage.clear(); localStorage.setItem("gramlingo_intro_seen_v1", "1"); });

  it('opens an authored question from the lesson plan', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    const startBtn = (await screen.findAllByText('Start Learning', {}, { timeout: 3000 }))[0];
    await user.click(startBtn);
    await user.click(await screen.findByText('New Player'));
    await user.type(screen.getByPlaceholderText('Username'), 'test');
    await user.click(screen.getByRole('button', { name: 'Log In' }));
    await user.click(await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ }));
    await user.click(await screen.findByRole('button', { name: /Identify Relative Clauses/ }));

    expect(await screen.findByText(/The woman who called me/)).toBeInTheDocument();
  });
});
