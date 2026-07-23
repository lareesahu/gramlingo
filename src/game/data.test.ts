import { describe, it, expect } from 'vitest';
import { GAME_DATA } from './data';

describe('GAME_DATA integrity', () => {
  it('has modules defined', () => {
    expect(GAME_DATA.modules.length).toBeGreaterThan(0);
  });

  it('has phases defined', () => {
    expect(GAME_DATA.phases.length).toBeGreaterThan(0);
  });

  it('has phaseLockOrder entries for each module', () => {
    for (const mod of GAME_DATA.modules) {
      expect(GAME_DATA.phaseLockOrder[mod.id]).toBeDefined();
      expect(GAME_DATA.phaseLockOrder[mod.id].length).toBeGreaterThan(0);
    }
  });

  it('every phase references a valid module', () => {
    const moduleIds = new Set(GAME_DATA.modules.map(m => m.id));
    for (const phase of GAME_DATA.phases) {
      expect(moduleIds.has(phase.module)).toBe(true);
    }
  });

  it('every phase in lockOrder exists in phases array', () => {
    const phaseIds = new Set(GAME_DATA.phases.map(p => p.id));
    for (const [, order] of Object.entries(GAME_DATA.phaseLockOrder)) {
      for (const pid of order) {
        expect(phaseIds.has(pid)).toBe(true);
      }
    }
  });

  it('keeps the full curriculum plan and the authored lesson bank', () => {
    expect(GAME_DATA.modules).toHaveLength(12);
    expect(GAME_DATA.phases).toHaveLength(92);
    expect(GAME_DATA.phases.filter(phase => phase.q.length > 0).length).toBeGreaterThan(80);
    expect(GAME_DATA.phases.flatMap(phase => phase.q)).toHaveLength(282);
  });

  it('every question has options and at least 1 correct answer', () => {
    for (const phase of GAME_DATA.phases) {
      for (const q of phase.q) {
        expect(q.o.length).toBeGreaterThan(1);
        expect(q.a).toBeDefined();
        expect(q.ex).toHaveLength(q.o.length);
        expect(q.exZh).toHaveLength(q.o.length);
        expect(q.exEs).toHaveLength(q.o.length);
        // Some explanations may be empty (uses fallback_tip)
      }
    }
  });

  it('modules have unique ids', () => {
    const ids = GAME_DATA.modules.map(m => m.id);
    expect(new Set(ids).size).toBe(ids.length);
  });

  it('phases have unique ids', () => {
    const ids = GAME_DATA.phases.map(p => p.id);
    expect(new Set(ids).size).toBe(ids.length);
  });

  it('modules have required fields', () => {
    for (const mod of GAME_DATA.modules) {
      expect(mod.name).toBeTruthy();
      expect(mod.nameZh).toBeTruthy();
      expect(mod.desc).toBeTruthy();
      expect(mod.gramlin).toBeTruthy();
    }
  });
});
