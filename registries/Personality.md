# Personality Registry｜角色 IP 人格气质库

> 用途：供 `SKILL.md` 在 25 宫格探索阶段和用户选中编号后的定稿阶段调用。
> 本文件是“人格候选语义库”，不是 25 种画风的固定绑定表。

---

# 1. 核心原则

## 1.1 人格不与画风固定一一对应

同一个 `style_id` 面对不同用户，可以匹配不同人格。画风只提供一种 **Personality Affinity（人格亲和方向）**，不能覆盖用户本人。

最终人格建议按以下权重编译：

`Final Personality = 70% User Base Persona + 20% Style Affinity + 10% Meme / Visual Contrast`

- **70% User Base Persona**：来自参考角色照片气质、账号 Bio、内容语言、职业角色、用户明确自述。
- **20% Style Affinity**：来自 `style.md` 对该画风更容易放大的气质倾向。
- **10% Meme / Visual Contrast**：加入一个轻微反差点，让角色更有网感和记忆点。

## 1.2 Personality Stack 使用规则

- 每个最终 Personality Stack 建议 4–5 个词。
- 至少包含：`1 个能力/认知词 + 1 个社交温度词 + 1 个网络人格词 + 1 个轻微缺陷/反差词`。
- 最多允许 1 个偏负面词；不要把参考角色 IP 设计成极端 Mascot 人格。
- 不允许机械随机抽取；必须先建立用户 Base Persona，再匹配。
- 不允许因为“男性/女性”直接决定人格；性别只影响表达方式，不决定人格内容。

## 1.3 25 宫格阶段

25 格应表现为“同一个人的 25 个侧面”，而不是 25 个互相矛盾的人格。

允许：
- 放大不同侧面：冷感、松弛、机灵、艺术、怪趣、克制等。
- 每格加入 1 个明显的人格钩子。

禁止：
- 把沉稳用户突然改成极端疯癫人格。
- 把温和用户硬改成 ruthless / cruel / aggressive。
- 为了做差异而让人格脱离账号本身。

## 1.4 用户选中编号后

一旦用户选中某格，该格的 `matched_personality` 就成为该方向的稳定人格设定。后续修改默认保持，除非用户明确要求改变。

---

# 2. Base Persona 提取顺序

按以下优先级判断：

1. 用户明确自述的人格 / 审美
2. 账号长期语言风格与内容气质
3. 参考角色照片中的基础气场（仅作为弱信号）
4. 内容领域和目标受众
5. 平台语境

> 注意：不要仅凭一张照片武断推断复杂人格。照片主要负责视觉身份；账号内容更适合判断 Personality。

---

# 3. Personality Stack Library｜150 组

以下 150 组是可直接使用或轻微重组的候选库。编号仅用于内部引用，不与 `style_id` 对应。

## A｜冷感 / 理性 / Deadpan

适合知识、财经、科技、评论型账号；强调克制、聪明、轻微疏离和冷幽默。

001. `deadpan + sarcastic + clever + tired + slightly smug`
002. `skeptical + analytical + calm + sharp + unimpressed`
003. `calm + intelligent + observant + restrained + dry`
004. `rational + precise + detached + competent + understated`
005. `clever + relaxed + self-aware + witty + slightly lazy`
006. `sharp + composed + skeptical + confident + dry`
007. `minimalist + rational + detached + precise + sophisticated`
008. `quiet + intelligent + observant + aloof + self-assured`
009. `analytical + curious + skeptical + patient + understated`
010. `logical + calm + efficient + blunt + quietly funny`

## B｜松弛 / Chill / Effortless

适合生活方式、创作者、轻吐槽；强调松弛、自洽、懒而不笨。

011. `chill + sleepy + clever + unbothered + self-aware`
012. `laid-back + observant + sarcastic + streetwise + cool`
013. `relaxed + witty + effortless + confident + playful`
014. `casual + clever + calm + slightly mischievous + likable`
015. `easygoing + observant + funny + grounded + self-aware`
016. `low-energy + competent + dry + relaxed + secretly ambitious`
017. `sleepy + understated + clever + detached + funny`
018. `effort-saving + clever + efficient + mischievous + calm`
019. `unbothered + witty + practical + observant + slightly smug`
020. `relaxed + independent + sharp + casual + quietly confident`

