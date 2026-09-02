# -*- coding: utf-8 -*-
"""Grammar Foundations deck 06 — Question Words / 疑问词 (standalone lecture, no game module)."""
LESSON = {
    "id": "question_words",
    "foundation": True,
    "name": "Question Words",
    "zh": "疑问词",
    "icon": "❓",
    "accent": "#E64980",
    "desc": {
        "en": "What, who, where, when, why, how — ask about things, people, places, time, reasons, and ways. Learn each word and the word order questions need.",
        "zh": "What、who、where、when、why、how——询问事物、人物、地点、时间、原因与方式，并学会疑问句的语序。",
    },
    "objectives": [
        {"en": "Use what and who for things and people", "zh": "用 what 问事物、who 问人"},
        {"en": "Use where and when for places and time", "zh": "用 where 问地点、when 问时间"},
        {"en": "Use why and how for reasons and ways", "zh": "用 why 问原因、how 问方式"},
        {"en": "Put the question word order right", "zh": "掌握疑问句的正确语序"},
    ],
    "phases": [
        {
            "id": "qw_what_who", "name": "What & Who", "zh": "什么 · 谁",
            "concept": {
                "en": "what asks about things, ideas, or information. who asks about people. When what or who is the subject of the question, no do / does is needed.",
                "zh": "what 询问事物、想法或信息；who 询问人。当 what / who 本身就是主语时，不需要 do / does。",
            },
            "rules": [
                {"label": "What", "en": "What is this? What do you like?", "zh": "这是什么？你喜欢什么？"},
                {"label": "Who", "en": "Who is that girl? Who is your teacher?", "zh": "那个女孩是谁？你的老师是谁？"},
                {"label": "问职业", "en": "What does he do? → He is a doctor.", "zh": "他是做什么的？→ 他是医生。"},
            ],
            "examples": [
                {"en": "What is your name?", "zh": "你叫什么名字？"},
                {"en": "What do you usually do on weekends?", "zh": "你周末通常做什么？"},
                {"en": "Who is the boy in the blue shirt?", "zh": "穿蓝色衬衫的那个男孩是谁？"},
            ],
            "mistakes": [
                {"en": "❌ Who is your name? → Names are information, so ask: What is your name?", "zh": "❌ 问名字用 what：What is your name?（你叫什么名字？）"},
                {"en": "❌ What is the woman?（把职业当成身份问句时较生硬）→ Who is the woman? / What does she do?", "zh": "❌ 问身份用 who，问职业用 what does she do？"},
            ],
        },
        {
            "id": "qw_where_when", "name": "Where & When", "zh": "哪里 · 何时",
            "concept": {
                "en": "where asks about places — where something or someone is, or where an action happens. when asks about time. Answers often start with in, on, at, or every.",
                "zh": "where 询问地点——某人某物在哪里，或动作发生在哪里。when 询问时间，回答常用 in、on、at 或 every。",
            },
            "rules": [
                {"label": "Where", "en": "Where are you from? Where is the station?", "zh": "你来自哪里？车站在哪里？"},
                {"label": "When", "en": "When do you get up? When is your birthday?", "zh": "你几点起床？你的生日是什么时候？"},
                {"label": "时间回答", "en": "at 7 o'clock · on Monday · in July · every day", "zh": "七点 · 周一 · 七月 · 每天"},
            ],
            "examples": [
                {"en": "Where do you live?", "zh": "你住在哪里？"},
                {"en": "Where are my glasses? I can't find them.", "zh": "我的眼镜在哪里？我找不到了。"},
                {"en": "When does the movie start?", "zh": "电影什么时候开始？"},
            ],
            "mistakes": [
                {"en": "❌ Where you live? → Questions need do: Where do you live?", "zh": "❌ 疑问句要加 do：Where do you live?（你住在哪里？）"},
                {"en": "❌ When you go to school? → When do you go to school?", "zh": "❌ 少助动词：When do you go to school?（你什么时候上学？）"},
            ],
        },
        {
            "id": "qw_why_how", "name": "Why & How", "zh": "为什么 · 怎么样",
            "concept": {
                "en": "why asks for reasons — answers often start with because. how asks about the way something happens, or combines with an adjective: how old, how much, how many, how long.",
                "zh": "why 询问原因，回答常用 because；how 询问做事的方式，也可以接形容词：how old（多大）、how much（多少钱）、how many（多少个）、how long（多久）。",
            },
            "rules": [
                {"label": "Why", "en": "Why are you late? → Because I missed the bus.", "zh": "你为什么迟到？→ 因为我没赶上公交。"},
                {"label": "How 方式", "en": "How do you go to school? — by bus / on foot", "zh": "你怎么上学？— 坐公交 / 走路"},
                {"label": "how + 形容词", "en": "how old / how much / how many / how long", "zh": "多大年纪 / 多少钱 / 多少个 / 多长时间"},
            ],
            "examples": [
                {"en": "Why is she crying?", "zh": "她为什么在哭？"},
                {"en": "How do you learn new words?", "zh": "你是怎么学新单词的？"},
                {"en": "How many languages do you speak?", "zh": "你会说几种语言？"},
            ],
            "mistakes": [
                {"en": "❌ Why you are late? → Word order: Why are you late?", "zh": "❌ 疑问句 be 提前：Why are you late?（你为什么迟到？）"},
                {"en": "❌ How much books do you have? → Countable nouns use how many: How many books?", "zh": "❌ 可数名词用 how many：How many books do you have?（你有多少本书？）"},
            ],
        },
        {
            "id": "qw_order", "name": "Question Word Order", "zh": "疑问句语序",
            "concept": {
                "en": "Most questions follow: question word + be / do / does + subject + verb? But when who or what is the subject (it does the action), the word order stays normal: Who + verb.",
                "zh": "大多数疑问句语序：疑问词 + be / do / does + 主语 + 动词？但当 who / what 本身就是主语（动作由它发出）时，语序不变：Who + 动词。",
            },
            "rules": [
                {"label": "be 提前", "en": "Where is she? Why are they happy?", "zh": "她在哪里？他们为什么开心？"},
                {"label": "do / does 帮忙", "en": "What do you want? Where does she work?", "zh": "你想要什么？她在哪里工作？"},
                {"label": "who / what 作主语", "en": "Who likes tea? What happened?（不加 does）", "zh": "谁喜欢喝茶？发生了什么？（不需要 does）"},
            ],
            "examples": [
                {"en": "Who broke the window?", "zh": "谁打破了窗户？"},
                {"en": "What makes you happy?", "zh": "什么让你开心？"},
                {"en": "What do you want to eat tonight?", "zh": "今晚你想吃什么？"},
            ],
            "mistakes": [
                {"en": "❌ Who does like tea? → who is the subject, so no does: Who likes tea?", "zh": "❌ who 作主语时不要加 does：Who likes tea?（谁喜欢喝茶？）"},
                {"en": "❌ What did happened? → Use the base verb after did: What happened?", "zh": "❌ did 后面用动词原形 happen：What happened?（发生了什么？）"},
            ],
        },
    ],
}
