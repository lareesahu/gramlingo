# -*- coding: utf-8 -*-
"""Grammar Foundations deck 03 — Third Person / 第三人称 (standalone lecture, no game module)."""
LESSON = {
    "id": "third_person",
    "foundation": True,
    "name": "Third Person",
    "zh": "第三人称",
    "icon": "👤",
    "accent": "#7048E8",
    "desc": {
        "en": "He, she, it — when we talk about one other person or thing in the present, the verb changes: likes, goes, has, is. Learn the -s rule, does / doesn't, and short answers.",
        "zh": "他、她、它——谈论一个其他人或事物时，动词会变化：likes、goes、has、is。学会 -s 规则、does / doesn't 和简短回答。",
    },
    "objectives": [
        {"en": "Understand who 'third person singular' means", "zh": "理解“第三人称单数”指谁"},
        {"en": "Add -s / -es / -ies to verbs correctly", "zh": "正确给动词加 -s / -es / -ies"},
        {"en": "Use is and has with he, she, it", "zh": "会用 is 和 has 搭配 he / she / it"},
        {"en": "Build negatives and questions with doesn't / does", "zh": "用 doesn't / does 造否定句和疑问句"},
    ],
    "phases": [
        {
            "id": "tp_who", "name": "Who Is Third Person?", "zh": "谁算第三人称？",
            "concept": {
                "en": "Speakers and listeners: I / we are first person, you is second person. Everyone and everything else — he, she, it, a name, or a thing — is third person. Third person singular means ONE person or thing that is not you or me.",
                "zh": "说话人与听话人：I / we 是第一人称，you 是第二人称。除此之外——he、she、it、一个人名或一个事物——都是第三人称。第三人称单数指“不是你也不是我”的一个对象。",
            },
            "rules": [
                {"label": "第一人称", "en": "I, we — the speaker(s)", "zh": "我、我们——说话人"},
                {"label": "第二人称", "en": "you — the listener", "zh": "你——听话人"},
                {"label": "第三人称单数", "en": "he, she, it, Anna, my father, the cat, this phone", "zh": "他、她、它、安娜、我爸爸、那只猫、这部手机"},
                {"label": "复数", "en": "they, Anna and Tom, the cats — 不用 -s", "zh": "他们、安娜和汤姆、那些猫——复数不加 -s"},
            ],
            "examples": [
                {"en": "Anna is my sister. She is ten years old.", "zh": "安娜是我妹妹。她十岁了。"},
                {"en": "My father works in a hospital. He is a doctor.", "zh": "我爸爸在医院工作。他是医生。"},
                {"en": "Look at the dog. It is very cute!", "zh": "看那只狗。它非常可爱！"},
            ],
            "mistakes": [
                {"en": "❌ My mother he is a teacher. → Do not repeat the subject: My mother is a teacher.", "zh": "❌ 不要重复主语：My mother is a teacher.（我妈妈是老师。）"},
                {"en": "❌ Tom and Anna is my friends. → Two people are plural: Tom and Anna are my friends.", "zh": "❌ 两个人为复数，用 are：Tom and Anna are my friends.（汤姆和安娜是我的朋友。）"},
            ],
        },
        {
            "id": "tp_s", "name": "The -s Rule", "zh": "动词加 -s 规则",
            "concept": {
                "en": "In the present simple, he / she / it takes a verb with -s: like → likes, work → works. Watch the spelling: -es after -s, -sh, -ch, -o, -x; consonant + y changes to -ies. And have becomes has.",
                "zh": "一般现在时中，he / she / it 后面的动词要加 -s：like → likes、work → works。注意拼写：-s、-sh、-ch、-o、-x 结尾加 -es；辅音 + y 变 -ies。have 要变成 has。",
            },
            "rules": [
                {"label": "一般加 -s", "en": "like → likes; work → works; play → plays", "zh": "喜欢→likes；工作→works；玩→plays"},
                {"label": "加 -es", "en": "go → goes; watch → watches; wash → washes; fix → fixes; do → does", "zh": "去→goes；看→watches；洗→washes；修理→fixes；做→does"},
                {"label": "辅音 + y", "en": "study → studies; carry → carries（但 play → plays，元音+y 加 s）", "zh": "学习→studies；搬运→carries（但 play→plays，元音+y 只加 s）"},
                {"label": "have → has", "en": "She has a cat. He has two brothers.", "zh": "她有一只猫。他有两个兄弟。"},
            ],
            "examples": [
                {"en": "She works at a big hospital.", "zh": "她在一家大医院工作。"},
                {"en": "He watches TV after dinner.", "zh": "他晚饭后看电视。"},
                {"en": "My father studies Chinese every evening.", "zh": "我爸爸每天晚上学中文。"},
            ],
            "mistakes": [
                {"en": "❌ He go to school by bus. → He goes to school by bus.", "zh": "❌ he 后面动词要加 -es：He goes to school by bus.（他坐公交上学。）"},
                {"en": "❌ She watch movies on weekends. → She watches movies on weekends.", "zh": "❌ watch 结尾 ch，加 es：She watches movies on weekends.（她周末看电影。）"},
                {"en": "❌ My brother have a bike. → My brother has a bike.", "zh": "❌ 第三人称单数用 has：My brother has a bike.（我弟弟有一辆自行车。）"},
            ],
        },
        {
            "id": "tp_be_has", "name": "Be and Have", "zh": "be 与 have 的变化",
            "concept": {
                "en": "The verb be has special forms: I am, he / she / it is, you / we / they are. Have also changes: he / she / it has. These are the most common verbs in English — get them right and your sentences sound natural.",
                "zh": "be 动词有特殊形式：I am，he / she / it is，you / we / they are。have 也会变化：he / she / it 用 has。这是英语中最常用的动词，用对它们句子才自然。",
            },
            "rules": [
                {"label": "I → am", "en": "I am a student.", "zh": "我是学生。"},
                {"label": "he / she / it → is", "en": "She is a nurse. It is sunny today.", "zh": "她是护士。今天阳光明媚。"},
                {"label": "you / we / they → are", "en": "You are welcome. We are classmates.", "zh": "不客气。我们是同学。"},
                {"label": "have → has", "en": "He has a new phone. Anna has long hair.", "zh": "他有一部新手机。安娜有一头长发。"},
            ],
            "examples": [
                {"en": "My mother is a doctor and my father is an engineer.", "zh": "我妈妈是医生，我爸爸是工程师。"},
                {"en": "It is very cold today.", "zh": "今天很冷。"},
                {"en": "She has a lovely little dog.", "zh": "她有一只可爱的小狗。"},
            ],
            "mistakes": [
                {"en": "❌ She are very happy. → She is very happy.", "zh": "❌ she 配 is：She is very happy.（她非常开心。）"},
                {"en": "❌ He have a car. → He has a car.", "zh": "❌ 第三人称单数用 has：He has a car.（他有一辆车。）"},
                {"en": "❌ Anna is my friend and I am is her classmate. → Say: … and I am her classmate.", "zh": "❌ 一个主语配一个 be 动词即可：and I am her classmate。（而我是她的同班同学。）"},
            ],
        },
        {
            "id": "tp_neg_ques", "name": "Negatives & Questions", "zh": "否定句与疑问句",
            "concept": {
                "en": "To make negatives and questions with he / she / it, use does or doesn't + the base verb (no -s). The -s travels onto does: She likes tea → She doesn't like tea → Does she like tea? Short answers: Yes, she does. / No, he doesn't.",
                "zh": "he / she / it 的否定句和疑问句要用 does / doesn't + 动词原形（不加 -s）。-s 跑到 does 上：She likes tea → She doesn't like tea → Does she like tea? 简短回答：Yes, she does.（是的。）/ No, he doesn't.（不。）",
            },
            "rules": [
                {"label": "否定", "en": "doesn't + 原形：She doesn't like coffee.", "zh": "doesn't + 动词原形：她不喜欢咖啡。"},
                {"label": "疑问", "en": "Does + 主语 + 原形？Does he live here?", "zh": "Does + 主语 + 动词原形？他住在这里吗？"},
                {"label": "原形回归", "en": "Main verb loses its -s: likes → like", "zh": "主要动词去掉 -s：likes 变回 like"},
                {"label": "简短回答", "en": "Yes, she does. / No, he doesn't.", "zh": "是的，她喜欢。/ 不，他不。"},
            ],
            "examples": [
                {"en": "He doesn't play football on Mondays.", "zh": "他周一不踢足球。"},
                {"en": "Does your mother speak English?", "zh": "你妈妈会说英语吗？"},
                {"en": "No, she doesn't, but she is learning it now.", "zh": "不，她不会，但她现在正在学。"},
            ],
            "mistakes": [
                {"en": "❌ She doesn't likes coffee. → The main verb goes back to base form: She doesn't like coffee.", "zh": "❌ doesn't 后面用动词原形：She doesn't like coffee.（她不喜欢咖啡。）"},
                {"en": "❌ Does he works here? → Does he work here?", "zh": "❌ does 后面的动词不加 -s：Does he work here?（他在这里工作吗？）"},
                {"en": "❌ He don't like tea. → He doesn't like tea.", "zh": "❌ he 用 doesn't，不用 don't：He doesn't like tea.（他不喜欢茶。）"},
            ],
        },
    ],
}
