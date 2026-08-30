# Module 02 — Visual Trait Translation

## 1. Purpose

当存在清晰参考角色参考图时，本模块负责让模型直接看参考图，理解这个人的整体头部特征、年龄感和气质，再把这些角色特征完整翻译进目标画风。

本模块不追求“参考角色脸复制”。

核心：

> Reference image supplies the person's visual character; the target style decides how that character is drawn.

---

## 2. P0 — Direct Visual Reference

每一次生图都必须重新直接参考原始参考角色图。

### 25 宫格
25 个格子都把原始参考角色图视为自己的直接 visual trait source。

禁止：
- 01 的生成脸变成 02–25 的脸部母版
- 用生成后的通用卡通脸继续推导
- 把某个 style template 当作角色身份源

### 选号后的单张定稿
必须再次引入原始参考角色图。

此时：
- 原始参考角色图 = person traits / age / vibe reference
- 选中宫格 = style / personality / pose / outfit direction

---

## 3. Trait Embodiment, Not Literal Copy

直接从参考图整体读取并体现：
- whole-character character
- face-shape tendency
- head/body proportion character
- hairstyle architecture and volume
- facial relationship character
- age impression
- gender expression
- overall vibe

这些信息由模型直接从图像理解，不需要先生成用户专属详细特征表。

最终允许：
- 简化
- 漫画化
- 图形化
- Q 化
- 夸张
- 符号化

但不能：
- 被通用模板脸替代
- 为了提高相似度增加参考角色质感

---

## 4. Implicit Visual Amplification

模型可以直接从参考图中自行判断最有辨识度的地方，并在当前 Style Recipe 允许的抽象程度内适度放大。

例如可以影响：
- hair mass / silhouette
- brow-eye attitude
- face-shape tendency
- mouth attitude
- head proportion impression

关键：

> Do not output or depend on a textual Face DNA inventory as the primary generator input.

---

## 5. No Beauty Normalization

风格化不等于“美型模板化”。

禁止模型无依据自动：
- 拉长窄化脸
- 统一 V-line 下巴
- 统一锐眉
- 统一狭长上挑眼
- 统一小鼻高鼻
- 统一韩漫 / 日漫主角脸
- 统一萌系圆脸

除非这些确实是参考图视觉特征，或用户明确要求。

---

## 6. Age Is Part of Character

必须保持原参考图的年龄感。

允许：
- mascot chibi
- mascot doodle
- mascot pixel
- mascot sticker

禁止：
- 大头 = 儿童
- 可爱 = 幼儿
- 极简 = 少年化

---

## 7. Reference Expression / Clothing Are Not Frozen

参考角色参考图负责角色特征，不默认锁定：
- source smile
- source neutral face
- source body pose
- source clothing
- source clothing colors

Expression 由 Personality / Expression Engine 生成。
Outfit 由 Style / Persona / Aesthetic 生成。

---

## 8. Head–Body Style Harmony

头部必须与身体属于同一画风。

禁止：
- photoreal head + cartoon body
- semi-real portrait face + flat body
- photographic skin + doodle / sticker / pixel body

Trait embodiment 与 photorealism 完全独立。

---

## 9. Trait Embodiment Check

生成后直接看结果是否成功体现角色特征，而不是检查是否像照片。

检查：
1. 头部整体有没有这个人的味道
2. 脸型/五官关系是否体现角色趋势而不是 style default
3. 发型是否有来源感
4. 年龄感是否稳定
5. 基础气质是否仍可识别
6. 是否出现模板脸覆盖
7. 是否保持目标画风统一

如果结果只是“一个好看的通用角色”：FAIL。
如果结果为了相似而变成半参考角色：FAIL。
