# -*- coding: utf-8 -*-
LESSON = {
    "id": "determiners",
    "name": "Articles & Determiners",
    "zh": "冠词与限定词",
    "icon": "🏷️",
    "accent": "#6741D9",
    "desc": {"en": "Signal whether nouns are known, specific, general, countable, or quantified.", "zh": "标示名词是已知、特指、泛指、可数还是量化。"},
    "objectives": [
        {"en": "Use a/an, the, and zero article correctly", "zh": "正确使用 a/an、the 和零冠词"},
        {"en": "Distinguish definite from indefinite reference", "zh": "区分定指与不定指"},
        {"en": "Choose quantifiers like some, any, much, many, few", "zh": "选择 some、any、much、many、few 等量词"},
        {"en": "Use demonstratives, possessives, and generic reference", "zh": "使用指示词、所有格与类指"},
    ],
    "phases": [
        {
            "id": "determiners_articles", "name": "Articles", "zh": "冠词",
            "concept": {"en": "a/an = one, non-specific, first mention (a before consonants, an before vowels); the = specific or known; zero article = general plural or uncountable.", "zh": "a/an 表【一个】，不特指，首次提及（辅音前用 a，元音前用 an）；the 表特指或已知；零冠词用于泛指复数或不可数。"},
            "rules": [
                {"label": "a/an", "en": "I saw a dog. / an apple; an hour (silent h).", "zh": "我见到一只狗。/ 一个苹果；an hour（h 不发音）。"},
                {"label": "the", "en": "The dog I saw was black. (specific)", "zh": "我见到的那只狗是黑色的。（特指）"},
                {"label": "零冠词", "en": "Dogs are friendly. / Water is important. (general)", "zh": "狗很友好。/ 水很重要。（泛指）"},
            ],
            "examples": [
                {"en": "She bought a car last week.", "zh": "她上周买了一辆车。"},
                {"en": "The car is parked outside.", "zh": "那辆车停在门外。"},
                {"en": "Children love ice cream.", "zh": "孩子们喜欢冰淇淋。"},
            ],
            "mistakes": [
                {"en": "❌ an university → a university (yoo sound).", "zh": "❌ university 发 /juː/，用 a。"},
                {"en": "❌ The dogs are friendly (general) → zero article: Dogs are friendly.", "zh": "❌ 泛指复数不加 the。"},
            ],
        },
        {
            "id": "determiners_definite", "name": "Definite vs Indefinite", "zh": "定指与不定指",
            "concept": {"en": "Use the when both speaker and listener know which one (mentioned before, unique, or clear from context). Use a/an for new or one-of-many.", "zh": "说话双方都知道是哪一个（前面提过、独一无二或语境明确）时用 the；新提到或众多之一用 a/an。"},
            "rules": [
                {"label": "提过", "en": "I saw a bird. The bird was singing.", "zh": "我看到一只鸟。那只鸟在唱歌。"},
                {"label": "独一无二", "en": "the sun, the moon, the president", "zh": "the sun（太阳）、the moon（月亮）"},
                {"label": "语境明确", "en": "Please close the door. (we know which door)", "zh": "请关门。（知道是哪扇门）"},
            ],
            "examples": [
                {"en": "There is a book on the desk. The book is mine.", "zh": "桌上有一本书。那本书是我的。"},
                {"en": "She is the manager of this store.", "zh": "她是这家店的经理。"},
                {"en": "I need a pen. Do you have one?", "zh": "我需要一支笔。你有吗？"},
            ],
            "mistakes": [
                {"en": "❌ I saw the bird (first mention) → a bird.", "zh": "❌ 首次提及用 a。"},
                {"en": "❌ the first mention of a non-specific thing → a/an.", "zh": "❌ 不特指时用 a/an。"},
            ],
        },
        {
            "id": "determiners_quantifiers", "name": "Quantifiers", "zh": "量词",
            "concept": {"en": "some = positive/offer; any = negative/question; much/little = uncountable; many/few = countable; a few = some (positive), few = almost none.", "zh": "some 用于肯定/提议；any 用于否定/疑问；much/little 修饰不可数；many/few 修饰可数；a few 表示【有一些】（肯定），few 表示【几乎没有】。"},
            "rules": [
                {"label": "可数", "en": "many books, a few friends, few chances", "zh": "many books（很多书）、a few friends（几个朋友）、few chances（几乎没有机会）"},
                {"label": "不可数", "en": "much time, a little sugar, little water", "zh": "much time（很多时间）、a little sugar（一点糖）、little water（几乎没有水）"},
                {"label": "some/any", "en": "I have some money. Do you have any? No, I don't have any.", "zh": "我有些钱。你有吗？不，我没有。"},
            ],
            "examples": [
                {"en": "Would you like some tea?", "zh": "要来点茶吗？"},
                {"en": "There aren't many seats left.", "zh": "剩下的座位不多了。"},
                {"en": "She has a few good ideas.", "zh": "她有一些好主意。"},
            ],
            "mistakes": [
                {"en": "❌ many water → much water (uncountable).", "zh": "❌ 不可数用 much。"},
                {"en": "❌ I don't have some → any in negatives: I don't have any.", "zh": "❌ 否定句用 any。"},
            ],
        },
        {
            "id": "determiners_demonstratives", "name": "Demonstratives", "zh": "指示词",
            "concept": {"en": "this/these = near; that/those = far. They point at people or things and agree in number.", "zh": "this/these 表近；that/those 表远。指示词在单复数上要一致。"},
            "rules": [
                {"label": "近", "en": "this book (singular), these books (plural)", "zh": "this book（这本书）、these books（这些书）"},
                {"label": "远", "en": "that house, those houses", "zh": "that house（那栋房子）、those houses（那些房子）"},
            ],
            "examples": [
                {"en": "This is my friend Tom.", "zh": "这是我的朋友汤姆。"},
                {"en": "Those shoes are expensive.", "zh": "那些鞋很贵。"},
                {"en": "Look at that bird in the tree.", "zh": "看树上的那只鸟。"},
            ],
            "mistakes": [
                {"en": "❌ these book → these books (plural).", "zh": "❌ these 后接复数。"},
                {"en": "❌ this books → this book.", "zh": "❌ this 后接单数。"},
            ],
        },
        {
            "id": "determiners_possessives", "name": "Possessives", "zh": "所有格",
            "concept": {"en": "Possessive determiners: my, your, his, her, its, our, their. They always come before a noun and agree with the owner, not the thing.", "zh": "所有格限定词：my、your、his、her、its、our、their。它们修饰名词，与所有者一致，而非与事物一致。"},
            "rules": [
                {"label": "形式", "en": "my book, your phone, his car, her bag, its tail, our home, their toys", "zh": "my book（我的书）、your phone（你的手机）、his car（他的车）……"},
                {"label": "不随事物", "en": "She has a brother. Her brother is tall. (her matches she)", "zh": "her 与所有者 she 一致。"},
            ],
            "examples": [
                {"en": "Is this your umbrella?", "zh": "这是你的伞吗？"},
                {"en": "The dog wagged its tail.", "zh": "狗摇了摇尾巴。"},
                {"en": "Their house is near the river.", "zh": "他们的房子在河边。"},
            ],
            "mistakes": [
                {"en": "❌ its vs it's: its = possessive; it's = it is.", "zh": "❌ its（它的）与 it's（它是）别混淆。"},
                {"en": "❌ her brother and his sister — match the owner, not the noun.", "zh": "❌ 所有格与所有者一致。"},
            ],
        },
        {
            "id": "determiners_generics", "name": "Generic Reference", "zh": "类指",
            "concept": {"en": "Talk about a whole class with: zero article + plural (Dogs are loyal), the + singular (The lion is a big cat), or a/an + singular (A teacher helps students).", "zh": "谈论整个类别：零冠词 + 复数（Dogs are loyal）、the + 单数（The lion...）、或 a/an + 单数（A teacher...）。"},
            "rules": [
                {"label": "复数类指", "en": "Cats are independent.", "zh": "猫是独立的。（泛指所有猫）"},
                {"label": "the + 单数", "en": "The smartphone changed communication.", "zh": "智能手机改变了沟通方式。"},
                {"label": "a/an + 单数", "en": "A doctor saves lives.", "zh": "医生救死扶伤。"},
            ],
            "examples": [
                {"en": "Elephants are intelligent animals.", "zh": "大象是聪明的动物。"},
                {"en": "The bicycle is a green way to travel.", "zh": "自行车是绿色出行方式。"},
                {"en": "A good book is a good friend.", "zh": "好书如好友。"},
            ],
            "mistakes": [
                {"en": "❌ The elephants are intelligent (general) → zero article: Elephants are...", "zh": "❌ 泛指用零冠词。"},
                {"en": "❌ Mixing plural generic with singular verb.", "zh": "❌ 类指单复数要一致。"},
            ],
        },
        {
            "id": "determiners_contrast", "name": "Determiner Contrast", "zh": "限定词对比",
            "concept": {"en": "Choose the determiner by what you mean: known (the/this), unknown (a/an/some/any), quantity (many/much/few/little), ownership (my/your/his).", "zh": "按含义选限定词：已知（the/this）、未知（a/an/some/any）、数量（many/much/few/little）、所属（my/your/his）。"},
            "rules": [
                {"label": "已知性", "en": "the/this for known; a/an/some for new.", "zh": "已知用 the/this；新信息用 a/an/some。"},
                {"label": "数量", "en": "countable: many/few; uncountable: much/little.", "zh": "可数：many/few；不可数：much/little。"},
            ],
            "examples": [
                {"en": "I bought some apples. The apples are in the fridge.", "zh": "我买了些苹果。苹果在冰箱里。"},
                {"en": "How much time do we have?", "zh": "我们还有多少时间？"},
                {"en": "There are few people in the park today.", "zh": "今天公园里人很少。"},
            ],
            "mistakes": [
                {"en": "❌ How many time → how much time (uncountable).", "zh": "❌ time 不可数，用 how much。"},
                {"en": "❌ few vs a few: few = almost none; a few = some.", "zh": "❌ few 几乎为零；a few 有一些。"},
            ],
        },
        {
            "id": "determiners_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Edit texts by asking about each noun: Is it specific or general? Countable or uncountable? Singular or plural? Then choose the determiner.", "zh": "改错时对每个名词提问：特指还是泛指？可数还是不可数？单数还是复数？再选限定词。"},
            "rules": [
                {"label": "四问", "en": "specific? countable? plural? known? → the/a/an/zero/quantifier.", "zh": "特指？可数？复数？已知？→ 决定冠词与量词。"},
                {"label": "首尾一致", "en": "The determiner must agree with the noun number.", "zh": "限定词与名词单复数一致。"},
            ],
            "examples": [
                {"en": "❌ I have few questions to ask. (few = almost none) → I have a few questions to ask.", "zh": "❌ 想说「有几个问题」用 a few。"},
                {"en": "❌ She gave me an useful advice → She gave me useful advice. (advice uncountable, no article)", "zh": "❌ advice 不可数，不用 a/an。"},
                {"en": "✔ The teacher gave the students some useful advice.", "zh": "✔ 老师给学生们一些有用的建议。"},
            ],
            "mistakes": [
                {"en": "❌ informations → information (uncountable, no plural).", "zh": "❌ information 不可数。"},
                {"en": "❌ a equipment → equipment (uncountable): some equipment.", "zh": "❌ equipment 不可数。"},
            ],
        },
    ],
}
