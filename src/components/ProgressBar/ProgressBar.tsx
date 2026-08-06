/* ═══════════════════════════════════════════════
   GRAMLINGO — ProgressBar Component
   ═══════════════════════════════════════════════ */

import './ProgressBar.css';

interface ProgressBarProps {
  value: number; // 0-100
  max?: number;
  label?: string;
  showPercent?: boolean;
  size?: 'sm' | 'md';
  color?: 'primary' | 'correct' | 'wrong';
}

export function ProgressBar({
  value,
  max = 100,
  label,
  showPercent = false,
  size = 'md',
  color = 'primary',
}: ProgressBarProps) {
  const pct = Math.min(100, Math.max(0, Math.round((value / max) * 100)));

  return (
    <div className={`progress-bar progress-bar--${size}`} role="progressbar" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100}>
      {(label || showPercent) && (
        <div className="progress-header">
          {label && <span className="progress-label">{label}</span>}
          {showPercent && <span className="progress-pct">{pct}%</span>}
        </div>
      )}
      <div className="progress-track">
        <div
          className={`progress-fill progress-fill--${color}`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
