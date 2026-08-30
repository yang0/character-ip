# Prompt Template — VISUAL_TRAIT_REFERENCE / HYBRID (v11)

Use case: stylized-character-ip
Asset type: dynamic 25-style personal IP exploration board
Canvas: strict 1:1 square


## Board Manifest / Number Binding — P0
Before rendering, a frozen Board Manifest already exists.
Use the supplied slot table exactly as given. Do NOT reorder styles or candidates.

Visible numbering is immutable and row-major:
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

For each tile, the visible number MUST equal its `grid_slot`.
The design assigned to slot 02 must be drawn in row 1 column 2 and labeled 02, etc.
Do not use style IDs as visible numbers.
Do not renumber after rendering.

Insert the frozen 25-slot manifest here in exact 01→25 order:
{{board_slot_manifest}}

## Primary Reference Contract
Image A is the primary visual person-trait reference.

For EVERY ONE of the 25 tiles, directly re-reference Image A.
Do not derive later faces from another generated tile.
Do not treat any generated cartoon face as the new master.

The goal is NOT literal photoreal resemblance.
The goal is to embody the person's recognizable head character, hairstyle, age impression and overall vibe in each target style.

Do not first convert the person into a long Face-DNA list and then rebuild from prose.
Use Image A directly as visual evidence.

## Trait Embodiment
Visually carry over the person's own character through stylized translation:
- overall whole-head character
- face-shape tendency
- head/face proportion character
- hairstyle architecture / volume
- facial relationship character
- age impression
- gender expression
- overall vibe

You may selectively amplify visually distinctive traits when that improves IP recognizability, but keep the amplification faithful to the person and appropriate to the style.

Do NOT increase realism to improve resemblance.

## Style Translation
Redraw the entire head fully in each tile's assigned art style.
The head, hair, face, body, clothing and background must belong to one coherent style system.

No photographic skin.
No portrait lighting.
No real head on a stylized body.

## Template Face Suppression
Do not redesign the person into the target style's default attractive face.
Avoid generic anime/webtoon/editorial beautification.
Do not automatically impose a universal V-line jaw, sharp hero brows, narrow upturned eyes, tiny nose, cute round face, or other style-default template.

Stylize the person's traits; do not replace the person.

## Reference Expression
The expression visible in Image A is NOT frozen identity.
Do not copy the source smile or neutral face across the board.
Each tile receives its own personality-driven expression, gaze, head attitude and body posture.

## Reference Clothing
Clothing visible in Image A is NOT identity unless explicitly requested.
Do not repeat the source outfit across the board.

## Social-IP Anatomy — Hard Rule
All 25 are stylized adult social characters.
- recommended: 4.2–5.2 heads
- normal allowed range: 3.8–5.4 heads
- absolute maximum: 5.6 heads
- never default to realistic 7–8 head fashion-model anatomy
- compact/chibi proportions must still read as adult, not child

## Per-Slot Proportion Profile — P0
Each slot already has a frozen `proportion_profile` in the Board Manifest. Render the character according to that profile. Do not infer body anatomy from Image A. The real photo is a head/person-trait reference, not a body-proportion reference.

## Grid
- one single 5x5 image-generation pass
- 25 equal cells
- one complete full-body character per cell
- semi-transparent numbers 01–25
- no style names
- no personality labels
- no extra text

## Personality / Expression
For every tile independently apply:
- matched personality
- expression family
- facial expression cue
- gaze cue
- head pose cue
- body pose cue
- empty-hand gesture

Across the board:
- at least 9 expression families
- obvious smiles <=5
- neutral/polite/mild-smile faces <=6 total
- allow deadpan, skeptical, tired, awkward, playful, unimpressed, focused, curious, quietly amused, detached, serious, mischievous and smug variations

## Pose Diversity
- at least 8 pose families
- both hands in pockets <=3
- all pocket poses <=8
- hands remain empty

## Style Diversity
Insert the 25 dynamically selected Style Recipes here.
Every style must transform the character itself, not merely the background.
Vary head rendering, facial abstraction, line system, body proportion, silhouette, outfit silhouette, material, palette, shading, expression language and graphic treatment.

## Trait Embodiment Gate
Before accepting the result, evaluate each tile as a stylized IP, not as a portrait.
Ask:
- does the head still carry this person's visual character?
- are the person's own traits visible through the style?
- is age stable?
- did a generic style-template face replace the person?
- is the face fully integrated with the art style?

A good-looking generic character is a failure.
A photoreal rescue is also a failure.

## Output
Generate the complete 25-grid in ONE image-generation pass.
After rendering, bind the resulting board image back to `{{board_id}}`; selection must later use board_id + grid_slot and the actual rendered tile position.
