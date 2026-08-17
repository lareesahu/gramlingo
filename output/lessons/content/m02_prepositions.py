# -*- coding: utf-8 -*-
LESSON = {
    "id": "prepositions",
    "name": "Prepositions",
    "zh": "介词",
    "icon": "📍",
    "accent": "#1971C2",
    "desc": {"en": "Build reliable intuition for place, time, movement, and common preposition patterns.", "zh": "建立地点、时间、运动方向与常用搭配的可靠直觉。"},
    "objectives": [
        {"en": "Use in / on / at correctly for place and time", "zh": "正确使用 in / on / at 表示地点和时间"},
        {"en": "Choose prepositions by conceptual relationship", "zh": "根据概念关系选择介词"},
        {"en": "Fix common preposition errors in writing", "zh": "改正写作中常见的介词错误"},
    ],
    "phases": [
        {
            "id": "prepositions_prep_place", "name": "In/On/At: Place", "zh": "in/on/at 表地点",
            "concept": {"en": "in = inside a space (city, room, box); on = on a surface (wall, table, floor); at = a point or location (bus stop, door, address).", "zh": "in 表示在空间内部（城市、房间、盒子）；on 表示在表面上（墙、桌子、地板）；at 表示某个点或位置（车站、门口、地址）。"},
            "rules": [
                {"label": "in", "en": "containment: in the room, in Shanghai, in the box", "zh": "空间内：in the room（房间里）、in Shanghai（在上海）"},
                {"label": "on", "en": "surface: on the wall, on the table, on the floor", "zh": "表面：on the wall（墙上）、on the table（桌上）"},
                {"label": "at", "en": "point/location: at the bus stop, at the door, at 25 Main Street", "zh": "点/地点：at the bus stop（公交站）、at the door（门口）"},
            ],
            "examples": [
                {"en": "She is waiting in the waiting room.", "zh": "她在候诊室里等着。"},
                {"en": "The picture is on the wall.", "zh": "画在墙上。"},
                {"en": "Meet me at the entrance.", "zh": "在入口处见我。"},
            ],
            "mistakes": [
                {"en": "❌ on Shanghai → cities use in: in Shanghai.", "zh": "❌ 城市用 in：in Shanghai。"},
                {"en": "❌ in the bus stop → a stop is a point: at the bus stop.", "zh": "❌ 车站是【点】，用 at。"},
            ],
        },
        {
            "id": "prepositions_prep_time", "name": "In/On/At: Time", "zh": "in/on/at 表时间",
            "concept": {"en": "at = precise times (3 o'clock, noon, night); on = days and dates (Monday, May 1st); in = longer periods (months, years, seasons, morning/afternoon/evening).", "zh": "at 用于精确时间点（三点、正午、夜晚）；on 用于某一天/日期（周一、5月1日）；in 用于较长时段（月份、年份、季节、上午/下午/晚上）。"},
            "rules": [
                {"label": "at", "en": "at 8 o'clock, at noon, at night, at midnight", "zh": "at 8 o'clock（八点）、at noon（正午）、at night（夜晚）"},
                {"label": "on", "en": "on Monday, on June 5th, on my birthday", "zh": "on Monday（周一）、on June 5th（6月5日）、on my birthday（我生日那天）"},
                {"label": "in", "en": "in the morning, in July, in 2026, in summer", "zh": "in the morning（早上）、in July（七月）、in 2026（2026年）、in summer（夏天）"},
            ],
            "examples": [
                {"en": "The meeting starts at 9 a.m.", "zh": "会议上午九点开始。"},
                {"en": "We have a test on Friday.", "zh": "我们周五有考试。"},
                {"en": "I was born in March.", "zh": "我三月出生。"},
            ],
            "mistakes": [
                {"en": "❌ in Friday → days use on: on Friday.", "zh": "❌ 星期几用 on：on Friday。"},
                {"en": "❌ at the morning → use in the morning.", "zh": "❌ 早上用 in：in the morning。"},
            ],
        },
        {
            "id": "prepositions_prep_mixed", "name": "Mixed Prepositions", "zh": "混合介词",
            "concept": {"en": "Choose the preposition by the relationship: across (from one side to the other), through (from inside to out), over (above), under (below), between (two), among (many), by (near/means), with (together/using), about (topic).", "zh": "根据概念关系选介词：across 横穿、through 穿过、over 上方、under 下方、between 两者之间、among 众多之间、by 旁边/方式、with 伴随/工具、about 关于。"},
            "rules": [
                {"label": "方位", "en": "across the street, through the tunnel, over the bridge, under the table", "zh": "across the street（街对面）、through the tunnel（穿过隧道）、over the bridge（桥上）、under the table（桌下）"},
                {"label": "之间", "en": "between you and me; among friends", "zh": "between 两者之间；among 三者以上之间"},
                {"label": "方式/主题", "en": "by train, with a pen, a book about history", "zh": "by train（乘火车）、with a pen（用笔）、a book about history（历史书）"},
            ],
            "examples": [
                {"en": "We walked across the bridge.", "zh": "我们走过桥。"},
                {"en": "She paid by card, not with cash.", "zh": "她用卡支付，不用现金。"},
                {"en": "The letter is between the books.", "zh": "信在书之间。"},
            ],
            "mistakes": [
                {"en": "❌ between my friends (3+) → use among.", "zh": "❌ 三个以上用 among。"},
                {"en": "❌ go in the door → movement through: go through the door.", "zh": "❌ 穿过门用 through。"},
            ],
        },
        {
            "id": "prepositions_prep_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Check every noun for the correct preposition; memorize common verb + preposition pairs (listen to, wait for, depend on, good at).", "zh": "检查每个名词前的介词；牢记常用动介搭配（listen to 听、wait for 等待、depend on 依靠、good at 擅长）。"},
            "rules": [
                {"label": "固定搭配", "en": "verb + preposition: listen to music, wait for the bus, depend on you", "zh": "动词+介词：listen to music（听音乐）、wait for the bus（等公交）、depend on you（依靠你）"},
                {"label": "形容词+介词", "en": "good at, interested in, afraid of, proud of", "zh": "形容词+介词：good at（擅长）、interested in（感兴趣）、afraid of（害怕）、proud of（自豪）"},
            ],
            "examples": [
                {"en": "She is good at math and interested in science.", "zh": "她擅长数学，对科学感兴趣。"},
                {"en": "I'm waiting for the bus at the stop.", "zh": "我在车站等公交。"},
                {"en": "His success depends on hard work.", "zh": "他的成功取决于努力。"},
            ],
            "mistakes": [
                {"en": "❌ listen music → listen to music.", "zh": "❌ listen 后要加 to。"},
                {"en": "❌ afraid from → afraid of.", "zh": "❌ afraid 后接 of。"},
            ],
        },
    ],
}
