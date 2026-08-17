# -*- coding: utf-8 -*-
LESSON = {
    "id": "tenses",
    "name": "Verb Tenses",
    "zh": "动词时态",
    "icon": "⏱️",
    "accent": "#E8590C",
    "desc": {"en": "Choose verb forms by timeline, duration, completion, and present relevance.", "zh": "根据时间线、持续、完成与当下的关联选择动词形式。"},
    "objectives": [
        {"en": "Use present, past, and future forms accurately", "zh": "准确使用现在、过去、将来时态"},
        {"en": "Distinguish perfect from simple tenses", "zh": "区分完成时与一般时"},
        {"en": "Use continuous forms for progress and duration", "zh": "用进行时表示进行与持续"},
        {"en": "Sequence tenses correctly in stories", "zh": "在叙事中正确安排时态顺序"},
        {"en": "Edit writing for consistent tense use", "zh": "修改写作中的时态一致问题"},
    ],
    "phases": [
        {
            "id": "tenses_present", "name": "Present Tenses", "zh": "现在时",
            "concept": {"en": "Simple present = habits, facts, schedules. Present continuous = happening now or temporary. Present perfect = past action with present relevance (experience or result).", "zh": "一般现在时表习惯、事实、时刻表；现在进行时表现在正在发生或暂时状态；现在完成时表对现在有影响的过去动作（经历或结果）。"},
            "rules": [
                {"label": "一般现在时", "en": "I work / She works — habits, facts: Water boils at 100°C.", "zh": "I work / She works — 习惯、事实：水在100°C沸腾。"},
                {"label": "现在进行时", "en": "am/is/are + -ing — now: She is reading now.", "zh": "am/is/are + -ing — 现在：她正在看书。"},
                {"label": "现在完成时", "en": "have/has + past participle — experience/result: I have seen that film.", "zh": "have/has + 过去分词 — 经历/结果：我看过那部电影。"},
            ],
            "examples": [
                {"en": "She works in a hospital.", "zh": "她在医院工作。"},
                {"en": "They are playing football right now.", "zh": "他们现在正在踢足球。"},
                {"en": "I have finished my homework.", "zh": "我已经做完作业了。"},
            ],
            "mistakes": [
                {"en": "❌ She work every day → third person -s: She works.", "zh": "❌ 第三人称单数加 -s：She works。"},
                {"en": "❌ I am knowing him → know is a state verb; I know him.", "zh": "❌ know 是状态动词，不用进行时。"},
            ],
        },
        {
            "id": "tenses_past", "name": "Past Tenses", "zh": "过去时",
            "concept": {"en": "Simple past = finished actions at a known time. Past continuous = background or interrupted action. Past perfect = an event before another past event.", "zh": "一般过去时表过去某时完成的动作；过去进行时表背景或被中断的动作；过去完成时表【过去的过去】。"},
            "rules": [
                {"label": "一般过去时", "en": "verb + -ed / irregular: I visited Paris in 2024.", "zh": "动词过去式：我2024年去过巴黎。"},
                {"label": "过去进行时", "en": "was/were + -ing: I was sleeping when you called.", "zh": "was/were + -ing：你打电话时我在睡觉。"},
                {"label": "过去完成时", "en": "had + past participle: The train had left before I arrived.", "zh": "had + 过去分词：我到达前火车已开走。"},
            ],
            "examples": [
                {"en": "We watched a movie last night.", "zh": "我们昨晚看了一部电影。"},
                {"en": "She was cooking when the phone rang.", "zh": "电话响时她正在做饭。"},
                {"en": "By the time we arrived, the show had started.", "zh": "我们到达时演出已经开始了。"},
            ],
            "mistakes": [
                {"en": "❌ I have seen him yesterday → yesterday needs simple past: I saw him yesterday.", "zh": "❌ yesterday 用一般过去时：I saw him yesterday。"},
                {"en": "❌ He didn't went → did + base form: He didn't go.", "zh": "❌ did 后用原形：He didn't go。"},
            ],
        },
        {
            "id": "tenses_future", "name": "Future Forms", "zh": "将来时",
            "concept": {"en": "will = prediction or decision at the moment of speaking. be going to = plan or evidence. Present continuous = arranged future.", "zh": "will 表预测或当场决定；be going to 表计划或有迹象的将来；现在进行时表已安排的将来。"},
            "rules": [
                {"label": "will", "en": "will + base — prediction/spontaneous: I'll help you.", "zh": "will + 原形 — 预测/临时决定：我来帮你。"},
                {"label": "going to", "en": "be going to + base — plan/evidence: It's going to rain.", "zh": "be going to + 原形 — 计划/迹象：要下雨了。"},
                {"label": "进行时表将来", "en": "present continuous — arrangement: We are flying to Tokyo tomorrow.", "zh": "现在进行时 — 安排：我们明天飞东京。"},
            ],
            "examples": [
                {"en": "I think it will be sunny tomorrow.", "zh": "我想明天会是晴天。"},
                {"en": "She is going to study abroad next year.", "zh": "她打算明年出国留学。"},
                {"en": "The meeting is starting at 3 p.m.", "zh": "会议下午三点开始。"},
            ],
            "mistakes": [
                {"en": "❌ I will going to → choose one: will go or am going to go.", "zh": "❌ 两种将来式不要混用。"},
                {"en": "❌ after if/when, no will: If it rains (not will rain).", "zh": "❌ if/when 从句用现在时：If it rains..."},
            ],
        },
        {
            "id": "tenses_perfect", "name": "Perfect Tenses", "zh": "完成时",
            "concept": {"en": "Present perfect connects past to now (since/for, experience, result). Past simple is for finished time (yesterday, ago). Past perfect puts one past event before another.", "zh": "现在完成时连接过去与现在（since/for、经历、结果）；一般过去时用于已结束的时间（yesterday、ago）；过去完成时表示先于另一过去事件。"},
            "rules": [
                {"label": "现在完成时", "en": "have/has + pp — unfinished time: I have lived here since 2020.", "zh": "have/has + 过去分词 — 时间未结束：我从2020年起住在这里。"},
                {"label": "一般过去时", "en": "finished time: I lived in London in 2019.", "zh": "时间已结束：我2019年住在伦敦。"},
                {"label": "过去完成时", "en": "had + pp — earlier past: She had finished before I called.", "zh": "had + 过去分词 — 更早的过去：我打电话前她已做完。"},
            ],
            "examples": [
                {"en": "I have known her for five years.", "zh": "我认识她五年了。"},
                {"en": "He visited the museum three years ago.", "zh": "他三年前参观过博物馆。"},
                {"en": "They had already left when we got there.", "zh": "我们到那里时他们已经离开了。"},
            ],
            "mistakes": [
                {"en": "❌ I have seen him yesterday → ago/yesterday = simple past.", "zh": "❌ ago/yesterday 用一般过去时。"},
                {"en": "❌ since three years → for + duration: for three years.", "zh": "❌ since 接起点，for 接时长：for three years。"},
            ],
        },
        {
            "id": "tenses_continuous", "name": "Continuous Forms", "zh": "进行时",
            "concept": {"en": "Continuous forms add the idea of progress, duration, or a temporary situation. They are built with be + -ing.", "zh": "进行时表达进行、持续或暂时状态，结构为 be + -ing。"},
            "rules": [
                {"label": "现在进行时", "en": "am/is/are + -ing: The kids are sleeping.", "zh": "am/is/are + -ing：孩子们在睡觉。"},
                {"label": "过去进行时", "en": "was/were + -ing: I was reading at 8 p.m.", "zh": "was/were + -ing：晚上八点我在读书。"},
                {"label": "状态动词", "en": "State verbs (know, like, own) rarely take continuous: I like it.", "zh": "状态动词（know、like、own）一般不用进行时。"},
            ],
            "examples": [
                {"en": "It is raining outside.", "zh": "外面正在下雨。"},
                {"en": "She was working when I saw her.", "zh": "我看见她时她正在工作。"},
                {"en": "I'm staying with friends this week.", "zh": "这周我暂住在朋友家。"},
            ],
            "mistakes": [
                {"en": "❌ I am understanding → understand is a state verb: I understand.", "zh": "❌ understand 是状态动词，不用进行时。"},
                {"en": "❌ She is work → missing -ing: She is working.", "zh": "❌ 进行时缺 -ing。"},
            ],
        },
        {
            "id": "tenses_contrast", "name": "Tense Contrast", "zh": "时态对比",
            "concept": {"en": "Time clues decide the tense: yesterday/last week/ago → past simple; since/for/already/yet/ever → present perfect; at the moment/look! → continuous; every day/usually → simple present.", "zh": "时间信号词决定时态：yesterday/last week/ago 用一般过去时；since/for/already/yet/ever 用现在完成时；at the moment/look! 用进行时；every day/usually 用一般现在时。"},
            "rules": [
                {"label": "过去信号词", "en": "yesterday, last night, two days ago, in 2020", "zh": "yesterday、last night、two days ago、in 2020"},
                {"label": "完成时信号词", "en": "since, for, already, yet, ever, never, just", "zh": "since、for、already、yet、ever、never、just"},
                {"label": "进行时信号词", "en": "now, at the moment, look!, listen!", "zh": "now、at the moment、look!、listen!"},
            ],
            "examples": [
                {"en": "She has already finished her report.", "zh": "她已经完成了报告。"},
                {"en": "We watched TV last night.", "zh": "我们昨晚看电视了。"},
                {"en": "Look! The baby is smiling.", "zh": "看！宝宝在笑。"},
            ],
            "mistakes": [
                {"en": "❌ I already finished (no time frame, focus on result) → I have already finished.", "zh": "❌ already 表结果关联，用现在完成时。"},
                {"en": "❌ She has gone to Beijing yesterday → yesterday 用过去时：She went to Beijing yesterday.", "zh": "❌ yesterday 与完成时冲突。"},
            ],
        },
        {
            "id": "tenses_narrative", "name": "Narrative Tenses", "zh": "叙事时态",
            "concept": {"en": "In stories: past simple = main events; past continuous = background; past perfect = earlier events. This creates a clear timeline.", "zh": "讲故事时：一般过去时表主要事件；过去进行时表背景；过去完成时表更早发生的事。这样时间线清晰。"},
            "rules": [
                {"label": "主事件", "en": "past simple: He opened the door.", "zh": "一般过去时：他打开门。"},
                {"label": "背景", "en": "past continuous: The sun was shining.", "zh": "过去进行时：阳光明媚。"},
                {"label": "更早事件", "en": "past perfect: She had already eaten.", "zh": "过去完成时：她已经吃过了。"},
            ],
            "examples": [
                {"en": "When I arrived, everyone was dancing and the music had already started.", "zh": "我到达时，大家都在跳舞，音乐已经开始了。"},
                {"en": "He was walking home when he met an old friend.", "zh": "他走回家时遇到了一位老朋友。"},
                {"en": "After we had finished dinner, we watched a film.", "zh": "吃完晚饭后，我们看了一部电影。"},
            ],
            "mistakes": [
                {"en": "❌ Mixing tenses without time clues confuses the reader.", "zh": "❌ 无时间线索地乱换时态会让读者困惑。"},
                {"en": "❌ He was walking home when he was meeting a friend → main event uses simple past: met.", "zh": "❌ 被打断的主事件用一般过去时：met。"},
            ],
        },
        {
            "id": "tenses_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "When writing, first fix the timeline, then check every verb: correct form, correct tense, consistent perspective.", "zh": "写作时先确定时间线，再逐一检查动词：形式正确、时态正确、视角一致。"},
            "rules": [
                {"label": "时间线优先", "en": "Decide: is the time now, past, or future? Then pick the tense family.", "zh": "先判断时间是现在、过去还是将来，再选时态。"},
                {"label": "一致性", "en": "Keep the same tense within one paragraph unless time shifts.", "zh": "同一段内保持时态一致，除非时间发生变化。"},
            ],
            "examples": [
                {"en": "❌ I go to the store yesterday and bought milk. → I went to the store yesterday and bought milk.", "zh": "❌ 昨天应统一用过去时：I went..."},
                {"en": "❌ She has lived here since three years. → She has lived here for three years.", "zh": "❌ for 接时长：for three years。"},
                {"en": "✔ Every morning I drink coffee, and today I am drinking tea.", "zh": "✔ 习惯用一般现在时，今天的情况用进行时。"},
            ],
            "mistakes": [
                {"en": "❌ I didn't saw → did + base: I didn't see.", "zh": "❌ did 后用原形：I didn't see。"},
                {"en": "❌ She have gone → has for third person singular: She has gone.", "zh": "❌ 第三人称单数用 has。"},
            ],
        },
    ],
}
