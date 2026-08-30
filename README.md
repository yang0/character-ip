# Mascot IP Prompt Studio V11

这是一个把你提供的 **Human Character IP Skill 的风格应用机制 1:1 移植到 Mascot 场景** 的版本。

## 这版的目标

不是继续微调旧版 Mascot Skill，而是把“人物 IP Skill 里风格为什么更容易拉开”的那整套机制，直接照搬到拟人化 Mascot IP：

- `Style Universe Index`
- `Dynamic Style Selector`
- `Selection Policy`
- `Family Recipe`
- `Progressive Disclosure`
- `Board Manifest / Slot Binding`
- `One-Shot 25 Grid Generation`

## 这版和人物 Skill 一样的地方

### 1. 先读 INDEX，再选 25 个 Style ID
不是一上来把 150 条风格全塞进 Prompt，而是：

1. 读取 `styles/INDEX.md`
2. 先选 25 个 canonical style IDs
3. 只读取对应 family files
4. 提取完整 recipe
5. 再编译 25 格 prompt

### 2. 选风格的 Mix 一模一样
- 10 Core Fit
- 7 Adjacent
- 5 Exploratory
- 3 Wildcard

### 3. Style 是真正的 Recipe，不是一个名字
每个 style 都有完整定义，例如：
- visual thesis
- line / edge
- palette logic
- shading
- material / texture
- dimensionality
- finish
- transformation strength
- anti-collapse

### 4. Board Manifest 机制一模一样
先冻结 `board_id + slot 01–25 + style_recipe_snapshot`，再一次生图。生图后不允许重新排序。

## 和人物 Skill 不一样、但已做 Mascot 化适配的地方

- 把 `Human / Adult / Personal IP` 改成 `Mascot / Sidekick / Account Mascot Universe`
- style 保留“应用方式”，但字段改成适合 mascot：
  - `sidekick_fit`
  - `character_rendering_mode`
  - `body_topology_window`
  - `costume_transformation_strength`
- 强调：
  - 25 格是 **25 个独立 mascot 候选**，不是同一个人跨 25 种风格
  - style 只负责 **怎么画**，不负责决定人格
  - personality / pose / carrier 仍然是上游冻结变量

## 你这版重点想看的

这版最重要的不是最终内容质量，而是看：

> **把人物 Skill 那套 Style 应用系统原封不动地迁到 Mascot 后，25 宫格的画风拉开程度会不会明显变好。**
