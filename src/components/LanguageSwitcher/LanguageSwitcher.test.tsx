import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../../app/AppProvider';
import { App } from '../../app/App';

async function login(user: ReturnType<typeof userEvent.setup>) {
  const newPlayerBtn = await screen.findByText('New Player', {}, { timeout: 3000 });
  await user.click(newPlayerBtn);
  await user.type(screen.getByPlaceholderText('Username'), 'test');
  await user.click(screen.getByText('Start Learning'));
}

describe('LanguageSwitcher', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('changes visible text when switching language', async () => {
    const user = userEvent.setup();
    render(
      <AppProvider>
        <App />
      </AppProvider>
    );
    await login(user);

    // Open user menu to access language toggles
    const userMenu = document.querySelector('.user-menu');
    await user.click(userMenu!);

    // Click Chinese language option in dropdown
    const zhBtn = screen.getByText('中文');
    await user.click(zhBtn);

    // Should show Chinese text
    expect(screen.getByText('学习路径')).toBeInTheDocument();

    // Open user menu again and switch to English
    await user.click(userMenu!);
    const enBtn = screen.getByText('English');
    await user.click(enBtn);

    expect(screen.getByText('Learning Path')).toBeInTheDocument();
  });
});
