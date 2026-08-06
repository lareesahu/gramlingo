import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

describe('AdminScreen', () => {
  beforeEach(() => localStorage.clear());

  it('opens from the visible admin action', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    const startBtn = (await screen.findAllByText('Start Learning', {}, { timeout: 3000 }))[0];
    await user.click(startBtn);
    await user.click(await screen.findByText('New Player'));
    await user.type(screen.getByPlaceholderText('Username'), 'admin');
    await user.type(screen.getByPlaceholderText('PIN (optional)'), 'gramlin');
    await user.click(screen.getByText('Log In'));

    await user.click(await screen.findByRole('button', { name: 'Admin Panel' }));
    expect(screen.getByRole('heading', { name: /Admin Panel/ })).toBeInTheDocument();
  });
});
