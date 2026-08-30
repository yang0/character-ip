# Dynamic Style Selection Policy — v10

## 1. Goal
从 `S001–S150` 中，为当前用户动态挑选 25 个真正有差异、适配度高、人物本体变化明显的方向。

## 2. Selection Mix
默认：
- `10 Core Fit`
- `7 Adjacent Exploration`
- `5 Cross-Style Exploration`
- `3 Wildcards`

## 3. Score
建议：

`Score = 42% User Fit + 23% Novelty + 15% Cross-Family Diversity + 10% Social/Meme Potential + 5% Character Transformation + 5% Surprise`

## 4. Character-First Transformation
风格差异必须主要落在人物身上。

轻量索引中的：
- `Char Δ` = character_transformation_strength
- `Outfit Δ` = outfit_transformation_strength
- `Expr Cap` = expression_capacity

每轮要求：
- 至少 20/25 的 `Char Δ >= 3`
- 至少 8/25 的 `Char Δ >= 4`
- 仅靠背景成立的 style 最多 5 个

## 5. Hard Diversity Constraints
每轮 25 个：
- 至少覆盖 `9/12` 个 Families
- 单个 Family 最多 `4`
- manga / webtoon 邻近方向总计最多 `6`
- 至少 `3` 个 hand-drawn / physical-media
- 至少 `2` 个 meme / doodle
- 至少 `2` 个 editorial / designer
- 至少 `2` 个 experimental
- 至少 `1` 个 stylized 3D/material
- 至少 `1` 个 pixel/digital-native

## 6. Outfit Diversity
参考图服装默认不是 identity。

25 个 style recipes 组合后应能覆盖至少：
`8` 种 outfit silhouette families。

禁止 25 格都复用：
- 同一白外套
- 同一西装
- 同一卫衣
- 同一套源图服装

## 7. Expression Potential
Style Selector 不直接决定人格，但应避免 25 个都属于“只能做安全中性脸”的方向。

所选 styles 应覆盖：
- low / subtle expression capacity
- medium
- high / meme-capable

让 Expression Engine 有足够视觉空间。

## 8. Freshness
存在上一轮 Board 时：

### 普通重新探索
至少 `60%` canonical style IDs 不重复。

### 用户说“再来一批 / 换一批 / 新鲜点”
至少 `80%` canonical style IDs 不重复。

### Recently Used Penalty
最近使用过的 style：
`score *= 0.40`

## 9. User Preference Learning
用户选择某格后，可更新：
- liked_style_ids
- liked_family_ids
- liked_rendering_tags
- disliked_style_ids
- disliked_tags

下一轮：
- 不机械重复原 style
- 优先探索同一审美邻域的 sibling styles
- 同时保留 Wildcard

## 10. Grid Placement
安排 01–25 时，相邻格尽量避免：
- 同 family
- 同 line language
- 同 palette
- 同 proportion
- 同 medium
- 同 expression family
- 同 pose family

## 11. Progressive Disclosure
1. 读取 `INDEX.md`
2. 选出 25 个 canonical style IDs
3. 识别对应 family files
4. 只读取这些 family files
5. 提取 25 个完整 Recipe
6. Personality Engine 分配人格
7. Expression Engine 分配表情与姿态
8. 编译 one-shot 25-grid prompt
