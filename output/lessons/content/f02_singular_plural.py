# -*- coding: utf-8 -*-
"""Grammar Foundations deck 02 — Singular & Plural / 单复数 (standalone lecture, no game module)."""
LESSON = {
    "id": "singular_plural",
    "foundation": True,
    "name": "Singular & Plural",
    "zh": "单数与复数",
    "icon": "🔢",
    "accent": "#0CA678",
    "desc": {
        "en": "One apple, two apples. Learn when nouns need -s or -es, which plurals are irregular, and how to handle uncountable nouns like water and information.",
        "zh": "一个苹果、两个苹果。学会名词何时加 -s / -es、哪些复数不规则，以及 water、information 这类不可数名词的用法。",
    },
    "objectives": [
        {"en": "Add -s or -es to make regular plurals", "zh": "用 -s / -es 构成规则复数"},
        {"en": "Apply plural spelling rules (-y, -f, -o)", "zh": "掌握 -y、-f、-o 等拼写规则"},
        {"en": "Remember the common irregular plurals", "zh": "记住常见的不规则复数"},
        {"en": "Use countable and uncountable nouns correctly", "zh": "正确使用可数与不可数名词"},
    ],
    "phases": [
        {
            "id": "sp_one_many", "name": "One or Many", "zh": "一个还是多个",
            "concept": {
                "en": "Singular means one thing; plural means more than one. In English, most nouns form the plural by adding -s. The words this / that / these / those must also match: one thing → this, that; many things → these, those.",
                "zh": "单数指一个，复数指多个。英语中大多数名词加 -s 变复数。this / that / these / those 也要搭配一致：一个用 this、that；多个用 these、those。",
            },
            "rules": [
                {"label": "单数", "en": "one book, a car, an apple", "zh": "一本书、一辆车、一个苹果"},
                {"label": "复数 +s", "en": "two books, three cars, four apples", "zh": "两本书、三辆车、四个苹果"},
                {"label": "this / these", "en": "this book → these books", "zh": "这本书 → 这些书"},
                {"label": "that / those", "en": "that car → those cars", "zh": "那辆车 → 那些车"},
            ],
            "examples": [
                {"en": "I have one apple and two bananas.", "zh": "我有一个苹果和两根香蕉。"},
                {"en": "This pen is mine. These pens are yours.", "zh": "这支笔是我的，这些笔是你的。"},
                {"en": "Look at those birds in the sky!", "zh": "看天上那些鸟！"},
            ],
            "mistakes": [
                {"en": "❌ I have two dog. → Plural needs -s: I have two dogs.", "zh": "❌ 复数要加 s：I have two dogs.（我有两只狗。）"},
                {"en": "❌ This are my shoes. → One thing takes this + is: These are my shoes.", "zh": "❌ this 配 is：These are my shoes.（这些是我的鞋。）"},
            ],
        },
        {
            "id": "sp_spelling", "name": "Spelling Rules", "zh": "复数拼写规则",
            "concept": {
                "en": "Nouns ending in -s, -ss, -sh, -ch, -x or -o add -es. Nouns ending in consonant + y change to -ies. Nouns ending in -f or -fe often change to -ves.",
                "zh": "以 -s、-ss、-sh、-ch、-x、-o 结尾的名词加 -es；辅音字母 + y 结尾要变 -ies；以 -f / -fe 结尾的常变 -ves。",
            },
            "rules": [
                {"label": "加 -es", "en": "bus → buses; watch → watches; box → boxes; potato → potatoes", "zh": "公共汽车→buses；手表→watches；盒子→boxes；土豆→potatoes"},
                {"label": "辅音 + y", "en": "city → cities; baby → babies（但 boy → boys，元音+y 只加 s）", "zh": "城市→cities；婴儿→babies（但 boy→boys，元音+y 直接加 s）"},
                {"label": "f / fe → ves", "en": "knife → knives; leaf → leaves", "zh": "刀→knives；树叶→leaves"},
                {"label": "注意例外", "en": "photo → photos; piano → pianos; roof → roofs", "zh": "照片→photos；钢琴→pianos；屋顶→roofs"},
            ],
            "examples": [
                {"en": "Three buses stop at this station.", "zh": "三辆公交车停在这个站。"},
                {"en": "The babies are sleeping now.", "zh": "宝宝们现在正在睡觉。"},
                {"en": "Please cut the apples with clean knives.", "zh": "请用干净的刀切苹果。"},
            ],
            "mistakes": [
                {"en": "❌ two citys → two cities", "zh": "❌ city 变复数要去 y 加 ies：two cities（两座城市）。"},
                {"en": "❌ three watchs → three watches", "zh": "❌ watch 结尾是 ch，要加 es：three watches（三块手表）。"},
                {"en": "❌ two knifes → two knives", "zh": "❌ knife 的 f 变 v 再加 es：two knives（两把刀）。"},
            ],
        },
        {
            "id": "sp_irregular", "name": "Irregular Plurals", "zh": "不规则复数",
            "concept": {
                "en": "Some plurals do not follow any rule. You simply have to remember them: man → men, child → children, foot → feet. A few nouns look the same in singular and plural: sheep, fish.",
                "zh": "有些复数没有任何规则，只能记住：man → men（男人）、child → children（孩子）、foot → feet（脚）。少数名词单复数同形：sheep（羊）、fish（鱼）。",
            },
            "rules": [
                {"label": "元音变化", "en": "man → men; woman → women; foot → feet; tooth → teeth; mouse → mice", "zh": "男人→men；女人→women；脚→feet；牙→teeth；老鼠→mice"},
                {"label": "加 -en", "en": "child → children; ox → oxen", "zh": "孩子→children；公牛→oxen"},
                {"label": "单复同形", "en": "sheep → sheep; fish → fish; deer → deer", "zh": "羊、鱼、鹿 单复数相同"},
                {"label": "person → people", "en": "one person, two people", "zh": "一个人，两个人"},
            ],
            "examples": [
                {"en": "Three men are waiting at the door.", "zh": "三个男人在门口等着。"},
                {"en": "The children are playing with their toys.", "zh": "孩子们正在玩玩具。"},
                {"en": "There are five sheep on the hill.", "zh": "山丘上有五只羊。"},
            ],
            "mistakes": [
                {"en": "❌ two mans → two men", "zh": "❌ man 的复数是 men：two men（两个男人）。"},
                {"en": "❌ The mouses ran away. → The mice ran away.", "zh": "❌ mouse 的复数是 mice：The mice ran away.（老鼠跑掉了。）"},
                {"en": "❌ three sheeps → three sheep", "zh": "❌ sheep 单复数同形：three sheep（三只羊）。"},
            ],
        },
        {
            "id": "sp_countable", "name": "Countable & Uncountable", "zh": "可数与不可数",
            "concept": {
                "en": "Countable nouns can be counted: a book, two books, many books. Uncountable nouns cannot: water, rice, money, information, advice, homework. They take no a / an and no plural. Use a piece of, a glass of, a lot of to talk about amounts.",
                "zh": "可数名词可以数：一本书、两本书、许多书。不可数名词不能数：水、米饭、钱、信息、建议、作业。它们前面不加 a / an，也没有复数形式。表示数量可用 a piece of、a glass of、a lot of。",
            },
            "rules": [
                {"label": "可数", "en": "a book / two books / many books; a banana / some bananas", "zh": "一本书/两本书/许多书；一根香蕉/一些香蕉"},
                {"label": "不可数", "en": "water, rice, money, information, advice, homework, news", "zh": "水、米饭、钱、信息、建议、作业、新闻"},
                {"label": "计量表达", "en": "a glass of water; a piece of advice / paper / information", "zh": "一杯水；一条建议 / 一张纸 / 一条信息"},
                {"label": "单数动词", "en": "The news is good. Money makes things easier.", "zh": "The news is good.（新闻很好。）主语是不可数名词时用单数动词。"},
            ],
            "examples": [
                {"en": "I drink a glass of water every morning.", "zh": "我每天早上喝一杯水。"},
                {"en": "She gave me two pieces of advice.", "zh": "她给了我两条建议。"},
                {"en": "How much money do you need?", "zh": "你需要多少钱？"},
            ],
            "mistakes": [
                {"en": "❌ an information → a piece of information (or: some information)", "zh": "❌ information 不可数，不能说 an information：应说 a piece of information 或 some information。"},
                {"en": "❌ I have many moneys. → I have a lot of money.", "zh": "❌ money 不可数，没有复数：I have a lot of money.（我有很多钱。）"},
                {"en": "❌ The news are good. → The news is good.", "zh": "❌ news 看似复数，其实作单数：The news is good.（新闻很好。）"},
            ],
        },
    ],
}
