---
name: character-ip-router-v13
description: Route Human Character IP versus Mascot IP requests; ask only when the requested role category is unresolved, then create a 5x5 exploration board.
metadata:
  version: 13
---

# Character IP Router V13

## 核心任务

为用户的账号 / 主题 / 栏目设计 Human Character IP 或拟人化 Mascot IP 候选。

重点不是解释，而是：

> 一次生成 1 张 5×5 25 宫格图，
> 并让 **画风应用方式与人物 IP Skill 保持同构**。

## 最高优先级

1. 只生成一张 25 宫格图
2. 25 格必须是独立候选，不是同一角色的纯换皮
3. 风格选择与风格编译，沿用 Human Skill 的流程
4. 先冻结 Board Manifest，再一次生图
5. style 必须真正作用于角色本体，而不只是背景

## P0｜Role Category Gate

先确定 `role_category`，再运行任何视觉/人格路由。

优先级：

1. 用户明确说“人类角色 / 人类 IP” → `HUMAN`
2. 用户明确说“吉祥物 / mascot” → `MASCOT`
3. 用户没有明确类别，但给出清晰人类照片 → `HUMAN`
4. 用户没有明确类别，但目标是有名有姓的具体人物 → `HUMAN`
5. 其他所有情况 → 必须先问：**“需要设计人类 IP 还是吉祥物 IP？”**

用户明确类别始终覆盖照片、人物姓名和历史偏好。第 5 条是 `No Forced Clarification` 的唯一 P0 例外：类别未决时，不得冻结 Board Manifest、生成候选或猜测类别。

## P0｜Design Context Gate

在读取 `state/`、`output/`、旧 Manifest、旧图片或历史风格/物种记录之前，先确定 `design_context`：

- `FRESH_DESIGN`：新会话；用户说“重新设计 / 重新做 / 从头设计 / 再来一批”；或新候选请求没有明确点名旧 Board。
- `CONTINUATION`：用户明确点名旧 Board/slot/图片，并明确要求“继续 / 精修 / 修改”。

`FRESH_DESIGN` 是默认值，且必须：

1. 不枚举、不读取、不引用任何历史 `state/`、`output/`、Manifest、旧图片、历史风格或物种记录。
2. 建立新的 `run_id`，写入 `state/runs/<run_id>/board-B001-manifest.yaml`；每个 fresh run 的首板固定为 `B001`。
3. 输出写入 `output/runs/<run_id>/`；不得覆盖或引用历史资产。
4. 在 Manifest 中记录 `history_access: none`。

`CONTINUATION` 仅可读取用户点名的单个 Board 及其关联选中格。创建后续 Board 时，必须在 Manifest 保存显式引用，并按 `modules/08_style_selector.md` 执行跨 Board 的 style 与 carrier 新鲜度校验。

## 固定流程

### Step 1｜确定设计上下文与角色类别
- 先执行 `modules/01_input_router.md` 的 Design Context Gate，再执行 Role Category Gate。
- `HUMAN`：使用 `prompts/25grid_human.md`，角色为人类 IP；不得引入动物 carrier。
- `MASCOT`：使用 mascot Prompt，角色为非人类拟人化 mascot；不得退化为人类角色。

### Step 2｜理解主题
提炼：
- 账号定位
- 内容主题
- 语义母题
- 平台气质
- sidekick 使用场景

### Step 3｜冻结上游角色变量与 Carrier Plan
在 style 选择之前，先冻结：
- `MASCOT`：25 个 `carrier_species`、`carrier_family`、`carrier_archetype`、`carrier_rationale`；同一 Board 内物种族群不得重复或近缘重复。
- personality
- expression family
- pose family
- silhouette family
- core hooks

### Step 4｜使用风格系统
严格按以下顺序：

1. 读取 `styles/INDEX.md`
2. 执行 `modules/08_style_selector.md`
3. 选出 25 个 canonical style IDs
4. 按 `styles/SELECTION_POLICY.md` 做约束
5. 只读取相关 `styles/families/*.md`
6. 提取每个 style 的完整 recipe
7. 写入 Frozen Board Manifest
8. 执行 `modules/09_single_25grid_generation.md`

### Step 5｜One-Shot 25-Grid
- 1:1 square
- 5×5 equal cells
- 25 个与 `role_category` 一致的 full-body IP 候选
- 半透明编号 01–25
- 每格一个独立候选
- no style names
- no explanatory text

## 重要约束

### Style Application Lock
- style 负责怎么画，不负责定义人格
- personality / pose / carrier 先冻结
- style recipe 必须改变角色本体，不只是背景

### Board Binding Lock
- slot 01–25 先冻结再渲染
- visible numbering row-major
- 不允许渲染后换位、重排、重编号

### Carrier Diversity Lock
- `MASCOT` Board 的 25 格必须分别记录 carrier species、family、archetype 与 rationale。
- 25 个 `carrier_species` 与 25 个 `carrier_family` 都必须唯一；狐狸/赤狐、松鼠/飞鼠、乌龟/机器人乌龟等近缘或修饰命名都视为重复。
- `FRESH_DESIGN` 只检查本板内部多样性，不读取历史。
- `CONTINUATION` 新 Board 相比用户点名的旧 Board，至少 80% 的 carrier families 与 style IDs 为新增。

### Diversity Lock
- 至少 9 个 style families
- 单 family 最多 4 格
- 至少 20 / 25 的 style 在角色本体上有明显 transformation
- 至少 8 / 25 属于强风格变化位

### Prompt Discipline
- 不把 150 个风格全文塞进一个 prompt
- 必须 progressive disclosure
- family recipes 只加载当前 25 个对应部分

## 本版的实验重点

如果用户反馈“人物 Skill 的画风差异更明显”，则本版默认假设：

> 不是风格数量少，而是风格应用机制太弱。

因此本版重点测试：

> **同样的 style application system，用在 mascot 上会不会更有效。**
