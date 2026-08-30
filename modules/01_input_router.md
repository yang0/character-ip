# Module 01 — Design Context + Role Category + Input Router v13

## Goal
先判断设计上下文与人类/吉祥物类别，再判断输入路线。

## P0 — Design Context Gate

此 Gate 必须先于任何历史读取、风格选择、Carrier Plan 或 Manifest 创建。

```text
explicit old Board/slot/image + continue/refine/modify → CONTINUATION
new session                                            → FRESH_DESIGN
"重新设计/重新做/从头设计/再来一批"                    → FRESH_DESIGN
new candidate request without explicit old Board       → FRESH_DESIGN
```

### FRESH_DESIGN Isolation — P0

- 不得枚举、读取或引用 `state/`、`output/`、旧 Manifest、旧图片、历史 style/carrier 记录。
- 生成新的 `run_id`；首张 Board 固定为 `B001`，不通过查找旧编号命名。
- Manifest 路径必须为 `state/runs/<run_id>/board-B001-manifest.yaml`，输出路径必须位于 `output/runs/<run_id>/`。
- Manifest 必须记录：`design_context: FRESH_DESIGN`、`run_id`、`history_access: none`。

### CONTINUATION Access — P0

- 只允许读取用户明确点名的单个 Board、其选中 slot 与必要的关联图片。
- 新 Manifest 必须记录 `design_context: CONTINUATION` 与 `history_access: {mode: explicit_single_board, board_id: <id>}`。
- 不得扫描其他历史 Board；新 Board 的 styles 和 carrier families 均需与点名 Board 至少 80% 不重合。

## P0 — Role Category Gate

在 `VISUAL_TRAIT_REFERENCE`、`PERSONA_ONLY`、`HYBRID_IDENTITY` 前完成：

```text
explicit HUMAN request              → HUMAN
explicit MASCOT request             → MASCOT
clear human reference photo         → HUMAN
named real person                   → HUMAN
otherwise                           → ASK_USER
```

“明确需求”必须明确指向人类或吉祥物；“设计 IP”“设计角色”“做个形象”不算。

当结果为 `ASK_USER` 时，只问：

> 需要设计人类 IP 还是吉祥物 IP？

此时立即停止，不得猜测、不得选择 style、不得创建 Board Manifest 或生成图。

### Explicit-Instruction Override

- 用户明确要求 mascot，即使同时给了人类照片或姓名，也走 `MASCOT`。
- 用户明确要求 human，即使账号历史曾使用 mascot，也走 `HUMAN`。
- 不得用历史项目、上次选择或 Skill 名称覆盖本次明确类别。

## Route A — VISUAL_TRAIT_REFERENCE
触发：
- 有清晰参考角色照片 / 头像
- 头部可辨识

策略：
- 图片是角色视觉特征主来源
- 直接做 Visual Trait Translation
- 不把“高相似度参考角色脸”当目标
- 不先生成长篇 Face DNA 再重建

## Route B — PERSONA_ONLY
触发：
- 无清晰参考角色图
- 但有账号链接 / 文件 / Bio / 作品 / 内容资料

策略：
- 从内容人格、审美、职业角色构造角色 IP
- 不声称参考角色长相还原

## Route C — HYBRID_IDENTITY
触发：
- 参考角色图 + 文本/账号/文件

策略：
- 图片负责角色视觉特征、年龄感、头部味道
- 文本负责长期人格、内容角色、审美

## Route Priority
在 `role_category` 已确定后：

`explicit user instruction > usable real image > persona source > inferred context`

## No Forced Clarification
`role_category` 是 P0 关键资料。类别已确定后，才不要因为缺少非关键资料而打断流程。
