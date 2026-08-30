# Module 06 — Personality Engine

## Source
调用：
`registries/Personality.md`

## Formula
`70% User Base Persona + 20% Style Affinity + 10% Meme Contrast`

## Grid Rule
25 格不是 25 个不同人，而是同一个人的不同侧面。

## Match Priorities
1. 用户明确自述
2. 账号长期内容语气
3. 文件 / Bio
4. 图片整体 base vibe 作为弱信号
5. Style Affinity

## Reference Expression Rule
不要因为参考照正在微笑，就把 `smiling / friendly` 当成人格结论。

单张照片的瞬时表情只能作为弱信号。

## Output Contract
每个 grid slot 输出一个：

```yaml
matched_personality: string
base_vibe: string
meme_contrast: string
```

然后交给 `07_expression_pose_engine.md` 编译为可见表情与姿态。

## Avoid
- 随机抽人格
- 与用户完全相反的人设
- 极端负面 Mascot 化人格
- 性别刻板人格
- 25 格人格文案不同但视觉表现完全一样
