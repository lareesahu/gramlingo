import { describe, it, expect } from 'vitest';
import { getStrings, EN, ZH, ES } from './i18n';

describe('getStrings', () => {
  it('returns English strings for "en"', () => {
    const s = getStrings('en');
    expect(s.appName).toBe('GramLingo');
    expect(s.tagline).toBe('Grammar Quest — Learn by playing');
  });

  it('returns Chinese strings for "zh"', () => {
    const s = getStrings('zh');
    expect(s.appName).toBe('GramLingo');
    expect(s.tagline).toBe('语法闯关 — 边玩边学');
  });

  it('returns Spanish strings for "es"', () => {
    const s = getStrings('es');
    expect(s.appName).toBe('GramLingo');
    expect(s.tagline).toBe('Grammar Quest — Aprende jugando');
  });

  it('defaults to English for unknown language', () => {
    const s = getStrings('fr');
    expect(s.appName).toBe('GramLingo');
    expect(s.tagline).toBe('Grammar Quest — Learn by playing');
  });

  it('has all keys in all languages', () => {
    const enKeys = Object.keys(EN).sort();
    const zhKeys = Object.keys(ZH).sort();
    const esKeys = Object.keys(ES).sort();

    expect(zhKeys).toEqual(enKeys);
    expect(esKeys).toEqual(enKeys);
  });

  it('has no empty string values in any language', () => {
    for (const lang of [EN, ZH, ES]) {
      for (const [_key, val] of Object.entries(lang)) {
        expect(val).toBeTruthy();
      }
    }
  });
});
