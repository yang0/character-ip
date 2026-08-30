# Module 05 — Square Social Character System + Proportion Lock v11

## 1. P0 — Square Is Canvas + Anatomy

所有标准个人 IP 资产默认：

`1:1 square`

包括：
- 25 宫格
- 选号后的单张定稿
- 后续标准角色资产

但 **1:1 画布本身不等于合格的 Square Social Character**。

必须同时满足：
- square canvas
- visibly stylized social-IP anatomy

如果角色恢复为普通成人立绘 / 时尚模特人体，即使画布是 1:1，也属于 FAIL。

---

## 2. P0 — Social-IP Anatomy, Not Human Model Anatomy

默认目标：

> stylized adult social character

不是：

> realistic fashion-model illustration

### Recommended Target
`4.2–5.2 heads`

### Normal Allowed Range
`3.8–5.4 heads`

### Hard Maximum
`5.6 heads`

超过 5.6 头身：

> quality gate fail

除非用户明确要求真人 / 模特比例，任何 Style Recipe、Editorial、Fashion、Webtoon、精修指令都无权突破。

---

## 3. P0 — Refinement Must Not Normalize Anatomy

选号后的单张 refinement 常见错误：

`small grid IP → high-resolution refinement → normal adult illustration proportion`

这是禁止的。

必须遵守：

> Refinement increases polish, not anatomical realism or normalization.

高清化可以提升：
- line quality
- color control
- material
- silhouette clarity
- facial stylization
- clothing detail

不得自动改变：
- head-to-body scale
- limb compactness
- torso-leg balance
- social-IP silhouette

---

## 4. Proportion Profile — Frozen Slot Property

每个 Board Slot 在渲染前必须冻结：

```yaml
proportion_profile:
  body_mode: social_ip
  target_head_count: 4.8
  allowed_variance: 0.3
  head_size_bias: slightly_large
  limb_length_bias: shortened
  torso_leg_balance: compact_stylized
  silhouette_compactness: medium_high
  realistic_anatomy_normalization_allowed: false
```

该 Profile 属于用户看到的候选设计状态。

选号后必须继承，不得重新从 Style 名称推断。

---

## 5. Reference Roles for Proportion

### Original Real Photo
只负责：
- visual person traits
- age impression
- hairstyle / head character
- base vibe

**绝不能用真人照片的身体作为单张 IP 的比例参考。**

### Selected Rendered Tile
负责：
- style look
- silhouette feeling
- character compactness
- stylization degree
- visual proportion read

### Frozen Proportion Profile
负责：
- canonical body envelope
- exact intended IP head/body balance

冲突时：

`Frozen proportion_profile > selected tile proportion read > style-family tendency > real-photo anatomy (never)`

---

## 6. Style Cannot Override Social-IP Envelope

即使是：
- fashion editorial
- sophisticated manga
- designer character
- webtoon
- watercolor fashion
- luxury illustration

也必须在 Social-IP Envelope 内表达高级感。

用这些表达高级感：
- tailoring
- silhouette design
- posture
- palette
- line language
- material
- negative space

不要靠：
- 7–8 头身
- 超长腿
- 超小头
- runway model anatomy

---

## 7. Head Presence

标准人物必须具有明显 IP 感：
- head visibly larger than realistic anatomy
- torso and limbs compact enough for square social-media readability
- full body readable at thumbnail scale

单张 1:1 建议角色占画布高度：

`72–82%`

---

## 8. Adult ≠ Realistic Proportion

成年人可以：
- 头略大
- 四肢更紧凑
- 身体更图形化
- 轮廓更有 IP 感

同时通过：
- 成人眉眼
- 成人肩颈
- 成人服装
- 成人表情
- 成人姿态

维持年龄感。

禁止用恢复真人比例来表达“成熟”。
