# -*- coding: utf-8 -*-
LESSON = {
    "id": "conditionals",
    "name": "Conditionals",
    "zh": "条件句",
    "icon": "🔀",
    "accent": "#9C36B5",
    "desc": {"en": "Express facts, possibilities, imagined situations, regrets, and conditions.", "zh": "表达事实、可能性、想象情境、遗憾与条件。"},
    "objectives": [
        {"en": "Use the zero and first conditionals for facts and real possibilities", "zh": "用零条件句和第一条件句表事实与现实可能"},
        {"en": "Use second and third conditionals for unreal situations", "zh": "用第二、第三条件句表虚拟情境"},
        {"en": "Build mixed conditionals across time", "zh": "构建跨时间的混合条件句"},
        {"en": "Use unless, provided, as long as instead of if", "zh": "用 unless、provided、as long as 替代 if"},
        {"en": "Express wishes and regrets with wish / if only", "zh": "用 wish / if only 表达愿望与遗憾"},
    ],
    "phases": [
        {
            "id": "conditionals_zero", "name": "Zero Conditional", "zh": "零条件句",
            "concept": {"en": "If + present, present — for general truths and scientific facts. Both parts are always true.", "zh": "If + 一般现在时，一般现在时 — 表示普遍真理和科学事实，两个部分都恒成立。"},
            "rules": [
                {"label": "结构", "en": "If + present simple, present simple: If you heat ice, it melts.", "zh": "If + 一般现在时，一般现在时：如果你加热冰，它会融化。"},
                {"label": "用途", "en": "facts, rules, habits: If I am late, my teacher is angry.", "zh": "事实、规则、习惯：如果我迟到，老师会生气。"},
            ],
            "examples": [
                {"en": "If you freeze water, it becomes ice.", "zh": "水结冰就会变成冰。"},
                {"en": "If plants get no sunlight, they die.", "zh": "植物没有阳光就会死。"},
                {"en": "If I drink coffee at night, I can't sleep.", "zh": "我晚上喝咖啡就睡不着。"},
            ],
            "mistakes": [
                {"en": "❌ If you will heat ice → no will in the if-clause: If you heat ice...", "zh": "❌ if 从句不用 will。"},
                {"en": "❌ If she is late, she misses the bus (general rule) — both present.", "zh": "❌ 一般规律：从句和主句都用一般现在时。"},
            ],
        },
        {
            "id": "conditionals_first", "name": "First Conditional", "zh": "第一条件句",
            "concept": {"en": "If + present, will + base — real future possibilities. The condition is possible and the result is a likely future.", "zh": "If + 一般现在时，will + 原形 — 表示现实的可能。条件有可能实现，结果是可能的未来。"},
            "rules": [
                {"label": "结构", "en": "If + present simple, will + base: If it rains, we will stay home.", "zh": "If + 一般现在时，will + 原形：如果下雨，我们就待在家里。"},
                {"label": "从句时态", "en": "Never use will in the if-clause: If I have time (not will have).", "zh": "if 从句绝不用 will。"},
            ],
            "examples": [
                {"en": "If you study hard, you will pass the exam.", "zh": "如果你努力学习，就会通过考试。"},
                {"en": "We will cancel the trip if the weather is bad.", "zh": "如果天气不好，我们就取消行程。"},
                {"en": "If she calls, I will tell her the news.", "zh": "如果她打电话来，我会告诉她这个消息。"},
            ],
            "mistakes": [
                {"en": "❌ If it will rain → present in if-clause: If it rains.", "zh": "❌ if 从句用现在时：If it rains。"},
                {"en": "❌ If I study, I pass (real future) → first conditional needs will: I will pass.", "zh": "❌ 表示未来可能结果用 will。"},
            ],
        },
        {
            "id": "conditionals_second", "name": "Second Conditional", "zh": "第二条件句",
            "concept": {"en": "If + past, would + base — unreal present or future situations. Imagining something that is not true now.", "zh": "If + 一般过去时，would + 原形 — 表示与现在或将来事实相反的假设。"},
            "rules": [
                {"label": "结构", "en": "If + past simple, would + base: If I had money, I would travel.", "zh": "If + 一般过去时，would + 原形：如果我有钱，我会去旅行。"},
                {"label": "be 动词", "en": "were for all persons in formal English: If I were you...", "zh": "正式语中 be 用 were：如果我是你……"},
                {"label": "含义", "en": "The situation is unreal or unlikely now.", "zh": "表示目前不真实或不太可能的情况。"},
            ],
            "examples": [
                {"en": "If I were you, I would take the job.", "zh": "如果我是你，我会接受这份工作。"},
                {"en": "If she spoke English, she could work abroad.", "zh": "如果她会说英语，她就能在国外工作。"},
                {"en": "If we had a car, we would drive there.", "zh": "如果我们有车，我们会开车去那里。"},
            ],
            "mistakes": [
                {"en": "❌ If I was you → use were in conditionals: If I were you.", "zh": "❌ 虚拟条件中 be 用 were：If I were you。"},
                {"en": "❌ If I have money, I would travel → mixed structure: If I had money...", "zh": "❌ 从句用过去时：If I had money..."},
            ],
        },
        {
            "id": "conditionals_third", "name": "Third Conditional", "zh": "第三条件句",
            "concept": {"en": "If + past perfect, would have + past participle — unreal past situations and regrets. The event did not happen.", "zh": "If + 过去完成时，would have + 过去分词 — 表示与过去事实相反的假设与遗憾。"},
            "rules": [
                {"label": "结构", "en": "If + had + pp, would have + pp: If I had known, I would have helped.", "zh": "If + had + 过去分词，would have + 过去分词：如果我早知道，我就会帮忙。"},
                {"label": "含义", "en": "The past event did not happen — pure regret or counterfactual.", "zh": "过去的事没有发生 — 纯遗憾或反事实。"},
            ],
            "examples": [
                {"en": "If she had studied, she would have passed.", "zh": "如果她学了，她本来会通过的。"},
                {"en": "We would have arrived earlier if we had left on time.", "zh": "如果我们准时出发，我们本来会更早到达。"},
                {"en": "If I had seen the sign, I wouldn't have turned left.", "zh": "如果我看到了标志，我就不会左转。"},
            ],
            "mistakes": [
                {"en": "❌ If I knew, I would have helped → past condition needs past perfect: If I had known.", "zh": "❌ 过去假设从句用 had known。"},
                {"en": "❌ If I had studied, I would pass → time mismatch; use would have passed.", "zh": "❌ 主句也要用 would have + 过去分词。"},
            ],
        },
        {
            "id": "conditionals_mixed", "name": "Mixed Conditionals", "zh": "混合条件句",
            "concept": {"en": "Mixed conditionals combine different times: past condition + present result (If I had studied, I would be rich now) or present condition + past result.", "zh": "混合条件句结合不同时间：过去条件 + 现在结果（如果我当初学了，现在就会很有钱）或现在条件 + 过去结果。"},
            "rules": [
                {"label": "过去条件+现在结果", "en": "If + had + pp, would + base: If I had taken that job, I would be in Shanghai now.", "zh": "If + had + pp，would + 原形：如果我当初接受那份工作，现在就在上海了。"},
                {"label": "现在条件+过去结果", "en": "If + past simple, would have + pp: If I weren't afraid of flying, I would have gone.", "zh": "If + 过去时，would have + pp：如果我不怕坐飞机，我早就去了。"},
            ],
            "examples": [
                {"en": "If she had studied medicine, she would be a doctor today.", "zh": "如果她当初学医，现在就是医生了。"},
                {"en": "If I were braver, I would have spoken up.", "zh": "如果我更勇敢，我当时就会说出来。"},
                {"en": "If he hadn't missed the train, he wouldn't be stuck here now.", "zh": "如果他没误了火车，现在就不会困在这里。"},
            ],
            "mistakes": [
                {"en": "❌ Mixing without a clear time reason → keep each half on its own timeline.", "zh": "❌ 混合必须理由清晰：半个句子一个时间线。"},
                {"en": "❌ If I had studied, I would be passing → use base form for present result: would pass.", "zh": "❌ 现在结果用 would + 原形。"},
            ],
        },
        {
            "id": "conditionals_alternatives", "name": "Alternatives to If", "zh": "if 的替代表达",
            "concept": {"en": "unless = if...not; provided that / as long as = on condition that; in case = because something might happen.", "zh": "unless 表示【如果不】；provided that / as long as 表示【只要】；in case 表示【以防】。"},
            "rules": [
                {"label": "unless", "en": "unless + positive verb = if...not: Unless you hurry, you'll miss it.", "zh": "unless + 肯定动词 = 如果不：除非你抓紧，否则会错过。"},
                {"label": "provided / as long as", "en": "condition: You can go as long as you finish first.", "zh": "条件：只要你先完成就能去。"},
                {"label": "in case", "en": "precaution: Take an umbrella in case it rains.", "zh": "预防：带把伞以防下雨。"},
            ],
            "examples": [
                {"en": "You won't pass unless you study.", "zh": "不学习你就不会通过。"},
                {"en": "I'll lend you the car provided that you drive carefully.", "zh": "只要你小心驾驶，我就把车借给你。"},
                {"en": "Keep the receipt in case you want to return it.", "zh": "留着收据，以防你想退货。"},
            ],
            "mistakes": [
                {"en": "❌ unless you don't hurry → unless is already negative; no double negative.", "zh": "❌ unless 本身就是否定，不能再加 not。"},
                {"en": "❌ as long as you will finish → present in condition clauses.", "zh": "❌ 条件从句用现在时。"},
            ],
        },
        {
            "id": "conditionals_wish", "name": "I Wish / If Only", "zh": "wish / if only 愿望句",
            "concept": {"en": "wish + past simple = present regret (unreal now); wish + past perfect = past regret; wish + would = a wish about someone's future behaviour.", "zh": "wish + 过去时 = 对现在的遗憾；wish + 过去完成时 = 对过去的遗憾；wish + would = 希望某人将来改变行为。"},
            "rules": [
                {"label": "现在遗憾", "en": "wish + past simple: I wish I knew the answer.", "zh": "wish + 过去时：我希望我知道答案（可惜不知道）。"},
                {"label": "过去遗憾", "en": "wish + past perfect: I wish I had studied harder.", "zh": "wish + 过去完成时：我多希望当初更用功。"},
                {"label": "行为愿望", "en": "wish + would: I wish you would stop talking.", "zh": "wish + would：我希望你别再说话了。"},
            ],
            "examples": [
                {"en": "I wish I were taller.", "zh": "我希望自己更高一些。"},
                {"en": "She wishes she had said yes.", "zh": "她后悔当时没答应。"},
                {"en": "If only the bus would come!", "zh": "要是公交车能来就好了！"},
            ],
            "mistakes": [
                {"en": "❌ I wish I am taller → unreal wish needs past: I wish I were taller.", "zh": "❌ 愿望句用过去时：I wish I were taller。"},
                {"en": "❌ I wish I have studied → past regret: I wish I had studied.", "zh": "❌ 过去遗憾用 had + 过去分词。"},
            ],
        },
        {
            "id": "conditionals_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Choose the conditional by reality: real fact → zero; real future → first; unreal now → second; unreal past → third. Check both halves.", "zh": "按现实度选条件句：事实用零条件句；现实未来用第一；虚拟现在用第二；虚拟过去用第三。检查前后两半。"},
            "rules": [
                {"label": "选型", "en": "Is it true? → zero. Possible? → first. Unlikely now? → second. Impossible past? → third.", "zh": "恒真→零；可能→第一；现在不可能→第二；过去不可能→第三。"},
                {"label": "检查", "en": "Never will after if. Match the tenses in both halves.", "zh": "if 后不用 will；两半时态要匹配。"},
            ],
            "examples": [
                {"en": "If I won the lottery, I would buy a house. (unreal now)", "zh": "如果我中彩票，我会买房。（现在虚拟）"},
                {"en": "If you heat metal, it expands. (fact)", "zh": "金属受热会膨胀。（事实）"},
                {"en": "If we leave now, we will catch the train. (real future)", "zh": "如果我们现在出发，就能赶上火车。（现实未来）"},
            ],
            "mistakes": [
                {"en": "❌ If I would win the lottery → no would in if-clause: If I won...", "zh": "❌ if 从句不用 would。"},
                {"en": "❌ Mixing zero and first without a reason.", "zh": "❌ 不要无理由混用条件句类型。"},
            ],
        },
    ],
}
