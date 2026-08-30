# Module 11 — Quality Gate v11

## Gate A — Square
- 25-grid = 1:1
- selected single = 1:1

## Gate B — Social-IP Proportion
- target: 4.2–5.2 heads
- normal range: 3.4–5.4
- hard max: 5.6
- 7–8 head fashion anatomy = FAIL
- style recipe cannot override this gate

## Gate B2 — Refinement Anti-Normalization — P0

单张 refinement 额外检查：
- 是否继承 source slot 的 frozen proportion_profile
- head 是否比候选明显缩小
- legs 是否明显被拉长
- silhouette 是否回退普通成人立绘
- 是否错误使用真人参考图身体比例

出现任何明显 anatomical normalization：FAIL。

## Gate C — Head / Body Style Harmony
真人模式：
- head must be fully stylized in target medium
- no photo-head mismatch
- no semi-real face on flat/chibi body

## Gate D — Trait Embodiment — P0
不要以“像不像照片”作为最高标准。

直接检查最终 IP 是否体现人物特征：
1. stylized_identity_read — 是否有这个人的整体味道
2. head_character_embodiment — 头脸趋势是否有来源感
3. hairstyle_embodiment — 发型结构/体积是否体现参考人物
4. age_impression_stability — 年龄感是否稳定
5. base_vibe_continuity — 基础气质是否仍可识别

如果其中至少 3 项明显缺失：FAIL。

## Gate E — Template Face Suppression — P0
以下属于 FAIL：
- 通用韩漫帅哥 / 美女脸覆盖人物特征
- 统一 V-line
- 统一锐眉
- 统一狭长上挑眼
- 统一萌系圆脸
- 换成任何 style-default ideal face

## Gate F — No Photoreal Rescue — P0
为了“更像”而增加：
- photographic skin
- portrait lighting
- realistic facial modeling

均为 FAIL。

## Gate G — Refinement Reference Roles
选中单格后：
- original photo = visual traits / age / vibe reference
- selected tile = style/personality authority

如果最终脸只是复制 selected tile 的模板脸：FAIL。
如果最终脸为了贴原图而变真人：FAIL。

## Gate H — Reference Expression Independence
- source smile must not dominate board
- obvious smiles <=5/25
- neutral/polite/mild-smile total <=6/25
- personality visible through face/gaze/pose

## Gate I — Pose Diversity
- >=8 pose families
- both hands in pockets <=3
- all pocket poses <=8

## Gate J — Clothing Independence
除非明确要求：
- source-like outfits <=3
- >=8 outfit silhouette families

## Gate K — Character-First Style Diversity
- style difference must affect character itself
- background-only differentiation does not count

## Gate L — Adult Age
- stylization must not childify adult reference

## Gate M — No Props
- no handheld canonical props

---

## Scoring Output
建议输出内部评分：

```yaml
feature_embodiment_score: 0..100
template_face_suppression: 0..100
stylized_identity_read: 0..100
age_impression_stability: 0..100
style_coherence: 0..100
photoreal_leakage: 0..100   # lower is better
proportion_continuity_score: 0..100
social_ip_anatomy_read: 0..100
```

推荐通过条件：
- feature_embodiment_score >= 65
- template_face_suppression >= 70
- stylized_identity_read >= 65
- age_impression_stability >= 75
- style_coherence >= 80
- photoreal_leakage <= 25
- proportion_continuity_score >= 85 for refinement
- social_ip_anatomy_read >= 80

---

## v10 Board Number Alignment Gate — P0

除人物质量外，每张 Board 还必须通过状态一致性检查：

- Board Manifest 已在渲染前冻结
- slots 恰好 25 个
- visible `01–25` 唯一且完整
- row-major 位置正确
- visible number == grid_slot
- slot 顺序与 Prompt 编译顺序一致
- board_image_ref 已回写 State
- 每个 slot 可通过 row/col/bbox 找到实际渲染 Tile

任何编号错位都属于 QA Failure，不能依赖用户自己猜。
