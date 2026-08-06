import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { StarRating } from './StarRating';

describe('StarRating', () => {
  it('renders 0 stars for score < 50', () => {
    render(<StarRating score={30} />);
    const container = screen.getByLabelText('0 out of 3 stars');
    expect(container).toBeInTheDocument();
  });

  it('renders 3 stars for score >= 90', () => {
    render(<StarRating score={95} />);
    const container = screen.getByLabelText('3 out of 3 stars');
    expect(container).toBeInTheDocument();
  });

  it('renders 1 star for score 50-69', () => {
    render(<StarRating score={55} />);
    expect(screen.getByLabelText('1 out of 3 stars')).toBeInTheDocument();
  });

  it('shows score when showScore is true', () => {
    render(<StarRating score={75} showScore />);
    expect(screen.getByText('75%')).toBeInTheDocument();
  });
});
