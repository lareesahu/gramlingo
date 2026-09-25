/* ═══════════════════════════════════════════════
   Verification for the pulse-pay entries:
   profile menu links + locked-surface unlock entry.
   ═══════════════════════════════════════════════ */

import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';
import { PAY_ACCOUNT_URL, PAY_PRICING_URL } from './pay';

async function login(user: ReturnType<typeof userEvent.setup>) {
  const startBtn = (await screen.findAllByText('Start Learning', {}, { timeout: 3000 }))[0];
  await user.click(startBtn);
  await user.click(await screen.findByText('New Player'));
  await user.type(screen.getByPlaceholderText('Username'), 'test');
  await user.click(screen.getByRole('button', { name: 'Log In' }));
  await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ });
}

describe('pulse-pay entries', () => {
  beforeEach(() => {
    localStorage.clear();
    localStorage.setItem('gramlingo_intro_seen_v1', '1');
  });

  it('links the profile menu to the hosted pricing and account pages', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    await login(user);

    await user.click(screen.getByRole('button', { name: 'Profile' }));

    const unlock = await screen.findByRole('link', { name: /Unlock more worlds/ });
    const account = screen.getByRole('link', { name: /My unlocks/ });
    expect(unlock).toHaveAttribute('href', PAY_PRICING_URL);
    expect(unlock).toHaveAttribute('target', '_blank');
    expect(account).toHaveAttribute('href', PAY_ACCOUNT_URL);
    expect(PAY_PRICING_URL).toContain('pulse-pay-97j0.onrender.com/pricing?site=gramlingo');
  }, 30000);

  it('shows the unlock entry on a locked module card', async () => {
    localStorage.setItem('gramlingo_state', JSON.stringify({ moduleLocks: { test: ['clauses'] } }));
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    await login(user);

    const link = await screen.findByRole('link', { name: /Unlock more worlds/ });
    expect(link).toHaveAttribute('href', PAY_PRICING_URL);
    expect(document.querySelector('.lp__card--locked')).toBeInTheDocument();
  }, 30000);

  it('shows the unlock entry inside a module whose lessons are locked', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    await login(user);

    await user.click(screen.getByRole('button', { name: /Relative Clauses: Lesson plan/ }));

    const modal = document.querySelector('.mm-modal');
    expect(modal).toBeInTheDocument();
    const link = modal!.querySelector('.mm-unlock');
    expect(link).toBeInTheDocument();
    expect(link!.getAttribute('href')).toBe(PAY_PRICING_URL);
  }, 30000);
});
