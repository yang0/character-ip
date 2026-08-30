# Character IP 25-Grid Studio
## Version 11 — Trait Embodiment + Dynamic 150 + Board-Slot Binding + Proportion Inheritance

## 1. Purpose

为用户设计具有强网感、可长期复用、适合 X / 小红书 / 社交媒体内容的个人 Human IP。

首轮：

> 从 150 种 Style Universe 中动态筛选 25 种，并一次生成完整 5×5 / 25 宫格。

用户选编号后：

> 用“原始真人图提供的人物特征 + 选中格风格/人格”重新生成一张 1:1 方形单人 IP，而不是简单放大宫格小图。

---

## 2. Input Router

### Route A — VISUAL_TRAIT_REFERENCE
存在清晰真人照片 / 头像。

### Route B — PERSONA_ONLY
没有真人图，但有账号 / Bio / 文件 / 内容资料。

### Route C — HYBRID_IDENTITY
真人图 + 账号 / 文件 / 文本。

分工：
- image = visual person traits
- text = persona/context
- style = how to translate
- expression engine = attitude

---

## 3. Core Goal — Trait Embodiment, Not Literal Resemblance — P0

当存在真人参考图时，目标不是把 IP 做得“越来越像照片”。

目标是：

> 让 IP 的头部、脸、发型、年龄感和整体神态，能够明显体现这个人的人物特征，同时完全属于目标画风。

必须遵守：

> The goal is not photoreal resemblance. The goal is stylized embodiment of the person's recognizable traits, age impression, and overall vibe.

成功标准不是：
- 像证件照
- 像真人肖像
- 五官位置逐点复刻

成功标准是：
- 有这个人的头部味道
- 有这个人的脸型/眉眼/发型/年龄感趋势
- 某些有辨识度的地方可以被适度放大
- 不被风格默认帅哥 / 美女脸吞掉
- 头部与整体画风完全一致

---

## 4. Visual Trait Authority — P0

只要存在真人参考图：

> 原始真人图始终是人物特征的视觉主源。

不要先把真人脸拆成一长串 Face DNA / S1-S5 / 五官参数，再依赖文字重建。

模型应直接看图，在生成过程中隐式理解并体现：
- whole-head character
- face-shape tendency
- hairstyle architecture
- facial relationship character
- age impression
- gender expression
- overall vibe

这些可以被风格化、简化、夸张，但不能被替换成通用模板脸。

### 25 宫格
每一格都必须独立直接重新参考原始真人图。

### 单张定稿
原始真人图再次作为人物特征主参考。
选中格只负责：
- style
- personality
- expression
- pose
- outfit
- palette
- material

如果选中格已经模板化：
> 定稿时应重新把人物特征带回来，而不是忠实放大错误脸。

---

## 5. Whole-Head Stylized Translation — P0

保留的是：
- recognizable head identity cues
- head/face overall character
- hairstyle family and volume
- age impression
- facial attitude / vibe

不保留的是：
- photographic skin
- portrait lighting
- realistic nose/lip modeling
- photo-like face texture

头必须完整重绘进目标 style。

核心：

> Preserve character traits; translate rendering language.

---

## 6. Implicit Trait Amplification — P0

允许模型直接从参考图视觉判断哪些地方最有辨识度，并在目标画风允许的范围内适度放大。

但必须：
- 不输出一份用户专属 Face DNA 清单作为主驱动
- 不把放大变成丑化
- 不凭空制造参考图中没有的人物特征
- 不为了“更像”而提高写实度

例如可以视觉上适度放大：
- 发型体积与轮廓
- 眉眼态度
- 脸型趋势
- 嘴角/神态
- 某个明显的头部比例特征

一句话：

> Amplify the person's own visual character, not the style's default face.

---

## 7. Template Face Suppression — P0

禁止风格化自动变成：
- generic anime protagonist
- generic webtoon handsome face
- universal V-line jaw
- universal sharp hero brows
- universal narrow/upturned eyes
- generic cute round face
- style-default beauty template

核心：

> Stylize this person, not the style's ideal person.

---

## 8. Reference Expression Is Not Identity

参考图某一瞬间的微笑 / 中性表情不是身份锁。

具体表达由：

`Personality Engine → Expression & Pose Engine`

动态生成。

明显 smile <=5/25。
neutral/polite/mild smile <=6/25。

---

## 9. Reference Clothing Is Not Identity

除非明确要求：
- 源图服装不得大量复制
- 25 格至少 8 种 outfit silhouette

---

## 10. Square Social Character System + Proportion Inheritance — P0

所有标准 IP 图，包括 25 宫格和选号后的单张定稿，都必须同时满足：

1. `1:1 square canvas`
2. `stylized social-IP anatomy`

仅画布是 1:1 不算达标。人物如果恢复成普通成人/时尚立绘比例，仍然属于失败。

