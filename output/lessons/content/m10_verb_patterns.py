# -*- coding: utf-8 -*-
LESSON = {
    "id": "verb_patterns",
    "name": "Verb Patterns",
    "zh": "动词搭配",
    "icon": "🧩",
    "accent": "#5C940D",
    "desc": {"en": "Control gerunds, infinitives, causatives, and meaning-changing verb patterns.", "zh": "掌握动名词、不定式、使役结构和会改变含义的动词搭配。"},
    "objectives": [
        {"en": "Use gerunds after certain verbs and prepositions", "zh": "在特定动词和介词后使用动名词"},
        {"en": "Use infinitives after other verbs", "zh": "在其他动词后使用不定式"},
        {"en": "Know verbs that change meaning with form", "zh": "了解形式改变含义的动词"},
        {"en": "Use causative patterns: make, let, have, get", "zh": "使用 make、let、have、get 使役结构"},
    ],
    "phases": [
        {
            "id": "verb_patterns_gerunds", "name": "Gerunds", "zh": "动名词",
            "concept": {"en": "Some verbs are always followed by the -ing form: enjoy, finish, mind, avoid, suggest, keep, practice.", "zh": "一些动词后永远接 -ing：enjoy、finish、mind、avoid、suggest、keep、practice。"},
            "rules": [
                {"label": "常用动词", "en": "enjoy, finish, mind, avoid, suggest, keep, practice, consider + -ing", "zh": "enjoy、finish、mind、avoid、suggest、keep、practice、consider + -ing"},
                {"label": "介词后", "en": "after any preposition: interested in learning, good at cooking", "zh": "任何介词后：interested in learning（对学习感兴趣）、good at cooking（擅长做饭）"},
            ],
            "examples": [
                {"en": "She enjoys reading before bed.", "zh": "她喜欢睡前读书。"},
                {"en": "Would you mind closing the window?", "zh": "你介意关上窗户吗？"},
                {"en": "He kept asking questions.", "zh": "他不停地问问题。"},
            ],
            "mistakes": [
                {"en": "❌ She enjoys to read → enjoy + -ing: enjoys reading.", "zh": "❌ enjoy 后接动名词。"},
                {"en": "❌ interested to learn → interested in learning.", "zh": "❌ 介词后接 -ing。"},
            ],
        },
        {
            "id": "verb_patterns_infinitives", "name": "Infinitives", "zh": "不定式",
            "concept": {"en": "Some verbs are always followed by to + base form: want, hope, decide, plan, learn, promise, agree, offer.", "zh": "一些动词后永远接 to + 原形：want、hope、decide、plan、learn、promise、agree、offer。"},
            "rules": [
                {"label": "常用动词", "en": "want, hope, decide, plan, learn, promise, agree, offer + to + base", "zh": "want、hope、decide、plan、learn、promise、agree、offer + to + 原形"},
                {"label": "疑问词+to", "en": "know/learn/decide + how/what/where + to: I know how to swim.", "zh": "know/learn/decide + how/what/where + to：我知道怎么游泳。"},
            ],
            "examples": [
                {"en": "I want to learn Spanish.", "zh": "我想学西班牙语。"},
                {"en": "She decided to stay home.", "zh": "她决定待在家里。"},
                {"en": "They promised to help us.", "zh": "他们答应帮助我们。"},
            ],
            "mistakes": [
                {"en": "❌ I want learning → want + to: want to learn.", "zh": "❌ want 后接不定式。"},
                {"en": "❌ She hopes passing → hopes to pass.", "zh": "❌ hope 后接 to + 原形。"},
            ],
        },
        {
            "id": "verb_patterns_both", "name": "Gerund vs Infinitive", "zh": "动名词与不定式",
            "concept": {"en": "Some verbs change meaning with the form: stop to smoke (stop in order to) vs stop smoking (quit); remember to do (future duty) vs remember doing (past memory); try to do (attempt) vs try doing (experiment).", "zh": "一些动词接不同形式含义不同：stop to smoke 停下来去抽烟 vs stop smoking 戒烟；remember to do 记得要做 vs remember doing 记得做过；try to do 尝试 vs try doing 试试看。"},
            "rules": [
                {"label": "stop", "en": "stop + -ing = quit; stop + to + base = pause in order to.", "zh": "stop + -ing 停止；stop + to 停下来去做。"},
                {"label": "remember/forget", "en": "+ to = duty; + -ing = memory.", "zh": "接 to 表待办；接 -ing 表记忆。"},
                {"label": "try", "en": "+ to = attempt; + -ing = experiment.", "zh": "接 to 表努力尝试；接 -ing 表试验方法。"},
            ],
            "examples": [
                {"en": "I stopped smoking last year.", "zh": "我去年戒烟了。"},
                {"en": "On the way home, he stopped to buy milk.", "zh": "回家路上，他停下来买牛奶。"},
                {"en": "Remember to lock the door. / I remember locking the door.", "zh": "记得锁门。/ 我记得锁过门。"},
            ],
            "mistakes": [
                {"en": "❌ I stopped to smoke (wrong context) → quitting means stop smoking.", "zh": "❌ 戒烟要说 stop smoking。"},
                {"en": "❌ Remember locking = past memory; if you mean future duty, use to lock.", "zh": "❌ 含义随形式变化，务必分清。"},
            ],
        },
        {
            "id": "verb_patterns_causatives", "name": "Causatives", "zh": "使役结构",
            "concept": {"en": "make + object + base (force); let + object + base (allow); have + object + base (arrange); get + object + to + base (persuade).", "zh": "make + 宾语 + 原形（迫使）；let + 宾语 + 原形（允许）；have + 宾语 + 原形（安排）；get + 宾语 + to + 原形（说服）。"},
            "rules": [
                {"label": "make", "en": "make + object + base: The joke made me laugh.", "zh": "make + 宾语 + 原形：笑话让我笑了。"},
                {"label": "let", "en": "let + object + base: My parents let me go.", "zh": "let + 宾语 + 原形：父母让我去。"},
                {"label": "have", "en": "have + object + base: I had him fix the car.", "zh": "have + 宾语 + 原形：我让他修车。"},
                {"label": "get", "en": "get + object + to + base: I got her to help.", "zh": "get + 宾语 + to + 原形：我说服她帮忙。"},
            ],
            "examples": [
                {"en": "The film made me cry.", "zh": "这部电影让我哭了。"},
                {"en": "She let her son play outside.", "zh": "她让儿子在外面玩。"},
                {"en": "We got the waiter to bring more water.", "zh": "我们让服务员多拿些水。"},
            ],
            "mistakes": [
                {"en": "❌ make someone to do → make + base, no to.", "zh": "❌ make 后接原形，不加 to。"},
                {"en": "❌ get someone do → get + to + base.", "zh": "❌ get 后要加 to。"},
            ],
        },
        {
            "id": "verb_patterns_preposition", "name": "Preposition + Gerund", "zh": "介词 + 动名词",
            "concept": {"en": "After every preposition, use the -ing form: interested in, good at, tired of, think about, look forward to, instead of.", "zh": "介词后一律用 -ing：interested in、good at、tired of、think about、look forward to、instead of。"},
            "rules": [
                {"label": "介词+ing", "en": "in/at/of/about/for + -ing: She is good at drawing.", "zh": "in/at/of/about/for + -ing：她擅长画画。"},
                {"label": "look forward to", "en": "to here is a preposition: I look forward to hearing from you.", "zh": "look forward to 中的 to 是介词：期待你的来信。"},
            ],
            "examples": [
                {"en": "He apologized for being late.", "zh": "他为迟到道歉。"},
                {"en": "I'm thinking about moving to Hangzhou.", "zh": "我在考虑搬到杭州。"},
                {"en": "She left without saying goodbye.", "zh": "她没说再见就离开了。"},
            ],
            "mistakes": [
                {"en": "❌ good at draw → good at drawing.", "zh": "❌ 介词后接 -ing。"},
                {"en": "❌ look forward to hear → looking forward to hearing.", "zh": "❌ to 是介词，后接 -ing。"},
            ],
        },
        {
            "id": "verb_patterns_adj", "name": "Adjective Patterns", "zh": "形容词搭配",
            "concept": {"en": "It is + adjective + to + base (It is easy to learn); subject + be + adjective + to + base (I am happy to help).", "zh": "It is + 形容词 + to + 原形（学起来很容易）；主语 + be + 形容词 + to + 原形（我很乐意帮忙）。"},
            "rules": [
                {"label": "It is + adj + to", "en": "It is important to sleep well.", "zh": "睡好觉很重要。"},
                {"label": "主语 + be + adj + to", "en": "She was surprised to see us.", "zh": "看到我们她很惊讶。"},
            ],
            "examples": [
                {"en": "It is difficult to learn a new language.", "zh": "学一门新语言很难。"},
                {"en": "We are ready to start.", "zh": "我们准备好开始了。"},
                {"en": "He was afraid to speak in public.", "zh": "他害怕当众讲话。"},
            ],
            "mistakes": [
                {"en": "❌ It is important sleep → to sleep.", "zh": "❌ 形容词后接 to + 原形。"},
                {"en": "❌ I am happy helping → with person adjectives, prefer to + base: happy to help.", "zh": "❌ happy to help 更常见。"},
            ],
        },
        {
            "id": "verb_patterns_contrast", "name": "Pattern Contrast", "zh": "搭配对比",
            "concept": {"en": "The verb decides the pattern — memorize the verb + form pairs. Group by pattern: verbs + -ing, verbs + to, verbs + both, verbs + object + form.", "zh": "动词决定搭配形式——记住【动词 + 形式】的组合，按模式分组记忆：接 -ing、接 to、两者皆可、接宾语 + 形式。"},
            "rules": [
                {"label": "接 -ing", "en": "enjoy, mind, avoid, suggest, keep, finish", "zh": "enjoy、mind、avoid、suggest、keep、finish"},
                {"label": "接 to", "en": "want, hope, decide, plan, promise, agree", "zh": "want、hope、decide、plan、promise、agree"},
                {"label": "宾语+原形", "en": "make, let, have", "zh": "make、let、have 接宾语 + 原形"},
                {"label": "宾语+to", "en": "get, ask, tell, want", "zh": "get、ask、tell、want 接宾语 + to"},
            ],
            "examples": [
                {"en": "She suggested taking a break.", "zh": "她建议休息一下。"},
                {"en": "He promised to call me.", "zh": "他答应给我打电话。"},
                {"en": "They asked us to wait.", "zh": "他们让我们等。"},
            ],
            "mistakes": [
                {"en": "❌ suggest me to go → suggest going / suggest that I go.", "zh": "❌ suggest 不接宾语 + to。"},
                {"en": "❌ want that he comes → want him to come.", "zh": "❌ want 接宾语 + to。"},
            ],
        },
        {
            "id": "verb_patterns_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "When writing, check every verb's pattern: does it take -ing, to + base, or object + form? Fix mismatches.", "zh": "写作时逐一检查动词搭配：接 -ing、to + 原形，还是宾语 + 形式？修正不匹配之处。"},
            "rules": [
                {"label": "查动词", "en": "For each verb, recall its pattern group before writing the next word.", "zh": "写每个动词前回忆它的搭配分组。"},
                {"label": "查介词", "en": "After any preposition, the next verb must be -ing.", "zh": "介词后的动词必须用 -ing。"},
            ],
            "examples": [
                {"en": "❌ I enjoy to cook → I enjoy cooking.", "zh": "❌ enjoy 接 -ing。"},
                {"en": "❌ She avoided to answer → She avoided answering.", "zh": "❌ avoid 接 -ing。"},
                {"en": "✔ I decided to start learning Chinese.", "zh": "✔ 我决定开始学中文。（decide + to; start + -ing）"},
            ],
            "mistakes": [
                {"en": "❌ He wants that I help → He wants me to help.", "zh": "❌ want 接宾语 + to。"},
                {"en": "❌ They made me to wait → They made me wait.", "zh": "❌ make 接原形，不加 to。"},
            ],
        },
    ],
}
