# Module 13 — Board / Slot State Registry v13

## Purpose

解决多张 25 宫格并存时，用户输入 `02`、`第二张图的02`、`上一版17` 后，底层 Style State 与用户实际看到的格子错位的问题。

这是 v10 的 P0 状态管理模块。

## 0. Run Scope and History Access — P0

每次请求先由 Module 01 决定 `design_context`。

- `FRESH_DESIGN`：不得解析或扫描旧 Board。创建独立 `run_id`，其首板为 `B001`，状态保存在 `state/runs/<run_id>/`。
- `CONTINUATION`：只有用户明确点名旧 Board/slot/图片并要求继续、精修或修改时成立；只读取该 Board 及必要关联资产。

新 Manifest 必须记录 `design_context`、`run_id`、`history_access`。`FRESH_DESIGN` 的 `history_access` 固定为 `none`；`CONTINUATION` 必须记录 `{mode: explicit_single_board, board_id: ...}`。

---

## 1. Three-Level Identity Key — P0

每一个可选择格子必须使用三层唯一键：

`run_id + character_id + board_id + grid_slot`

例如：

`20260830T201000-x / C001 / B002 / 02`

含义：
- `run_id`：隔离的设计运行；fresh run 之间不共享历史
- `C001`：同一个角色 / 同一个 IP 项目
- `B002`：该角色生成的第二张 25 宫格
- `02`：第二张宫格里的视觉编号 02

禁止只用 `02` 作为全局唯一键。

---

## 2. Visible Number = grid_slot — P0

图片上显示的 `01–25` 必须与 State 中的 `grid_slot` 完全一致。

规则：
- top-left = `01`
- row 1 col 2 = `02`
- ...
- bottom-right = `25`

固定 row-major 映射：

```text
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

位置计算：

```text
row = floor((slot - 1) / 5) + 1
col = ((slot - 1) mod 5) + 1
```

图片编号必须由 `grid_slot` 派生，不能由 Style ID、Style 排名或生成后猜测得到。

---

## 3. Board Manifest Must Exist Before Rendering — P0

在调用一次性 25 宫格生图之前，必须先冻结一个 Board Manifest。

Manifest 至少包含：

```yaml
design_context: FRESH_DESIGN
run_id: 20260830T201000-x
history_access: none
character_id: C001
board_id: B002
board_ordinal: 2
active_board: true
slots:
  "01":
    grid_slot: "01"
    row: 1
    col: 1
    style_id: S087
    style_recipe_snapshot: {...}
    personality_snapshot: {...}
    expression_snapshot: {...}
    pose_snapshot: {...}
    outfit_snapshot: {...}
    proportion_profile: {...}
  "02":
    grid_slot: "02"
    row: 1
    col: 2
    style_id: S131
    ...
```

然后 Prompt 必须严格按照这个 Manifest 的 `01 → 25` 顺序编译。

禁止：
- 先生成图，再反推每格是什么 Style
- 生成后重新排序 Style
- 用户选号时重新运行 Style Selector

---

## 4. Selection Is Retrieval, Not Regeneration — P0

用户选择编号时：

> Selection is retrieval, not regeneration.

正确：

```text
selected_state = frozen_board_manifest[board_id].slots[grid_slot]
```

错误：

```text
selected_state = rerun_style_selector()[grid_slot]
```

Style Selector 只在“创建新 Board”时运行一次。

Board 生成后：
- style_id 冻结
- style recipe snapshot 冻结
- personality 冻结
- expression direction 冻结
- pose direction 冻结
- outfit direction 冻结
- proportion_profile 冻结

除非用户明确要求“换风格 / 重新设计”。

---

## 5. Rendered Tile Is What the User Chose — P0

由于一次生成 25 格时，模型实际画出的 Style 可能与预编译 Recipe 存在一定偏差，因此选号时必须同时绑定：

1. **Frozen Slot State** — 底层语义设计状态
2. **Actual Rendered Tile Visual** — 用户实际看到并选择的格子

如果二者存在视觉冲突：

> 对“选中的外观风格”以用户实际看到的 Rendered Tile 为第一视觉依据；
> Frozen Recipe 作为语义补充，而不是把结果强行拉回原计划 Style。

但参考角色模式下：
- Original Real Photo 仍然是角色特征主参考
- Rendered Tile 不是脸部身份主参考

因此定稿参考优先级为：

### Identity
`Original Real Photo > generated tile face`

### Chosen Look
`Actual Selected Tile Visual > frozen style recipe semantics`

---

## 6. Tile Visual Extraction

Board 渲染完成后，应记录：
- `board_image_ref`
- 每格 `row / col`
- 每格规范化 bbox

例如 slot `02`：

```yaml
tile_bbox_normalized:
  x0: 0.2
  y0: 0.0
  x1: 0.4
  y1: 0.2
```

如果运行环境支持裁切：
- 用户选号后优先裁出该格作为 `selected_tile_visual_ref`

如果不支持裁切：
- 使用完整 board image + `board_id + row + col + grid_slot` 明确指向该格

不得通过 Style 名称猜选中格。

---

## 7. Multi-Board Resolution Rules

同一个角色可以存在多个 Board：

```text
C001 / B001
C001 / B002
C001 / B003
```

解析用户输入：

### 用户只说 `02`
默认解析：
- 当前 active board
- 若没有显式 active board，则使用最新生成的 board

### 用户说 `第二张图的02`
解析：
- `board_ordinal = 2`
- `grid_slot = 02`

### 用户说 `上一版17`
解析：
- active/latest board 的前一个 board
- `grid_slot = 17`

### 用户说 `第一版04`
解析：
- `board_ordinal = 1`
- `grid_slot = 04`

只有在真实歧义无法由 State 消解时才询问用户。

---

## 8. Board Activation

新 Board 创建后：
- 新 Board 设为 `active_board = true`
- 旧 Board 保留，但 `active_board = false`

如果用户明确引用旧 Board：
- 只为本次 selection resolution 使用该旧 Board
- 不必改变 active board，除非用户明确要求“回到这一版继续做”

---

## 9. Refinement Lineage

每一张单图 refinement 都必须记录来源：

```yaml
refinement_id: R004
source:
  character_id: C001
  board_id: B002
  grid_slot: "02"
  style_id: S131
parent_refinement_id: null
```

后续用户说：
- “这个头发短一点”
- “表情冷一点”
- “衣服换成更日常”

应沿当前 `refinement_id` 继续修改，不重新解析到其他 Board / Slot。

---

## 10. Number Alignment Quality Gate

Board 输出前必须检查：
- 01–25 是否唯一
- 是否全部出现
- 是否严格 row-major
- visible number 是否等于 grid_slot
- slot manifest 数量是否恰好 25
- 图片第 N 个位置与 Manifest 第 N 个 slot 是否同序编译

发现编号重复、错位、漏号时，视为 Board QA Failure。

---

## 11. Critical Summary

三个不可违反的规则：

> **Visible grid number = immutable grid_slot.**

> **Board + slot is the selection key.**

> **Selection retrieves frozen state and the actual rendered tile; it never reruns style selection.**


## 11. v11 Proportion Binding — P0

每个 `board_id + grid_slot` 还必须唯一绑定一个 `proportion_profile`。

用户选号后：
- Style 不重抽
- Personality 不重抽
- **身体比例也不重算**

单张 refinement 默认继承该 profile。

原始参考角色图不能覆盖这个比例状态。
