# Porting Notes

## 这版怎么“照搬”的

以下部分基本按 Human Character IP Skill 的结构直接迁移：

- `styles/INDEX.md`
- `styles/SELECTION_POLICY.md`
- `styles/families/*.md`
- `modules/08_style_selector.md`
- `modules/09_single_25grid_generation.md`
- `prompts/25grid_*`

## 只做了三类必要改造

1. 名称改造：Human → Mascot
2. 字段改造：identity / head / outfit 等真人专属字段 → mascot sidekick 可用字段
3. 任务改造：同一个人物跨 25 风格 → 25 个独立 mascot 候选

## 暂不追求完全“最终最优”

这版的目的，是先验证：

- 画风有没有明显被拉开
- `Style Recipe` 是否比旧版 `Render Code` 更有效
- Progressive Disclosure 是否更适合 25 宫格
