import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

async function login(user: ReturnType<typeof userEvent.setup>) {
  const newPlayerBtn = await screen.findByText('New Player', {}, { timeout: 3000 });
  await user.click(newPlayerBtn);
  await user.type(screen.getByPlaceholderText('Username'), 'admin');
  await user.type(screen.getByPlaceholderText('PIN (optional)'), 'gramlin');
  await user.click(screen.getByText('Start Learning'));
}

describe('AdminScreen', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('shows admin panel after admin login', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    await login(user);

    // Click user menu to show dropdown
    const userMenu = document.querySelector('.user-menu');
    expect(userMenu).toBeInTheDocument();
    await user.click(userMenu!);

    // Now "Admin Panel" should be visible in dropdown
    const adminBtn = await screen.findByText('Admin Panel');
    expect(adminBtn).toBeInTheDocument();
    await user.click(adminBtn);

    // Should now see admin screen content
    expect(screen.getByText(/⚙/)).toBeInTheDocument();
  });
});
