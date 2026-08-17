# -*- coding: utf-8 -*-
LESSON = {
    "id": "sentence_structure",
    "name": "Sentence Structure",
    "zh": "句子结构",
    "icon": "🏗️",
    "accent": "#364FC7",
    "desc": {"en": "Build, question, negate, combine, and repair complete English sentences.", "zh": "构建、提问、否定、合并并修复完整的英语句子。"},
    "objectives": [
        {"en": "Use correct subject-verb-object word order", "zh": "使用正确的主谓宾语序"},
        {"en": "Form yes/no and wh- questions correctly", "zh": "正确构成一般与特殊疑问句"},
        {"en": "Negate sentences without double negatives", "zh": "否定句子，避免双重否定"},
        {"en": "Identify main, subordinate, and coordinate clauses", "zh": "识别主句、从句与并列句"},
        {"en": "Repair fragments and run-on sentences", "zh": "修复残缺句与流水句"},
    ],
    "phases": [
        {
            "id": "sentence_structure_word_order", "name": "Word Order", "zh": "语序",
            "concept": {"en": "Standard English order: subject + verb + object (+ place + time). Adverbs of frequency go before the main verb.", "zh": "英语基本语序：主语 + 谓语 + 宾语（+ 地点 + 时间）。频率副词放在主要动词之前。"},
            "rules": [
                {"label": "SVO", "en": "Subject + verb + object: She reads books.", "zh": "主语 + 谓语 + 宾语：她读书。"},
                {"label": "时间地点", "en": "place before time: We met at the café yesterday.", "zh": "地点在前，时间在后：我们昨天在咖啡馆见面。"},
                {"label": "频率副词", "en": "She always gets up early. / I have never seen it.", "zh": "她总是早起。/ 我从未见过。"},
            ],
            "examples": [
                {"en": "The students finished their homework quickly.", "zh": "学生们很快完成了作业。"},
                {"en": "He usually walks to school.", "zh": "他通常步行上学。"},
                {"en": "They visited the museum in Beijing last summer.", "zh": "他们去年夏天参观了北京的博物馆。"},
            ],
            "mistakes": [
                {"en": "❌ I every day drink coffee → I drink coffee every day.", "zh": "❌ 时间状语放句末或句首。"},
                {"en": "❌ She reads always books → She always reads books.", "zh": "❌ 频率副词在动词前。"},
            ],
        },
        {
            "id": "sentence_structure_questions", "name": "Question Formation", "zh": "疑问句构成",
            "concept": {"en": "Yes/no questions: auxiliary + subject + verb. Wh- questions: wh-word + auxiliary + subject + verb. With be, invert be and subject.", "zh": "一般疑问句：助动词 + 主语 + 谓语。特殊疑问句：疑问词 + 助动词 + 主语 + 谓语。be 动词直接与主语倒装。"},
            "rules": [
                {"label": "一般疑问", "en": "Do you like tea? / Is she ready?", "zh": "Do you like tea? / Is she ready?"},
                {"label": "特殊疑问", "en": "Where do you live? / What is your name?", "zh": "Where do you live? / What is your name?"},
                {"label": "主语疑问", "en": "Who called you? (no auxiliary when who is the subject)", "zh": "Who called you?（who 作主语时不加助动词）"},
            ],
            "examples": [
                {"en": "Did you watch the match last night?", "zh": "你昨晚看比赛了吗？"},
                {"en": "How often do you exercise?", "zh": "你多久锻炼一次？"},
                {"en": "Who lives in that house?", "zh": "谁住在那栋房子里？"},
            ],
            "mistakes": [
                {"en": "❌ You like tea? (informal) → standard: Do you like tea?", "zh": "❌ 标准疑问句要加助动词。"},
                {"en": "❌ Who did call you? → Who called you? (who is subject)", "zh": "❌ who 作主语时不加 did。"},
            ],
        },
        {
            "id": "sentence_structure_negation", "name": "Negation", "zh": "否定",
            "concept": {"en": "not goes after the auxiliary or be; negative adverbs include never, hardly, rarely; avoid double negatives in standard English.", "zh": "not 放在助动词或 be 之后；否定副词有 never、hardly、rarely；标准英语避免双重否定。"},
            "rules": [
                {"label": "not 位置", "en": "I am not tired. / She does not work here.", "zh": "I am not tired. / She does not work here."},
                {"label": "否定副词", "en": "I never eat meat. / She rarely calls.", "zh": "I never eat meat. / She rarely calls."},
                {"label": "无双重否定", "en": "❌ I don't have no money → I don't have any money.", "zh": "❌ 不能说 I don't have no money。"},
            ],
            "examples": [
                {"en": "He hasn't finished his work yet.", "zh": "他还没完成工作。"},
                {"en": "We hardly ever eat out.", "zh": "我们几乎从不下馆子。"},
                {"en": "Nobody answered the phone.", "zh": "没有人接电话。"},
            ],
            "mistakes": [
                {"en": "❌ I don't want nothing → I don't want anything.", "zh": "❌ 避免双重否定。"},
                {"en": "❌ She doesn't likes → doesn't + base: She doesn't like.", "zh": "❌ doesn't 后接原形。"},
            ],
        },
        {
            "id": "sentence_structure_clauses", "name": "Clause Types", "zh": "从句类型",
            "concept": {"en": "A main clause can stand alone; a subordinate clause cannot. Coordinate clauses are joined by and/but/or. Subordinate clauses start with because, when, if, although...", "zh": "主句可独立成句；从句不能。并列句用 and/but/or 连接；从句以 because、when、if、although 等开头。"},
            "rules": [
                {"label": "主句", "en": "main clause: She left. (complete)", "zh": "主句：She left. 她离开了。（完整）"},
                {"label": "从句", "en": "subordinate: because she was tired. (incomplete alone)", "zh": "从句：因为她累了。（不能单独成句）"},
                {"label": "并列句", "en": "coordinate: She left, but he stayed.", "zh": "并列句：她走了，但他留下了。"},
            ],
            "examples": [
                {"en": "When the rain stopped, we went out.", "zh": "雨停后我们出去了。"},
                {"en": "He stayed home because he was sick.", "zh": "他因为生病待在家里。"},
                {"en": "I called her, but she didn't answer.", "zh": "我给她打了电话，但她没接。"},
            ],
            "mistakes": [
                {"en": "❌ Because he was sick. (fragment) → join to a main clause.", "zh": "❌ 从句不能单独成句。"},
                {"en": "❌ Joining two main clauses with only a comma → run-on.", "zh": "❌ 两个主句不能只用逗号连接。"},
            ],
        },
        {
            "id": "sentence_structure_cleft", "name": "Cleft Sentences", "zh": "强调句",
            "concept": {"en": "Cleft sentences emphasize one part: It is/was + emphasized part + that/who...; What + subject + verb + is/was + emphasized part.", "zh": "强调句突出某一部分：It is/was + 被强调部分 + that/who...；What + 主语 + 谓语 + is/was + 被强调部分。"},
            "rules": [
                {"label": "It is...that", "en": "It was Tom who called you.", "zh": "是汤姆给你打了电话。"},
                {"label": "What...is", "en": "What I need is a break.", "zh": "我需要的是休息。"},
                {"label": "用途", "en": "Adds focus in speaking and writing.", "zh": "口语与写作中增加焦点。"},
            ],
            "examples": [
                {"en": "It is English that she loves most.", "zh": "她最爱的是英语。"},
                {"en": "What surprised me was his calmness.", "zh": "让我惊讶的是他的冷静。"},
                {"en": "It was in Shanghai that we first met.", "zh": "我们是在上海初次相遇的。"},
            ],
            "mistakes": [
                {"en": "❌ It was Tom which called → people take who/that.", "zh": "❌ 指人用 who/that。"},
                {"en": "❌ What I need is a break — not 'What do I need is' (no do).", "zh": "❌ What 从句不用助动词倒装。"},
            ],
        },
        {
            "id": "sentence_structure_fragments", "name": "Fragments and Run-ons", "zh": "残缺句与流水句",
            "concept": {"en": "A fragment is an incomplete sentence missing a subject or verb. A run-on joins two sentences without proper punctuation. Fix both by adding or splitting.", "zh": "残缺句缺少主语或谓语；流水句没有正确标点就连接两个句子。通过补充或拆分来修复。"},
            "rules": [
                {"label": "残缺句", "en": "❌ Because I was late. → I was late, so I missed the bus.", "zh": "❌ 残缺：Because I was late. 要补主句。"},
                {"label": "流水句", "en": "❌ I was late I missed the bus → I was late, so I missed the bus.", "zh": "❌ 流水句要加标点或连词。"},
                {"label": "修复法", "en": "Add the missing part, or split into two sentences with punctuation.", "zh": "补充缺失部分，或用标点拆分。"},
            ],
            "examples": [
                {"en": "❌ The dog barking all night. → The dog was barking all night.", "zh": "❌ 缺谓语：加 was。"},
                {"en": "❌ She loves music she plays piano. → She loves music, and she plays piano.", "zh": "❌ 流水句：加 and。"},
                {"en": "✔ After the meeting, we went for coffee.", "zh": "✔ 会后我们去喝了咖啡。"},
            ],
            "mistakes": [
                {"en": "❌ Fragment: Walking to school. → She was walking to school.", "zh": "❌ 缺主语或谓语。"},
                {"en": "❌ Run-on without any punctuation: He came he left.", "zh": "❌ 两个句子要连接或拆开。"},
            ],
        },
        {
            "id": "sentence_structure_parallelism", "name": "Parallel Structure", "zh": "平行结构",
            "concept": {"en": "Items in a list or pair must have the same grammatical form: verb + verb, noun + noun, -ing + -ing.", "zh": "并列项语法形式必须一致：动词对动词、名词对名词、-ing 对 -ing。"},
            "rules": [
                {"label": "一致形式", "en": "She likes reading, writing, and painting.", "zh": "她喜欢阅读、写作和绘画。（都是 -ing）"},
                {"label": "错误示例", "en": "❌ She likes reading, to write, and painting.", "zh": "❌ 形式混杂：reading、to write、painting。"},
                {"label": "成对结构", "en": "not only...but also, either...or keep the same form on both sides.", "zh": "not only...but also、either...or 两边形式一致。"},
            ],
            "examples": [
                {"en": "He is smart, kind, and funny.", "zh": "他聪明、善良又风趣。（都是形容词）"},
                {"en": "She enjoys swimming and hiking.", "zh": "她喜欢游泳和远足。"},
                {"en": "We decided to save money and to travel less.", "zh": "我们决定省钱，少旅行。"},
            ],
            "mistakes": [
                {"en": "❌ I like cooking, to read, and swim → keep all -ing.", "zh": "❌ 列表项形式要统一。"},
                {"en": "❌ She is both smart and works hard → both + adj + and + verb phrase (unbalanced).", "zh": "❌ 并列结构要对称。"},
            ],
        },
        {
            "id": "sentence_structure_prod", "name": "Production and Editing", "zh": "综合运用与改错",
            "concept": {"en": "Edit for sentence quality: check every sentence has a subject and verb, correct word order, no fragments or run-ons, and parallel lists.", "zh": "修改句子质量：检查每句有主有谓、语序正确、无残缺句或流水句、列表平行。"},
            "rules": [
                {"label": "五项检查", "en": "subject? verb? order? punctuation? parallel?", "zh": "主语？谓语？语序？标点？平行？"},
                {"label": "一个句子一个焦点", "en": "One main idea per sentence; split long chains.", "zh": "一句一个重点，长链要拆分。"},
            ],
            "examples": [
                {"en": "❌ He go to school every day. → He goes to school every day.", "zh": "❌ 主谓一致：goes。"},
                {"en": "❌ Because it was raining. → Because it was raining, we stayed inside.", "zh": "❌ 残缺句：补主句。"},
                {"en": "✔ She speaks English fluently and writes clearly.", "zh": "✔ 平行结构：speaks...writes。"},
            ],
            "mistakes": [
                {"en": "❌ I am agree → I agree.", "zh": "❌ agree 是动词，不加 am。"},
                {"en": "❌ There is many people → There are many people.", "zh": "❌ there be 与主语一致。"},
            ],
        },
    ],
}
