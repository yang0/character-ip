# Architecture V11 — Human Style Application Ported to Mascot

```text
User / Account Context
        ↓
Semantic Understanding
        ↓
Carrier / Personality / Pose Freeze
        ↓
Style Universe Index (S001–S150)
        ↓
Dynamic Style Selector
10 Core + 7 Adjacent + 5 Exploratory + 3 Wildcard
        ↓
Progressive Disclosure
read INDEX → choose style IDs → load family recipes only
        ↓
Board Manifest / Slot Binding
freeze slot 01–25 + style recipe snapshot
        ↓
One-Shot 25-Grid Generation
        ↓
User Selection → Refinement
```

## Porting Principle

这版只做一件事：

> **把人物 IP Skill 的风格应用方式完整照搬到 Mascot Skill。**

也就是说：

- 用同样的 Style Universe 结构
- 用同样的风格选择权重
- 用同样的 Family Recipe 读取方式
- 用同样的 Frozen Board Manifest
- 用同样的 single-shot 25-grid 流程

而不是继续用旧版 Mascot 的“style tag + render code”轻量路线。