## C｜内向 / Awkward / Gentle

适合安静、陪伴、观察型账号；强调内向、细腻、轻微社交笨拙。

021. `awkward + introverted + smart + cautious + gentle`
022. `nerdy + curious + socially awkward + focused + proud`
023. `quiet + thoughtful + observant + intelligent + slightly awkward`
024. `introverted + witty + cautious + curious + self-aware`
025. `soft-spoken + clever + weird + observant + deadpan`
026. `gentle + intelligent + introverted + quietly funny + warm`
027. `reserved + analytical + sensitive + thoughtful + dry`
028. `shy + curious + earnest + clever + quietly stubborn`
029. `awkward + competent + sincere + cautious + relatable`
030. `socially quiet + perceptive + clever + dry + endearing`

## D｜极客 / Curious / Obsessive

适合 AI、科技、开发者、研究型账号；强调好奇、专注、技术兴奋感。

031. `curious + nerdy + focused + energetic + obsessive`
032. `enthusiastic + intelligent + curious + fast-thinking + slightly chaotic`
033. `focused + obsessive + competent + impatient + self-aware`
034. `inventive + curious + energetic + analytical + playful`
035. `nerdy + obsessive + confident + curious + slightly awkward`
036. `experimental + clever + restless + curious + optimistic`
037. `technical + focused + dry + curious + quietly excited`
038. `detail-obsessed + competent + enthusiastic + quirky + proud`
039. `creative + analytical + curious + energetic + unconventional`
040. `fast-thinking + sharp + curious + playful + easily distracted`

## E｜疲惫 / Cynical / Burnt-out

适合职场、财经、成年人生存吐槽；强调疲惫但靠谱、看透但还在做事。

041. `cynical + rational + observant + restrained + witty`
042. `skeptical + calm + dry + perceptive + slightly sarcastic`
043. `deadpan + observant + detached + clever + darkly funny`
044. `world-weary + competent + sarcastic + practical + relatable`
045. `socially tired + polite + restrained + internally screaming + relatable`
046. `burnt-out + competent + dry + self-aware + dependable`
047. `exhausted + responsible + competent + annoyed + dependable`
048. `tired + unimpressed + clever + patient + quietly funny`
049. `restrained + cynical + thoughtful + sharp + self-aware`
050. `overworked + competent + sarcastic + calm + strangely optimistic`

## F｜自信 / Sharp / Experienced

适合专业人士、主理人、成熟账号；强调能力感、判断力、少量傲气。

051. `confident + experienced + relaxed + sharp + slightly arrogant`
052. `self-assured + analytical + composed + witty + independent`
053. `decisive + efficient + calm + sharp + darkly funny`
054. `ambitious + composed + intelligent + demanding + self-aware`
055. `confident + playful + clever + socially fluent + slightly smug`
056. `poised + analytical + confident + restrained + slightly sarcastic`
057. `independent + sharp + calm + fearless + understated`
058. `experienced + practical + skeptical + relaxed + dry`
059. `direct + confident + competent + impatient + funny`
060. `disciplined + intelligent + calm + demanding + quietly rebellious`

## G｜温和 / Warm / Reliable

适合教育、生活、成长、陪伴型内容；强调可靠、温暖、低攻击性。

061. `warm + calm + reliable + understated + slightly awkward`
062. `thoughtful + gentle + perceptive + grounded + quietly witty`
063. `warm + witty + emotionally intelligent + relaxed + grounded`
064. `soft-spoken + observant + thoughtful + quietly funny + warm`
065. `patient + intelligent + reliable + calm + subtly playful`
066. `kind + practical + perceptive + understated + self-aware`
067. `gentle + composed + thoughtful + independent + quietly confident`
068. `grounded + reliable + humorous + mature + relaxed`
069. `empathetic + sharp + calm + thoughtful + restrained`
070. `approachable + intelligent + relaxed + observant + dry`

