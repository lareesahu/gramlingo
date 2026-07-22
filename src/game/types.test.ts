import { describe, it, expect } from 'vitest';
import { scoreToStars } from './types';

describe('scoreToStars', () => {
  it('returns 3 stars for score >= 90', () => {
    expect(scoreToStars(100)).toBe(3);
    expect(scoreToStars(95)).toBe(3);
    expect(scoreToStars(90)).toBe(3);
  });

  it('returns 2 stars for score 70-89', () => {
    expect(scoreToStars(89)).toBe(2);
    expect(scoreToStars(70)).toBe(2);
    expect(scoreToStars(75)).toBe(2);
  });

  it('returns 1 star for score 50-69', () => {
    expect(scoreToStars(69)).toBe(1);
    expect(scoreToStars(50)).toBe(1);
    expect(scoreToStars(55)).toBe(1);
  });

  it('returns 0 stars for score < 50', () => {
    expect(scoreToStars(49)).toBe(0);
    expect(scoreToStars(0)).toBe(0);
    expect(scoreToStars(25)).toBe(0);
  });
});
