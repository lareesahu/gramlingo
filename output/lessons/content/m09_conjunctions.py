# -*- coding: utf-8 -*-
LESSON = {
    "id": "conjunctions",
    "name": "Conjunctions",
    "zh": "连词",
    "icon": "🔌",
    "accent": "#2B8A3E",
    "desc": {"en": "Connect ideas by addition, contrast, cause, result, condition, and concession.", "zh": "用并列、对比、因果、结果、条件与让步的方式连接观点。"},
    "objectives": [
        {"en": "Use coordinating conjunctions: and, but, or, so, yet", "zh": "使用并列连词 and、but、or、so、yet"},
        {"en": "Use subordinating conjunctions to build complex sentences", "zh": "用从属连词构建复合句"},
        {"en": "Use correlative pairs: both...and, either...or, neither...nor", "zh": "使用关联词对 both...and、either...or、neither...nor"},
        {"en": "Express contrast, cause, purpose with the right connector", "zh": "用正确的连接词表达对比、因果、目的"},
        {"en": "Use linking adverbs for cohesion", "zh": "用连接副词增强连贯性"},
    ],
    "phases": [
        {
            "id": "conjunctions_coordinating", "name": "Coordinating", "zh": "并列连词",
            "concept": {"en": "FANBOYS: for, and, nor, but, or, yet, so. They join equal words, phrases, or clauses.", "zh": "并列连词口诀 FANBOYS：for、and、nor、but、or、yet、so。它们连接对等的词、短语或从句。"},
            "rules": [
                {"label": "添加", "en": "and: I like tea and coffee.", "zh": "and 表添加：我喜欢茶和咖啡。"},
                {"label": "转折", "en": "but / yet: She is small but strong.", "zh": "but/yet 表转折：她个子小但很强壮。"},
                {"label": "选择", "en": "or: Tea or coffee?", "zh": "or 表选择：茶还是咖啡？"},
                {"label": "结果", "en": "so: It rained, so we stayed home.", "zh": "so 表结果：下雨了，所以我们待在家。"},
            ],
            "examples": [
                {"en": "He was tired, yet he kept working.", "zh": "他很累，但仍然继续工作。"},
                {"en": "We can walk or take the bus.", "zh": "我们可以走路或坐公交。"},
                {"en": "She studied hard, so she passed easily.", "zh": "她努力学习，所以轻松通过了。"},
            ],
            "mistakes": [
                {"en": "❌ Comma splice without a conjunction: It rained, we stayed → add so.", "zh": "❌ 两个句子之间要有连词：It rained, so we stayed."},
                {"en": "❌ Although...but double conjunction → use one.", "zh": "❌ although 和 but 不能同时使用。"},
            ],
        },
        {
            "id": "conjunctions_subordinating", "name": "Subordinating", "zh": "从属连词",
            "concept": {"en": "Subordinating conjunctions (because, although, while, since, if, when) introduce a dependent clause that gives context to the main clause.", "zh": "从属连词（because、although、while、since、if、when）引导从句，为主句提供背景。"},
            "rules": [
                {"label": "原因", "en": "because / since: She left because she was tired.", "zh": "because/since 表原因：她离开是因为累了。"},
                {"label": "让步", "en": "although / while: Although it rained, we went out.", "zh": "although/while 表让步：虽然下雨，我们还是出去了。"},
                {"label": "时间/条件", "en": "when / if: Call me when you arrive. If you are free, join us.", "zh": "when 表时间；if 表条件。"},
            ],
            "examples": [
                {"en": "Since you are here, let's start.", "zh": "既然你来了，我们开始吧。"},
                {"en": "I was reading while she cooked.", "zh": "她做饭时我在看书。"},
                {"en": "We will go out if the weather is fine.", "zh": "如果天气好我们就出去。"},
            ],
            "mistakes": [
                {"en": "❌ Because she was tired, so she left → one connector only.", "zh": "❌ because 和 so 只用其一。"},
                {"en": "❌ Although it rained, but we went → drop but.", "zh": "❌ although 与 but 不并用。"},
            ],
        },
        {
            "id": "conjunctions_correlative", "name": "Correlative", "zh": "关联连词",
            "concept": {"en": "Pairs that join equal elements: both...and (two), either...or (choice), neither...nor (none of two), not only...but also.", "zh": "成对连接对等成分：both...and 两者都；either...or 二选一；neither...nor 两者都不；not only...but also 不仅……而且。"},
            "rules": [
                {"label": "both...and", "en": "Both Tom and Anna came.", "zh": "汤姆和安娜都来了。"},
                {"label": "either...or", "en": "You can have either tea or coffee.", "zh": "你可以喝茶或咖啡（二选一）。"},
                {"label": "neither...nor", "en": "Neither he nor I smoke.", "zh": "他和我都不抽烟。"},
                {"label": "not only...but also", "en": "She is not only smart but also kind.", "zh": "她不仅聪明而且善良。"},
            ],
            "examples": [
                {"en": "Either you apologize or I leave.", "zh": "要么你道歉，要么我走。"},
                {"en": "Neither the manager nor the staff knew.", "zh": "经理和员工都不知道。"},
                {"en": "He can speak both English and Chinese.", "zh": "他英语和中文都会说。"},
            ],
            "mistakes": [
                {"en": "❌ Neither...or → neither...nor.", "zh": "❌ neither 与 nor 搭配。"},
                {"en": "❌ Both he and I is → plural verb: are.", "zh": "❌ both...and 用复数谓语。"},
            ],
        },
        {
            "id": "conjunctions_contrast", "name": "Contrast and Concession", "zh": "对比与让步",
            "concept": {"en": "although / even though / though + clause; despite / in spite of + noun or -ing. despite is followed by a noun phrase, not a clause.", "zh": "although/even though/though 后接从句；despite/in spite of 后接名词或动名词，不接从句。"},
            "rules": [
                {"label": "从句", "en": "Although it was cold, he wore a T-shirt.", "zh": "虽然很冷，他还是穿T恤。"},
                {"label": "名词", "en": "Despite the cold, he wore a T-shirt.", "zh": "尽管天冷，他还是穿T恤。"},
                {"label": "even though", "en": "stronger contrast: Even though she failed, she kept trying.", "zh": "even though 让步更强：尽管失败了，她仍继续尝试。"},
            ],
            "examples": [
                {"en": "Though he is young, he is very mature.", "zh": "虽然他年轻，但很成熟。"},
                {"en": "In spite of the rain, the match continued.", "zh": "尽管下雨，比赛继续进行。"},
                {"en": "Even though it was late, she stayed.", "zh": "即使很晚了，她还是留了下来。"},
            ],
            "mistakes": [
                {"en": "❌ Despite it was cold → despite + noun: Despite the cold / Despite being cold.", "zh": "❌ despite 后接名词，不接从句。"},
                {"en": "❌ Although...but → one connector.", "zh": "❌ 一个让步连词即可。"},
            ],
        },
        {
            "id": "conjunctions_cause", "name": "Cause and Result", "zh": "因果",
            "concept": {"en": "because / since / as + clause (cause); so...that / such...that (result); therefore / as a result (linking).", "zh": "because/since/as + 从句表原因；so...that / such...that 表结果；therefore/as a result 为连接性表达。"},
            "rules": [
                {"label": "原因", "en": "As it was late, we went home.", "zh": "因为晚了，我们回家了。"},
                {"label": "结果", "en": "so + adj/adv + that: It was so hot that we stayed in.", "zh": "so + 形容词/副词 + that：太热了，我们待在室内。"},
                {"label": "such + 名词", "en": "It was such a good film that I saw it twice.", "zh": "such + 名词 + that：电影太好看了，我看了两遍。"},
            ],
            "examples": [
                {"en": "Since you asked, I'll explain.", "zh": "既然你问了，我就解释一下。"},
                {"en": "The bag was so heavy that I couldn't lift it.", "zh": "包太重了，我提不动。"},
                {"en": "He spoke so fast that nobody understood.", "zh": "他说得太快，没人听懂。"},
            ],
            "mistakes": [
                {"en": "❌ so + noun → such a good film, NOT so a good film.", "zh": "❌ so 修饰形容词，名词前用 such。"},
                {"en": "❌ Because...so double → use one.", "zh": "❌ because 与 so 不并用。"},
            ],
        },
        {
            "id": "conjunctions_purpose", "name": "Purpose", "zh": "目的",
            "concept": {"en": "so that / in order that + clause (purpose); in order to / so as to + base (purpose); for + noun (-ing for verb actions).", "zh": "so that / in order that + 从句表目的；in order to / so as to + 原形表目的；for + 名词（动词用 -ing）。"},
            "rules": [
                {"label": "从句", "en": "I left early so that I wouldn't be late.", "zh": "我早出发，以免迟到。"},
                {"label": "不定式", "en": "She studies hard in order to pass.", "zh": "她努力学习以求通过。"},
                {"label": "for + 名词", "en": "This knife is for cutting bread.", "zh": "这把刀是用来切面包的。"},
            ],
            "examples": [
                {"en": "He spoke slowly so that everyone could understand.", "zh": "他慢慢说，以便大家都能听懂。"},
                {"en": "We arrived early so as to get good seats.", "zh": "我们早到，以便有好座位。"},
                {"en": "She went to the shop for some milk.", "zh": "她去商店买牛奶。"},
            ],
            "mistakes": [
                {"en": "❌ for + verb → for cutting, not for cut.", "zh": "❌ for 后接名词或 -ing。"},
                {"en": "❌ so that + to → so that I can..., not so that to.", "zh": "❌ so that 后接从句，不用 to。"},
            ],
        },
        {
            "id": "conjunctions_linking", "name": "Linking Adverbs", "zh": "连接副词",
            "concept": {"en": "Linking adverbs connect ideas across sentences: however (contrast), therefore (result), moreover / furthermore (addition), nevertheless (contrast).", "zh": "连接副词跨句连接观点：however 然而、therefore 因此、moreover/furthermore 此外、nevertheless 尽管如此。"},
            "rules": [
                {"label": "然而", "en": "It was raining. However, we went out.", "zh": "下雨了。然而我们还是出去了。"},
                {"label": "因此", "en": "She studied hard. Therefore, she passed.", "zh": "她努力学习，因此通过了。"},
                {"label": "此外", "en": "The plan is cheap. Moreover, it is simple.", "zh": "这个方案便宜，而且简单。"},
            ],
            "examples": [
                {"en": "He was tired. Nevertheless, he finished the race.", "zh": "他很累，尽管如此，还是完成了比赛。"},
                {"en": "The film was long. However, it was interesting.", "zh": "电影很长，不过很有趣。"},
                {"en": "We lost the game. Therefore, we practiced harder.", "zh": "我们输了比赛，因此练得更努力。"},
            ],
            "mistakes": [
                {"en": "❌ however joins two sentences with a period/semicolon, not a comma alone.", "zh": "❌ however 前用句号或分号，不能只用逗号连接两个句子。"},
                {"en": "❌ therefore is not a conjunction — needs a period or semicolon.", "zh": "❌ therefore 是副词，需要句号或分号。"},
            ],
        },
        {
            "id": "conjunctions_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Combine sentences by choosing the connector that matches the logic: addition, contrast, cause, result, condition, purpose.", "zh": "根据逻辑关系（添加、对比、因果、条件、目的）选择连接词来合并句子。"},
            "rules": [
                {"label": "逻辑匹配", "en": "same idea → and; opposite → but/although; reason → because; result → so/therefore; choice → or.", "zh": "相同用 and；相反用 but/although；原因用 because；结果用 so/therefore；选择用 or。"},
                {"label": "单连接词", "en": "One connector per connection: no although...but, no because...so.", "zh": "一个连接只用一个连词。"},
            ],
            "examples": [
                {"en": "He was ill. He went to work. → Although he was ill, he went to work.", "zh": "尽管他病了，还是去上班了。"},
                {"en": "She trained daily. She won the race. → She trained daily, so she won the race.", "zh": "她每天训练，所以赢得了比赛。"},
                {"en": "You can call me. You can send an email. → You can either call me or send an email.", "zh": "你可以打电话，也可以发邮件。"},
            ],
            "mistakes": [
                {"en": "❌ Comma splice: She was tired, she slept → add a connector or use a period.", "zh": "❌ 逗号不能直接连接两个完整句子。"},
                {"en": "❌ Wrong connector changes the meaning — choose by logic.", "zh": "❌ 连接词选错会改变句意。"},
            ],
        },
    ],
}
