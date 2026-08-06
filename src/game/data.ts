/* ═══════════════════════════════════════════════
   GRAMLINGO — Game Data (loads from game-data.json)
   Adapts lang-nested format to flat i18n props.
   ═══════════════════════════════════════════════ */

import rawData from '../../data/game-data.json';
import type { GameData, Module, Phase, Question } from './types';

function pickLang<T extends Record<string, unknown>>(obj: T, key: string, def: string = ''): string {
  const val = (obj as any)[key];
  return typeof val === 'string' ? val : def;
}

function adaptModules(raw: any[]): Module[] {
  return raw.map((m: any) => ({
    id: m.id,
    name: pickLang(m.name, 'en'),
    nameZh: pickLang(m.name, 'zh'),
    desc: pickLang(m.desc, 'en'),
    descZh: pickLang(m.desc, 'zh'),
    gramlin: m.gramlin || '',
    icon: m.icon || '',
    sort: m.sort || 99,
  }));
}

function adaptQuestions(rawQs: any[]): Question[] {
  return rawQs.map((q: any) => ({
    q: pickLang(q.q, 'en', q.q),
    qZh: pickLang(q.q, 'zh', q.q),
    a: q.a,
    o: Array.isArray(q.o) ? q.o : (q.o?.en || []),
    t: pickLang(q.t, 'en'),
    tZh: pickLang(q.t, 'zh'),
    tEs: pickLang(q.t, 'es'),
    ex: q.ex?.en,
    exZh: q.ex?.zh,
    exEs: q.ex?.es,
  }));
}

function adaptPhases(rawPhases: any[]): Phase[] {
  return rawPhases.map((p: any, i: number) => ({
    module: p.module,
    id: p.id,
    name: pickLang(p.name, 'en'),
    nameZh: pickLang(p.name, 'zh'),
    sub: pickLang(p.s, 'en'),
    subZh: pickLang(p.s, 'zh'),
    sort: p.sort || i + 1,
    q: adaptQuestions(p.q || []),
  }));
}

export const GAME_DATA: GameData = {
  title: rawData.title || 'Gramlingo',
  modules: adaptModules(rawData.modules || []),
  phaseLockOrder: rawData.phaseLockOrder || {},
  phases: adaptPhases(rawData.phases || []),
};
