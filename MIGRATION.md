# Migration — v10 → v11

## Why v11

v10 解决了选号状态错位。

新发现的问题：用户在宫格里选择一个明显 IP 化比例的角色后，单张高清 refinement 有时会自动变成正常吉祥物 / 时尚立绘人体。

这不是画幅 Bug，而是 **Anatomy Normalization Bug**。

## v11 Changes

### 1. Proportion Profile Becomes Slot State
每个 Board Slot 新增 frozen `proportion_profile`。

### 2. Single Refinement Must Inherit It
用户选号后，不仅继承 Style / Personality / Expression，也继承身体比例。

### 3. Real Photo Is Not Body-Proportion Authority
参考角色参考图只负责角色头部特征、年龄感、发型和 vibe。

### 4. Anti-Normalization Gate
新增专门 Gate，阻止：
- 头变小
- 腿拉长
- body 恢复参考角色比例
- 1:1 画布里的普通时装立绘

### 5. Global Envelope Tightened
- target 4.2–5.2
- normal 3.8–5.4
- hard max 5.6

### 6. Refinement Meaning Clarified

> Refinement increases polish, not anatomical realism or normalization.
