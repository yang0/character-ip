# Module 08 — Dynamic Style Selector v11

## Input
- User persona
- personal aesthetic
- content role
- visual identity availability
- recent board history
- `styles/INDEX.md`

## Output
25 canonical styles from `S001–S150`.

## Mix
- 10 Core Fit
- 7 Adjacent
- 5 Exploratory
- 3 Wildcard

## Scoring
`42% User Fit + 23% Visual Novelty + 15% Cross-Family Diversity + 10% Social/Meme Potential + 5% Character Transformation + 5% Surprise`

## Character-First Constraint
风格不能只靠背景成立。

优先选择：
- `character_transformation_strength >= 3`
- 能明显改变头部画法 / 身体比例 / 线条 / 材质 / 服装轮廓 / 表情语言的 style

每轮至少：
- 20 / 25 styles 的 character transform >=3
- 8 / 25 >=4
- background-primary styles <=5

## Outfit Diversity Constraint
源图服装不属于 Identity Lock。

选 25 格时要确保 style recipes 能产生至少 8 种 outfit silhouette families。

## Diversity Constraints
- at least 9 families
- max 4 per family
- max 6 manga/webtoon-neighbor styles
- >=3 hand-made / physical-media
- >=2 meme/doodle
- >=2 editorial/designer
- >=2 experimental
- >=1 stylized 3D or digital-native

## Freshness
If previous board exists:
- normal next board: >=60% new styles
- “再来一批”: >=80% new styles

## Progressive Disclosure
1. read INDEX only
2. choose style IDs
3. identify required family files
4. load only those recipes
5. compile selected 25

## Slot Mapping
安排 01–25 时避免相邻视觉克隆：
- 同 family 不连排
- 同 medium 不连排
- 同 body proportion 不连排
- 同 expression family 尽量不相邻


## Board Manifest Handoff — P0

Style Selector 的输出不能直接临时塞进生图 Prompt 后丢弃。

选择完 25 个 Style 后必须：
1. 分配固定 `grid_slot 01–25`
2. 写入 `board_id` 对应的 Frozen Board Manifest
3. 为每个 slot 保存 Style Recipe Snapshot，而不仅是 style_id
4. 再把同一个 Manifest 按 01→25 顺序交给 One-Shot Grid Generator

Board 一旦进入渲染阶段，slot 映射不可重新排序。