## H｜嘴硬心软 / Grumpy / Dependable

适合实用型、吐槽型、资深人士；强调直白、可靠、轻微不耐烦。

071. `grumpy + helpful + blunt + reliable + soft-hearted`
072. `stoic + loyal + practical + slightly grumpy + dependable`
073. `blunt + competent + impatient + caring + funny`
074. `serious + reliable + dry + protective + quietly warm`
075. `skeptical + practical + mature + blunt + dependable`
076. `reserved + loyal + stubborn + competent + soft-hearted`
077. `strict + responsible + sharp + secretly gentle + dry`
078. `impatient + practical + helpful + sarcastic + dependable`
079. `tough + calm + caring + restrained + slightly awkward`
080. `gruff + experienced + observant + reliable + quietly funny`

## I｜顽皮 / Cheeky / Rebellious

适合社媒、潮流、年轻化账号；强调机灵、叛逆、会玩梗。

081. `playful + cheeky + clever + energetic + rebellious`
082. `mischievous + clever + playful + self-aware + slightly smug`
083. `innocent-looking + clever + playful + secretly chaotic + witty`
084. `cheeky + observant + confident + funny + opportunistic`
085. `playful + sharp + spontaneous + rebellious + charming`
086. `crafty + street-smart + witty + relaxed + slightly smug`
087. `bold + playful + independent + clever + unserious`
088. `teasing + clever + relaxed + mischievous + likable`
089. `rebellious + cynical + independent + witty + fearless`
090. `streetwise + playful + opportunistic + confident + funny`

## J｜怪趣 / Weird / Absurd

适合独立创作者、meme、文化账号；强调反常识、冷脸荒诞和 cult 感。

091. `calm-faced + absurd + unpredictable + witty + secretly chaotic`
092. `serious + absurd + disciplined + deadpan + weird`
093. `quiet + weird + intelligent + observant + unexpectedly funny`
094. `composed + eccentric + clever + dry + unpredictable`
095. `normal-looking + strange + analytical + deadpan + self-aware`
096. `precise + weird + calm + obsessive + darkly funny`
097. `reserved + quirky + intelligent + unpredictable + likable`
098. `deadpan + surreal + thoughtful + calm + subtly chaotic`
099. `earnest + strange + curious + serious + unintentionally funny`
100. `disciplined + eccentric + focused + calm + oddly charming`

## K｜戏剧 / Expressive / Emotional

适合情绪、生活、娱乐、强表达账号；强调情绪可读性和表演张力。

101. `dramatic + sensitive + expressive + neurotic + lovable`
102. `expressive + witty + emotional + self-aware + playful`
103. `sensitive + artistic + dramatic + thoughtful + charming`
104. `emotionally transparent + clever + anxious + funny + relatable`
105. `dramatic + confident + playful + expressive + self-aware`
106. `passionate + sensitive + outspoken + funny + slightly chaotic`
107. `expressive + curious + impulsive + warm + entertaining`
108. `emotional + sharp + playful + honest + self-aware`
109. `enthusiastic + dramatic + optimistic + chaotic + endearing`
110. `sensitive + witty + intense + creative + lovable`

## L｜焦虑 / Perfectionist / Overthinking

适合职场、学习、效率、精细化账号；强调认真、过度准备、可共鸣。

111. `perfectionist + anxious + competent + tired + obsessive`
112. `cautious + analytical + responsible + overthinking + dry`
113. `anxious + intelligent + prepared + cautious + self-aware`
114. `detail-oriented + competent + perfectionist + restrained + tired`
115. `overthinking + thoughtful + clever + cautious + relatable`
116. `careful + analytical + skeptical + responsible + quietly funny`
117. `high-strung + competent + precise + self-aware + dependable`
118. `cautious + timid + clever + survival-minded + suspicious`
119. `worried + practical + observant + responsible + dry`
120. `controlled + anxious + ambitious + competent + quietly obsessive`

