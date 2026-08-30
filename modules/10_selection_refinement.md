# Module 10 — Selection Refinement v13

## 1. Trigger

用户可以输入：
- `02`
- `第二张图的02`
- `上一版17`
- `第一版04`

先由 Board State Registry 解析 `run_id + board_id + grid_slot`。只有 `CONTINUATION` 且用户明确点名旧 Board 时，才可读取历史 Board。

---

## 2. Selection Is Retrieval — P0

选号后禁止重新运行 Style Selector。

必须从 Frozen Board Manifest 读取该 slot：
- role_category
- style_id
- style_recipe_snapshot
- matched personality
- expression / gaze / pose state
- outfit logic
- **proportion_profile**

> Selection is retrieval, not regeneration.

---

## 3. Bind the Actual Rendered Tile — P0

用户选择的是“他实际看到的那个格子”。

因此必须获取：
- `board_image_ref`
- selected slot row / col
- selected tile bbox
- `selected_tile_visual_ref`（支持裁切时）

如果不能裁切，使用完整 Board + 明确 row/col/slot 指向该格。

---

## 4. Role Continuity — P0

refinement 必须继承 source slot 的 `role_category`。不得在精修时把 human 改成 mascot，或把 mascot 改成人类；只有用户明确要求重新设计并改变类别时，才可创建新 Board。

## 5. Triple Reference Contract — P0

参考角色模式下：

### Reference A — Original Real Photo
职责：
- visual person traits
- age impression
- hairstyle source character
- base vibe

**Reference A 不负责身体比例。**
不得因为参考角色图存在，就恢复参考角色照片中的 head/body anatomy。

### Reference B — Actual Selected Rendered Tile
职责：
- 用户真正选择的 style look
- visual abstraction
- expression feeling
- pose / outfit silhouette
- palette / material
- stylization / compactness read

### Frozen Slot State
职责：
- canonical style semantics
- personality semantics
- expression/pose/outfit intent
- **frozen proportion_profile**
- continuity metadata

角色 Trait：`A > B`

用户选中的视觉 Look：`B > Frozen Recipe`

身体比例：`Frozen proportion_profile > B's visual proportion read > style defaults > A body anatomy (never)`

---

## 6. Re-Embodiment, Not Enlargement

用户点选某格后，不是像素放大。

执行：

`original visual traits + actual selected tile look + frozen slot semantics + frozen proportion_profile → clean re-render`

如果选中格的脸模板化：
- 角色特征从原图重新带回来
- 不增加参考角色感

如果单张生成开始恢复参考角色身体：
- 立即恢复 frozen proportion_profile
- 不允许以“更精致 / 更成熟 / 更时尚”为理由拉长身体

---

## 7. P0 — Proportion Inheritance Contract

每个 selected slot 必须有：

```yaml
proportion_profile:
  body_mode: social_ip
  target_head_count: 4.2..5.2
  allowed_variance: <=0.4
  head_size_bias: slightly_large | large | style_compact
  limb_length_bias: shortened | compact | moderate
  torso_leg_balance: compact_stylized | balanced_stylized
  silhouette_compactness: medium | medium_high | high
  realistic_anatomy_normalization_allowed: false
```

单张 refinement 必须继承。

禁止：
- 把 4.7 头身候选变成 6.5 头身
- 头明显缩小
- 腿明显增长
- 肩腰恢复时装模特人体
- 仅因为高清化就改吉祥物体正常比例

如果 selected tile 的实际渲染比例已经略超规则：
- 不继续放大错误
- 收回到 global social-IP envelope
- 保留它的风格和 silhouette 味道

---

## 8. Output

默认：
- strict 1:1 square
- one full-body IP consistent with role_category
- character height 72–82%
- target 4.2–5.2 heads
- normal 3.8–5.4
- hard max 5.6
- no handheld props

强调：

> 1:1 canvas alone is insufficient; the anatomy must still read as an IP character.

---

## 9. Anti-Normalization Check — P0

最终输出前检查：

FAIL if:
- body visibly shifts toward normal realistic mascot anatomy
- head becomes too small relative to body
- legs become fashion-illustration long
- silhouette loses compact social-IP readability
- result reads as a normal character illustration placed on a square canvas

PASS only if:
- selected style remains intact
- mascot age remains intact
- body remains clearly stylized / IP-proportioned

---

## 10. Refinement Lineage

创建：

```yaml
refinement_id: Rxxx
source:
  character_id: Cxxx
  board_id: Bxxx
  grid_slot: "02"
  style_id: Sxxx
  proportion_profile_id: PP_Bxxx_02
parent_refinement_id: null
```

后续“这个再改一下”沿 refinement lineage 继续。

除非用户明确说“身体比例改成……”，否则比例 Profile 保持冻结。

---

## 11. Trait Embodiment Goal

最终应：
- 有本人特征来源感
- 充分 IP 化
- 年龄感稳定
- 画风与用户所选实际 Tile 一致
- 不被 template face 覆盖
- 不是半参考角色脸
- **不是正常人体立绘**

优先级：

`selected-tile look fidelity + trait embodiment + proportion continuity > style-registry literalism > polish > realism`
