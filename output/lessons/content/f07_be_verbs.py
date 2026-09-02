# -*- coding: utf-8 -*-
"""Grammar Foundations deck 07 — Be Verbs & There is/are / be 动词与存在句 (standalone lecture)."""
LESSON = {
    "id": "be_verbs",
    "foundation": True,
    "name": "Be & There is/are",
    "zh": "be 动词与存在句",
    "icon": "💬",
    "accent": "#4263EB",
    "desc": {
        "en": "am / is / are — the most useful verb in English. Say who people are, what things are like, where they are, and say 'there is / there are' for what exists somewhere.",
        "zh": "am / is / are——英语中最常用的动词。说明人的身份、事物的样子、所在的位置，并用 there is / there are 表示“某处有某物”。",
    },
    "objectives": [
        {"en": "Match am / is / are to the subject", "zh": "根据主语正确搭配 am / is / are"},
        {"en": "Use be + noun / adjective / place", "zh": "掌握 be + 名词 / 形容词 / 地点"},
        {"en": "Use there is / there are for existence", "zh": "用 there is / there are 表示存在"},
        {"en": "Make be and there sentences negative and ask questions", "zh": "掌握 be 句与存在句的否定和疑问"},
    ],
    "phases": [
        {
            "id": "be_forms", "name": "am / is / are", "zh": "be 动词三兄弟",
            "concept": {
                "en": "The verb be changes with the subject: I am, he / she / it is, you / we / they are. In speech and writing we often shorten them: I'm, she's, they're.",
                "zh": "be 动词随主语变化：I am，he / she / it is，you / we / they are。口语和书写中常缩写：I'm、she's、they're。",
            },
            "rules": [
                {"label": "I → am", "en": "I am a student. I'm from China.", "zh": "我是学生。我来自中国。"},
                {"label": "he / she / it → is", "en": "She is my friend. It is a cat.", "zh": "她是我的朋友。它是一只猫。"},
                {"label": "you / we / they → are", "en": "You are right. We are classmates.", "zh": "你是对的。我们是同学。"},
                {"label": "缩写", "en": "I'm · you're · he's · she's · it's · we're · they're", "zh": "I'm、you're、he's、she's、it's、we're、they're"},
            ],
            "examples": [
                {"en": "I am very happy today.", "zh": "我今天很开心。"},
                {"en": "She is my best friend.", "zh": "她是我最好的朋友。"},
                {"en": "They are my parents.", "zh": "他们是我的父母。"},
            ],
            "mistakes": [
                {"en": "❌ I are a teacher. → I takes am: I am a teacher.", "zh": "❌ I 搭配 am：I am a teacher.（我是老师。）"},
                {"en": "❌ She are a doctor. → she takes is: She is a doctor.", "zh": "❌ she 搭配 is：She is a doctor.（她是医生。）"},
                {"en": "❌ We is students. → we takes are: We are students.", "zh": "❌ we 搭配 are：We are students.（我们是学生。）"},
            ],
        },
        {
            "id": "be_use", "name": "be + 名词 / 形容词 / 地点", "zh": "be 后面接什么",
            "concept": {
                "en": "After be comes: a noun for identity (a teacher), an adjective for a state or quality (hot, tired), or a place phrase (at home, in Shanghai). Chinese often leaves out the 'is' — English never does.",
                "zh": "be 后面接三类内容：名词表身份（老师）、形容词表状态或特征（热、累）、地点短语（在家、在上海）。中文常省略“是/在”，英语绝不可以省。",
            },
            "rules": [
                {"label": "身份", "en": "be + 名词: My father is an engineer.", "zh": "be + 名词：我爸爸是工程师。"},
                {"label": "状态特征", "en": "be + 形容词: The soup is hot. I am tired.", "zh": "be + 形容词：汤很烫。我很累。"},
                {"label": "地点", "en": "be + 介词短语: We are at home.", "zh": "be + 介词短语：我们在家。"},
            ],
            "examples": [
                {"en": "My mother is a nurse.", "zh": "我妈妈是护士。"},
                {"en": "The coffee is too hot to drink.", "zh": "咖啡太烫了，没法喝。"},
                {"en": "They are in the classroom now.", "zh": "他们现在在教室里。"},
            ],
            "mistakes": [
                {"en": "❌ I hungry. → English needs the verb: I am hungry.", "zh": "❌ 中文可以说“我饿”，英语必须加 be：I am hungry.（我饿了。）"},
                {"en": "❌ She is doctor. → Need an article: She is a doctor.", "zh": "❌ 单数可数名词前要有冠词：She is a doctor.（她是医生。）"},
                {"en": "❌ They happy. → They are happy.", "zh": "❌ 不能省略 are：They are happy.（他们很开心。）"},
            ],
        },
        {
            "id": "there_is_are", "name": "There is / There are", "zh": "存在句：某处有……",
            "concept": {
                "en": "To say something exists somewhere, English uses there is (singular or uncountable) and there are (plural), followed by the thing and then the place.",
                "zh": "表示“某处有某物”用 there is（单数或不可数）和 there are（复数），后面先说东西再说地点。注意：不要翻译成 there has。",
            },
            "rules": [
                {"label": "单数", "en": "There is a book on the desk.", "zh": "桌上有一本书。"},
                {"label": "复数", "en": "There are two cats in the garden.", "zh": "花园里有两只猫。"},
                {"label": "不可数", "en": "There is some milk in the fridge.", "zh": "冰箱里有一些牛奶。"},
                {"label": "不用 have", "en": "存在句用 there is/are，不用 there has / there have", "zh": "存在句不用 there has / there have"},
            ],
            "examples": [
                {"en": "There is a park near my home.", "zh": "我家附近有一个公园。"},
                {"en": "There are many stars in the sky.", "zh": "天空中有许多星星。"},
                {"en": "There is some water in the bottle.", "zh": "瓶子里有一些水。"},
            ],
            "mistakes": [
                {"en": "❌ There has a book on the table. → There is a book on the table.", "zh": "❌ 存在句用 there is，不用 has：There is a book on the table.（桌上有一本书。）"},
                {"en": "❌ There are a bird in the tree. → Singular: There is a bird in the tree.", "zh": "❌ 一只鸟用 is：There is a bird in the tree.（树上有一只鸟。）"},
            ],
        },
        {
            "id": "there_neg_ques", "name": "否定与疑问", "zh": "存在句的否定与疑问",
            "concept": {
                "en": "Make there sentences negative with there isn't / there aren't (+ any), and ask questions with Is there ...? / Are there ...? Answer with Yes, there is / are, or No, there isn't / aren't.",
                "zh": "存在句的否定用 there isn't / there aren't（+ any）；疑问句把 is / are 提前：Is there...? / Are there...? 用 Yes, there is / are 或 No, there isn't / aren't 回答。",
            },
            "rules": [
                {"label": "否定", "en": "There isn't any sugar. There aren't any students.", "zh": "没有糖。没有学生。"},
                {"label": "疑问", "en": "Is there a bank near here? Are there any eggs?", "zh": "这附近有银行吗？有鸡蛋吗？"},
                {"label": "简短回答", "en": "Yes, there is. / No, there isn't. Yes, there are. / No, there aren't.", "zh": "是的，有。/ 不，没有。"},
            ],
            "examples": [
                {"en": "There isn't any milk left.", "zh": "没有牛奶剩下了。"},
                {"en": "Are there any good restaurants near here?", "zh": "这附近有好餐馆吗？"},
                {"en": "No, there aren't, but there is a great one downtown.", "zh": "没有，但市中心有一家很棒的。"},
            ],
            "mistakes": [
                {"en": "❌ There is no any water. → One negative only: There isn't any water (or: There is no water).", "zh": "❌ 不要双重否定：There isn't any water 或 There is no water。（没有水。）"},
                {"en": "❌ Are there some eggs? → Questions usually take any: Are there any eggs?", "zh": "❌ 疑问句一般用 any：Are there any eggs?（有鸡蛋吗？）"},
            ],
        },
    ],
}
