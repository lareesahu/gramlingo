# -*- coding: utf-8 -*-
"""Grammar Foundations deck 09 — Possessives / 物主代词与所有格 (standalone lecture, no game module)."""
LESSON = {
    "id": "possessives",
    "foundation": True,
    "name": "Possessives",
    "zh": "物主代词与所有格",
    "icon": "🔑",
    "accent": "#B8452E",
    "desc": {
        "en": "My, mine, Anna's — say who owns what. Learn possessive adjectives (my book), possessive pronouns (it's mine), and the 's genitive (Anna's book).",
        "zh": "my、mine、Anna's——说明东西属于谁。学习形容词性物主代词（my book）、名词性物主代词（it's mine）和 's 所有格（Anna's book）。",
    },
    "objectives": [
        {"en": "Use my / your / his / her / its / our / their before nouns", "zh": "在名词前正确使用物主代词"},
        {"en": "Use mine / yours / hers / ours / theirs alone", "zh": "单独使用名词性物主代词"},
        {"en": "Build the 's genitive for people and animals", "zh": "掌握人和动物的 's 所有格"},
        {"en": "Untangle tricky pairs: its / it's, her / hers", "zh": "辨析易混点：its / it's、her / hers"},
    ],
    "phases": [
        {
            "id": "poss_adj", "name": "my / your / his / her", "zh": "形容词性物主代词",
            "concept": {
                "en": "Possessive adjectives always come before a noun and say who it belongs to: my, your, his, her, its, our, their. They do not change with singular or plural nouns.",
                "zh": "形容词性物主代词永远放在名词前，说明归属：my、your、his、her、its、our、their。单复数名词前都用同一个词。",
            },
            "rules": [
                {"label": "对应人称", "en": "I → my; you → your; he → his; she → her; it → its; we → our; they → their", "zh": "我→我的；你→你的；他→他的；她→她的；它→它的；我们→我们的；他们→他们的"},
                {"label": "看所有者", "en": "Anna's book → her book; Tom's bike → his bike", "zh": "东西属于安娜 → her；属于汤姆 → his"},
                {"label": "its 用于物", "en": "The dog wagged its tail.", "zh": "狗摇了摇它的尾巴。"},
            ],
            "examples": [
                {"en": "This is my phone.", "zh": "这是我的手机。"},
                {"en": "Her name is Lily and his name is Leo.", "zh": "她叫莉莉，他叫利奥。"},
                {"en": "Our school is very big.", "zh": "我们的学校很大。"},
            ],
            "mistakes": [
                {"en": "❌ This is I book. → Before a noun, use my, not I: This is my book.", "zh": "❌ “我的书”用 my：This is my book.（这是我的书。）"},
                {"en": "❌ She mother is a doctor. → Use her: Her mother is a doctor.", "zh": "❌ “她的妈妈”用 her：Her mother is a doctor.（她妈妈是医生。）"},
                {"en": "❌ The dog is licking it's bowl. → its = 它的；it's = it is", "zh": "❌ 表示“它的”用 its，it's 是 it is：The dog is licking its bowl.（狗在舔它的碗。）"},
            ],
        },
        {
            "id": "poss_pron", "name": "mine / yours / hers", "zh": "名词性物主代词",
            "concept": {
                "en": "Possessive pronouns stand alone and mean 'my one / yours / his / hers / ours / theirs'. No noun follows them. This book is mine = This is my book.",
                "zh": "名词性物主代词单独使用，意思是“我的（那个）”，后面不再跟名词：mine、yours、his、hers、ours、theirs。This book is mine 就等于 This is my book。",
            },
            "rules": [
                {"label": "对应", "en": "my → mine; your → yours; her → hers; our → ours; their → theirs（his 不变）", "zh": "my→mine；your→yours；her→hers；our→ours；their→theirs（his 不变）"},
                {"label": "后面无名词", "en": "It's mine. (= my phone)", "zh": "它是我的。（= 我的手机）"},
                {"label": "问归属", "en": "Whose is this? → It's hers.", "zh": "这是谁的？→ 是她的。"},
            ],
            "examples": [
                {"en": "This umbrella is mine.", "zh": "这把伞是我的。"},
                {"en": "The blue car is theirs.", "zh": "那辆蓝色的车是他们的。"},
                {"en": "Is this pen yours or his?", "zh": "这支笔是你的还是他的？"},
            ],
            "mistakes": [
                {"en": "❌ This is my. → With no noun after it, use mine: This is mine.", "zh": "❌ 后面没有名词时用 mine：This is mine.（这是我的。）"},
                {"en": "❌ The bag is her. → Use hers: The bag is hers.", "zh": "❌ 单独作表语用 hers：The bag is hers.（这个包是她的。）"},
            ],
        },
        {
            "id": "poss_genitive", "name": "'s 所有格", "zh": "名词所有格 's",
            "concept": {
                "en": "For people and animals, add 's to show ownership: Anna's book, my brother's bike. For regular plurals, just add an apostrophe: my parents' house. For irregular plurals, keep 's: children's toys.",
                "zh": "表示人或动物的所属，加 's：Anna's book（安娜的书）。规则复数只加撇号：my parents' house（我父母的房子）。不规则复数仍加 's：children's toys（孩子们的玩具）。",
            },
            "rules": [
                {"label": "单数 + 's", "en": "Anna's book; Tom's bag; the dog's bowl", "zh": "安娜的书；汤姆的包；狗的碗"},
                {"label": "复数 + '", "en": "my parents' house; the students' books", "zh": "我父母的房子；学生们的书"},
                {"label": "不规则复数 + 's", "en": "children's toys; men's shoes", "zh": "孩子们的玩具；男鞋"},
                {"label": "Whose?", "en": "Whose phone is this? → It's Lucy's.", "zh": "这是谁的手机？→ 是露西的。"},
            ],
            "examples": [
                {"en": "That is Tom's backpack.", "zh": "那是汤姆的背包。"},
                {"en": "My grandparents' garden is beautiful.", "zh": "我爷爷奶奶的花园很漂亮。"},
                {"en": "Whose glasses are these? They're Mr. Wang's.", "zh": "这是谁的眼镜？是王老师的。"},
            ],
            "mistakes": [
                {"en": "❌ Annas book is new. → Need the apostrophe: Anna's book", "zh": "❌ 撇号不能省：Anna's book（安娜的书）。"},
                {"en": "❌ my parents's house → Regular plural takes only ': my parents' house", "zh": "❌ 规则复数只加撇号：my parents' house（我父母的房子）。"},
                {"en": "❌ Its Tom's car. → It's (= it is) Tom's car.", "zh": "❌ 这里表示“它是”，写 It's：It's Tom's car.（这是汤姆的车。）"},
            ],
        },
        {
            "id": "poss_mix", "name": "易混点辨析", "zh": "容易混淆的对",
            "concept": {
                "en": "Some pairs look alike but work differently. Train yourself to see which job the word is doing: my = adjective + noun; mine = pronoun alone. it's = it is; its = belonging to it. who's = who is; whose = belonging to whom.",
                "zh": "有些词长相接近，用法完全不同。训练自己看它们在句中的职责：my 后面跟名词；mine 单独用。it's = it is；its = 它的。who's = who is；whose = 谁的。",
            },
            "rules": [
                {"label": "my vs mine", "en": "my book（后面有名词）vs This book is mine（无名词）", "zh": "my book（后面有名词）vs This book is mine（没有名词）"},
                {"label": "his / her 双职", "en": "his book / it's his; her book / it's hers", "zh": "his、her 可作形容词也可单独用（his 不变，her 变 hers）"},
                {"label": "it's vs its", "en": "It's rainy. (= it is) · its name (= 它的)", "zh": "It's rainy（= it is）· its name（它的名字）"},
                {"label": "whose vs who's", "en": "Whose bag is this? · Who's at the door? (= who is)", "zh": "Whose bag?（谁的包）· Who's at the door?（谁在门口？）"},
            ],
            "examples": [
                {"en": "It's my turn. This seat is yours.", "zh": "轮到我了。这个座位是你的。"},
                {"en": "The company is proud of its history.", "zh": "这家公司为自己的历史感到自豪。"},
                {"en": "Whose jacket is this? I think it's Ben's.", "zh": "这是谁的夹克？我觉得是本（Ben）的。"},
            ],
            "mistakes": [
                {"en": "❌ Its raining outside. → it's = it is: It's raining outside.", "zh": "❌ “正在下雨”是 it is raining：It's raining outside.（外面在下雨。）"},
                {"en": "❌ Whose your teacher? → who's = who is: Who's your teacher?", "zh": "❌ 问“谁是”，用 Who's（who is）：Who's your teacher?（谁是你的老师？）"},
                {"en": "❌ This pen is your's. → No apostrophe: yours", "zh": "❌ yours 不加撇号：This pen is yours.（这支笔是你的。）"},
            ],
        },
    ],
}
