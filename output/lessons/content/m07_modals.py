# -*- coding: utf-8 -*-
LESSON = {
    "id": "modals",
    "name": "Modals",
    "zh": "情态动词",
    "icon": "🎯",
    "accent": "#F08C00",
    "desc": {"en": "Express ability, permission, advice, obligation, probability, and deduction.", "zh": "表达能力、许可、建议、义务、可能性与推断。"},
    "objectives": [
        {"en": "Use can, could, be able to for ability", "zh": "用 can、could、be able to 表能力"},
        {"en": "Give and ask permission politely", "zh": "礼貌地请求和给予许可"},
        {"en": "Express obligation and advice with must, have to, should", "zh": "用 must、have to、should 表义务与建议"},
        {"en": "Make deductions with must, might, can't", "zh": "用 must、might、can't 作推断"},
        {"en": "Use past modals like could have, should have", "zh": "使用 could have、should have 等过去情态"},
    ],
    "phases": [
        {
            "id": "modals_ability", "name": "Ability", "zh": "能力",
            "concept": {"en": "can = present ability; could = past ability; be able to = any tense or for achievements.", "zh": "can 表现在能力；could 表过去能力；be able to 可用于任何时态或表示成功做到。"},
            "rules": [
                {"label": "现在", "en": "can + base: I can swim.", "zh": "can + 原形：我会游泳。"},
                {"label": "过去", "en": "could + base: When I was young, I could run fast.", "zh": "could + 原形：年轻时我能跑很快。"},
                {"label": "成功做到", "en": "was/were able to for specific achievements: I was able to finish on time.", "zh": "具体成功做到用 was able to：我按时完成了。"},
            ],
            "examples": [
                {"en": "She can speak three languages.", "zh": "她会说三种语言。"},
                {"en": "He couldn't swim until he was ten.", "zh": "他十岁才会游泳。"},
                {"en": "They were able to escape the fire.", "zh": "他们成功逃离了火灾。"},
            ],
            "mistakes": [
                {"en": "❌ She can to swim → modal + base, no to.", "zh": "❌ 情态动词后接原形，不加 to。"},
                {"en": "❌ I can swims → modal + base form.", "zh": "❌ 情态动词后动词用原形。"},
            ],
        },
        {
            "id": "modals_permission", "name": "Permission", "zh": "许可",
            "concept": {"en": "can = informal permission; may = formal permission; could = polite request; be allowed to = other tenses.", "zh": "can 非正式许可；may 正式许可；could 礼貌请求；be allowed to 用于其他时态。"},
            "rules": [
                {"label": "非正式", "en": "Can I go out?", "zh": "我能出去吗？（口语）"},
                {"label": "正式", "en": "May I come in?", "zh": "我可以进来吗？（正式）"},
                {"label": "礼貌", "en": "Could I borrow your pen?", "zh": "我能借用你的笔吗？（更礼貌）"},
                {"label": "其他时态", "en": "You will be allowed to enter later.", "zh": "稍后你会被允许进入。"},
            ],
            "examples": [
                {"en": "Can I use your phone?", "zh": "我能用你的电话吗？"},
                {"en": "May I ask a question?", "zh": "我可以问个问题吗？"},
                {"en": "Students are allowed to use the library.", "zh": "学生可以使用图书馆。"},
            ],
            "mistakes": [
                {"en": "❌ May I... in very informal speech can sound stiff — can is fine among friends.", "zh": "❌ 朋友之间用 can 更自然。"},
                {"en": "❌ I am allowed to go yesterday → use was allowed to.", "zh": "❌ 过去时用 was allowed to。"},
            ],
        },
        {
            "id": "modals_obligation", "name": "Obligation", "zh": "义务",
            "concept": {"en": "must = strong obligation (internal/rule); have to = external necessity; should/ought to = advice; mustn't = prohibition; don't have to = not necessary.", "zh": "must 表强烈义务（内部/规则）；have to 表外部必要性；should/ought to 表建议；mustn't 表禁止；don't have to 表不必。"},
            "rules": [
                {"label": "must", "en": "You must wear a seatbelt.", "zh": "你必须系安全带。"},
                {"label": "have to", "en": "I have to work on Saturdays.", "zh": "我周六必须上班。"},
                {"label": "should", "en": "You should drink more water.", "zh": "你应该多喝水。"},
                {"label": "禁止 vs 不必", "en": "You mustn't smoke here. / You don't have to come.", "zh": "禁止：你不能在这里抽烟。不必：你不必来。"},
            ],
            "examples": [
                {"en": "You must finish your homework before playing.", "zh": "你必须先完成作业再玩。"},
                {"en": "She has to wear a uniform at work.", "zh": "她上班必须穿制服。"},
                {"en": "You ought to see a doctor.", "zh": "你应该去看医生。"},
            ],
            "mistakes": [
                {"en": "❌ You don't have to = no obligation (optional), NOT prohibition.", "zh": "❌ don't have to 表【不必】，不是【禁止】。"},
                {"en": "❌ must not vs don't have to — different meanings!", "zh": "❌ mustn't（禁止）与 don't have to（不必）意思不同。"},
            ],
        },
        {
            "id": "modals_probability", "name": "Probability", "zh": "可能性",
            "concept": {"en": "Deduction about the present: must = almost certain; might/may/could = possible; can't = impossible/almost certainly not.", "zh": "对现在的推断：must 几乎确定；might/may/could 可能；can't 不可能。"},
            "rules": [
                {"label": "几乎确定", "en": "must + base: She has a key, so she must be the owner.", "zh": "must + 原形：她肯定就是主人。"},
                {"label": "可能", "en": "might/may/could: He might be at home now.", "zh": "might/may/could：他现在可能在家。"},
                {"label": "不可能", "en": "can't + base: That can't be true!", "zh": "can't + 原形：那不可能是真的！"},
            ],
            "examples": [
                {"en": "The lights are on, so she must be home.", "zh": "灯亮着，所以她一定在家。"},
                {"en": "It might rain later.", "zh": "稍后可能会下雨。"},
                {"en": "He can't be 40 — he looks so young!", "zh": "他不可能是40岁——他看起来太年轻了！"},
            ],
            "mistakes": [
                {"en": "❌ mustn't for deduction → use can't: He can't be at home.", "zh": "❌ 否定推断用 can't，不用 mustn't。"},
                {"en": "❌ may not = possibly not, NOT prohibition.", "zh": "❌ may not 表【可能不】，不是禁止。"},
            ],
        },
        {
            "id": "modals_past", "name": "Past Modals", "zh": "过去情态",
            "concept": {"en": "modal + have + past participle for the past: could have (possibility), should have (regret/criticism), must have (certainty), might have (guess), can't have (impossible).", "zh": "情态动词 + have + 过去分词表过去：could have 可能、should have 本应、must have 一定、might have 也许、can't have 不可能。"},
            "rules": [
                {"label": "must have", "en": "certainty: She must have left early.", "zh": "一定：她一定早就离开了。"},
                {"label": "should have", "en": "regret: I should have studied harder.", "zh": "本应：我本该更用功。"},
                {"label": "could have", "en": "possibility: He could have been hurt.", "zh": "可能：他可能受伤了。"},
                {"label": "can't have", "en": "impossibility: He can't have seen us.", "zh": "不可能：他不可能看到我们。"},
            ],
            "examples": [
                {"en": "You must have been tired after the trip.", "zh": "旅行后你一定很累。"},
                {"en": "She should have called me.", "zh": "她本应给我打电话。"},
                {"en": "They might have missed the bus.", "zh": "他们可能错过了公交车。"},
            ],
            "mistakes": [
                {"en": "❌ She must left early → modal + have + pp: must have left.", "zh": "❌ 过去情态结构是 must have + 过去分词。"},
                {"en": "❌ I should studied → should have studied.", "zh": "❌ 漏掉 have。"},
            ],
        },
        {
            "id": "modals_requests", "name": "Requests and Offers", "zh": "请求与提议",
            "concept": {"en": "Requests: Can/Could/Would you...? Offers: Shall I...? / Can I...? / Would you like...?", "zh": "请求：Can/Could/Would you...? 提议：Shall I...? / Can I...? / Would you like...?"},
            "rules": [
                {"label": "请求", "en": "Could you open the door, please? (polite)", "zh": "请把门打开好吗？（礼貌）"},
                {"label": "提议帮助", "en": "Shall I carry your bag?", "zh": "要我帮你拿包吗？"},
                {"label": "邀请", "en": "Would you like some tea?", "zh": "要来点茶吗？"},
            ],
            "examples": [
                {"en": "Can you help me with this box?", "zh": "你能帮我搬这个箱子吗？"},
                {"en": "Shall I turn on the light?", "zh": "要我开灯吗？"},
                {"en": "Would you like to join us?", "zh": "你愿意加入我们吗？"},
            ],
            "mistakes": [
                {"en": "❌ Do you want I help? → correct: Shall I help?", "zh": "❌ 提议帮助用 Shall I...?"},
                {"en": "❌ Give me the book (too direct) → Could you give me the book?", "zh": "❌ 请求更礼貌的说法。"},
            ],
        },
        {
            "id": "modals_contrast", "name": "Modal Contrast", "zh": "情态动词对比",
            "concept": {"en": "Choose the modal by meaning: ability (can), permission (may), obligation (must), advice (should), possibility (might), certainty (must/can't).", "zh": "按含义选情态动词：能力 can、许可 may、义务 must、建议 should、可能 might、确定 must/can't。"},
            "rules": [
                {"label": "强度排序", "en": "can't < might < could < may < must (certainty scale)", "zh": "可能性从低到高：can't < might < could < may < must"},
                {"label": "语境决定", "en": "Same modal, different job: Can you swim? (ability) / Can I leave? (permission) / It can rain here. (possibility)", "zh": "同一个 can 在不同语境功能不同。"},
            ],
            "examples": [
                {"en": "You must be joking! (certainty — deduction)", "zh": "你一定在开玩笑！（确定推断）"},
                {"en": "We might visit them next week. (possibility)", "zh": "我们下周可能会去拜访他们。（可能）"},
                {"en": "Everyone should recycle. (advice/general rule)", "zh": "每个人都应该回收利用。（建议）"},
            ],
            "mistakes": [
                {"en": "❌ Using must for advice → must is strong obligation; use should for suggestions.", "zh": "❌ 建议用 should，不用 must。"},
                {"en": "❌ Using can't for 'not allowed' vs 'impossible' — check context.", "zh": "❌ 分清 can't 表「不允许」还是「不可能」。"},
            ],
        },
        {
            "id": "modals_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "In real scenarios, identify the function (ability, permission, obligation, advice, possibility) and pick the modal, then check the form: modal + base verb.", "zh": "在实际场景中先判断功能（能力、许可、义务、建议、可能），再选情态动词，最后检查形式：情态动词 + 动词原形。"},
            "rules": [
                {"label": "功能优先", "en": "What is the speaker doing? Asking permission, giving advice, making a deduction?", "zh": "说话人在做什么：请求许可、给建议、作推断？"},
                {"label": "形式检查", "en": "modal + base (no -s, no to): She must go.", "zh": "情态动词 + 原形（不加 -s、不加 to）。"},
                {"label": "过去式", "en": "For past meaning: modal + have + pp.", "zh": "表过去：情态动词 + have + 过去分词。"},
            ],
            "examples": [
                {"en": "You look pale — you should rest.", "zh": "你脸色不好——应该休息一下。"},
                {"en": "Passengers must fasten their seatbelts.", "zh": "乘客必须系好安全带。"},
                {"en": "She can't have forgotten — we reminded her twice.", "zh": "她不可能忘了——我们提醒过她两次。"},
            ],
            "mistakes": [
                {"en": "❌ He can sings → modal + base: He can sing.", "zh": "❌ 情态动词后动词用原形。"},
                {"en": "❌ You must to go → no to after modals.", "zh": "❌ 情态动词后不加 to。"},
            ],
        },
    ],
}
