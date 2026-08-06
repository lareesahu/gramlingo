# Build complete Gramlingo curriculum CSVs
# Run: python build_curriculum.py

import csv, os, copy

BASE = r'C:\Users\hunin\projects\gramlingo\content'
L = ['en','zh','es']

# Load existing modules (12-module version)
with open(os.path.join(BASE, 'modules-new.csv'), encoding='utf-8-sig') as f:
    EXISTING_MODULES = list(csv.DictReader(f))
# Keep only the ones from the 12-module set
MODULE_IDS = [m['module_id'] for m in EXISTING_MODULES]
print(f"Modules: {len(MODULE_IDS)} — {MODULE_IDS}")

# Load existing questions (keep the 79 from WeChat as base)
with open(os.path.join(BASE, 'questions.csv'), encoding='utf-8-sig') as f:
    EXISTING_QUESTIONS = list(csv.DictReader(f))
print(f"Existing questions: {len(EXISTING_QUESTIONS)}")

# ============================================================
# PHASE DEFINITIONS for all 12 modules
# ============================================================
MODULE_PHASES = {
    'clauses': [
        ('rec', 'Identify Relative Clauses', 'Identify the relative clause and its antecedent'),
        ('subj', 'Subject Relatives', 'Use who/which/that as subject relative pronouns'),
        ('obj', 'Object Relatives', 'Identify object relatives and pronoun omission'),
        ('subobj', 'Subject vs Object', 'Distinguish subject from object relatives'),
        ('oblq', 'Oblique Relatives', 'Use where/when/why and preposition relatives'),
        ('gen', 'Genitive Relatives', 'Use whose for possession'),
        ('rest', 'Restrictive vs Non-restrictive', 'Choose meaning, punctuation, and pronouns'),
        ('prod', 'Production and Editing', 'Combine, rewrite, and produce relative clauses'),
    ],
    'prepositions': [
        ('prep_place', 'In/On/At: Place', 'Containment, surface, and point/location'),
        ('prep_time', 'In/On/At: Time', 'Periods, days/dates, and precise times'),
        ('prep_mixed', 'Mixed Prepositions', 'Select by conceptual relationship'),
        ('prod', 'Production and Editing', 'Correct and produce contextual uses'),
    ],
    'tenses': [
        ('present', 'Present Tenses', 'Simple vs continuous; present perfect basics'),
        ('past', 'Past Tenses', 'Simple past, past continuous, past perfect basics'),
        ('future', 'Future Forms', 'Will, going to, present continuous for future'),
        ('perfect', 'Perfect Tenses', 'Present perfect vs past simple; past perfect'),
        ('continuous', 'Continuous Forms', 'When continuous adds meaning'),
        ('contrast', 'Tense Contrast', 'Choose correct tense by context clues'),
        ('narrative', 'Narrative Tenses', 'Sequence tenses in stories'),
        ('prod', 'Production and Editing', 'Write and edit for correct tense usage'),
    ],
    'conditionals': [
        ('zero', 'Zero Conditional', 'General truths and scientific facts'),
        ('first', 'First Conditional', 'Real future possibilities'),
        ('second', 'Second Conditional', 'Unreal present and future'),
        ('third', 'Third Conditional', 'Unreal past and regrets'),
        ('mixed', 'Mixed Conditionals', 'Combining time references'),
        ('alternatives', 'Alternatives to If', 'Unless, provided that, as long as, otherwise'),
        ('wish', 'I Wish / If Only', 'Expressing wishes and regrets'),
        ('prod', 'Production and Editing', 'Write conditional sentences in context'),
    ],
    'passive': [
        ('recognition', 'Recognize Passive', 'Identify passive vs active voice'),
        ('formation', 'Form the Passive', 'Be + past participle across tenses'),
        ('agent', 'With/Without Agent', 'When to include or omit the doer'),
        ('tenses', 'Passive Across Tenses', 'Passive in present, past, future, perfect'),
        ('modals', 'Passive with Modals', 'Can/must/should be done'),
        ('causative', 'Causative Forms', 'Have/get something done'),
        ('impersonal', 'Impersonal Passive', 'It is said/believed/thought that...'),
        ('prod', 'Production and Editing', 'Rewrite active to passive and vice versa'),
    ],
    'reported': [
        ('statements', 'Reported Statements', 'Backshift and pronoun changes'),
        ('questions', 'Reported Questions', 'Word order and if/whether'),
        ('commands', 'Reported Commands', 'Tell/ask + to-infinitive'),
        ('time', 'Time and Place Shifts', 'Now/then, today/that day, here/there'),
        ('verbs', 'Reporting Verbs', 'Say, tell, explain, admit, deny, suggest'),
        ('tense', 'Tense Backshift Rules', 'When backshift is required vs optional'),
        ('embedded', 'Embedded Questions', 'Do you know where... / Can you tell me what...'),
        ('prod', 'Production and Editing', 'Convert direct to reported speech'),
    ],
    'modals': [
        ('ability', 'Ability', 'Can, could, be able to'),
        ('permission', 'Permission', 'Can, may, could, be allowed to'),
        ('obligation', 'Obligation', 'Must, have to, should, ought to'),
        ('probability', 'Probability', 'Must, might, may, could, cant for deduction'),
        ('past', 'Past Modals', 'Could have, should have, must have, might have'),
        ('requests', 'Requests and Offers', 'Can/could/would you... Shall I...'),
        ('contrast', 'Modal Contrast', 'Choose the right modal by meaning'),
        ('prod', 'Production and Editing', 'Use modals in realistic scenarios'),
    ],
    'determiners': [
        ('articles', 'Articles', 'A/an, the, zero article rules'),
        ('definite', 'Definite vs Indefinite', 'When to use the vs a/an'),
        ('quantifiers', 'Quantifiers', 'Some, any, much, many, few, little'),
        ('demonstratives', 'Demonstratives', 'This, that, these, those'),
        ('possessives', 'Possessives', 'My, your, his, her, its, our, their'),
        ('generics', 'Generic Reference', 'Referring to classes and categories'),
        ('contrast', 'Determiner Contrast', 'Choose the right determiner by context'),
        ('prod', 'Production and Editing', 'Edit texts for correct determiner use'),
    ],
    'conjunctions': [
        ('coordinating', 'Coordinating', 'And, but, or, so, yet, for, nor'),
        ('subordinating', 'Subordinating', 'Because, although, while, since, if, when'),
        ('correlative', 'Correlative', 'Both...and, either...or, neither...nor, not only...but also'),
        ('contrast', 'Contrast and Concession', 'Although, even though, despite, in spite of'),
        ('cause', 'Cause and Result', 'Because, since, as, so...that, such...that'),
        ('purpose', 'Purpose', 'So that, in order that, for'),
        ('linking', 'Linking Adverbs', 'However, therefore, moreover, furthermore, nevertheless'),
        ('prod', 'Production and Editing', 'Combine sentences using conjunctions'),
    ],
    'verb_patterns': [
        ('gerunds', 'Gerunds', 'Verbs followed by -ing forms'),
        ('infinitives', 'Infinitives', 'Verbs followed by to + infinitive'),
        ('both', 'Gerund vs Infinitive', 'Verbs that change meaning with form'),
        ('causatives', 'Causatives', 'Make, let, have, get + object + verb'),
        ('preposition', 'Preposition + Gerund', 'After prepositions, always -ing'),
        ('adj', 'Adjective Patterns', 'It is + adj + to / I am + adj + to'),
        ('contrast', 'Pattern Contrast', 'Choose the right pattern by verb and meaning'),
        ('prod', 'Production and Editing', 'Complete and produce correct verb patterns'),
    ],
    'sentence_structure': [
        ('word_order', 'Word Order', 'Subject-verb-object basics and inversion'),
        ('questions', 'Question Formation', 'Yes/no and wh- questions'),
        ('negation', 'Negation', 'Not, never, no, and negative adverbs'),
        ('clauses', 'Clause Types', 'Main, subordinate, and coordinate clauses'),
        ('cleft', 'Cleft Sentences', 'It is...that / What...is emphasis structures'),
        ('fragments', 'Fragments and Run-ons', 'Diagnose and repair incomplete sentences'),
        ('parallelism', 'Parallel Structure', 'Consistent grammatical form in lists and pairs'),
        ('prod', 'Production and Editing', 'Write and revise for sentence quality'),
    ],
    'advanced': [
        ('emphasis', 'Emphasis', 'Inversion, fronting, and emphatic auxiliaries'),
        ('inversion', 'Inversion', 'Negative adverbs, conditionals without if'),
        ('substitution', 'Substitution and Ellipsis', 'So/not, do so, leaving words out'),
        ('register', 'Register', 'Formal vs informal grammar choices'),
        ('cohesion', 'Cohesion', 'Reference, substitution, and discourse markers'),
        ('nominalisation', 'Nominalisation', 'Turning verbs and adjectives into nouns'),
        ('hedging', 'Hedging and Stance', 'Seem, appear, tend to, it is likely that'),
        ('prod', 'Production and Editing', 'Write with advanced grammar in context'),
    ],
}
print("All 12 modules planned with phases.")
print(f"Total phases: {sum(len(v) for v in MODULE_PHASES.values())}")
