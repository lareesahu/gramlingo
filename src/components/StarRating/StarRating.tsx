/* ═══════════════════════════════════════════════
   GRAMLINGO — StarRating Component
   ═══════════════════════════════════════════════ */

import { scoreToStars } from '../../game/types';
import './StarRating.css';

interface StarRatingProps {
  score: number; // 0-100
  showScore?: boolean;
  size?: 'sm' | 'md' | 'lg';
  animated?: boolean;
}

const STAR_CHARS = ['☆', '☆', '☆'];

export function StarRating({ score, showScore = false, size = 'md', animated = false }: StarRatingProps) {
  const stars = scoreToStars(score);

  return (
    <div className={`star-rating star-rating--${size}`} aria-label={`${stars} out of 3 stars`}>
      <div className="stars" role="img">
        {STAR_CHARS.map((_, i) => (
          <span
            key={i}
            className={`star ${i < stars ? 'star--filled' : ''} ${animated ? 'star--animated' : ''}`}
            style={animated ? { animationDelay: `${i * 200}ms` } : undefined}
          >
            {i < stars ? '★' : '☆'}
          </span>
        ))}
      </div>
      {showScore && <span className="star-score">{score}%</span>}
    </div>
  );
}
