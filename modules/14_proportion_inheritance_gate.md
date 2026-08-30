# Module 14 — Proportion Inheritance & Anti-Normalization Gate v11

## Purpose

专门阻止选号后的单张 IP 在高清重绘时自动恢复成普通成人 / 时尚立绘身体比例。

---

## 1. Core P0

> Refinement increases polish, not anatomical realism or normalization.

单张定稿不是把“小比例 IP”升级成“正常人体插画”。

---

## 2. Frozen Proportion Profile

Board 创建时，每个 slot 都必须获得独立 `proportion_profile`。

Profile 至少包含：

```yaml
profile_id: PP_B001_01
body_mode: social_ip
target_head_count: 4.8
allowed_variance: 0.3
head_size_bias: slightly_large
limb_length_bias: shortened
torso_leg_balance: compact_stylized
silhouette_compactness: medium_high
realistic_anatomy_normalization_allowed: false
```

Profile 必须在 Board 渲染前冻结。

---

## 3. Proportion Source Priority

单张 refinement 的身体比例来源优先级：

1. Frozen `proportion_profile`
2. Actual selected tile 的视觉 compactness / silhouette
3. 当前 style family 的比例倾向
4. Original real photo body anatomy — **never**

真人图只供头部人物特征、年龄感和气质参考。

---

## 4. Global Envelope

默认：
- target: 4.2–5.2 heads
- normal: 3.8–5.4 heads
- hard max: 5.6 heads

Style、Fashion、Editorial、Webtoon、高清化、成熟化等都不能突破。

---

## 5. Anti-Normalization Signals

以下任一明显出现，应判 FAIL：
- head/body ratio 比选中候选明显变小
- 腿部被明显拉长
- torso + legs 进入普通时装插画比例
- 肩腰和四肢恢复真人模特感
- 原本 compact silhouette 被拉成长条立绘
- 角色虽然在 1:1 画布里，但看起来像正常 2:3 人物被塞进方图

---

## 6. Allowed Refinement

允许提升：
- 清晰度
- 线条
- 面部 IP 化表达
- 材质
- 服装设计细节
- 色彩
- 背景
- 微姿态

默认不允许改变：
- target head count
- head size bias
- limb compactness
- torso-leg balance
- silhouette compactness

---

## 7. Explicit User Override

只有用户明确提出：
- “做成真人比例”
- “腿拉长一点”
- “改成六头身”
- “更接近时装模特比例”

才允许更新 `proportion_profile`。

普通的：
- “放大”
- “高清一点”
- “精修”
- “成熟一点”
- “高级一点”
- “更时尚”

都不得触发人体正常化。
