# Prompt Template — MASCOT VISUAL BOARD (V13)

Use case: stylized-mascot-ip
Asset type: dynamic 25-style mascot exploration board
Canvas: strict 1:1 square

Role category: `MASCOT` only. Do not use this prompt until the Role Category Gate has resolved to `MASCOT`.

## Board Manifest / Number Binding — P0
Before rendering, a frozen Board Manifest already exists.
Use the supplied slot table exactly as given. Do NOT reorder styles or candidates.
For a fresh design, the supplied Manifest is the only design history: do not infer or reuse any prior Board.

Visible numbering is immutable and row-major:
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

Insert the frozen 25-slot manifest here in exact 01→25 order:
{{board_slot_manifest}}

## Mascot Contract
Each tile is a separate mascot candidate, not a style variant of another tile.
Every tile must preserve its frozen:
- carrier / archetype
- carrier_species / carrier_family / carrier_rationale
- personality
- expression family
- pose family
- silhouette family
- hooks
- palette logic
- style recipe snapshot

## Grid
- one single 5x5 image-generation pass
- 25 equal cells
- one complete full-body mascot per cell
- semi-transparent numbers 01–25
- no style names
- no personality labels
- no extra text

## Style Diversity
Insert the 25 dynamically selected Style Recipes here.
Every style must transform the mascot itself, not merely the background.
Vary line system, facial abstraction, body simplification, silhouette treatment, material, palette, shading, graphic treatment and dimensionality.

## Output
Generate the complete 25-grid in ONE image-generation pass.
