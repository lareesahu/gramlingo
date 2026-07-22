import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { ProgressBar } from './ProgressBar';

describe('ProgressBar', () => {
  it('renders with value', () => {
    render(<ProgressBar value={50} />);
    expect(screen.getByRole('progressbar')).toBeInTheDocument();
  });

  it('shows percentage when showPercent is true', () => {
    render(<ProgressBar value={75} showPercent />);
    expect(screen.getByText('75%')).toBeInTheDocument();
  });

  it('renders fill with correct width', () => {
    const { container } = render(<ProgressBar value={60} />);
    const fill = container.querySelector('.progress-fill');
    expect(fill).toHaveStyle({ width: '60%' });
  });

  it('clamps value to 0-100', () => {
    const { container, rerender } = render(<ProgressBar value={-10} />);
    expect(container.querySelector('.progress-fill')).toHaveStyle({ width: '0%' });

    rerender(<ProgressBar value={150} />);
    expect(container.querySelector('.progress-fill')).toHaveStyle({ width: '100%' });
  });
});
