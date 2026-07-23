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

    await user.click(await screen.findByText('New Player', {}, { timeout: 3000 }));
    await user.type(screen.getByPlaceholderText('Username'), 'admin');
    await user.type(screen.getByPlaceholderText('PIN (optional)'), 'gramlin');
    await user.click(screen.getByText('Start Learning'));

    await user.click(await screen.findByRole('button', { name: 'Admin Panel' }));
    expect(screen.getByRole('heading', { name: /Admin Panel/ })).toBeInTheDocument();
  });
});
