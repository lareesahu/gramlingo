import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Badge } from './Badge';

describe('Badge', () => {
  it('renders children text', () => {
    render(<Badge>Test</Badge>);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });

  it('renders success variant', () => {
    render(<Badge variant="success">Success</Badge>);
    expect(screen.getByText('Success')).toHaveClass('badge--success');
  });

  it('renders warning variant', () => {
    render(<Badge variant="warning">Warning</Badge>);
    expect(screen.getByText('Warning')).toHaveClass('badge--warning');
  });

  it('renders danger variant', () => {
    render(<Badge variant="danger">Danger</Badge>);
    expect(screen.getByText('Danger')).toHaveClass('badge--danger');
  });

  it('applies size classes', () => {
    const { rerender } = render(<Badge size="sm">Small</Badge>);
    expect(screen.getByText('Small')).toHaveClass('badge--sm');

    rerender(<Badge size="md">Medium</Badge>);
    expect(screen.getByText('Medium')).toHaveClass('badge--md');
  });
});