全局比例：
- default target: 4.2–5.2 heads
- normal allowed: 3.8–5.4 heads
- hard max: 5.6 heads
- realistic 6.5–8 head fashion/model anatomy: forbidden unless user explicitly requests it

每个 Board Slot 必须冻结一个 `proportion_profile`。

用户选号后，单张 refinement 必须继承该 `proportion_profile`，禁止重新正常化人体。

真人参考图：
- 可以决定头部人物特征、年龄感、气质
- **不得作为身体比例参考**

选中 Tile：
- 提供 style / silhouette / characterization / proportion read
- 但若实际 Tile 本身超过全局 Social-IP 上限，则全局比例锁优先

核心：

> Refinement increases polish, not anatomical realism or normalization.

---

## 11. Dynamic 150 Style Universe

Canonical IDs：
`S001–S150`

用户看到的 `01–25` 只是当前 board slot。

每轮动态选择：
- 10 Core Fits
- 7 Adjacent
- 5 Exploratory
- 3 Wildcards

使用 Progressive Disclosure：
1. 读 styles/INDEX.md
2. 选 25
3. 只读相关 Family Recipe

---

## 12. Character-First Style Diversity

背景不同不算人物风格不同。

差异必须进入：
- head rendering
- facial abstraction
- line system
- body proportion
- silhouette
- outfit
- material
- palette
- shading
- expression / pose language

---

## 13. Personality / Expression / Pose

沿用：
`70% User Base Persona + 20% Style Affinity + 10% Meme Contrast`

人格必须编译成：
- expression
- gaze
- head pose
- body pose
- empty-hand gesture

25 格至少 9 个 Expression Families，至少 8 个 Pose Families。

---

## 13.5. Selected-Slot Proportion Continuity — P0

用户选择某个格子后，必须从 Frozen Slot State 读取：
- `proportion_profile`
- `target_head_count`
- `head_size_bias`
- `limb_length_bias`
- `torso_leg_balance`
- `silhouette_compactness`

单张定稿不得因为“高清、精修、成熟、时尚、Editorial”等词自动把身体拉回普通真人比例。

Reference priority for body proportion:

`Frozen proportion_profile > selected tile proportion read > style default > real-photo body anatomy (never)`

如果用户明确要求改变比例，才允许更新 proportion profile。

---

## 14. Board / Slot Binding — P0

每次 25 宫格生成前必须先创建并冻结 Board Manifest。

唯一选择键：

`character_id + board_id + grid_slot`

其中：
- `grid_slot` 永远与图片上可见编号 `01–25` 一致
- `01–25` 只代表当前 Board 的位置，不代表固定 style_id
- 新 Board 可以重新分配 25 个 Style，但旧 Board 的 slot 映射永久不变

用户选号时：

> **Selection is retrieval, not regeneration.**

禁止重新运行 Style Selector。必须读取该 Board 已冻结的 slot state。

多张 Board 并存时：
- `02` → 当前 active / 最新 Board 的 02
- `第二张图的02` → board_ordinal=2 + slot=02
- `上一版17` → previous board + slot=17

此外，选号后必须同时使用：
1. Frozen Slot State（style/personality/expression/pose/outfit 语义）
2. Actual Rendered Tile Visual（用户实际看到的该格视觉）

如果“计划 Style Recipe”和“实际画出来的格子”有偏差：
- 用户实际看到并选中的 Tile 决定最终 Look
- Frozen Recipe 只做语义辅助
- 真人原图仍负责人物 Trait Embodiment，不让生成 Tile 的模板脸成为身份主源

详见：`modules/13_board_state_registry.md`。

---

## 15. Trait Embodiment Gate — P0

生成后不再用“像不像照片”作为最高验收标准。

检查：
1. stylized identity read — 是否有这个人的整体味道
2. head character embodiment — 头脸趋势是否体现人物本身
3. hairstyle embodiment — 发型结构/体积是否有来源感
4. age impression stability — 年龄感是否稳定
5. vibe/personality continuity — 基础气质是否仍可识别
6. template-face suppression — 是否掉进通用模板脸
7. style coherence — 脸是否完整属于目标画风

如果最终只是“一个很好看的风格人物，但人物特征被模板脸吞掉”：FAIL。

如果为了提高相似度而变得更真人：FAIL。

---

## 16. Selection Refinement — P0

选号后执行：

`Original Visual Traits + Selected Tile Look + Frozen Slot State + Frozen Proportion Profile → New 1:1 Render`

不是：

`Selected Grid Face → Upscale`

最终优先级：

`trait embodiment > style coherence > age stability > personality readability > social-IP proportion > polish > literal resemblance > realism`

---

## 17. Final Success Standard

最终角色应该让用户感受到：

> “这不是我的真人脸复制，但这个 IP 的头、气质和神态明显有我的特征。”

而不是：

> “这是一个和我发型差不多的通用动漫帅哥/美女。”
