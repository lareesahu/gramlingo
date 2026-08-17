# -*- coding: utf-8 -*-
LESSON = {
    "id": "advanced",
    "name": "Advanced Expressions",
    "zh": "高级表达",
    "icon": "🚀",
    "accent": "#A61E4D",
    "desc": {"en": "Use emphasis, inversion, register, compression, and idiomatic grammar in context.", "zh": "在语境中运用强调、倒装、语域、省略与地道语法。"},
    "objectives": [
        {"en": "Add emphasis with fronting and emphatic auxiliaries", "zh": "用前置与强调助动词增加强调"},
        {"en": "Use inversion after negative adverbs", "zh": "否定副词后用倒装"},
        {"en": "Use substitution and ellipsis to avoid repetition", "zh": "用替代与省略避免重复"},
        {"en": "Choose formal vs informal grammar", "zh": "区分正式与非正式语法"},
        {"en": "Use nominalisation and hedging for academic style", "zh": "用名词化与模糊限制语实现学术风格"},
    ],
    "phases": [
        {
            "id": "advanced_emphasis", "name": "Emphasis", "zh": "强调",
            "concept": {"en": "Emphasize with: fronting (move key words to the front), emphatic do (do/did + base), and cleft structures.", "zh": "强调手法：前置（把关键词移到句首）、强调 do（do/did + 原形）、强调句。"},
            "rules": [
                {"label": "前置", "en": "Never have I seen such a view. / That I know for sure.", "zh": "前置：我从未见过这样的景色。/ 这个我确定知道。"},
                {"label": "强调 do", "en": "I do like your idea. / She did call you.", "zh": "强调 do：我确实喜欢你的主意。/ 她确实给你打了电话。"},
                {"label": "强调句", "en": "It was the price that surprised me.", "zh": "是价格让我惊讶。"},
            ],
            "examples": [
                {"en": "What really matters is your health.", "zh": "真正重要的是你的健康。"},
                {"en": "He did finish the report on time.", "zh": "他确实按时完成了报告。"},
                {"en": "Never in my life have I felt so happy.", "zh": "我一生中从未如此快乐。"},
            ],
            "mistakes": [
                {"en": "❌ Do I like your idea (question) vs I do like it (emphasis).", "zh": "❌ 注意语序：强调 do 不放句首。"},
                {"en": "❌ Overusing emphasis weakens writing — use it sparingly.", "zh": "❌ 强调要节制使用。"},
            ],
        },
        {
            "id": "advanced_inversion", "name": "Inversion", "zh": "倒装",
            "concept": {"en": "After negative or restrictive adverbs (never, rarely, hardly, not only, no sooner), the subject and auxiliary invert: Never have I... Conditionals can drop if with inversion: Had I known...", "zh": "否定或限制性副词（never、rarely、hardly、not only、no sooner）后主谓倒装：Never have I...；条件句可省略 if 用倒装：Had I known..."},
            "rules": [
                {"label": "否定副词", "en": "Never have I seen that. / Rarely does she complain.", "zh": "否定副词倒装：我从未见过。/ 她很少抱怨。"},
                {"label": "虚拟倒装", "en": "Had I known, I would have come. (= If I had known)", "zh": "虚拟倒装：要是我知道，我就来了。"},
                {"label": "Not only...but", "en": "Not only did he apologize, but he also offered help.", "zh": "Not only 倒装：他不仅道歉，还主动帮忙。"},
            ],
            "examples": [
                {"en": "Hardly had we left when it started to rain.", "zh": "我们刚离开就开始下雨了。"},
                {"en": "Never before had she felt so confident.", "zh": "她从未如此自信。"},
                {"en": "Should you need help, please call me.", "zh": "如果你需要帮助，请给我打电话。"},
            ],
            "mistakes": [
                {"en": "❌ Never I have seen → inversion: Never have I seen.", "zh": "❌ 否定副词后要倒装。"},
                {"en": "❌ If I had known... would have come → with inversion: Had I known... (no if).", "zh": "❌ 倒装时去掉 if。"},
            ],
        },
        {
            "id": "advanced_substitution", "name": "Substitution and Ellipsis", "zh": "替代与省略",
            "concept": {"en": "Avoid repetition: so/not replace clauses (I think so), do so replaces a verb phrase, ellipsis leaves shared words out in the second half.", "zh": "避免重复：so/not 替代从句（I think so）、do so 替代动词短语、后半句省略共有词。"},
            "rules": [
                {"label": "so/not", "en": "Will it rain? I hope not. / I think so.", "zh": "so/not 替代：会下雨吗？我希望不会。/ 我想是的。"},
                {"label": "do so", "en": "She said she would call, and she did so.", "zh": "do so 替代：她说会打电话，她也确实打了。"},
                {"label": "省略", "en": "I like tea and she (likes) coffee.", "zh": "省略：我喜欢茶，她（喜欢）咖啡。"},
            ],
            "examples": [
                {"en": "Are you coming? I believe so.", "zh": "你来吗？我想是的。"},
                {"en": "He promised to help, and he did.", "zh": "他答应帮忙，也确实帮了。"},
                {"en": "She sings better than anyone else (sings).", "zh": "她比任何人都唱得好。"},
            ],
            "mistakes": [
                {"en": "❌ I think yes (non-standard) → I think so.", "zh": "❌ 标准表达是 I think so。"},
                {"en": "❌ Over-ellipsis can confuse — keep enough context.", "zh": "❌ 省略过多会造成歧义。"},
            ],
        },
        {
            "id": "advanced_register", "name": "Register", "zh": "语域",
            "concept": {"en": "Formal writing prefers full forms, passive voice, and precise connectors; informal speech uses contractions, phrasal verbs, and simple connectors.", "zh": "正式写作用完整形式、被动语态和精确连接词；非正式口语用缩略形式、短语动词和简单连接词。"},
            "rules": [
                {"label": "正式", "en": "The meeting has been postponed due to unforeseen circumstances.", "zh": "正式：会议因不可预见的情况被推迟。"},
                {"label": "非正式", "en": "The meeting is put off because something came up.", "zh": "非正式：会议推迟了，因为出了点事。"},
                {"label": "选择", "en": "Match the register to the audience: essays and emails to bosses = formal.", "zh": "按受众选择：论文和给上司的邮件用正式语。"},
            ],
            "examples": [
                {"en": "We regret to inform you that... (formal)", "zh": "我们遗憾地通知您……（正式）"},
                {"en": "Sorry, but... (informal)", "zh": "抱歉，不过……（非正式）"},
                {"en": "The experiment was conducted over three months. (formal)", "zh": "实验历时三个月。（正式）"},
            ],
            "mistakes": [
                {"en": "❌ Using slang in academic writing weakens it.", "zh": "❌ 学术写作慎用俚语。"},
                {"en": "❌ Mixing registers in one document confuses readers.", "zh": "❌ 一篇文章内语域要统一。"},
            ],
        },
        {
            "id": "advanced_cohesion", "name": "Cohesion", "zh": "衔接",
            "concept": {"en": "Cohesion ties sentences together: reference (it, they, this), substitution (so, one), discourse markers (however, therefore, in addition).", "zh": "衔接手段把句子串起来：指代（it、they、this）、替代（so、one）、话语标记（however、therefore、in addition）。"},
            "rules": [
                {"label": "指代", "en": "The plan was good. However, it had one problem.", "zh": "指代：计划很好，但它有一个问题。"},
                {"label": "替代", "en": "I wanted the blue one, not the red one.", "zh": "替代：我要蓝色的那个，不是红色的。"},
                {"label": "话语标记", "en": "In addition, the cost is low. / Therefore, we agreed.", "zh": "标记：此外，成本很低。/ 因此我们同意了。"},
            ],
            "examples": [
                {"en": "The team trained hard. As a result, they won.", "zh": "团队训练刻苦，结果他们赢了。"},
                {"en": "She offered a plan, and he accepted it.", "zh": "她提出了一个计划，他接受了。"},
                {"en": "First, prepare the tools. Then, start the work.", "zh": "首先准备工具，然后开始工作。"},
            ],
            "mistakes": [
                {"en": "❌ Unclear it: The dog chased the cat. It was hungry. (which one?)", "zh": "❌ 指代不明会造成歧义。"},
                {"en": "❌ Overusing connectors makes writing mechanical.", "zh": "❌ 连接词过多会显得机械。"},
            ],
        },
        {
            "id": "advanced_nominalisation", "name": "Nominalisation", "zh": "名词化",
            "concept": {"en": "Turn verbs and adjectives into nouns: decide → decision, improve → improvement, important → importance. Common in academic and formal writing.", "zh": "把动词和形容词变成名词：decide → decision、improve → improvement、important → importance。常见于学术与正式写作。"},
            "rules": [
                {"label": "转换", "en": "verb → noun: We decided → Our decision...", "zh": "动词转名词：我们决定 → 我们的决定……"},
                {"label": "用途", "en": "compresses ideas and sounds formal: The improvement of service...", "zh": "压缩表达、更正式：服务的改善……"},
            ],
            "examples": [
                {"en": "Their arrival surprised everyone.", "zh": "他们的到来让所有人惊讶。"},
                {"en": "The development of the city was rapid.", "zh": "城市的发展非常迅速。"},
                {"en": "Her success came from hard work.", "zh": "她的成功来自努力。"},
            ],
            "mistakes": [
                {"en": "❌ Over-nominalisation makes sentences heavy: use verbs when clarity matters.", "zh": "❌ 名词化过度会让句子笨重。"},
                {"en": "❌ The decision was decided → redundant: The decision was made.", "zh": "❌ 避免同源重复。"},
            ],
        },
        {
            "id": "advanced_hedging", "name": "Hedging and Stance", "zh": "模糊限制与立场",
            "concept": {"en": "Hedging softens claims: seem, appear, tend to, it is likely that, may/might, arguably. Stance shows your position: clearly, surprisingly, importantly.", "zh": "模糊限制语软化断言：seem、appear、tend to、it is likely that、may/might、arguably。立场词表明态度：clearly、surprisingly、importantly。"},
            "rules": [
                {"label": "模糊限制", "en": "It is likely that prices will rise.", "zh": "价格可能会上涨。"},
                {"label": "委婉", "en": "This seems to be a good solution.", "zh": "这似乎是一个好方案。"},
                {"label": "立场", "en": "Clearly, more research is needed.", "zh": "显然，还需要更多研究。"},
            ],
            "examples": [
                {"en": "The results appear to support the theory.", "zh": "结果似乎支持这一理论。"},
                {"en": "There may be some risks involved.", "zh": "可能涉及一些风险。"},
                {"en": "Interestingly, the opposite happened.", "zh": "有趣的是，结果恰恰相反。"},
            ],
            "mistakes": [
                {"en": "❌ Hedging too much sounds weak: use strong verbs for real certainty.", "zh": "❌ 过度模糊会显得缺乏自信。"},
                {"en": "❌ Unhedged absolute claims in academic writing: 'This proves...' → 'This suggests...'.", "zh": "❌ 学术写作中绝对断言要软化。"},
            ],
        },
        {
            "id": "advanced_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Write with advanced grammar in context: add emphasis where needed, invert for style, nominalise for formality, hedge for accuracy, and keep cohesion.", "zh": "在语境中使用高级语法：需要强调处强调、为风格倒装、为正式名词化、为准确模糊化，并保持衔接。"},
            "rules": [
                {"label": "风格匹配", "en": "Match advanced structures to the text type: essay → nominalisation + hedging; speech → emphasis + fronting.", "zh": "高级结构要匹配文体：论文用名词化+模糊限制；演讲用强调+前置。"},
                {"label": "适度", "en": "Advanced grammar adds power only when used naturally.", "zh": "高级语法只有用得自然才有力量。"},
            ],
            "examples": [
                {"en": "Never have I seen such dedication. (inversion for emphasis)", "zh": "我从未见过如此投入。（倒装强调）"},
                {"en": "The company's growth was remarkable. (nominalisation)", "zh": "公司的增长非常显著。（名词化）"},
                {"en": "It could be argued that the benefits outweigh the costs. (hedging)", "zh": "可以说利大于弊。（模糊限制）"},
            ],
            "mistakes": [
                {"en": "❌ Using inversion or cleft sentences in every sentence — too theatrical.", "zh": "❌ 每句都倒装会太戏剧化。"},
                {"en": "❌ Formal words in spoken chat sound unnatural — know your audience.", "zh": "❌ 口语中用太正式的词会不自然。"},
            ],
        },
    ],
}
