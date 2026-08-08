# GramLingo Misleading-Question Audit — 2026-08-06

Scope: all 346 questions in data/game-data.json (282 multiple-choice + 64 cloze).
Trigger: 3 screenshots from Lareesa (Past Tenses Q3/Q5, Future Forms Q2) where a
grammatically correct answer was marked wrong.

## Root cause (one sentence)

The bank teaches **"textbook-preferred form" as "only correct form"**: every MCQ has a
single accepted answer, but ~20 questions have 2+ genuinely correct options — and the
explanations (ex[]) often state the rejected option is impossible when it is simply
less preferred. A separate bug: 8 questions accept an *incorrect* answer, and 6 comma
questions accept *both* answers (making them useless for learning).

---

## The 3 screenshots (confirmed)

| Question | Bank answer | User picked | Verdict |
|---|---|---|---|
| tenses_past_q05 — "He ___ his keys and could not enter." | had lost | lost | **Wrong marking.** "He lost his keys and could not enter" is perfectly correct English. Past perfect is optional; the sequence is clear from "and could not enter". ex[1] "needs earlier completion" is false. |
| tenses_past_q03 — "She ___ her homework before dinner yesterday." | had finished | finished | **Wrong marking.** "She finished her homework before dinner yesterday" is fully grammatical; "before" already establishes order. Past perfect is preferred in formal style, not required. |
| tenses_future_q02 — "I ___ you tomorrow at 3 PM as agreed." | am seeing | will see | **Wrong marking.** "I will see you tomorrow at 3 PM as agreed" is natural and correct. Present continuous is the textbook favourite for arrangements, but will is not wrong. ex[2] even says "less natural" while marking it wrong. |

---

## CATEGORY A — Same trap as the screenshots (grammatical alternative marked wrong)

~20 questions. Format: ID — question — bank answer | why the rejected option is also correct.

### Past / Future Tenses
1. tenses_past_q06 — "By the time we arrived, the film ___." — had started | "started" is standard in real usage: "By the time we arrived, the film started." ex[1] is false.
2. tenses_future_q01 — "Look at those clouds! It ___." — is going to rain | "will rain" is equally natural: "Look at those clouds! It will rain." The evidence-based-vs-will distinction is a myth; will is used for evidence-based predictions constantly.
3. tenses_future_q03 — "The train ___ at 6 PM per the schedule." — leaves | "will leave" and "is leaving" are both acceptable; ex[2] admits "will leave is possible but less conventional" yet still rejects it.
4. tenses_future_q04 — "I think she ___ the competition." — will win | "wins" is defensible in live-commentary/regular contexts ("She wins the competition every year"); "is winning" fits mid-race.

### Conditionals (zero vs first)
5. conditionals_zero_q01 — "If you ___ water to 100 degrees, it ___." — heat…boils | "heat…will boil" is equally correct (first conditional for a real result).
6. conditionals_zero_q02 — "If you ___ plants, they ___." — do not water…die | "do not water…will die" is equally correct.
7. conditionals_zero_q03 — "When the temperature ___ below zero, water ___." — drops…freezes | "drops…will freeze" is equally correct.

### Reported Speech (optional backshift)
8. reported_statements_q02 — "He said: 'I like coffee.' → He said he ___ coffee." — liked | "likes" is correct when the statement is still true — modern usage prefers no backshift. ex[0] "Likes = direct speech" is a false rule.
9. reported_questions_q01 — "She asked: 'Where do you live?' → She asked where I ___." — lived | "live" is correct if still true.
10. reported_questions_q03 — "She asked: 'What time does the train leave?' → She asked what time the train ___." — left | "leaves" is fine for timetable facts.
11. reported_tense_q01 — "He said: 'I have finished.' → He said he ___." — had finished | "finished" is widely accepted as backshift of present perfect.

### Modals
12. modals_probability_q01 — "She is not here. She ___ be at home." — might | "must" is equally natural — logical deduction: "She must be at home." ex[0] "too strong for speculation" ignores deduction usage.
13. modals_contrast_q01 — "You ___ smoke here. It is a hospital." — must not | "should not" is perfectly fine English; the must-vs-should prohibition split is over-taught.
14. modals_probability_q03 — "That ___ be true. I saw it with my own eyes." — can not | **Semantically contradictory question**: if you saw it with your own eyes, it IS true → "must be true" fits better; "could not" is equally valid.

