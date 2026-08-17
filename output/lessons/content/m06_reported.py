# -*- coding: utf-8 -*-
LESSON = {
    "id": "reported",
    "name": "Reported Speech",
    "zh": "间接引语",
    "icon": "🗣️",
    "accent": "#E03131",
    "desc": {"en": "Retell statements, questions, requests, and ideas accurately and naturally.", "zh": "准确自然地转述陈述、疑问、请求与想法。"},
    "objectives": [
        {"en": "Backshift tenses and change pronouns", "zh": "时态后退与代词转换"},
        {"en": "Report questions with correct word order", "zh": "用正确语序转述疑问句"},
        {"en": "Report commands with tell/ask + to-infinitive", "zh": "用 tell/ask + 不定式转述命令"},
        {"en": "Shift time and place words correctly", "zh": "正确转换时间与地点词"},
        {"en": "Choose the right reporting verb", "zh": "选择正确的转述动词"},
    ],
    "phases": [
        {
            "id": "reported_statements", "name": "Reported Statements", "zh": "转述陈述句",
            "concept": {"en": "When reporting, move tenses back one step (backshift) and change pronouns to match the speaker's perspective.", "zh": "转述时把时态后退一步（backshift），并把代词改为符合说话人视角的形式。"},
            "rules": [
                {"label": "时态后退", "en": "present → past: 'I am tired' → She said she was tired.", "zh": "现在 → 过去：她说她累了。"},
                {"label": "过去完成不变", "en": "past perfect stays: 'I had seen it' → She said she had seen it.", "zh": "过去完成时不变。"},
                {"label": "代词变化", "en": "I/we → he/she/they; my → his/her; you → I/we.", "zh": "I/we 变 he/she/they；my 变 his/her；you 变 I/we。"},
            ],
            "examples": [
                {"en": "He said, 'I love this city.' → He said he loved that city.", "zh": "他说他喜欢那座城市。"},
                {"en": "'We are leaving now,' she said. → She said they were leaving then.", "zh": "她说他们当时正要离开。"},
                {"en": "'I have finished,' Tom said. → Tom said he had finished.", "zh": "汤姆说他已完成。"},
            ],
            "mistakes": [
                {"en": "❌ She said she is tired (no backshift when reporting past) → was tired.", "zh": "❌ 转述过去的话要后退时态。"},
                {"en": "❌ Forgetting pronoun changes: 'I' in reported speech is not always I.", "zh": "❌ 代词要随视角变化。"},
            ],
        },
        {
            "id": "reported_questions", "name": "Reported Questions", "zh": "转述疑问句",
            "concept": {"en": "Reported questions use statement word order (no inversion) and no question mark. Yes/no questions use if or whether.", "zh": "转述疑问句用陈述语序（不倒装），句末不用问号。一般疑问句用 if 或 whether。"},
            "rules": [
                {"label": "一般疑问", "en": "if/whether + statement order: 'Are you ready?' → He asked if I was ready.", "zh": "if/whether + 陈述语序：他问我是否准备好了。"},
                {"label": "特殊疑问", "en": "wh-word + statement order: 'Where do you live?' → She asked where I lived.", "zh": "疑问词 + 陈述语序：她问我住在哪里。"},
                {"label": "无问号", "en": "Reported questions end with a period.", "zh": "转述疑问句以句号结尾。"},
            ],
            "examples": [
                {"en": "'Do you like tea?' → She asked if I liked tea.", "zh": "她问我是否喜欢茶。"},
                {"en": "'What time is it?' → He asked what time it was.", "zh": "他问几点了。"},
                {"en": "'Can you help me?' → They asked whether I could help them.", "zh": "他们问我能否帮忙。"},
            ],
            "mistakes": [
                {"en": "❌ He asked where did I live → no inversion: where I lived.", "zh": "❌ 转述疑问不倒装。"},
                {"en": "❌ She asked do you like tea → keep original words; use if + past.", "zh": "❌ 不要照抄原问句结构。"},
            ],
        },
        {
            "id": "reported_commands", "name": "Reported Commands", "zh": "转述命令",
            "concept": {"en": "Commands and requests become tell/ask + object + to-infinitive. Negative commands use not to.", "zh": "命令与请求变为 tell/ask + 宾语 + to 不定式。否定命令用 not to。"},
            "rules": [
                {"label": "肯定", "en": "'Sit down!' → He told me to sit down.", "zh": "他让我坐下。"},
                {"label": "否定", "en": "'Don't talk!' → She told us not to talk.", "zh": "她叫我们不要说话。"},
                {"label": "请求", "en": "ask for polite requests: 'Please wait' → He asked me to wait.", "zh": "礼貌请求用 ask。"},
            ],
            "examples": [
                {"en": "'Open the window,' she said. → She told me to open the window.", "zh": "她叫我把窗户打开。"},
                {"en": "'Don't be late!' → The teacher told us not to be late.", "zh": "老师叫我们不要迟到。"},
                {"en": "'Please help me,' he said. → He asked me to help him.", "zh": "他请我帮忙。"},
            ],
            "mistakes": [
                {"en": "❌ He said me to sit down → say takes no object; use told me.", "zh": "❌ say 后不加宾语，用 told me。"},
                {"en": "❌ She told to sit down → need object: told me/him/us to sit.", "zh": "❌ tell 后必须接宾语。"},
            ],
        },
        {
            "id": "reported_time", "name": "Time and Place Shifts", "zh": "时间与地点转换",
            "concept": {"en": "When reporting, shift time and place words: now → then, today → that day, here → there, tomorrow → the next day, yesterday → the day before.", "zh": "转述时转换时间地点词：now → then、today → that day、here → there、tomorrow → the next day、yesterday → the day before。"},
            "rules": [
                {"label": "时间词", "en": "now→then; today→that day; tomorrow→the next day; yesterday→the day before; ago→before.", "zh": "now→then；today→that day；tomorrow→the next day；yesterday→the day before；ago→before。"},
                {"label": "地点词", "en": "here→there; this→that; these→those.", "zh": "here→there；this→that；these→those。"},
            ],
            "examples": [
                {"en": "'I will come here tomorrow.' → He said he would come there the next day.", "zh": "他说他第二天会去那里。"},
                {"en": "'We met here yesterday.' → She said they had met there the day before.", "zh": "她说他们前一天在那里见过面。"},
                {"en": "'I am busy now.' → He said he was busy then.", "zh": "他说他当时很忙。"},
            ],
            "mistakes": [
                {"en": "❌ here stays here → shift to there.", "zh": "❌ here 要变 there。"},
                {"en": "❌ tomorrow stays tomorrow → the next day.", "zh": "❌ tomorrow 要变 the next day。"},
            ],
        },
        {
            "id": "reported_verbs", "name": "Reporting Verbs", "zh": "转述动词",
            "concept": {"en": "Choose the reporting verb for the meaning: say/tell for statements, explain, admit, deny, suggest, promise, agree.", "zh": "按语义选转述动词：say/tell 表陈述，explain 解释、admit 承认、deny 否认、suggest 建议、promise 承诺、agree 同意。"},
            "rules": [
                {"label": "say vs tell", "en": "say + (that) clause; tell + object + (that) clause: He said (that) he was tired. He told me (that) he was tired.", "zh": "say + 从句；tell + 宾语 + 从句。"},
                {"label": "suggest", "en": "suggest + -ing or that-clause: She suggested going out.", "zh": "suggest + -ing 或 that 从句：她建议出去。"},
                {"label": "deny/admit", "en": "deny/admit + -ing: He denied taking the money.", "zh": "deny/admit + -ing：他否认拿了钱。"},
            ],
            "examples": [
                {"en": "She explained that the shop was closed.", "zh": "她解释说商店关门了。"},
                {"en": "He admitted making a mistake.", "zh": "他承认犯了错误。"},
                {"en": "They promised to come early.", "zh": "他们答应早点来。"},
            ],
            "mistakes": [
                {"en": "❌ He said me... → say takes no object.", "zh": "❌ say 后面不能直接接宾语。"},
                {"en": "❌ She suggested me to go → suggest + going / that I go.", "zh": "❌ suggest 后不用 me to。"},
            ],
        },
        {
            "id": "reported_tense", "name": "Tense Backshift Rules", "zh": "时态后退规则",
            "concept": {"en": "Backshift is required after a past reporting verb, but optional when the reported fact is still true: 'I am hungry' → She said she was hungry (or is hungry if still true).", "zh": "转述动词是过去时时态通常后退；若事实仍然成立，可保留现在时。"},
            "rules": [
                {"label": "必然后退", "en": "past reporting verb + past time: She said she was tired.", "zh": "转述动词过去时 + 过去语境：必须后退。"},
                {"label": "可保留", "en": "still-true facts: He said the earth is round.", "zh": "仍然成立的事实：他说地球是圆的。"},
                {"label": "不变", "en": "past perfect and would never backshift further.", "zh": "过去完成时和 would 不再后退。"},
            ],
            "examples": [
                {"en": "She said she worked in a bank. (backshift)", "zh": "她说她在银行工作。"},
                {"en": "He said water boils at 100°C. (still true — present kept)", "zh": "他说水在100°C沸腾。（仍成立，保留现在时）"},
                {"en": "They said they had already eaten.", "zh": "他们说他们已经吃过了。"},
            ],
            "mistakes": [
                {"en": "❌ She said she has been to Paris (no time reference) → had been when reporting past.", "zh": "❌ 转述过去时用过去完成。"},
                {"en": "❌ Backshifting universal truths is awkward: keep the present for facts.", "zh": "❌ 普遍真理可保留现在时。"},
            ],
        },
        {
            "id": "reported_embedded", "name": "Embedded Questions", "zh": "嵌入式疑问句",
            "concept": {"en": "Polite questions embed a question inside a phrase: Do you know where...? Can you tell me when...? The embedded part keeps statement word order.", "zh": "礼貌问句把疑问嵌入短语：Do you know where...? Can you tell me when...? 嵌入部分用陈述语序。"},
            "rules": [
                {"label": "结构", "en": "Do you know / Can you tell me + wh-word + statement order.", "zh": "Do you know / Can you tell me + 疑问词 + 陈述语序。"},
                {"label": "无倒装", "en": "Do you know where the station is? (not where is the station)", "zh": "不倒装：你知道车站在哪里吗？"},
            ],
            "examples": [
                {"en": "Do you know where the station is?", "zh": "你知道车站在哪里吗？"},
                {"en": "Can you tell me when the bus leaves?", "zh": "你能告诉我公交车什么时候开吗？"},
                {"en": "I wonder if she is coming.", "zh": "我想知道她是否要来。"},
            ],
            "mistakes": [
                {"en": "❌ Do you know where is the station? → statement order: where the station is.", "zh": "❌ 嵌入疑问不倒装。"},
                {"en": "❌ Can you tell me what time does it start? → what time it starts.", "zh": "❌ 去掉助动词倒装。"},
            ],
        },
        {
            "id": "reported_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Convert direct speech to reported speech in four steps: choose the reporting verb, add the object if needed, backshift the tense, shift pronouns and time/place words.", "zh": "直接引语转间接引语四步：选转述动词、按需加宾语、时态后退、转换代词与时间地点词。"},
            "rules": [
                {"label": "四步法", "en": "1) reporting verb 2) object (for tell/ask) 3) backshift 4) shift pronouns + time/place.", "zh": "1) 转述动词 2) 宾语（tell/ask）3) 时态后退 4) 代词与时间地点词转换。"},
                {"label": "检查", "en": "No inversion in reported questions; no question mark; no double that.", "zh": "转述疑问不倒装、不用问号、不重复 that。"},
            ],
            "examples": [
                {"en": "'I will call you tomorrow,' she said. → She said she would call me the next day.", "zh": "她说她第二天会给我打电话。"},
                {"en": "'Where did you go?' → He asked where I had gone.", "zh": "他问我去了哪里。"},
                {"en": "'Don't touch that!' → She told me not to touch it.", "zh": "她叫我不许碰那个。"},
            ],
            "mistakes": [
                {"en": "❌ She said she will call me tomorrow (no backshift) → would...the next day.", "zh": "❌ 时态与时间词都要转。"},
                {"en": "❌ He asked me that where I went → no that before wh-words.", "zh": "❌ wh- 疑问前不加 that。"},
            ],
        },
    ],
}
