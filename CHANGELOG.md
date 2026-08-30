# Changelog

## V12

### Role Category Gate
- 用户明确说“人类 IP”或“吉祥物 / mascot”时，按当前请求执行。
- 未明确类别时，清晰人类照片或有名有姓的具体人物自动走 Human Character IP。
- 其他所有情况先问：“需要设计人类 IP 还是吉祥物 IP？”
- 类别未决时禁止冻结 Manifest、选择风格或生成图。
- Board、Prompt、QA 与 refinement 均绑定并继承 `role_category`。

## V11

### 目标
把你提供的 Human Character IP Skill 中“风格怎么被应用”的整套系统，按同构方式移植到 Mascot Skill。

### 核心变化
- 从 Human Skill 直接移植：
  - `modules/08_style_selector.md`
  - `styles/INDEX.md`
  - `styles/SELECTION_POLICY.md`
  - `styles/families/*.md`
  - `modules/09_single_25grid_generation.md`
  - `prompts/25grid_*`
- 保留 `10 Core + 7 Adjacent + 5 Exploratory + 3 Wildcard`
- 保留 Progressive Disclosure
- 保留 Board Manifest / Slot Binding
- 保留“先冻结，再一次生图”

### Mascot 化改造
- Human / Personal IP → Mascot / Sidekick
- identity fields → sidekick fields
- head translation → whole-character stylized translation
- source clothing → source costume
- 更强调：25 格是 25 个独立 mascot 候选，不是一个角色换 25 套画风

### 本版意图
这是一次 **风格应用机制实验版**。
重点验证：

> 当 Mascot Skill 使用与 Human Skill 几乎相同的 Style Selection + Style Recipe + Board Binding 机制时，画风差异是否会明显拉开。
