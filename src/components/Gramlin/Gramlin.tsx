import type { GramlinPose } from '../../game/types';
import './Gramlin.css';

interface GramlinProps {
  pose: GramlinPose;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  alt?: string;
  className?: string;
  animated?: boolean;
}

const poseToFile: Record<GramlinPose, string> = {
  neutral: 'neutral-gramlin.png',
  graduate: 'graduate-gramlin.png',
  book: 'study-gramlin.png',
  celebrate: 'celebrate-gramlin.png',
  sad: 'sad-gramlin.png',
  think: 'thinking-gramlin.png',
  sleeper: 'sleepy-gramlin.png',
  pencil: 'writer-gramlin.png',
  hearts: 'happy-gramlin.png',
  trophy: 'champion-gramlin.png',
  power: 'determined-gramlin.png',
  peeking: 'peekaboo-gramlin.png',
  confused: 'neutral-gramlin.png',
  party: 'party-gramlin.png',
  juggler: 'party-gramlin.png',
  grad: 'graduate-gramlin.png',
  angry: 'sprint-gramlin.png',
  crying: 'sad-gramlin.png',
  laptop: 'study-gramlin.png',
  'sleep-ground': 'cozy-gramlin.png',
};

const baseUrl = `${import.meta.env.BASE_URL}assets/gramlin/`;

export function Gramlin({ pose, size = 'md', alt = '', className = '', animated = false }: GramlinProps) {
  const classes = ['gramlin', `gramlin--${size}`, animated && 'gramlin--animated', className].filter(Boolean).join(' ');

  return (
    <div className={classes} role="img" aria-label={alt || `${pose} Gramlin`}>
      <img src={`${baseUrl}${poseToFile[pose]}`} alt={alt || `Gramlin ${pose}`} className="gramlin-img" loading="lazy" />
    </div>
  );
}