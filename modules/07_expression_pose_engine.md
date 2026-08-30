# Module 07 — Expression & Pose Engine

## 1. Purpose

把 `Final Personality` 真正编译成可见的角色气质，而不是只停留在文字标签。

本模块负责把人格映射到：
- facial expression
- brow / eye attitude
- gaze direction
- head tilt
- shoulder / torso tension
- standing posture
- empty-hand gesture

核心目标：

> 同一个人可以有稳定身份，但 25 格不能共享同一个“礼貌微笑模板”。

---

## 2. Reference Expression Is Not Identity — P0

参考角色参考图中的瞬时表情不是身份锁。

有参考角色图时：
- 保留 whole-character identity
- 保留 age impression
- 保留 gender expression
- 可把照片里的基础气质作为弱信号
- **不得把照片中的微笑 / 抿嘴 / 正脸神态复制到全部 25 格**

必须遵守：

> Preserve identity and base vibe; regenerate expression per variant.

---

## 3. Base Vibe vs Variant Expression

### Base Vibe
来自用户本人 / 账号长期气质，例如：
- calm
- sharp
- relaxed
- warm
- clean
- composed
- playful

Base Vibe 可以跨 25 格稳定存在。

### Variant Expression
必须根据每格的：
- matched personality
- style affinity
- meme contrast

动态生成，例如：
- deadpan
- skeptical
- tired
- faintly smug
- awkward
- playful
- unimpressed
- focused
- quietly amused
- confused / blank
- curious
- restrained serious

---

## 4. Personality-to-Visual Compiler

每个格子都必须生成以下 4 个视觉字段：

```yaml
expression_cue: string
gaze_cue: string
head_pose_cue: string
body_pose_cue: string
empty_hand_gesture: string
```

人格不能只影响衣服或背景。

至少同时影响：
1. 眉眼 / 嘴角
2. 头部角度或视线
3. 身体重心 / 肩颈
4. 空手姿态

---

## 5. Expression Families

调用：
`registries/ExpressionFamilies.md`

25 格至少覆盖 `9` 个 Expression Families。

同一个 Expression Family 最多：
`5 / 25` 格。

### Smile Cap
带明显上扬嘴角、礼貌微笑或甜笑的格子总计最多：
`5 / 25`。

参考照片即使在微笑，也不提高该上限。

### Deadpan / Skeptical / Tired 等
允许成为互联网人格的重要表达，但不能 25 格都变成冷脸。

---

## 6. Pose Diversity — P0

No-Prop 不等于全员插兜。

25 格至少覆盖 `8` 种空手 Pose Families。

可用：
- arms relaxed at sides
- one hand in pocket
- both hands in pockets
- arms folded
- one hand on hip
- hands behind back
- one hand loosely holding the other wrist
- small empty conversational gesture
- asymmetric relaxed lean
- slight forward lean
- compact inward posture
- straight composed stance

### Limits
- 任意单一 pose family 最多 `7 / 25`
- `both hands in pockets` 最多 `3 / 25`
- 所有 pocket poses 合计最多 `8 / 25`

---

## 7. Adult Age Preservation

人格表达和 Q 化不能改变年龄层。

允许：
- 成年人做 deadpan / awkward / cute / playful

禁止：
- 因为 kawaii / chibi 风格把成年用户变成儿童
- 用幼儿式圆脸、婴儿表情、幼童肢体语言替代吉祥物年龄感

核心：

> Cute proportion does not imply child age.

---

## 8. Expression Intensity by Style

不同 style 有不同 expression_capacity：

- `low`：主要靠微表情、眉眼和姿态
- `medium`：允许明显但克制的表情变化
- `high`：允许更强表情图形化
- `very-high`：允许 Reaction / Meme 级夸张

即使 `very-high`：
- 仍保留年龄感
- 仍保留头部身份感
- 不做极端颜艺污染标准 IP 身份

---

## 9. Anti-Safe-Smile Rule

以下结果视为失败：
- 25 格大多数都是轻微微笑
- 25 格眉眼张力几乎相同
- Personality 文本不同但脸部看不出区别
- 所有姿态都是双手插兜 + 微笑

目标：

> 25 格既像同一个人，又像这个人拥有 25 个可用于互联网表达的侧面。
