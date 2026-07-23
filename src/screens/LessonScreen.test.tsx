import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../app/AppProvider';
import { App } from '../app/App';

describe('Lesson flow', () => {
  beforeEach(() => localStorage.clear());

  it('opens an authored question from the lesson plan', async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);

    await user.click(await screen.findByText('New Player', {}, { timeout: 3000 }));
    await user.type(screen.getByPlaceholderText('Username'), 'test');
    await user.click(screen.getByText('Start Learning'));
    await user.click(await screen.findByRole('button', { name: /Relative Clauses: Lesson plan/ }));
    await user.click(await screen.findByRole('button', { name: /Identify Relative Clauses/ }));

    expect(await screen.findByText(/Which part of this sentence is the relative clause/)).toBeInTheDocument();
  });
});
