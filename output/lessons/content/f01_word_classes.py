# -*- coding: utf-8 -*-
"""Grammar Foundations deck 01 — Word Classes / 词性 (standalone lecture, no game module)."""
LESSON = {
    "id": "word_classes",
    "foundation": True,
    "name": "Word Classes",
    "zh": "词性",
    "icon": "🧩",
    "accent": "#E8590C",
    "desc": {
        "en": "Meet the building blocks of every sentence: nouns, verbs, adjectives, adverbs, pronouns and more — and learn quick tests to spot each one.",
        "zh": "认识构成句子的积木：名词、动词、形容词、副词、代词等，并学会快速识别它们的检验方法。",
    },
    "objectives": [
        {"en": "Name the main word classes in English", "zh": "说出英语的主要词性"},
        {"en": "Use quick tests to spot a noun or a verb", "zh": "用检验法快速识别名词与动词"},
        {"en": "Place adjectives and adverbs correctly", "zh": "正确摆放形容词与副词"},
        {"en": "Choose subject and object pronouns", "zh": "选用主格与宾格代词"},
    ],
    "phases": [
        {
            "id": "wc_nouns", "name": "Nouns", "zh": "名词",
            "concept": {
                "en": "A noun is a word that names a person, a place, a thing, or an idea. Quick test: if you can put a, an or the in front of a word — or make it plural — it is almost always a noun.",
                "zh": "名词是表示人、地点、事物或想法的词。快速检验：如果某个词前面可以加 a / an / the，或者可以变成复数，它通常就是名词。",
            },
            "rules": [
                {"label": "人", "en": "Anna, teacher, doctor, friend", "zh": "Anna、老师、医生、朋友"},
                {"label": "地点", "en": "school, park, Shanghai, office", "zh": "学校、公园、上海、办公室"},
                {"label": "事物与想法", "en": "book, music, freedom, happiness", "zh": "书、音乐、自由、幸福"},
                {"label": "检验法", "en": "a book / an apple / the sun → 名词", "zh": "a book / an apple / the sun → 名词"},
            ],
            "examples": [
                {"en": "The teacher reads a book in the park.", "zh": "老师正在公园里读书。"},
                {"en": "Music brings me happiness.", "zh": "音乐带给我快乐。"},
                {"en": "Anna is my best friend.", "zh": "安娜是我最好的朋友。"},
            ],
            "mistakes": [
                {"en": "❌ I like the beautiful. → Use a noun: I like beauty / beautiful things.", "zh": "❌ 形容词不能直接当名词：应说 I like beauty（我喜欢美）或 beautiful things（美丽的事物）。"},
                {"en": "❌ He has two cat. → Make the noun plural: He has two cats.", "zh": "❌ 复数名词要加 s：He has two cats.（他有两只猫。）"},
            ],
        },
        {
            "id": "wc_verbs", "name": "Verbs", "zh": "动词",
            "concept": {
                "en": "A verb says what the subject does or is. Every sentence needs one. Verbs can change their form to show time: walk, walked, will walk.",
                "zh": "动词说明主语做什么或是什么。每个句子都离不开动词。动词会随时间变化：walk（走）、walked（走过）、will walk（将走）。",
            },
            "rules": [
                {"label": "动作", "en": "run, eat, play, write, study", "zh": "跑、吃、玩、写、学习"},
                {"label": "状态", "en": "be, like, have, think, feel", "zh": "是、喜欢、有、想、感觉"},
                {"label": "句子核心", "en": "Every sentence has a verb: Birds sing.", "zh": "每个句子都有动词：Birds sing.（鸟儿歌唱。）"},
            ],
            "examples": [
                {"en": "I play football after school.", "zh": "我放学后踢足球。"},
                {"en": "She likes music very much.", "zh": "她非常喜欢音乐。"},
                {"en": "We are in the same class.", "zh": "我们在同一个班。"},
            ],
            "mistakes": [
                {"en": "❌ I am agree with you. → be + verb is wrong here: I agree with you.", "zh": "❌ agree 是动词，前面不要再加 am：I agree with you.（我同意你。）"},
                {"en": "❌ He can to swim. → After can, use the verb without to: He can swim.", "zh": "❌ can 后面用动词原形，不加 to：He can swim.（他会游泳。）"},
            ],
        },
        {
            "id": "wc_adjectives", "name": "Adjectives", "zh": "形容词",
            "concept": {
                "en": "An adjective describes a noun — what something is like. It usually goes before the noun, or after be (am / is / are / was / were).",
                "zh": "形容词描写名词，说明事物是什么样的。它通常放在名词前面，或放在 be 动词（am / is / are…）后面。",
            },
            "rules": [
                {"label": "名词之前", "en": "a red apple, a big house, a happy child", "zh": "一个红苹果、一座大房子、一个快乐的孩子"},
                {"label": "be 之后", "en": "The apple is red. She is happy.", "zh": "苹果是红的。她很快乐。"},
                {"label": "检验法", "en": "very + 形容词：very big, very delicious", "zh": "very + 形容词：非常大、非常美味"},
            ],
            "examples": [
                {"en": "It is a beautiful sunny day.", "zh": "今天是美丽晴朗的一天。"},
                {"en": "The soup smells delicious.", "zh": "这汤闻起来很香。"},
                {"en": "My little brother is very clever.", "zh": "我的小弟弟非常聪明。"},
            ],
            "mistakes": [
                {"en": "❌ She is a girl beautiful. → Adjectives come before nouns: a beautiful girl.", "zh": "❌ 形容词放在名词前：a beautiful girl（一个美丽的女孩）。"},
                {"en": "❌ The soup is deliciously. → After is, use the adjective: delicious.", "zh": "❌ is 后面用形容词：The soup is delicious.（汤很美味。）"},
            ],
        },
        {
            "id": "wc_adverbs", "name": "Adverbs", "zh": "副词",
            "concept": {
                "en": "An adverb describes a verb, an adjective, or another adverb. Many adverbs end in -ly (quickly, slowly), but some do not: fast, well, hard, early.",
                "zh": "副词修饰动词、形容词或另一个副词。许多副词以 -ly 结尾（quickly 快速地），也有一些不加 -ly：fast（快）、well（好）、hard（努力）、early（早）。",
            },
            "rules": [
                {"label": "修饰动词", "en": "She sings beautifully. He runs fast.", "zh": "她唱得很好听。他跑得很快。"},
                {"label": "修饰形容词", "en": "very good, really tired, extremely hot", "zh": "非常好、真的很累、极其炎热"},
                {"label": "常见 -ly", "en": "quickly, slowly, carefully, happily", "zh": "快速地、缓慢地、仔细地、开心地"},
                {"label": "不规则", "en": "fast, well, hard, early, late", "zh": "快、好、努力、早、晚"},
            ],
            "examples": [
                {"en": "Please speak slowly and clearly.", "zh": "请说慢一点、清楚一点。"},
                {"en": "She dances very well.", "zh": "她跳舞跳得很好。"},
                {"en": "He works hard every day.", "zh": "他每天都很努力地工作。"},
            ],
            "mistakes": [
                {"en": "❌ He runs very fastly. → fast has no -ly form: He runs very fast.", "zh": "❌ fast 不加 -ly：He runs very fast.（他跑得很快。）"},
                {"en": "❌ She sings beautiful. → To describe a verb, use the adverb: beautifully.", "zh": "❌ 修饰动词要用副词：She sings beautifully.（她唱得很好听。）"},
            ],
        },
        {
            "id": "wc_pronouns", "name": "Pronouns", "zh": "代词",
            "concept": {
                "en": "A pronoun replaces a noun so we do not repeat it. Subject pronouns do the action: I, you, he, she, it, we, they. Object pronouns receive the action: me, you, him, her, it, us, them.",
                "zh": "代词用来代替名词，避免重复。主格代词做动作：I、you、he、she、it、we、they；宾格代词接受动作：me、you、him、her、it、us、them。",
            },
            "rules": [
                {"label": "主语位置", "en": "I like tea. She is my teacher.", "zh": "我喜欢茶。她是我的老师。"},
                {"label": "宾语位置", "en": "Please help me. I called him yesterday.", "zh": "请帮帮我。我昨天给他打了电话。"},
                {"label": "指人用 he / she", "en": "Anna → she; Tom → he", "zh": "安娜 → she；汤姆 → he"},
                {"label": "指物用 it", "en": "The phone is new. It is black.", "zh": "这部手机是新的。它是黑色的。"},
            ],
            "examples": [
                {"en": "My friend and I often play basketball.", "zh": "我和我的朋友经常打篮球。"},
                {"en": "This is Lisa. I know her very well.", "zh": "这是丽莎。我跟她很熟。"},
                {"en": "The cat is hungry. Please feed it.", "zh": "猫饿了，请喂喂它。"},
            ],
            "mistakes": [
                {"en": "❌ Me and Tom went to the park. → In the subject position, use I last: Tom and I went to the park.", "zh": "❌ 主语位置用 I，且把自己放后面：Tom and I went to the park.（汤姆和我去了公园。）"},
                {"en": "❌ Please give the book to I. → After to, use the object form: to me.", "zh": "❌ to 后面用宾格：Please give the book to me.（请把书给我。）"},
            ],
        },
        {
            "id": "wc_teamwork", "name": "Word Classes at Work", "zh": "词性大协作",
            "concept": {
                "en": "A sentence is a team. The subject (noun or pronoun) does the action, the verb carries the action, adjectives dress up nouns, and adverbs dress up verbs.",
                "zh": "句子是一个团队：主语（名词或代词）发出动作，动词承载动作，形容词修饰名词，副词修饰动词。",
            },
            "rules": [
                {"label": "主语", "en": "noun / pronoun: The dog, She", "zh": "名词或代词：那只狗、她"},
                {"label": "谓语", "en": "verb: runs, sings", "zh": "动词：跑、唱"},
                {"label": "修饰名词", "en": "adjective before noun: a happy dog", "zh": "形容词放在名词前：一只快乐的狗"},
                {"label": "修饰动词", "en": "adverb after verb: runs quickly", "zh": "副词修饰动词：跑得很快"},
            ],
            "examples": [
                {"en": "The happy dog runs quickly.", "zh": "那只快乐的小狗跑得很快。（the + 形容词 happy + 名词 dog + 动词 runs + 副词 quickly）"},
                {"en": "My little sister sings sweetly.", "zh": "我的小妹妹唱得很甜。"},
                {"en": "We study English carefully every day.", "zh": "我们每天认真地学英语。"},
            ],
            "mistakes": [
                {"en": "❌ Is raining. → Every sentence needs a subject: It is raining.", "zh": "❌ 句子不能没有主语：It is raining.（正在下雨。）"},
                {"en": "❌ I very like pizza. → very cannot touch the verb here: I like pizza very much.", "zh": "❌ very 一般不直接修饰动词：I like pizza very much.（我非常喜欢披萨。）"},
            ],
        },
    ],
}
