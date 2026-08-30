# Module 01 — Input Router v11

## Goal
判断当前任务走哪条人物 IP 路线。

## Route A — VISUAL_TRAIT_REFERENCE
触发：
- 有清晰真人照片 / 头像
- 头部可辨识

策略：
- 图片是人物视觉特征主来源
- 直接做 Visual Trait Translation
- 不把“高相似度真人脸”当目标
- 不先生成长篇 Face DNA 再重建

## Route B — PERSONA_ONLY
触发：
- 无清晰真人图
- 但有账号链接 / 文件 / Bio / 作品 / 内容资料

策略：
- 从内容人格、审美、职业角色构造人物 IP
- 不声称真人长相还原

## Route C — HYBRID_IDENTITY
触发：
- 真人图 + 文本/账号/文件

策略：
- 图片负责人物视觉特征、年龄感、头部味道
- 文本负责长期人格、内容角色、审美

## Route Priority
`explicit user instruction > usable real image > persona source > inferred context`

## No Forced Clarification
只要已有输入足够开始设计，就不要因为缺少非关键资料而打断流程。
