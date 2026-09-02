# -*- coding: utf-8 -*-
"""Grammar Foundations deck 04 — Word Building / 构词法·词缀 (standalone lecture, no game module)."""
LESSON = {
    "id": "word_building",
    "foundation": True,
    "name": "Word Building",
    "zh": "构词法 · 词根与词缀",
    "icon": "🌱",
    "accent": "#1971C2",
    "desc": {
        "en": "Grow your vocabulary from roots: teach → teacher, act → action, nation → national → nationalism. Learn the suffixes -er / -or, -tion, -al and -ism.",
        "zh": "从词根长出词汇：teach → teacher（教→教师）、act → action（做→行动）、nation → national → nationalism（国家→国家的→民族主义）。学习 -er / -or、-tion、-al、-ism 后缀。",
    },
    "objectives": [
        {"en": "See how suffixes grow new words from roots", "zh": "理解后缀如何从词根衍生新词"},
        {"en": "Make 'doer' nouns with -er / -or", "zh": "用 -er / -or 构成“做某事的人”"},
        {"en": "Turn verbs into nouns with -tion / -sion", "zh": "用 -tion / -sion 把动词变成名词"},
        {"en": "Build adjectives with -al and belief nouns with -ism", "zh": "用 -al 构形容词、-ism 构“主义”名词"},
    ],
    "phases": [
        {
            "id": "wb_roots", "name": "Roots & Suffixes", "zh": "词根与后缀",
            "concept": {
                "en": "Many English words are built from a base word (the root) plus small endings called suffixes. A suffix can change the meaning — and often the word class: teach (verb) → teacher (noun). Learn a few suffixes and one root gives you several words.",
                "zh": "许多英语单词由“词根 + 后缀”构成。后缀可以改变词义，也常常改变词性：teach（动词，教）→ teacher（名词，教师）。学会几个后缀，记住一个词根就能认识好几个词。",
            },
            "rules": [
                {"label": "词根", "en": "the base meaning: teach, act, nation", "zh": "基本含义所在：教、做/行动、国家"},
                {"label": "后缀", "en": "the ending added to a root: -er, -tion, -al, -ism", "zh": "加在词根后面的部分：-er、-tion、-al、-ism"},
                {"label": "词性变化", "en": "verb → noun: teach → teacher; noun → adjective: nation → national", "zh": "动词→名词：teach→teacher；名词→形容词：nation→national"},
            ],
            "examples": [
                {"en": "teach → teacher: A teacher teaches students.", "zh": "teach（教）→ teacher（教师）：教师教学生。"},
                {"en": "sing → singer: My sister is a good singer.", "zh": "sing（唱）→ singer（歌手）：我姐姐是个好歌手。"},
                {"en": "act → action: We must take action now.", "zh": "act（行动）→ action（行动/措施）：我们必须现在采取行动。"},
            ],
            "mistakes": [
                {"en": "❌ She is a teach. → A person who teaches is a teacher.", "zh": "❌ “教的人”是 teacher，不是 teach：She is a teacher.（她是教师。）"},
                {"en": "❌ The educate is very important. → Use the noun: Education is very important.", "zh": "❌ “教育”作名词是 education：Education is very important.（教育非常重要。）"},
            ],
        },
        {
            "id": "wb_er_or", "name": "-er / -or", "zh": "-er / -or 表示“做…的人”",
            "concept": {
                "en": "Add -er or -or to many verbs to name the person who does the action: teach → teacher, work → worker, act → actor, visit → visitor. Watch the spelling: write → writer (drop the silent e), run → runner (double the consonant).",
                "zh": "在许多动词后加 -er 或 -or，表示“做这个动作的人”：teach→teacher（教师）、work→worker（工人）、act→actor（演员）、visit→visitor（访客）。注意拼写：write→writer（去掉不发音的 e）、run→runner（双写辅音）。",
            },
            "rules": [
                {"label": "加 -er", "en": "teach → teacher; work → worker; play → player; drive → driver", "zh": "教→教师；工作→工人；玩→球员；开车→司机"},
                {"label": "去 e 加 -er", "en": "write → writer; dance → dancer; make → maker", "zh": "写→作家；跳舞→舞者；制造→制造者"},
                {"label": "双写加 -er", "en": "run → runner; swim → swimmer", "zh": "跑→跑步者；游泳→游泳者"},
                {"label": "加 -or", "en": "act → actor; visit → visitor; invent → inventor", "zh": "表演→演员；参观→访客；发明→发明家"},
            ],
            "examples": [
                {"en": "A teacher teaches; a learner learns.", "zh": "教师负责教，学习者负责学。"},
                {"en": "My uncle is a famous actor.", "zh": "我叔叔是一位著名的演员。"},
                {"en": "The runner won the race!", "zh": "那位跑步者赢得了比赛！"},
            ],
            "mistakes": [
                {"en": "❌ acter → actor（-or，不是 -er）", "zh": "❌ actor 用 -or：actor（演员）。"},
                {"en": "❌ A teacher teach English. → A teacher teaches English.", "zh": "❌ 主语第三人称单数时动词加 -s：A teacher teaches English.（教师教英语。）"},
                {"en": "❌ He is a good runer. → He is a good runner.", "zh": "❌ run 要双写 n 再加 -er：runner（跑步者）。"},
            ],
        },
        {
            "id": "wb_tion", "name": "-tion / -sion", "zh": "-tion / -sion 动词变名词",
            "concept": {
                "en": "Add -tion or -sion to many verbs to make nouns of actions, states, or results: act → action, educate → education, inform → information, decide → decision. Spelling tip: verbs ending in -te take -tion; verbs ending in -de often take -sion.",
                "zh": "在许多动词后加 -tion 或 -sion，构成表示“动作、状态或结果”的名词：act→action（行动）、educate→education（教育）、inform→information（信息）、decide→decision（决定）。拼写提示：以 -te 结尾的动词接 -tion；以 -de 结尾的常接 -sion。",
            },
            "rules": [
                {"label": "-te → -tion", "en": "educate → education; create → creation; celebrate → celebration", "zh": "教育→教育；创造→创造；庆祝→庆祝"},
                {"label": "-de → -sion", "en": "decide → decision; divide → division", "zh": "决定→决定；分开→除法/分歧"},
                {"label": "其他 -tion", "en": "act → action; inform → information; invent → invention", "zh": "行动→行动；告知→信息；发明→发明"},
                {"label": "常为不可数", "en": "information 不可数：some information, a piece of information", "zh": "information 不可数：一些信息、一条信息"},
            ],
            "examples": [
                {"en": "act → action: Actions speak louder than words.", "zh": "act（行动）→ action：行动胜于言语。"},
                {"en": "Education changes lives.", "zh": "教育改变人生。"},
                {"en": "She made a quick decision.", "zh": "她很快做出了决定。"},
            ],
            "mistakes": [
                {"en": "❌ I need an information. → information is uncountable: I need some information.", "zh": "❌ information 不可数：I need some information.（我需要一些信息。）"},
                {"en": "❌ invent is useful. → Use the noun: The invention is useful.", "zh": "❌ “发明物/发明”作名词是 invention：The invention is useful.（这项发明很有用。）"},
            ],
        },
        {
            "id": "wb_al", "name": "-al 名词变形容词", "zh": "-al 构成形容词",
            "concept": {
                "en": "Add -al to many nouns to make adjectives meaning 'relating to': nation → national, education → educational, profession → professional, tradition → traditional. Watch spelling changes: nature → natural, music → musical.",
                "zh": "在许多名词后加 -al，构成“与…有关的”形容词：nation（国家）→ national（国家的）、education（教育）→ educational（教育的）、profession（职业）→ professional（职业的/专业的）、tradition（传统）→ traditional（传统的）。注意拼写变化：nature→natural、music→musical。",
            },
            "rules": [
                {"label": "-tion → -tional", "en": "education → educational; tradition → traditional", "zh": "教育→教育的；传统→传统的"},
                {"label": "nation → national", "en": "national flag, national team", "zh": "国旗、国家队"},
                {"label": "profession → professional", "en": "professional advice, a professional player", "zh": "专业的建议、职业球员"},
                {"label": "拼写变化", "en": "nature → natural; music → musical; culture → cultural", "zh": "自然→自然的；音乐→音乐的；文化→文化的"},
            ],
            "examples": [
                {"en": "This is a national holiday.", "zh": "这是一个全国性的节日。"},
                {"en": "Educational games help children learn.", "zh": "教育类游戏帮助孩子学习。"},
                {"en": "You should ask a professional for advice.", "zh": "你应该咨询专业人士的意见。"},
            ],
            "mistakes": [
                {"en": "❌ a nation festival → a national festival", "zh": "❌ “国家的节日”用形容词 national：a national festival（国庆节/全国性节日）。"},
                {"en": "❌ an education video → an educational video", "zh": "❌ “教育类的视频”用形容词 educational：an educational video（教育视频）。"},
            ],
        },
        {
            "id": "wb_ism", "name": "-ism 主义与信念", "zh": "-ism 表示主义/体系",
            "concept": {
                "en": "The suffix -ism makes nouns for beliefs, systems, or movements. See how a word can grow step by step: profession → professional → professionalism; nation → national → nationalism; environment → environmental → environmentalism.",
                "zh": "后缀 -ism 构成表示“主义、体系、运动”的名词。看一个词如何一步步长大：profession（职业）→ professional（专业的）→ professionalism（专业精神）；nation（国家）→ national（国家的）→ nationalism（民族主义）；environment（环境）→ environmental（环境的）→ environmentalism（环保主义）。",
            },
            "rules": [
                {"label": "-al + ism", "en": "professional → professionalism; traditional → traditionalism", "zh": "专业的→专业精神；传统的→传统主义"},
                {"label": "常见 -ism 词", "en": "capital → capitalism; tour → tourism; real → realism", "zh": "资本→资本主义；旅游→旅游业；现实→现实主义"},
                {"label": "词义方向", "en": "名词/形容词 + ism = 一种信念或体系", "zh": "名词/形容词 + ism = 一种信念或体系"},
                {"label": "不可随意造词", "en": "只有真实存在的词才能用：可说 tourism，不说 bookism", "zh": "只有真实存在的词才能用：可以说 tourism，不能自己造 bookism"},
            ],
            "examples": [
                {"en": "profession → professional → professionalism: Her professionalism impressed everyone.", "zh": "职业→专业的→专业精神：她的专业精神打动了所有人。"},
                {"en": "nation → national → nationalism: Sports can unite people beyond nationalism.", "zh": "国家→国家的→民族主义：体育能把人们团结起来，超越民族主义。"},
                {"en": "Tourism brings money to small towns.", "zh": "旅游业为小镇带来收入。"},
            ],
            "mistakes": [
                {"en": "❌ He is famous for his professional. → Use the noun: his professionalism.", "zh": "❌ “专业精神”是 professionalism：He is famous for his professionalism.（他以专业精神著称。）"},
                {"en": "❌ I love the tradition food. → Use the adjective: traditional food.", "zh": "❌ “传统的食物”用形容词 traditional：traditional food（传统美食）。"},
                {"en": "❌ 造词如 teacheism ✗ → 查词典，用真实存在的词", "zh": "❌ 不要随意创造 -ism 词：先查词典确认，用真实存在的词。"},
            ],
        },
    ],
}
