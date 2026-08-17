# -*- coding: utf-8 -*-
LESSON = {
    "id": "clauses",
    "name": "Relative Clauses",
    "zh": "定语从句",
    "icon": "🔗",
    "accent": "#2F9E44",
    "desc": {"en": "Describe people, things, places, times, and reasons with precise connected sentences.", "zh": "用精确的连缀句描述人、事物、地点、时间与原因。"},
    "objectives": [
        {"en": "Spot a relative clause and its antecedent", "zh": "识别定语从句及其先行词"},
        {"en": "Choose who / which / that / whose / where / when / why correctly", "zh": "正确选用关系词"},
        {"en": "Decide when the relative pronoun can be omitted", "zh": "判断关系代词何时可省略"},
        {"en": "Punctuate restrictive vs non-restrictive clauses", "zh": "区分限定性从句的标点用法"},
        {"en": "Combine sentences smoothly without double subjects", "zh": "顺畅合并句子，避免双重主语"},
    ],
    "phases": [
        {
            "id": "clauses_rec", "name": "Identify Relative Clauses", "zh": "识别定语从句",
            "concept": {"en": "A relative clause is a group of words that describes a noun. The noun it describes is called the antecedent. The clause usually starts with a relative word: who, which, that, whose, where, when, why.", "zh": "定语从句是修饰名词的从句，被修饰的名词叫先行词。从句通常以关系词开头：who、which、that、whose、where、when、why。"},
            "rules": [
                {"label": "位置", "en": "The clause comes right after the noun it describes.", "zh": "从句紧跟在它所修饰的名词后面。"},
                {"label": "先行词", "en": "Find the noun first, then the clause that explains it.", "zh": "先找名词，再找解释它的从句。"},
                {"label": "关系词", "en": "The relative word links the clause back to the noun.", "zh": "关系词把从句和名词连接起来。"},
            ],
            "examples": [
                {"en": "The woman who lives next door is a doctor.", "zh": "住在隔壁的那位女士是医生。"},
                {"en": "I read the book that you recommended.", "zh": "我读了你推荐的那本书。"},
                {"en": "This is the café where we first met.", "zh": "这是我们初次见面的那家咖啡馆。"},
            ],
            "mistakes": [
                {"en": "❌ The book is on the table is mine. → Missing relative word: The book that is on the table is mine.", "zh": "❌ 缺少关系词。应说 The book that is on the table is mine.（桌上的那本书是我的。）"},
                {"en": "❌ I know the man which lives here. → People need who, not which.", "zh": "❌ 指人用 who，不用 which。"},
            ],
        },
        {
            "id": "clauses_subj", "name": "Subject Relatives", "zh": "主语关系词",
            "concept": {"en": "who and that refer to people; which and that refer to things. When the relative pronoun is the subject of its clause, it can never be omitted.", "zh": "who/that 指人，which/that 指物。关系代词在从句中作主语时绝不可省略。"},
            "rules": [
                {"label": "人", "en": "who / that + verb  →  The girl who sings well is my friend.", "zh": "who/that + 动词 → 唱歌唱得好的那个女孩是我朋友。"},
                {"label": "物", "en": "which / that + verb  →  The phone which costs $500 is new.", "zh": "which/that + 动词 → 那部价值 500 美元的手机是新的。"},
                {"label": "动词一致", "en": "The verb agrees with the antecedent: The man who lives here (singular).", "zh": "谓语动词与先行词保持一致（单复数）。"},
            ],
            "examples": [
                {"en": "The student who won the prize is my classmate.", "zh": "获奖的那个学生是我的同学。"},
                {"en": "The train that leaves at 6 is always crowded.", "zh": "六点出发的那班火车总是很挤。"},
                {"en": "People who exercise daily feel healthier.", "zh": "每天锻炼的人感觉更健康。"},
            ],
            "mistakes": [
                {"en": "❌ The woman who lives... → who is the subject, so it cannot be dropped.", "zh": "❌ who 在从句中作主语时不可省略。"},
                {"en": "❌ The dog which eat the food... → subject-verb agreement: which eats.", "zh": "❌ 注意主谓一致：which eats。"},
            ],
        },
        {
            "id": "clauses_obj", "name": "Object Relatives", "zh": "宾语关系词",
            "concept": {"en": "When the relative pronoun is the object of the clause, it can be omitted in everyday English. whom is the formal object form for people.", "zh": "关系代词在从句中作宾语时，口语中常可省略。whom 是书面语中指人的宾格形式。"},
            "rules": [
                {"label": "结构", "en": "noun + (who/whom/which/that) + subject + verb  →  The film (that) we watched was great.", "zh": "名词 + (关系词) + 主语 + 动词 → 我们看的那部电影很棒。"},
                {"label": "省略", "en": "Object relatives can be left out in informal English.", "zh": "宾语关系词在口语中可省略。"},
                {"label": "正式语", "en": "whom for people in formal writing: The man whom I met.", "zh": "书面语指人用 whom：The man whom I met."},
            ],
            "examples": [
                {"en": "The book (that) she wrote became a bestseller.", "zh": "她写的那本书成了畅销书。"},
                {"en": "The person (who) I called didn't answer.", "zh": "我打电话的那个人没接。"},
                {"en": "The house (which) they bought is near the park.", "zh": "他们买的房子在公园附近。"},
            ],
            "mistakes": [
                {"en": "❌ The book that she wrote it became... → No double object: drop it.", "zh": "❌ 不要重复宾语：去掉 it。"},
                {"en": "❌ who in 'The man whom I met' in formal writing → whom is correct.", "zh": "❌ 正式文体中作宾语指人用 whom。"},
            ],
        },
        {
            "id": "clauses_subobj", "name": "Subject vs Object", "zh": "主语与宾语关系词",
            "concept": {"en": "Look at what follows the relative pronoun. If a verb follows → it is a subject relative (no omission). If a noun or pronoun follows → it is an object relative (omission allowed).", "zh": "看关系词后面的成分：后面是动词→主语关系词（不可省略）；后面是名词/代词→宾语关系词（可省略）。"},
            "rules": [
                {"label": "主语从句", "en": "relative + verb  →  who lives (who = subject)", "zh": "关系词 + 动词 → who lives（who 作主语）"},
                {"label": "宾语从句", "en": "relative + noun/pronoun + verb  →  who(m) I met (who = object)", "zh": "关系词 + 名词/代词 + 动词 → whom I met（作宾语）"},
                {"label": "判定法", "en": "If you can drop the relative word, it is an object relative.", "zh": "能省略的就是宾语关系词。"},
            ],
            "examples": [
                {"en": "The man who called you is my boss. (subject — cannot drop who)", "zh": "给你打电话的那个人是我老板。（主语，不可省略）"},
                {"en": "The man (who) you called is my boss. (object — can drop who)", "zh": "你打电话给的那个人是我老板。（宾语，可省略）"},
                {"en": "The cake that smells great is chocolate. (subject)", "zh": "闻起来很香的蛋糕是巧克力味的。（主语）"},
            ],
            "mistakes": [
                {"en": "❌ The man you called him is my boss. → Remove him: The man you called is my boss.", "zh": "❌ 画蛇添足加 him：直接 The man you called is my boss."},
                {"en": "❌ Dropping a subject relative: The man called you is my boss → wrong.", "zh": "❌ 主语关系词不能省略：The man who called you..."},
            ],
        },
        {
            "id": "clauses_oblq", "name": "Oblique Relatives", "zh": "地点/时间/原因关系词",
            "concept": {"en": "where = place, when = time, why = reason. Prepositions can also sit before which/whom in formal style.", "zh": "where 表地点，when 表时间，why 表原因。正式语中介词可放在 which/whom 之前。"},
            "rules": [
                {"label": "地点", "en": "place + where + clause  →  the town where I grew up", "zh": "地点 + where → 我长大的小镇"},
                {"label": "时间", "en": "time + when + clause  →  the day when we met", "zh": "时间 + when → 我们相遇的那天"},
                {"label": "原因", "en": "reason + why + clause  →  the reason why I left", "zh": "原因 + why → 我离开的原因"},
                {"label": "介词+which", "en": "the table on which the book lay (formal) = the table (that) the book lay on", "zh": "介词+which：the table on which...（正式）"},
            ],
            "examples": [
                {"en": "This is the school where I studied English.", "zh": "这是我学英语的学校。"},
                {"en": "Do you remember the day when we first met?", "zh": "你还记得我们初次见面的那天吗？"},
                {"en": "That's the reason why she left early.", "zh": "那就是她早退的原因。"},
            ],
            "mistakes": [
                {"en": "❌ the place where I live in → where already means 'in which'; do not add in.", "zh": "❌ where 已含介词意义，不要重复加 in。"},
                {"en": "❌ the reason why because... → redundant; choose one.", "zh": "❌ why 与 because 重复，选其一。"},
            ],
        },
        {
            "id": "clauses_gen", "name": "Genitive Relatives", "zh": "所有格关系词 whose",
            "concept": {"en": "whose shows possession and works for both people and things. It is followed directly by a noun.", "zh": "whose 表示所属关系，人和物都可用，后面直接跟名词。"},
            "rules": [
                {"label": "人", "en": "person + whose + noun  →  the girl whose name I forgot", "zh": "人 + whose + 名词 → 我忘了名字的那个女孩"},
                {"label": "物", "en": "thing + whose + noun  →  the car whose engine broke", "zh": "物 + whose + 名词 → 发动机坏了的车"},
                {"label": "不可省略", "en": "whose can never be omitted.", "zh": "whose 不可省略。"},
            ],
            "examples": [
                {"en": "The writer whose books I love is coming to town.", "zh": "作品我很喜欢的那个作家要来城里了。"},
                {"en": "We adopted a dog whose owner had moved away.", "zh": "我们收养了一只主人已搬走的狗。"},
                {"en": "I know a family whose house is on the hill.", "zh": "我认识一家住在山上的房子的人。"},
            ],
            "mistakes": [
                {"en": "❌ the girl who name I forgot → use whose, not who.", "zh": "❌ 表所属要用 whose，不是 who。"},
                {"en": "❌ the book which cover is red → use whose: the book whose cover is red.", "zh": "❌ 物也用 whose：the book whose cover is red."},
            ],
        },
        {
            "id": "clauses_rest", "name": "Restrictive vs Non-restrictive", "zh": "限定性 vs 非限定性从句",
            "concept": {"en": "A restrictive clause is essential to identify the noun — no commas. A non-restrictive clause adds extra information — set off by commas, uses who/which (never that).", "zh": "限定性从句是确定名词所必需的信息，不加逗号；非限定性从句只是补充信息，用逗号隔开，用 who/which（不用 that）。"},
            "rules": [
                {"label": "限定性", "en": "No commas, essential: My brother who lives in Beijing is a doctor. (I have more than one brother)", "zh": "无逗号，必需信息：My brother who lives in Beijing...（暗示还有其他兄弟）"},
                {"label": "非限定性", "en": "Commas, extra info: My brother, who lives in Beijing, is a doctor. (I have one brother)", "zh": "逗号隔开，补充信息：My brother, who lives in Beijing, ...（只有一位兄弟）"},
                {"label": "which 指整句", "en": "which can refer to the whole clause: He passed, which surprised me.", "zh": "which 可指代整个句子：He passed, which surprised me."},
                {"label": "禁止 that", "en": "that is never used in non-restrictive clauses.", "zh": "非限定性从句中不用 that。"},
            ],
            "examples": [
                {"en": "The students who study hard will pass. (restrictive — only those students)", "zh": "用功学习的学生会通过。（限定）"},
                {"en": "The students, who study hard, will pass. (non-restrictive — all students)", "zh": "学生们都会通过，他们都很用功。（非限定）"},
                {"en": "She missed the bus, which made her late.", "zh": "她错过了公交车，这让她迟到了。"},
            ],
            "mistakes": [
                {"en": "❌ My brother, that lives in Beijing → that is wrong in non-restrictive clauses.", "zh": "❌ 非限定性从句不能用 that。"},
                {"en": "❌ Adding a comma changes the meaning — be careful with punctuation.", "zh": "❌ 逗号的有无会改变句意，务必小心。"},
            ],
        },
        {
            "id": "clauses_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Combine two short sentences into one sentence with a relative clause; check for double subjects, missing relative words, and wrong relative pronouns.", "zh": "把两个短句合并成带定语从句的句子；检查双重主语、漏掉关系词、关系词误用等问题。"},
            "rules": [
                {"label": "合并法", "en": "Find the shared noun → make it the antecedent → choose who/which/whose/where/when/why → place the clause right after it.", "zh": "找共有名词→作为先行词→选关系词→从句紧跟其后。"},
                {"label": "检查", "en": "No double subject/object. Verb agrees with antecedent. Punctuation matches meaning.", "zh": "无重复主语/宾语；主谓一致；标点与句意匹配。"},
            ],
            "examples": [
                {"en": "I met a man. The man speaks five languages. → I met a man who speaks five languages.", "zh": "我遇到一个会说五种语言的人。"},
                {"en": "This is the house. We lived in it for years. → This is the house (that) we lived in for years.", "zh": "这是我们住了多年的房子。"},
                {"en": "She has a cat. Its eyes are green. → She has a cat whose eyes are green.", "zh": "她有一只绿眼睛的猫。"},
            ],
            "mistakes": [
                {"en": "❌ The man he speaks... → drop the extra pronoun.", "zh": "❌ 去掉多余的代词 he。"},
                {"en": "❌ I met a man speaks five languages → missing who.", "zh": "❌ 漏掉关系词 who。"},
            ],
        },
    ],
}
