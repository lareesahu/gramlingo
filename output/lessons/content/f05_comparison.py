# -*- coding: utf-8 -*-
"""Grammar Foundations deck 05 — Comparison / 比较级与最高级 (standalone lecture, no game module)."""
LESSON = {
    "id": "comparison",
    "foundation": True,
    "name": "Comparison",
    "zh": "比较级与最高级",
    "icon": "⚖️",
    "accent": "#F08C00",
    "desc": {
        "en": "Taller or more interesting? Compare two things with -er / more ... than, rank three or more with the -est / the most, and use as ... as for equal comparison.",
        "zh": "taller 还是 more interesting？用 -er / more ... than 比较两者，用 the -est / the most 在三者以上中排序，用 as ... as 表示同等比较。",
    },
    "objectives": [
        {"en": "Build the comparative with -er / more", "zh": "用 -er / more 构成比较级"},
        {"en": "Build the superlative with the -est / the most", "zh": "用 the -est / the most 构成最高级"},
        {"en": "Remember irregular forms: good, bad, much, far", "zh": "记住不规则形式：good、bad、much、far"},
        {"en": "Compare equally with as ... as", "zh": "用 as ... as 表示同等比较"},
    ],
    "phases": [
        {
            "id": "cmp_two", "name": "Comparing Two", "zh": "比较两者",
            "concept": {
                "en": "To compare two things, use the comparative: short adjectives add -er, long adjectives use more, and than introduces the other side of the comparison.",
                "zh": "比较两者用比较级：短形容词加 -er，长形容词用 more，than 引出比较的另一方。",
            },
            "rules": [
                {"label": "短词 -er", "en": "tall → taller; fast → faster; big → bigger", "zh": "高→更高；快→更快；大→更大"},
                {"label": "长词 more", "en": "careful → more careful; interesting → more interesting", "zh": "仔细→更仔细；有趣→更有趣"},
                {"label": "引出比较对象", "en": "than: Tom is taller than me.", "zh": "than：汤姆比我高。"},
                {"label": "程度修饰", "en": "much / a lot / a little + 比较级: much taller", "zh": "much / a lot / a little + 比较级：高得多"},
            ],
            "examples": [
                {"en": "My bag is heavier than yours.", "zh": "我的包比你的重。"},
                {"en": "This movie is more interesting than that one.", "zh": "这部电影比那部更有趣。"},
                {"en": "She is much more patient than her brother.", "zh": "她比她哥哥有耐心得多。"},
            ],
            "mistakes": [
                {"en": "❌ He is more tall than me. → One comparative is enough: He is taller than me.", "zh": "❌ 不要重复比较级：He is taller than me.（他比我高。）"},
                {"en": "❌ This is more better. → Say: This is better.", "zh": "❌ better 已是比较级，前面不加 more：This is better.（这个更好。）"},
            ],
        },
        {
            "id": "cmp_est", "name": "Superlatives", "zh": "三者以上最高级",
            "concept": {
                "en": "To rank three or more things, use the superlative: the + short adjective + -est, or the most + long adjective. Say which group you mean with in or of.",
                "zh": "三者以上排序用最高级：the + 短形容词 + -est，或 the most + 长形容词。用 in / of 说明范围。",
            },
            "rules": [
                {"label": "短词 the -est", "en": "the tallest; the biggest; the happiest", "zh": "最高的；最大的；最快乐的"},
                {"label": "长词 the most", "en": "the most careful; the most beautiful", "zh": "最仔细的；最美丽的"},
                {"label": "范围 in / of", "en": "in + 地点/团体: in our class; of + 复数: of all", "zh": "in + 地点/集体：在我们班；of + 复数：在所有之中"},
                {"label": "one of the...", "en": "one of the best players（最高级后接复数名词）", "zh": "最优秀的球员之一（最高级后用复数名词）"},
            ],
            "examples": [
                {"en": "Everest is the highest mountain in the world.", "zh": "珠穆朗玛峰是世界上最高的山。"},
                {"en": "She is the most careful student in our class.", "zh": "她是我们班最认真的学生。"},
                {"en": "It was one of the best days of my life.", "zh": "那是我一生中最美好的日子之一。"},
            ],
            "mistakes": [
                {"en": "❌ She is tallest in our class. → Superlatives need the: She is the tallest in our class.", "zh": "❌ 最高级前面要加 the：She is the tallest in our class.（她是我们班最高的。）"},
                {"en": "❌ the most biggest → the biggest", "zh": "❌ biggest 已是最高级，不要加 most：the biggest（最大的）。"},
            ],
        },
        {
            "id": "cmp_irr", "name": "Irregulars & Spelling", "zh": "不规则与拼写",
            "concept": {
                "en": "A few very common adjectives are irregular: good → better → best, bad → worse → worst, much / many → more → most, little → less → least. Spelling also changes for short words: big → bigger, happy → happier, nice → nicer.",
                "zh": "少数常用形容词是不规则的：good → better → best（好）、bad → worse → worst（坏）、much / many → more → most（多）、little → less → least（少）。短词拼写也会变化：big → bigger、happy → happier、nice → nicer。",
            },
            "rules": [
                {"label": "good / bad", "en": "good → better → best; bad → worse → worst", "zh": "好→更好→最好；坏→更坏→最坏"},
                {"label": "多 / 少", "en": "much / many → more → most; little → less → least", "zh": "多→更多→最多；少→更少→最少"},
                {"label": "双写", "en": "big → bigger → biggest; hot → hotter → hottest", "zh": "大→更大→最大；热→更热→最热"},
                {"label": "y 与 e", "en": "happy → happier → happiest; nice → nicer → nicest", "zh": "快乐→更快乐→最快乐；好→更好→最好"},
            ],
            "examples": [
                {"en": "Today is better than yesterday.", "zh": "今天比昨天好。"},
                {"en": "This is the worst weather we have had this week.", "zh": "这是本周最糟糕的天气。"},
                {"en": "My little sister is the happiest girl I know.", "zh": "我妹妹是我认识的最快乐的女孩。"},
            ],
            "mistakes": [
                {"en": "❌ My English is gooder than his. → good is irregular: better", "zh": "❌ good 的比较级是 better：My English is better than his.（我的英语比他好。）"},
                {"en": "❌ She is more happy now. → Short word: happier", "zh": "❌ happy 直接变 happier：She is happier now.（她现在更快乐。）"},
                {"en": "❌ This is the most worst day. → the worst", "zh": "❌ worst 已是最高级：This is the worst day.（这是最糟糕的一天。）"},
            ],
        },
        {
            "id": "cmp_equal", "name": "as ... as 同等比较", "zh": "同等与不及比较",
            "concept": {
                "en": "Use as + adjective + as to say two things are equal: as tall as. Use not as + adjective + as to say something is less: not as expensive as = cheaper than.",
                "zh": "用 as + 形容词 + as 表示两者相同：as tall as（一样高）。用 not as + 形容词 + as 表示“不如”：not as expensive as（不如……贵）= cheaper than（比……便宜）。",
            },
            "rules": [
                {"label": "同等", "en": "as + 原级 + as: as tall as, as fast as", "zh": "as + 形容词原级 + as：一样高、一样快"},
                {"label": "不如", "en": "not as + 原级 + as: not as cheap as", "zh": "not as + 原级 + as：不如……便宜"},
                {"label": "副词也适用", "en": "as well as, as carefully as", "zh": "副词也能这样用：一样好、一样仔细"},
            ],
            "examples": [
                {"en": "He is as tall as his father.", "zh": "他和他爸爸一样高。"},
                {"en": "This phone is not as expensive as that one.", "zh": "这部手机不如那部贵。"},
                {"en": "She sings as well as her sister.", "zh": "她唱得和她姐姐一样好。"},
            ],
            "mistakes": [
                {"en": "❌ She is as taller as me. → Use the base form: as tall as", "zh": "❌ as...as 之间用原级：She is as tall as me.（她和我一样高。）"},
                {"en": "❌ This book is not as cheap than that one. → not as cheap as", "zh": "❌ 否定同等用 not as...as：This book is not as cheap as that one.（这本书不如那本便宜。）"},
            ],
        },
    ],
}
