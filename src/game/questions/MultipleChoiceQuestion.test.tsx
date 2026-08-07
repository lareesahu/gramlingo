import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { answerMatches } from './MultipleChoiceQuestion';

// Reference normalizer — exact-equality semantics, independent of the implementation.
function norm(s: string): string {
  return s.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim().toLowerCase();
}

interface DataQuestion {
  id: string;
  type: string;
  a: string | string[];
  o: { en: string[] };
}

interface DataPhase {
  id: string;
  q: DataQuestion[];
}

const data = JSON.parse(
  readFileSync(resolve(process.cwd(), 'data/game-data.json'), 'utf8')
) as { phases: DataPhase[] };

const mcQuestions: { phase: string; q: DataQuestion }[] = [];
for (const ph of data.phases) {
  for (const q of ph.q) {
    if (q.type === 'multiple_choice_single') mcQuestions.push({ phase: ph.id, q });
  }
}

describe('answerMatches — D9 regression (substring-matching scoring defect)', () => {
  it('exact answer still matches', () => {
    expect(answerMatches('goes', ['goes'])).toBe(true);
    expect(answerMatches('she lives', ['she lives'])).toBe(true);
    expect(answerMatches('who', ['who', 'whose'])).toBe(true);
    expect(answerMatches('whose', ['who', 'whose'])).toBe(true);
  });

  it('never accepts substring-wrong options (known D9 offenders)', () => {
    expect(answerMatches('go', ['goes'])).toBe(false);        // tenses_present_q01
    expect(answerMatches('having', ['are having'])).toBe(false); // tenses_present_q02
    expect(answerMatches('a', ['an'])).toBe(false);           // determiners_articles_q01
    expect(answerMatches('can', ['cannot'])).toBe(false);     // modals_permission_q02
    expect(answerMatches('where the', ['where'])).toBe(false);  // reported_embedded_q02
    expect(answerMatches('where is', ['where'])).toBe(false);
    expect(answerMatches('did', ['did so'])).toBe(false);     // advanced_substitution_q02
    expect(answerMatches('whom', ['who', 'whose'])).toBe(false); // clauses_gen_q01
    expect(answerMatches('broke', ['was broken'])).toBe(false);  // passive_recognition_q02
    expect(answerMatches('will heat ... boils', ['heat ... boils'])).toBe(false); // conditionals_zero_q01
  });

  it('accepts every intended option across ALL 282 MC questions (no false negatives)', () => {
    const misses: string[] = [];
    for (const { phase, q } of mcQuestions) {
      const answers = Array.isArray(q.a) ? q.a : [q.a];
      for (const opt of q.o.en) {
        const intended = answers.some((a) => norm(a) === norm(opt));
        if (intended && !answerMatches(opt, answers)) {
          misses.push(`${phase}/${q.id}: intended ${JSON.stringify(opt)} rejected`);
        }
      }
    }
    expect(misses).toEqual([]);
  });

  it('rejects every non-intended option across ALL 282 MC questions (no false positives)', () => {
    const extras: string[] = [];
    for (const { phase, q } of mcQuestions) {
      const answers = Array.isArray(q.a) ? q.a : [q.a];
      for (const opt of q.o.en) {
        const intended = answers.some((a) => norm(a) === norm(opt));
        if (!intended && answerMatches(opt, answers)) {
          extras.push(`${phase}/${q.id}: wrong option ${JSON.stringify(opt)} accepted`);
        }
      }
    }
    expect(extras).toEqual([]);
  });
});
