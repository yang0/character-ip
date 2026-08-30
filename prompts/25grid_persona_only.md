# Board / Slot Binding — P0
A frozen Board Manifest has already assigned designs to slots 01–25. Use it exactly.
Visible numbers are row-major and immutable. Never reorder or regenerate slot mapping.
{{board_slot_manifest}}

# Prompt Template — PERSONA_ONLY (v11)

Use case: stylized-character-ip
Asset type: dynamic 25-style persona exploration board
Canvas: strict 1:1 square

Identity premise:
No reliable real-person visual identity is available.
Build one coherent human IP identity from the provided account/persona/aesthetic context.
Do not claim real-person resemblance.

Character:
- every slot follows its frozen proportion_profile from the Board Manifest
- same base persona across all 25 cells
- stylized adult social character
- target 4.2–5.2 heads
- normal allowed 3.8–5.4 heads, hard max 5.6
- avoid realistic model proportions
- no handheld props
- compact styles must still read as adult

Personality-to-expression:
Each tile receives its own matched personality and visual expression package:
- expression family
- facial expression cue
- gaze cue
- head pose cue
- body pose cue
- empty-hand gesture

Expression diversity:
- >=9 expression families
- same expression family <=5 tiles
- obvious smiles <=5 tiles
- do not default to friendly smiling faces

Pose diversity:
- >=8 pose families
- both hands in pockets <=3 tiles
- all pocket poses <=8 tiles

Outfit diversity:
- clothing follows style + persona, not one repeated canonical outfit
- use >=8 outfit silhouette families across the board

Grid:
- one single 5x5 image
- 25 equal cells
- full body in every cell
- semi-transparent 01–25
- no style names or explanatory text

Style instructions:
Insert 25 dynamically selected Style Recipes.
Each tile must transform the character itself, not only the background.

Output:
One-shot complete 25-grid.
