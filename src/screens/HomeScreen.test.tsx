import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

async function login(user: ReturnType<typeof userEvent.setup>) {
  await user.click(await screen.findByText('New Player', {}, { timeout: 3000 }));
  await user.type(screen.getByPlaceholderText('Username'), 'test');
  await user.click(screen.getByText('Start Learning'));
  await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ });
}

describe('Learning path', () => {
  beforeEach(() => localStorage.clear());

  it('renders every module card after login', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    await login(user);

    expect(document.querySelectorAll('.lp__card')).toHaveLength(12);
  });

  it('reveals a module lesson plan', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    await login(user);

    await user.click(screen.getByRole('button', { name: /Relative Clauses: Lesson plan/ }));

    expect(await screen.findByText('Identify Relative Clauses')).toBeInTheDocument();
    expect(document.querySelector('.lp__panel')).toBeInTheDocument();
  });
});
