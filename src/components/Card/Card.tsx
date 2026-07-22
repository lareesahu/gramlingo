/* ═══════════════════════════════════════════════
   GRAMLINGO — Card Component
   ═══════════════════════════════════════════════ */

import './Card.css';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
  hoverable?: boolean;
  padded?: boolean;
}

export function Card({ children, className = '', onClick, hoverable = false, padded = true }: CardProps) {
  const classes = [
    'card',
    hoverable && 'card--hoverable',
    !padded && 'card--no-pad',
    onClick && 'card--clickable',
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div
      className={classes}
      onClick={onClick}
      role={onClick ? 'button' : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={
        onClick
          ? (e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                onClick();
              }
            }
          : undefined
      }
    >
      {children}
    </div>
  );
}
