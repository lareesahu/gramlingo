const fs = require('fs');

// Load game data
const src = 'C:/Users/hunin/projects/gramlingo/data/game-data.json';
const dst = 'C:/Users/hunin/projects/gramlingo/public/data/game-data.json';
const data = JSON.parse(fs.readFileSync(src, 'utf8'));

// Phase-level teaching tips — one per phase
const phaseTips = {
  rec: { en: 'A relative clause describes a noun. Look for "who," "which," or "that" connecting to the word before it.', zh: '定语从句修饰名词，寻找 who/which/that 连接前面的词。' },
  subj: { en: 'When the relative pronoun is the subject of the clause, it comes right after the noun it describes.', zh: '当关系代词是主语时，它紧跟在所修饰的名词之后。' },
  obj: { en: 'When the relative pronoun is the object, it can often be omitted in informal English.', zh: '当关系代词是宾语时，非正式英语中常可省略。' },
  subobj: { en: 'Subject relative clauses keep the pronoun; object relative clauses can drop it. Check who does the action.', zh: '主语从句保留代词，宾语从句可省略。看谁在做动作。' },
  oblq: { en: '"Where" for places, "when" for time, "why" for reasons — these replace prepositional phrases.', zh: 'where 表地点，when 表时间，why 表原因——它们代替介词短语。' },
  gen: { en: '"Whose" shows possession. It comes between the noun it owns and the noun it belongs to.', zh: 'whose 表示所属关系，放在所属物和被所属者之间。' },
  rest: { en: 'Restrictive clauses are essential to meaning (no commas). Non-restrictive add extra info (use commas).', zh: '限制性从句不可省略（无逗号），非限制性从句是额外信息（有逗号）。' },
  prod: { en: 'Combine what you have learned — identify clause type, check pronoun choice, and verify punctuation.', zh: '综合运用所学——判断从句类型、选择正确代词、检查标点。' },
  prep_place: { en: '"In" for enclosed spaces, "on" for surfaces, "at" for specific points. Picture the relationship.', zh: 'in 表封闭空间，on 表表面，at 表具体点。想象空间关系。' },
  prep_time: { en: '"In" for months/years, "on" for days/dates, "at" for specific times. Think big to small.', zh: 'in 用于月/年，on 用于天/日期，at 用于具体时刻。从大到小。' },
  prep_mixed: { en: 'Context decides — is it a location or a time? The same preposition can work differently.', zh: '语境决定——是地点还是时间？同一个介词可有不同用法。' },
  prep_prod: { en: 'Apply prepositions in full sentences. Check both meaning and collocation.', zh: '在完整句子中运用介词，同时检查意义和搭配。' },
  // Default fallback
  default: { en: 'Read the sentence carefully. The correct answer follows standard English grammar rules.', zh: '仔细阅读句子，正确答案遵循标准英语语法规则。' }
};

// Per-option explanation templates
const correctExplanations = {
  en: ['Correct! This is the right choice.', 'That is right — good eye!', 'Yes, this matches the grammar rule.', 'Correct — this follows the expected pattern.'],
  zh: ['正确！就是这个选项。', '对了，眼光不错！', '是的，这符合语法规则。', '正确——符合预期模式。']
};

const wrongExplanations = {
  en: ['Not this one — it does not fit the grammar pattern.', 'This option is incorrect. Check the sentence structure.', 'Wrong choice — this does not follow the rule.', 'This is not right. Try reading the sentence aloud.'],
  zh: ['不是这个——不符合语法模式。', '这个选项不对，检查句子结构。', '选择错误——不符合规则。', '不对，试着朗读句子看看。']
};

let totalQuestions = 0;
let filledTips = 0;
let filledEx = 0;

data.phases.forEach(phase => {
  const tip = phaseTips[phase.id] || phaseTips.default;
  
  // Fill phase-level s fields if empty (subtitle)
  if (!phase.s || !phase.s.en) {
    phase.s = { en: tip.en.substring(0, 60), zh: tip.zh.substring(0, 60) };
  }

  phase.q.forEach((q, qi) => {
    totalQuestions++;
    
    // Fill t (teaching tip) fields if empty
    if (!q.t || !q.t.en || q.t.en.trim() === '') {
      if (!q.t) q.t = {};
      q.t.en = tip.en;
      q.t.zh = tip.zh;
      q.t.es = tip.en; // Use English for Spanish fallback
      filledTips++;
    }
    
    // Fill ex (per-option explanations) if missing
    if (!q.ex) {
      q.ex = { en: [], zh: [], es: [] };
    }
    
    const correctAnswers = Array.isArray(q.a) ? q.a : [q.a];
    const options = Array.isArray(q.o) ? q.o : (q.o?.en || []);
    
    // Generate explanations for each option
    const enEx = [];
    const zhEx = [];
    const esEx = [];
    
    // Get correct indices
    const correctSet = new Set();
    options.forEach((opt, i) => {
      if (correctAnswers.some(a => opt.includes(a) || a.includes(opt))) {
        correctSet.add(i);
      }
    });
    
    options.forEach((opt, i) => {
      if (correctSet.has(i)) {
        const cIdx = i % correctExplanations.en.length;
        enEx.push(correctExplanations.en[cIdx]);
        zhEx.push(correctExplanations.zh[cIdx]);
        esEx.push(correctExplanations.en[cIdx]);
      } else {
        const wIdx = i % wrongExplanations.en.length;
        enEx.push(wrongExplanations.en[wIdx]);
        zhEx.push(wrongExplanations.zh[wIdx]);
        esEx.push(wrongExplanations.en[wIdx]);
      }
    });
    
    // Only fill if the existing ex array is empty or incomplete
    if (!q.ex.en || q.ex.en.length === 0) {
      q.ex.en = enEx;
      q.ex.zh = zhEx;
      q.ex.es = esEx;
      filledEx++;
    }
  });
});

// Write updated data
const json = JSON.stringify(data, null, 2);
fs.writeFileSync(src, json, 'utf8');
fs.writeFileSync(dst, json, 'utf8');

console.log('Questions:', totalQuestions);
console.log('Filled tips:', filledTips);
console.log('Filled explanations:', filledEx);
