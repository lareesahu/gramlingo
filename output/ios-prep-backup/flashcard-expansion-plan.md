# GramLingo — Flashcard Word-Family Expansion Plan

**Status: AWAITING EXECUTION — plan written per DATASET RULE**
**Backup:** `output/ios-prep-backup/flashcards.json.backup-20260813-*`
**Date:** 2026-08-13

## Goal

Expand the Flashcards panel from the current partial deck to the locked target:
**2,000 word families across 8 modules (250/module)**, plus complete Irregular
Verbs (95) and Word Pairs (collocations).

## Current state (verified)

| Deck | Target | Current | Gap |
|---|---|---|---|
| Word Families | 8 modules × 250 = 2,000 | 1 module, 64 families, 230 members | 7 modules + ~1,750 families |
| Irregular Verbs | 95 verbs (AAA/ABB/ABC) | 24 | ~71 |
| Word Pairs | make/do/take/have/get + pairs | 20 | under-spec'd |

## Authoritative word-list source (NO LLM-invented words)

- **File:** `content/ngsl-headwords.json` — 2,801 headwords from the New General
  Service List (Browne, Culligan & Phillips, 2013/2023), the standard
  high-frequency list for L2 learners. Extracted 2026-08-13 from EAPFoundation's
  published full list.
- Word *selection* and *family membership* MUST come from this list (or the
  already-existing 64 families, which follow the same frequency bands).
- Agents may author: `clue` (English gloss), `clueZh` (中文 gloss), `phonetic`,
  `pos`/`posZh`, and per-member `example`/`exampleZh` sentences.
- Agents MUST NOT invent a family whose root is not a real high-frequency word.

## Schema contract (must match `src/game/types.ts` + existing data)

```json
{
  "id": "act",
  "root": "act",
  "phonetic": "/ækt/",
  "pos": "v. · n.",
  "clue": "to do something; a thing done",
  "clueZh": "行动",
  "members": [
    { "pos": "v.", "posZh": "动", "word": "act",
      "example": "She acted quickly.", "exampleZh": "她迅速行动。", "level": 0 }
  ]
}
```

- `posZh` values: 动 / 名 / 形 / 副 / 介 / 连 / 代 / 数 / 叹 / 限定词 (verb/noun/
  adj/adv/prep/conj/pron/num/interj/determiner).
- `level` = morphological distance from root (0=root, 1=+1 affix, 2=+2 affixes).
- Bilingual (EN + 中文). No Spanish in the flashcard schema.
- Module shape: `{ id, name, nameZh, desc, descZh, gramlin, icon, sort, deckType, lessons: [{ id, name, nameZh, sort, families: [...] }] }`

## Module layout (locked target — 8 word-family modules)

| Module id | Band | Theme | Lessons |
|---|---|---|---|
| wordfamilies1 | 1–250 (exists, 64 families) | Survival | 8 lessons × 8 |
| wordfamilies2 | 251–500 | Conversation | 8 × 8 |
| wordfamilies3 | 501–750 | Intermediate | 8 × 8 |
| wordfamilies4 | 751–1000 | Advanced | 8 × 8 |
| wordfamilies5 | 1001–1250 | Upper-intermediate | 8 × 8 |
| wordfamilies6 | 1251–1500 | High-frequency academic | 8 × 8 |
| wordfamilies7 | 1501–1750 | Academic | 8 × 8 |
| wordfamilies8 | 1751–2000 | Academic/abstract | 8 × 8 |

Each module: ~8 lessons of ~8 families (not morphological grouping — grouped by
frequency band and difficulty, per Lareesa's 2026-08-07 instruction).

## Reorder (already done 2026-08-13)

Module display order is now: Irregular Verbs (sort 1) → Word Pairs (sort 2) →
Word Families 1–8 (sort 3–10).

## Execution (agent swarm + proof agents)

1. Spawn parallel builder subagents — one per word-family module (2–8) and one
   for irregular verbs + one for word pairs. Each writes its module as a JSON
   file to `content/flashcards-modules/<id>.json`.
2. Each builder is given: the NGSL headword slice for its band, the exact schema,
   and the existing 64-family module as a style reference.
3. Spawn a proof-agent (independent verifier) per builder to check: JSON validity,
   schema conformance, word-list provenance, bilingual completeness, family counts.
4. Merge validated modules into `data/flashcards.json` + mirror to
   `public/data/flashcards.json`.
5. `npm run build` + `npx vitest run` must pass. Commit on `v4`.

## Guards

- Backup exists before any merge.
- No module is merged until its proof-agent returns PASS.
- No invented roots — every family root must trace to NGSL headwords or existing data.
- Bilingual only (EN + 中文) — matching the existing schema.
