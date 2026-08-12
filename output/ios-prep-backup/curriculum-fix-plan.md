# GramLingo — Curriculum Data Fix Plan (Category A & D)

**Status: AWAITING LARESESA'S EXPLICIT GO-AHEAD**
**Backup:** `output/ios-prep-backup/game-data.json.backup-20260812-234526`
**Date:** 2026-08-12

Per the DATASET RULE, no changes are made to `data/game-data.json` until Lareesa
approves this plan. This document is the written plan required before any bulk
edit to the curriculum.

## Already fixed (verified — no action needed)

- **Category B** (answer key accepted WRONG English): FIXED in commit `5eb61a4`.
  All 10 questions now accept only the correct form (`who`/`that` for subject,
  `whose` for genitive).
- **Category C** (comma questions accepting both answers): FIXED in commit
  `5eb61a4`. Each `clauses_rest_q01–q08` now has a single correct answer.

## Remaining: Category A (~23 questions) — grammatical alternative marked wrong

The root issue: the bank teaches "textbook-preferred form" as "only correct
form." Each question has a single accepted answer, but a second answer is
genuinely correct English.

**Proposed fix — two options, recommend Option 1:**

**Option 1 (recommended, low-risk): multi-accept.**
The app already supports `a: [...]` arrays (28 questions use it). For each
Category A question, add the valid alternative to the `a` array AND add a note
in the tip (`t`) clarifying which form is preferred vs. merely acceptable.
No question text or options are deleted — we only widen acceptance + educate.

**Option 2: rewrite question context.**
Tighten each question so only the intended form fits (add time markers, context
clauses, etc.). Higher effort, higher risk of introducing new ambiguity.

### Affected question IDs (Option 1 → add these to `a`)

| Question | Bank answer | Add as valid |
|---|---|---|
| tenses_past_q03 | had finished | finished |
| tenses_past_q05 | had lost | lost |
| tenses_past_q06 | had started | started |
| tenses_future_q01 | is going to rain | will rain |
| tenses_future_q02 | am seeing | will see |
| tenses_future_q03 | leaves | will leave |
| tenses_future_q04 | will win | wins |
| conditionals_zero_q01 | heat…boils | heat…will boil |
| conditionals_zero_q02 | do not water…die | do not water…will die |
| conditionals_zero_q03 | drops…freezes | drops…will freeze |
| reported_statements_q02 | liked | likes |
| reported_questions_q01 | lived | live |
| reported_questions_q03 | left | leaves |
| reported_tense_q01 | had finished | finished |
| modals_probability_q01 | might | must |
| modals_contrast_q01 | must not | should not |
| verb_patterns_both_q02 | to lock | locking |
| verb_patterns_causatives_q02 | let…drive | made…drive |
| sentence_structure_word_order_q02 | Never have I seen… | I have never seen… |
| sentence_structure_negation_q02 | never | not |
| advanced_inversion_q01 | Had I | If I had |
| advanced_substitution_q02 | did so | did |
| determiners_generics_q01 | The | A |

*(Note: modals_probability_q03 and conjunctions_correlative_q01/q02 also fall
here but need a content decision — see Category D below.)*

## Remaining: Category D (3 questions) — malformed / data bugs

| Question | Issue | Proposed fix |
|---|---|---|
| reported_embedded_q02 — "Can you tell me ___ the bus stop?" | No option produces a grammatical sentence (needs "where the bus stop is") | Rewrite options to include "where the bus stop is"; accept only that |
| conditionals_mixed_q01 | Duplicate option "had studied … would have" appears twice | Deduplicate — replace one with a distinct distractor |
| modals_probability_q03 — "That ___ be true. I saw it with my own eyes." | Self-contradictory (if you saw it, it IS true) | Rewrite question or change to "can't" vs "must" with clear context |

## What I need from Lareesa

1. **Approve Option 1 (multi-accept) for Category A?** Yes/No
2. **For Category D:** approve the three specific rewrites above, or provide
   preferred replacement text.
3. Anything she wants to keep as-is (e.g. keep teaching "textbook-preferred"
   as a deliberate product choice — then we skip Category A entirely).

## Execution (once approved)

1. Confirm backup exists (done).
2. Apply multi-accept + tip updates via a script that ONLY edits the listed
   question IDs — never bulk-rewrites unrelated fields.
3. Re-run `npm run test` (the data-integrity test asserts option/answer counts).
4. `npm run build` + verify dist data hash matches source.
5. Report the exact diff (questions changed + new accepted answers).
