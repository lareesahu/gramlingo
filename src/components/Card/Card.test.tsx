import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Card } from './Card';

describe('Card', () => {
  it('renders children', () => {
    render(<Card>Content</Card>);
    expect(screen.getByText('Content')).toBeInTheDocument();
  });

  it('applies hoverable class', () => {
    render(<Card hoverable>Hover</Card>);
    expect(screen.getByText('Hover').closest('.card')).toHaveClass('card--hoverable');
  });

  it('applies clickable class when onClick provided', () => {
    render(<Card onClick={() => {}}>Click</Card>);
    expect(screen.getByText('Click').closest('.card')).toHaveClass('card--clickable');
  });

  it('adds role=button when clickable', () => {
    render(<Card onClick={() => {}}>Role</Card>);
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  it('removes padding with padded=false', () => {
    render(<Card padded={false}>No pad</Card>);
    expect(screen.getByText('No pad').closest('.card')).toHaveClass('card--no-pad');
  });
});
