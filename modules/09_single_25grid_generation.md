# Module 09 — One-Shot 25-Grid Generation v13

## P0
必须一次生成完整 25 宫格。

禁止默认：
- 5 批 × 5
- 25 张单图再拼
- 逐行生成

---

## 1. Pre-Render Board Manifest — P0

在生图之前必须已经存在冻结的：
- `design_context`
- `run_id`
- `history_access`
- `character_id`
- `board_id`
- `board_ordinal`
- `slots[01..25]`

每个 slot 已经绑定：
- canonical style_id
- style_recipe_snapshot
- matched_personality
- expression / gaze / head pose
- body pose / empty-hand gesture
- outfit logic
- frozen proportion_profile
- `MASCOT`：carrier_species / carrier_family / carrier_archetype / carrier_rationale

生成阶段只消费 Manifest，不得重新选 Style 或重新排序。

`FRESH_DESIGN` 必须从 run-scoped Manifest 读取，并在生成前确认 `history_access: none`；不得回查旧 Board 来补全任何 slot。

---

## 2. Visible Number / Position Lock — P0

必须严格 row-major：

```text
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

图片左上角显示的编号必须等于该位置的 `grid_slot`。

禁止：
- Style ID 直接充当可见编号
- 根据画面生成结果重新编号
- 生成后重新排序候选

---

## 3. Canvas
- 1:1
- 5×5 equal cells
- 25 full-body characters
- semitransparent 01–25 labels

---

## 4. Character Continuity
参考角色模式下：
- 25 格都直接参考原始参考角色图的角色视觉特征
- 保持年龄感和头部来源感
- 不要求每格做成同一张参考角色脸
- 不允许 style-default template face 抹掉角色特征
- no handheld props
- stylized mascot IP proportions; every slot must carry a frozen proportion_profile

---

## 5. Source Photo Rules
参考角色模式下：
- 体现 whole-character visual character
- 允许隐式放大角色本身有辨识度的地方
- 不复制源图瞬时表情
- 不复制源图服装
- 不复制源图姿态
- 不保留摄影式参考角色脸质感

---

## 6. Per-Slot Compile Contract

每格从 Frozen Manifest 读取：

```yaml
grid_slot
row
col
carrier_species
carrier_family
carrier_archetype
carrier_rationale
style_id
style_recipe_snapshot
matched_personality
expression_family
expression_cue
gaze_cue
head_pose_cue
body_pose_cue
empty_hand_gesture
outfit_logic
proportion_profile
```

Prompt 中必须明确写：

> Slot 02 is row 1 column 2 and must be labeled 02. Render the exact design state assigned to slot 02.

其余 slot 同理。

---

## 7. Expression Diversity
- >=9 expression families
- same expression family <=5
- obvious smile variants <=5
- neutral/polite/mild-smile <=6

## 8. Pose Diversity
- >=8 pose families
- same pose family <=7
- both hands in pockets <=3
- all pocket poses <=8

## 9. Outfit Diversity
- >=8 outfit silhouette families
- source-reference-like outfits <=3 unless user explicitly requests preservation

## 10. Visual Separation
每格至少在以下维度中有 4 项明显不同：
- head rendering
- facial abstraction
- line / edge system
- frozen proportion_profile
- texture
- palette
- medium
- outfit silhouette
- silhouette
- expression language
- pose language
- background graphic treatment

仅背景不同不算 style difference。

## 11. Adult Age Rule
Q / kawaii / chibi 只能改变比例，不得改变年龄层。

## 12. Post-Render State Binding — P0

渲染完成后必须把 `board_image_ref` 写回对应 Board。

每个 slot 保存：
- row / col
- normalized bbox
- actual rendered tile visual reference（若环境支持 crop）
- render_alignment_score（可选）

之后用户选号时必须通过：

`board_id + grid_slot → actual tile position`

找到用户真正看到的格子，而不是通过 Style 名称猜测。

## 13. Number Alignment Gate
接受结果前检查：
- 01–25 全部存在
- 无重复
- 无漏号
- 位置严格 row-major
- visible label = frozen grid_slot

编号错位属于 Board 生成失败。