### Verb patterns
15. verb_patterns_both_q02 — "She remembered ___ the door before leaving." — to lock | "locking" is also correct with a different (valid) meaning: "remembered locking" = recalls the act. Question doesn't disambiguate.
16. verb_patterns_causatives_q02 — "She ___ me ___ her car last weekend." — let…drive | "made…drive" is equally grammatical (forced). Question doesn't disambiguate permission vs force.

### Sentence structure
17. sentence_structure_word_order_q02 — "Choose the correct word order:" — Never have I seen such beauty | "I have never seen such beauty" is ALSO correct — ex[3] literally admits "I have never = correct". Question doesn't demand fronted never.
18. sentence_structure_negation_q02 — "I have ___ been to Japan." — never | "not" is equally correct and extremely common: "I have not been to Japan."
19. advanced_inversion_q01 — "___ known the truth, I would have acted differently." — Had I | "If I had" is the standard form and completely correct; the app rejects the normal version and demands the inverted one.
20. advanced_substitution_q02 — "She asked me to help and I ___." — did so | "did" is arguably MORE natural: "She asked me to help and I did."

### Conjunctions / Determiners
21. conjunctions_correlative_q01 — "___ my mother ___ my father can attend the meeting." — Neither…nor | **No context given** — "Both…and" and "Either…or" are equally grammatical. 3 of 4 options are valid.
22. conjunctions_correlative_q02 — "She is ___ intelligent ___ hardworking." — not only…but also | "both…and" is equally correct and more natural.
23. determiners_generics_q01 — "___ tiger is an endangered species." — The | "A tiger is an endangered species" is also grammatical generic reference.

---

## CATEGORY B — Answer key accepts WRONG English (8 questions)

These teach errors — the app marks an incorrect form as correct:

1. clauses_subj_q01 — "The woman ___ called me is my manager." — accepts **who, whom** | "whom called me" is wrong (whom = object case, cannot be subject).
2. clauses_subj_q02 — "The doctor ___ treated me was kind." — accepts who, that, **whom** | "whom treated me" wrong.
3. clauses_subj_q06 — "People ___ exercise regularly live longer." — accepts who, **whom** | "whom exercise" wrong.
4. clauses_gen_q01 — "The man ___ car was stolen reported it." — accepts **who**, whose | "who car" wrong; only "whose" is correct.
5. clauses_gen_q02 — "I know a woman ___ son is a pilot." — accepts **who**, whose | "who son" wrong.
6. clauses_gen_q03 — "The company ___ CEO resigned is in trouble." — accepts **who**, whose | wrong.
7. clauses_gen_q04 — "The tree ___ branches fell was very old." — accepts **who**, whose | wrong.
8. clauses_gen_q05 — "She adopted a dog ___ owner had passed away." — accepts **who**, whose | wrong.
9. clauses_gen_q06 — "That is the writer ___ books I love." — accepts **who**, whose | wrong.
10. clauses_gen_q07 — "Fix: The woman who her car was stolen. who her = ?" — accepts **who**, whose | "who her" → fix is whose; "who" is the error, not a fix.

---

## CATEGORY C — Degenerate questions (both answers accepted, no learning)

clauses_rest_q01–q08 (comma questions): every one accepts BOTH "No comma" AND "Comma".
The teaching intent (restrictive vs non-restrictive) never fires — any answer is correct.
e.g. rest_q03 "(one brother) comma?" → correct answer is Comma (non-restrictive), but
"No comma" is also accepted.

---

## CATEGORY D — Malformed / data bugs

1. reported_embedded_q02 — "Can you tell me ___ the bus stop?" — answer "where" | Sentence would read "Can you tell me where the bus stop?" — incomplete; needs "is" but it's not in any option.
2. conditionals_mixed_q01 — options contain duplicate "had studied … would have" twice.
3. modals_probability_q03 — logic contradiction (see A14).

---

## Numbers

- Category A (grammatical answer rejected): ~23 questions (incl. the 3 screenshots) ≈ 8% of MCQs.
- Category B (wrong answer accepted): 10 questions.
- Category C (both accepted): 6 questions.
- Category D (malformed): 3 questions.
- Total affected: ~42 of 282 MCQs (15%).

## Fix direction (not applied — investigation only)

1. For A: either add the valid alternatives to the answer list (a: [..]) where the app
   supports multi-accept (it already does for 28 questions), or rewrite the question with
   stronger context that disambiguates the intended form.
2. For B: remove whom/who from the accepted lists — keep only who/that (subject) and
   whose (genitive).
3. For C: pick the single correct comma answer per question context.
4. For D: add "is" option / dedupe / fix logic.

No files in data/game-data.json were modified.
