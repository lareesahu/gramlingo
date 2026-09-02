# -*- coding: utf-8 -*-
"""Grammar Foundations deck 08 — Frequency Adverbs / 频率副词 (standalone lecture, no game module)."""
LESSON = {
    "id": "frequency_adverbs",
    "foundation": True,
    "name": "Frequency Adverbs",
    "zh": "频率副词",
    "icon": "🗓️",
    "accent": "#099268",
    "desc": {
        "en": "always, usually, often, sometimes, rarely, never — say how often things happen, put them in the right place, and ask with How often...?",
        "zh": "always、usually、often、sometimes、rarely、never——说明事情发生的频率，掌握它们在句中的位置，并用 How often...? 提问。",
    },
    "objectives": [
        {"en": "Understand the frequency scale from always to never", "zh": "理解从 always 到 never 的频率等级"},
        {"en": "Place frequency adverbs in the right spot", "zh": "把频率副词放在正确的位置"},
        {"en": "Ask and answer How often...? questions", "zh": "会用 How often...? 提问并回答"},
    ],
    "phases": [
        {
            "id": "fa_levels", "name": "always → never", "zh": "从总是到从不",
            "concept": {
                "en": "Frequency adverbs tell how often something happens. Think of a scale: always (100%), usually (about 80%), often (70%), sometimes (50%), rarely (10%), never (0%).",
                "zh": "频率副词说明事情发生的频率。可以想成一条刻度：always（100%）、usually（约 80%）、often（70%）、sometimes（50%）、rarely（10%）、never（0%）。",
            },
            "rules": [
                {"label": "高频", "en": "always 总是 · usually 通常 · often 经常", "zh": "always 总是 · usually 通常 · often 经常"},
                {"label": "中频", "en": "sometimes 有时（约一半）", "zh": "sometimes 有时（大约一半）"},
                {"label": "低频", "en": "rarely 很少 · never 从不", "zh": "rarely 很少 · never 从不"},
                {"label": "never 即否定", "en": "I never drink coffee.（句中不再加 don't）", "zh": "never 本身表否定，不再加 don't"},
            ],
            "examples": [
                {"en": "She always smiles when she sees me.", "zh": "她见到我总是微笑。"},
                {"en": "I usually get up at seven.", "zh": "我通常七点起床。"},
                {"en": "He never eats meat.", "zh": "他从不吃肉。"},
            ],
            "mistakes": [
                {"en": "❌ I don't never eat fast food. → One negative: I never eat fast food.", "zh": "❌ never 已是否定，别再写 don't：I never eat fast food.（我从不吃快餐。）"},
                {"en": "❌ She always is busy? → Wrong spot, see next phase: She is always busy.", "zh": "❌ always 放在 be 动词后面：She is always busy.（她总是很忙。）"},
            ],
        },
        {
            "id": "fa_position", "name": "Position 位置", "zh": "频率副词的位置",
            "concept": {
                "en": "Frequency adverbs sit in one of three spots: before a normal main verb (I often read), after the verb be (He is always late), and between an auxiliary (can / do / will) and the main verb (I can never forget it).",
                "zh": "频率副词的位置有三条规则：一般动词前（I often read）、be 动词后（He is always late）、助动词（can / do / will）与实义动词之间（I can never forget it）。",
            },
            "rules": [
                {"label": "实义动词前", "en": "I often read before bed.", "zh": "我经常睡前读书。"},
                {"label": "be 动词后", "en": "He is always late for school.", "zh": "他上学总是迟到。"},
                {"label": "助动词后", "en": "She can never forget that day.", "zh": "她永远忘不了那一天。"},
                {"label": "sometimes 句首", "en": "Sometimes I walk to work.（也可放句首）", "zh": "sometimes 也可以放在句首"},
            ],
            "examples": [
                {"en": "We often play football after school.", "zh": "我们放学后经常踢足球。"},
                {"en": "My mother is always busy on weekdays.", "zh": "我妈妈工作日总是很忙。"},
                {"en": "I can usually finish my homework before dinner.", "zh": "我通常能在晚饭前写完作业。"},
            ],
            "mistakes": [
                {"en": "❌ I read often books. → Often goes before the verb: I often read books.", "zh": "❌ often 放在动词前：I often read books.（我经常读书。）"},
                {"en": "❌ She is late always. → After be: She is always late.", "zh": "❌ always 放在 is 后面：She is always late.（她总是迟到。）"},
            ],
        },
        {
            "id": "fa_questions", "name": "How often...?", "zh": "多久一次？",
            "concept": {
                "en": "To ask about frequency, use How often + do / does + subject + verb? Answer with a frequency adverb, or with every day / week, once a week, twice a month, three times a year.",
                "zh": "询问频率用 How often + do / does + 主语 + 动词？回答时用频率副词，或用 every day（每天）、once a week（一周一次）、twice a month（一个月两次）、three times a year（一年三次）。",
            },
            "rules": [
                {"label": "提问", "en": "How often do you exercise?", "zh": "你多久锻炼一次？"},
                {"label": "every 表达", "en": "every day / every week / every morning", "zh": "每天 / 每周 / 每天早上"},
                {"label": "次数表达", "en": "once a week · twice a month · three times a year", "zh": "一周一次 · 一月两次 · 一年三次"},
            ],
            "examples": [
                {"en": "How often do you exercise? I exercise three times a week.", "zh": "你多久锻炼一次？我一周锻炼三次。"},
                {"en": "How often does he travel? He rarely travels.", "zh": "他多久旅行一次？他很少旅行。"},
                {"en": "I brush my teeth twice a day.", "zh": "我每天刷两次牙。"},
            ],
            "mistakes": [
                {"en": "❌ How often you exercise? → Need do: How often do you exercise?", "zh": "❌ 疑问句要加 do：How often do you exercise?（你多久锻炼一次？）"},
                {"en": "❌ I every day play games. → Time phrases go at the end: I play games every day.", "zh": "❌ every day 放在句尾：I play games every day.（我每天玩游戏。）"},
            ],
        },
    ],
}
