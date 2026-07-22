import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Gramlin } from './Gramlin';

describe('Gramlin', () => {
  it('renders an image with correct pose', () => {
    render(<Gramlin pose="peeking" />);
    const imgs = screen.getAllByRole('img');
    expect(imgs.length).toBeGreaterThan(0);
    // First role=img is the container div with aria-label
    expect(imgs[0]).toHaveAttribute('aria-label');
    expect(imgs[0].getAttribute('aria-label')).toContain('peeking');
  });

  it('applies size class', () => {
    const { container, rerender } = render(<Gramlin pose="book" size="sm" />);
    expect(container.querySelector('.gramlin--sm')).toBeInTheDocument();

    rerender(<Gramlin pose="book" size="lg" />);
    expect(container.querySelector('.gramlin--lg')).toBeInTheDocument();
  });
});
