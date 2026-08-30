# Architecture — v11 Trait Embodiment + Dynamic 150 + Board-Slot Binding + Proportion Inheritance

## 1. Core Change from v10

v10 已解决 Board / Slot 选号状态错位。

v11 新增 P0：

> **Proportion Inheritance：选号后的单张高清定稿必须继承宫格候选的 IP 身体比例，禁止自动恢复普通真人 / 时尚立绘比例。**

重点：
1. 原始真人图仍然是视觉人物特征主源
2. 不先输出详细 Face DNA / S1-S5 特征表
3. 模型直接看图，隐式抓人物特征
4. 允许把有辨识度的地方适度风格化放大
5. 不追求摄影式相似
6. 严格压制 style-default template face
7. 头部必须完全属于目标画风

---

## 2. Pipeline

```text
INPUT
↓
Input Router
↓
├─ VISUAL_TRAIT_REFERENCE
│  └─ original photo = visual trait authority
├─ PERSONA_ONLY
│  └─ persona/account → constructed character identity
└─ HYBRID_IDENTITY
   └─ photo = visual traits / text = persona
↓
Base Persona / Aesthetic Context
↓
150 Style INDEX
↓
Dynamic 25 Style Selection
↓
Progressive Family Recipe Loading
↓
Personality Engine
↓
Expression & Pose Engine
↓
CREATE + FREEZE BOARD MANIFEST
  ├─ character_id
  ├─ board_id
  └─ slots 01–25 with full style/personality/expression/pose/outfit/proportion snapshots
↓
ONE-SHOT 25-GRID
  ├─ every tile directly references original photo for visual traits
  └─ visible number = frozen grid_slot
↓
Trait Embodiment + Number Alignment Gate
↓
User selects board + slot
↓
RETRIEVE frozen slot state (never rerun selector)
↓
Bind actual rendered tile visual
↓
TRIPLE-SOURCE REFINEMENT
  ├─ original photo = visual person traits
  ├─ actual selected tile = chosen visual look
  └─ frozen slot state = semantic + proportion continuity
↓
1:1 Square Social-IP Final
↓
Trait Embodiment Gate
```

---

## 3. Visual Trait Architecture

禁止：

`photo → detailed textual face DNA → regenerate`

主路线：

`photo → direct visual trait reading → stylized embodiment`

不保存用户专属的长篇五官参数表。

保存的是：
- original reference handle
- visual trait policy
- age-stability policy
- style/personality state
- quality scores

---

## 4. Implicit Amplification Architecture

模型可以在视觉层面自行判断并强调参考图中最有识别力的头部特征。

这一步：
- 不要求输出文字特征表
- 不要求固定 S1-S5
- 不要求逐点几何匹配

它只要求：

> 最终 IP 脸不能被风格模板覆盖，而且人物自己的视觉特点要被读出来。

---

## 5. Refinement Architecture

选号不是“把宫格小图放大”。

正确逻辑：

`Original Visual Traits + Selected Style/Persona State → New Clean Render`

如果宫格脸已经模板化：
- 把人物特征重新带回来
- 不高清化错误脸
- 不通过增加写实度来补救

---

## 6. Social-IP Body Architecture

标准资产：
- 1:1
- target 4.2–5.2 heads
- normal 3.8–5.4
- hard max 5.6

高级 / 时尚感应通过服装、姿态、版式、材质表达，而不是 7–8 头身。

---

## 7. Quality Philosophy

v10 继续不把 photoreal resemblance 作为成功标准，同时把选号一致性纳入质量标准。

高质量 =
- 高 trait embodiment
- 高 style coherence
- 高 age stability
- 高 template-face suppression
- 高 personality readability
- 低 photoreal leakage
- 高 board/slot numbering integrity

---

## 8. Failure Modes

以下视为失败：
- 为了“像”而做成半真人脸
- 只剩发型像，人物脸味道丢失
- 风格默认美型模板覆盖用户特征
- 年龄感明显漂移
- 头部与身体画风不一致
- 选中格错误模板脸在定稿中被放大
- 结果虽然好看，但换个人也一样成立

---

## 9. Style / Expression / Outfit

继续沿用：
- 150 Style Universe
- 25 dynamic selection
- expression diversity
- pose diversity
- outfit independence
- character-first style diversity


---

## 10. Board / Slot Architecture — v10 P0

每个候选格子的唯一键：

`character_id + board_id + grid_slot`

例如：`C001/B002/02`。

Board Manifest 必须在生图之前生成并冻结。可见数字使用固定 row-major 位置：

```text
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

用户选中后不是重新计算 Style，而是取回：
- frozen slot state
- actual rendered tile visual

如果实际 Tile 与计划 Recipe 有偏差，最终 Look 以用户实际看到的 Tile 为主；人物身份/特征仍以原始真人图为主。

这样解决多张宫格后 `02` 串到其他 Board 或其他 Style 的问题。


## 11. Proportion Inheritance Architecture — v11 P0

每个 Board Slot 在渲染前冻结 `proportion_profile`。

单张 refinement 使用：

```text
Original Real Photo → head/person traits only
Actual Selected Tile → chosen look / compactness read
Frozen Proportion Profile → body anatomy authority
```

比例权威：

`Frozen proportion_profile > selected tile proportion read > style default > real-photo body anatomy (never)`

高清、精修、成熟、高级、Editorial、Fashion 等语义不得触发人体正常化。

Anti-Normalization Gate 对单张图强制检查：
- head/body ratio continuity
- limb compactness
- torso-leg balance
- silhouette compactness
- social-IP anatomy read

1:1 画布但普通真人比例仍属于失败。
