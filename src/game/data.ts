/* GRAMLINGO — Game Data (loads from game-data.json) */

import rawData from "../../data/game-data.json";
import type { GameData, Module, Phase, Question, LegacyQuestion } from "./types";

function pickLang<T extends Record<string, unknown>>(obj: T, key: string, def: string = ""): string {
  const val = (obj as any)[key];
  return typeof val === "string" ? val : def;
}

function adaptModules(raw: any[]): Module[] {
  return raw.map((m: any) => ({
    id: m.id, name: pickLang(m.name, "en"), nameZh: pickLang(m.name, "zh"),
    desc: pickLang(m.desc, "en"), descZh: pickLang(m.desc, "zh"),
    gramlin: m.gramlin || "", icon: m.icon || "", sort: m.sort || 99,
  }));
}

function adaptQuestion(raw: any, index: number, phaseId: string): LegacyQuestion | Question {
  if (raw.type === "block_builder" || raw.type === "cloze") {
    return raw as Question;
  }
  return {
    id: raw.id || phaseId + "_q" + String(index + 1).padStart(2, "0"),
    type: raw.type || "multiple_choice_single",
    q: pickLang(raw.q, "en", raw.q),
    qZh: pickLang(raw.q, "zh", raw.q),
    qEs: pickLang(raw.q, "es", raw.q || ""),
    a: raw.a,
    o: Array.isArray(raw.o) ? raw.o : (raw.o?.en || []),
    oZh: Array.isArray(raw.o) ? null : (raw.o?.zh || undefined),
    oEs: Array.isArray(raw.o) ? null : (raw.o?.es || undefined),
    t: pickLang(raw.t, "en"),
    tZh: pickLang(raw.t, "zh"),
    tEs: pickLang(raw.t, "es"),
    ex: raw.ex?.en,
    exZh: raw.ex?.zh,
    exEs: raw.ex?.es,
  };
}

function adaptQuestions(rawQs: any[], phaseId: string): (LegacyQuestion | Question)[] {
  return rawQs.map((q: any, i: number) => adaptQuestion(q, i, phaseId));
}

function adaptPhases(rawPhases: any[]): Phase[] {
  return rawPhases.map((p: any, i: number) => ({
    module: p.module, id: p.id,
    name: pickLang(p.name, "en"), nameZh: pickLang(p.name, "zh"), nameEs: pickLang(p.name, "es"),
    sub: pickLang(p.s, "en"), subZh: pickLang(p.s, "zh"),
    sort: p.sort || i + 1, q: adaptQuestions(p.q || [], p.id),
  }));
}

export const GAME_DATA: GameData = {
  title: rawData.title || "Gramlingo",
  modules: adaptModules(rawData.modules || []),
  phaseLockOrder: rawData.phaseLockOrder || {},
  phases: adaptPhases(rawData.phases || []),
};