## M｜乐观 / Scrappy / Resilient

适合创业、成长、行动派账号；强调资源有限但会想办法、韧性强。

121. `optimistic + scrappy + resourceful + slightly unrealistic + lovable`
122. `enthusiastic + inexperienced + confident + chaotic + endearing`
123. `earnest + curious + awkward + persistent + adorable`
124. `hopeful + clever + resourceful + stubborn + playful`
125. `ambitious + optimistic + impulsive + clever + self-aware`
126. `scrappy + energetic + practical + funny + resilient`
127. `idealistic + intelligent + enthusiastic + stubborn + charming`
128. `curious + optimistic + fearless + inexperienced + likable`
129. `determined + resourceful + playful + slightly overconfident + warm`
130. `energetic + ambitious + earnest + chaotic + self-aware`

## N｜时髦 / Poised / Editorial

适合设计、时尚、知识女性/男性主理人；强调审美、克制、独立和高级感。

131. `composed + intelligent + stylish + independent + slightly aloof`
132. `elegant + restrained + sharp + self-assured + dry`
133. `calm + refined + perceptive + understated + sophisticated`
134. `cool + independent + skeptical + stylish + quietly rebellious`
135. `minimal + elegant + quiet + precise + emotionally restrained`
136. `stylish + witty + confident + relaxed + self-aware`
137. `refined + intelligent + detached + observant + subtly playful`
138. `poised + sharp + independent + calm + quietly intimidating`
139. `understated + stylish + analytical + cool + self-assured`
140. `effortless + sophisticated + witty + detached + confident`

## O｜艺术 / Dreamy / Creative

适合设计、文化、艺术、生活方式账号；强调想象力、敏感度和独立气质。

141. `artistic + sensitive + curious + dreamy + self-aware`
142. `creative + quiet + observant + emotional + unconventional`
143. `dreamy + intelligent + introverted + playful + thoughtful`
144. `artistic + relaxed + curious + eccentric + gentle`
145. `imaginative + sensitive + witty + slightly chaotic + warm`
146. `creative + restrained + introspective + curious + stylish`
147. `romantic + thoughtful + artistic + self-aware + understated`
148. `experimental + expressive + independent + curious + playful`
149. `introspective + creative + observant + quietly rebellious + warm`
150. `artistic + sharp + unconventional + calm + subtly strange`

---

# 4. 动态重组规则

当现成组合不完全匹配用户时，可以从库中抽取词语重新组合，但必须满足：

- 优先保留 Base Persona 的 2–3 个核心词。
- 最多加入 1–2 个 Style Affinity 词。
- 最多加入 1 个 Meme Contrast 词。
- 组合后仍然像“同一个人”，而不是为了画风强行换人格。

示例：

用户 Base Persona：`analytical + calm + competent + understated`

- Deadpan Doodle 可编译为：`analytical + calm + deadpan + understated + quietly funny`
- Cool Flat Editorial 可编译为：`analytical + composed + understated + stylish + self-assured`
- Ugly-Cute Internet Cartoon 可编译为：`analytical + awkward + dry + self-aware + subtly weird`

三者仍然是同一个人的不同侧面。

---

# 5. 禁用 / 慎用人格词

角色Mascot IP 默认慎用以下过度负面或道德判断过强的词：

`greedy, ruthless, cruel, manipulative, shameless, paranoid, predatory, malicious, psychotic`

如果想表达类似网感，优先软化为：

- `greedy` → `opportunistic / value-conscious`
- `ruthless` → `decisive / uncompromising`
- `paranoid` → `hyper-cautious / suspicious`
- `sneaky` → `crafty / mischievous`
- `shameless` → `bold / shamelessly practical`

---

# 6. 最终检查

每次生吉祥物格前检查：

- 是否仍然符合用户本人/账号？
- 是否只是把画风人格硬套到用户身上？
- 是否具有 1 个可读的网感钩子？
- 是否避免了 5 个词全部同义重复？
- 是否避免了极端负面人格？
- 用户选中编号后，是否保持人格连续性？
