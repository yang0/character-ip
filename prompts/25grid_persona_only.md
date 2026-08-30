# Board / Slot Binding — P0
A frozen Board Manifest has already assigned mascot designs to slots 01–25. Use it exactly.
Visible numbers are row-major and immutable. Never reorder or regenerate slot mapping.
For every slot, consume its frozen `carrier_species`, `carrier_family`, `carrier_archetype`, and `carrier_rationale`; do not substitute a related animal or reuse another slot's carrier family.
{{board_slot_manifest}}

# Prompt Template — MASCOT (V13)

Use case: stylized-mascot-ip
Asset type: dynamic 25-style mascot exploration board

Role category: `MASCOT` only. Do not use this prompt until the Role Category Gate has resolved to `MASCOT`.
Canvas: strict 1:1 square

Mascot premise:
- 25 independent mascot candidates within one account/content universe
- every slot follows its frozen carrier, personality, pose, silhouette and style recipe
- full-body mascot in every cell
- no handheld props
- suitable as long-term article-illustration sidekick

Grid:
- one single 5x5 image
- 25 equal cells
- full body in every cell
- semi-transparent 01–25
- no style names or explanatory text

Style instructions:
Insert 25 dynamically selected Style Recipes.
Each tile must transform the mascot itself, not only the background.

Output:
One-shot complete 25-grid.
