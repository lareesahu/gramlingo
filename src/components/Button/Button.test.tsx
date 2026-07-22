import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button', () => {
  it('renders children text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('renders primary variant by default', () => {
    render(<Button>Primary</Button>);
    const btn = screen.getByText('Primary').closest('button');
    expect(btn).toHaveClass('btn--primary');
  });

  it('renders secondary variant', () => {
    render(<Button variant="secondary">Secondary</Button>);
    const btn = screen.getByText('Secondary').closest('button');
    expect(btn).toHaveClass('btn--secondary');
  });

  it('renders danger variant', () => {
    render(<Button variant="danger">Danger</Button>);
    const btn = screen.getByText('Danger').closest('button');
    expect(btn).toHaveClass('btn--danger');
  });

  it('renders ghost variant', () => {
    render(<Button variant="ghost">Ghost</Button>);
    const btn = screen.getByText('Ghost').closest('button');
    expect(btn).toHaveClass('btn--ghost');
  });

  it('applies size classes', () => {
    const { rerender } = render(<Button size="sm">Small</Button>);
    expect(screen.getByText('Small').closest('button')).toHaveClass('btn--sm');

    rerender(<Button size="lg">Large</Button>);
    expect(screen.getByText('Large').closest('button')).toHaveClass('btn--lg');
  });

  it('applies fullWidth class', () => {
    render(<Button fullWidth>Full</Button>);
    expect(screen.getByText('Full').closest('button')).toHaveClass('btn--full');
  });

  it('calls onClick when clicked', async () => {
    const user = userEvent.setup();
    let clicked = 0;
    render(<Button onClick={() => clicked++}>Click</Button>);
    await user.click(screen.getByText('Click'));
    expect(clicked).toBe(1);
  });

  it('does not call onClick when disabled', async () => {
    const user = userEvent.setup();
    let clicked = 0;
    render(<Button onClick={() => clicked++} disabled>Click</Button>);
    await user.click(screen.getByText('Click'));
    expect(clicked).toBe(0);
  });

  it('shows spinner when loading', () => {
    render(<Button loading>Loading</Button>);
    const btn = screen.getByText('Loading').closest('button');
    expect(btn).toBeDisabled();
    expect(btn?.querySelector('.btn-spinner')).toBeInTheDocument();
  });
});
