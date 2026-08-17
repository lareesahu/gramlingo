# -*- coding: utf-8 -*-
LESSON = {
    "id": "passive",
    "name": "Passive Voice",
    "zh": "被动语态",
    "icon": "🔄",
    "accent": "#0B7285",
    "desc": {"en": "Shift focus between the doer, the action, and the result across timelines.", "zh": "在施动者、动作与结果之间转换焦点。"},
    "objectives": [
        {"en": "Recognize passive vs active voice", "zh": "识别被动与主动语态"},
        {"en": "Form the passive with be + past participle", "zh": "用 be + 过去分词构成被动"},
        {"en": "Decide when to include or omit the agent", "zh": "判断何时保留或省略施动者"},
        {"en": "Use passive across tenses and with modals", "zh": "在不同时态和情态动词中使用被动"},
        {"en": "Use causative and impersonal passive forms", "zh": "使用使役与无人称被动结构"},
    ],
    "phases": [
        {
            "id": "passive_recognition", "name": "Recognize Passive", "zh": "识别被动语态",
            "concept": {"en": "Active: the subject does the action. Passive: the subject receives the action. Passive = be + past participle.", "zh": "主动：主语执行动作。被动：主语接受动作。被动 = be + 过去分词。"},
            "rules": [
                {"label": "主动", "en": "subject + verb + object: The chef cooks the meal.", "zh": "主语 + 动词 + 宾语：厨师做饭。"},
                {"label": "被动", "en": "subject + be + past participle (+ by agent): The meal is cooked by the chef.", "zh": "主语 + be + 过去分词（+ by 施动者）：饭由厨师做。"},
                {"label": "检测", "en": "Can you ask 'who does it?' If the subject receives the action → passive.", "zh": "主语是接受动作的一方→被动。"},
            ],
            "examples": [
                {"en": "Active: The dog chased the cat.", "zh": "主动：狗追猫。"},
                {"en": "Passive: The cat was chased by the dog.", "zh": "被动：猫被狗追。"},
                {"en": "The window was broken last night.", "zh": "窗户昨晚被打破了。"},
            ],
            "mistakes": [
                {"en": "❌ The window was broken by someone — often better without by: The window was broken.", "zh": "❌ 不知道施动者时省略 by 短语。"},
                {"en": "❌ Confusing was broken (passive) with broke (active).", "zh": "❌ 分清主动与被动形式。"},
            ],
        },
        {
            "id": "passive_formation", "name": "Form the Passive", "zh": "被动语态的构成",
            "concept": {"en": "Move the object to subject position, change the verb to be + past participle, and optionally add by + original subject.", "zh": "把宾语移到主语位置，动词改为 be + 过去分词，可加 by + 原主语。"},
            "rules": [
                {"label": "转换步骤", "en": "object → subject; verb → be (same tense) + pp; subject → by + subject.", "zh": "宾语变主语；动词变 be（保持时态）+ 过去分词；原主语变 by 短语。"},
                {"label": "时态保持", "en": "The company builds phones. → Phones are built (by the company).", "zh": "时态不变：公司生产手机。→ 手机被（公司）生产。"},
            ],
            "examples": [
                {"en": "Active: They painted the house. → Passive: The house was painted.", "zh": "他们粉刷了房子。→ 房子被粉刷了。"},
                {"en": "Active: She writes many emails. → Passive: Many emails are written.", "zh": "她写很多邮件。→ 很多邮件被写。"},
                {"en": "Active: We will finish the project. → Passive: The project will be finished.", "zh": "我们将完成项目。→ 项目将被完成。"},
            ],
            "mistakes": [
                {"en": "❌ The house was paint → past participle: painted.", "zh": "❌ 用过去分词 painted。"},
                {"en": "❌ The house painted (no be) → need be: was painted.", "zh": "❌ 被动必须带 be。"},
            ],
        },
        {
            "id": "passive_agent", "name": "With/Without Agent", "zh": "施动者的取舍",
            "concept": {"en": "Include by + agent when it is important or surprising; omit it when it is unknown, obvious, or unimportant.", "zh": "施动者重要或出乎意料时保留 by 短语；不知道、显而易见或不重要时省略。"},
            "rules": [
                {"label": "保留 by", "en": "important/surprising: This cake was baked by my grandmother.", "zh": "重要/意外：这个蛋糕是我奶奶烤的。"},
                {"label": "省略 by", "en": "unknown/obvious: The road was repaired. (by someone)", "zh": "未知/明显：这条路被修好了。"},
                {"label": "科学/报道", "en": "Passive without agent is common in science and news: The results were published.", "zh": "科学与新闻常用无施动者被动：结果被发表了。"},
            ],
            "examples": [
                {"en": "The song was written by a famous composer.", "zh": "这首歌是一位著名作曲家写的。"},
                {"en": "English is spoken in many countries.", "zh": "许多国家说英语。"},
                {"en": "The letters were delivered this morning.", "zh": "信件今天早上被送达。"},
            ],
            "mistakes": [
                {"en": "❌ The window was broken by the wind by the storm → one agent only.", "zh": "❌ 施动者只留一个。"},
                {"en": "❌ Overusing by people → usually dropped.", "zh": "❌ by people 通常省略。"},
            ],
        },
        {
            "id": "passive_tenses", "name": "Passive Across Tenses", "zh": "被动语态与时态",
            "concept": {"en": "Change be to the right tense: is built (present), was built (past), will be built (future), has been built (perfect).", "zh": "把 be 换成相应时态：is built（现在）、was built（过去）、will be built（将来）、has been built（完成）。"},
            "rules": [
                {"label": "现在", "en": "am/is/are + pp: Rice is grown here.", "zh": "am/is/are + pp：这里种水稻。"},
                {"label": "过去", "en": "was/were + pp: The bridge was built in 1990.", "zh": "was/were + pp：这座桥建于1990年。"},
                {"label": "将来/完成", "en": "will be + pp; have/has been + pp: The report will be finished. It has been checked.", "zh": "will be + pp；have/has been + pp：报告将完成。已被检查。"},
            ],
            "examples": [
                {"en": "The room is cleaned every day.", "zh": "房间每天被打扫。"},
                {"en": "The film was shot in Tokyo.", "zh": "这部电影是在东京拍摄的。"},
                {"en": "The tickets have been sold out.", "zh": "票已售罄。"},
            ],
            "mistakes": [
                {"en": "❌ The bridge was build → past participle: built.", "zh": "❌ 用过去分词 built。"},
                {"en": "❌ has been broke → has been broken.", "zh": "❌ 完成被动也用过去分词。"},
            ],
        },
        {
            "id": "passive_modals", "name": "Passive with Modals", "zh": "情态动词+被动",
            "concept": {"en": "modal + be + past participle: can be done, must be done, should be done.", "zh": "情态动词 + be + 过去分词：can be done、must be done、should be done。"},
            "rules": [
                {"label": "结构", "en": "modal + be + pp: The work must be finished today.", "zh": "情态动词 + be + pp：工作今天必须完成。"},
                {"label": "完成式", "en": "modal + have been + pp: The letter should have been sent.", "zh": "情态动词 + have been + pp：信本应已寄出。"},
            ],
            "examples": [
                {"en": "Rules can be changed.", "zh": "规则可以改变。"},
                {"en": "Your homework must be handed in on time.", "zh": "你的作业必须按时上交。"},
                {"en": "This medicine should be taken after meals.", "zh": "这种药应在饭后服用。"},
            ],
            "mistakes": [
                {"en": "❌ must done → must be done.", "zh": "❌ 情态动词被动要加 be。"},
                {"en": "❌ can be do → past participle: done.", "zh": "❌ 用过去分词。"},
            ],
        },
        {
            "id": "passive_causative", "name": "Causative Forms", "zh": "使役结构",
            "concept": {"en": "have/get + object + past participle = arrange for someone to do something: have my hair cut, get the car fixed.", "zh": "have/get + 宾语 + 过去分词 = 安排别人做事：have my hair cut（理发）、get the car fixed（修车）。"},
            "rules": [
                {"label": "have + obj + pp", "en": "I had my phone repaired.", "zh": "我请人修了手机。"},
                {"label": "get + obj + pp", "en": "She got the report translated.", "zh": "她请人翻译了报告。"},
                {"label": "含义", "en": "You arrange it; someone else does it.", "zh": "你安排，别人执行。"},
            ],
            "examples": [
                {"en": "He had his car washed yesterday.", "zh": "他昨天洗了车（请人洗）。"},
                {"en": "We are getting the house painted.", "zh": "我们正在请人粉刷房子。"},
                {"en": "I need to have my eyes checked.", "zh": "我需要检查眼睛。"},
            ],
            "mistakes": [
                {"en": "❌ I had my hair cutted → irregular pp: cut.", "zh": "❌ cut 的过去分词还是 cut。"},
                {"en": "❌ I had my car wash → past participle: washed.", "zh": "❌ 用过去分词 washed。"},
            ],
        },
        {
            "id": "passive_impersonal", "name": "Impersonal Passive", "zh": "无人称被动",
            "concept": {"en": "It is said / believed / thought / known that... — used in news and formal writing to report opinions without naming the speaker.", "zh": "It is said/believed/thought/known that... — 用于新闻和正式文体，不指明说话人。"},
            "rules": [
                {"label": "结构", "en": "It + be + pp + that + clause: It is said that he is rich.", "zh": "It + be + pp + that + 从句：据说他很有钱。"},
                {"label": "变体", "en": "subject + be + pp + to: He is said to be rich.", "zh": "主语 + be + pp + to：据说他很有钱。"},
            ],
            "examples": [
                {"en": "It is believed that the company will grow.", "zh": "人们相信公司会成长。"},
                {"en": "She is thought to be the best player.", "zh": "人们认为她是最好的选手。"},
                {"en": "It was reported that the train was delayed.", "zh": "据报道火车晚点了。"},
            ],
            "mistakes": [
                {"en": "❌ It is said he is rich (informal) → keep that in formal writing.", "zh": "❌ 正式文体保留 that。"},
                {"en": "❌ It is say → past participle: said.", "zh": "❌ 用过去分词 said。"},
            ],
        },
        {
            "id": "passive_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Rewrite active ↔ passive, keep the tense, keep the meaning, and choose the voice that fits the focus.", "zh": "主动与被动互转，保持时态与含义，按焦点选择语态。"},
            "rules": [
                {"label": "主动转被动", "en": "object → subject; be + pp; optional by + doer.", "zh": "宾语变主语；be + 过去分词；可加 by + 施动者。"},
                {"label": "被动转主动", "en": "by + doer becomes subject; verb returns to active form.", "zh": "by 后施动者变主语；动词变回主动。"},
                {"label": "选语态", "en": "Focus on doer → active. Focus on result/object → passive.", "zh": "强调施动者用主动；强调结果/对象用被动。"},
            ],
            "examples": [
                {"en": "The chef prepares the menu. → The menu is prepared by the chef.", "zh": "厨师准备菜单。→ 菜单由厨师准备。"},
                {"en": "The prizes were given by the mayor. → The mayor gave the prizes.", "zh": "奖品由市长颁发。→ 市长颁发了奖品。"},
                {"en": "Mistakes were made. (focus on the mistake, not who made it)", "zh": "犯了错误。（强调错误而非谁犯的）"},
            ],
            "mistakes": [
                {"en": "❌ The menu is prepared by the chef yesterday → tense shift; keep the time: was prepared.", "zh": "❌ 保持时态一致。"},
                {"en": "❌ Overusing passive makes writing weak — use active for clear actions.", "zh": "❌ 过度使用被动会使表达无力。"},
            ],
        },
    ],
}
