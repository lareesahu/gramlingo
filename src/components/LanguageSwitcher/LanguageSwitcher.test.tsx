import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../../app/AppProvider';
import { App } from '../../app/App';

describe('LanguageSwitcher', () => {
  beforeEach(() => localStorage.clear());

  it('switches between Chinese and English', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    const startBtn = (await screen.findAllByText('Start Learning', {}, { timeout: 3000 }))[0];
    await user.click(startBtn);
    await user.click(await screen.findByText('New Player'));
    await user.type(screen.getByPlaceholderText('Username'), 'test');
    await user.click(screen.getByText('Log In'));

    const languageMenu = await screen.findByRole('button', { name: 'Language' });
    await user.click(languageMenu);
    await user.click(screen.getByText('中文'));
    expect(screen.getByText('挑一个模块开始吧')).toBeInTheDocument();

    await user.click(languageMenu);
    await user.click(screen.getByText('English'));
    expect(screen.getByText('Pick a module to start')).toBeInTheDocument();
  });
});
