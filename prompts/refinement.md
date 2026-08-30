# Prompt Template — Selected Style Refinement (v11 Proportion-Locked)

Use case: stylized-mascot-ip
Canvas: strict 1:1 square
Asset: one selected personal IP character

## Frozen Selection Identity — P0
- character_id: {{character_id}}
- board_id: {{board_id}}
- board_ordinal: {{board_ordinal}}
- grid_slot: {{grid_slot}}
- row: {{row}}
- col: {{col}}
- canonical_style_id: {{style_id}}

This selection was RETRIEVED from an existing frozen Board Manifest.
Do not rerun style selection.
Do not reinterpret `{{grid_slot}}` as a global style number.

## Frozen Slot State
- style_recipe_snapshot: {{style_recipe_snapshot}}
- matched_personality: {{matched_personality}}
- expression_family: {{expression_family}}
- expression_cue: {{expression_cue}}
- gaze_cue: {{gaze_cue}}
- head_pose_cue: {{head_pose_cue}}
- body_pose_cue: {{body_pose_cue}}
- empty_hand_gesture: {{empty_hand_gesture}}
- outfit_logic: {{outfit_logic}}

## Frozen Proportion Profile — P0
{{proportion_profile}}

This proportion profile is IMMUTABLE unless the user explicitly asks to change body proportion.
High resolution, refinement, maturity, elegance, fashion, editorial polish, or better rendering MUST NOT normalize the anatomy.

Refinement increases polish, not anatomical realism or normalization.

## Actual Selected Tile — P0
Image B / selected_tile_visual_ref is the ACTUAL rendered tile the user saw and chose from Board {{board_id}}, slot {{grid_slot}}.
Use it as the primary visual authority for the chosen LOOK: style feel, abstraction, pose, outfit silhouette, palette, material, expression energy, and social-IP compactness.

If Image B visually differs from the planned style recipe, follow Image B for the chosen look. The user selected what they saw.

## Original Person Reference — P0
If a real-person reference exists:
Image A = ORIGINAL REAL PERSON = visual trait authority.
Use Image A for the person's recognizable head traits, age impression, hairstyle source character and base vibe.

IMPORTANT: Image A is NOT a body-proportion reference.
Do not restore Image A's realistic mascot anatomy, limb length, torso-leg balance or head/body scale.
Do not increase photorealism.

Identity priority: Image A > generated tile face.
Chosen-look priority: Image B > frozen recipe literalism.
Body-proportion priority: Frozen proportion_profile > Image B compactness read > style defaults > Image A body anatomy (never).

## Trait Embodiment Goal
The goal is not literal photo likeness.
The stylized IP face should embody the person's recognizable head character, hairstyle architecture, age impression and overall vibe while fully belonging to the chosen style.

## Expression / Outfit
- do NOT restore source photo expression unless requested
- do NOT restore source photo clothing unless requested
- preserve the personality/expression/look that made the user choose this actual tile

## Square Social-IP Anatomy — HARD P0
A square canvas alone is NOT enough. The character anatomy itself must remain visibly IP-stylized.

Global envelope:
- target: 4.2–5.2 heads
- normal allowed: 3.8–5.4 heads
- hard maximum: 5.6 heads
- realistic 6.5–8 head fashion/model anatomy forbidden unless explicitly requested
- character occupies about 72–82% of square canvas height

Never:
- shrink the head toward realistic scale
- lengthen the legs into fashion-illustration anatomy
- restore normal mascot torso/limb proportions
- turn the selected IP into a normal character illustration merely placed on a square canvas

## Props
Hands empty. No handheld canonical props.

## Anti-Normalization Gate — P0
Before accepting the output, compare it with the frozen proportion profile and the selected tile.
FAIL if the final character is more anatomically realistic than the selected IP direction.
FAIL if the head is visibly smaller, the legs visibly longer, or the silhouette less compact.

## Final Check
- selected tile look fidelity
- trait embodiment
- template-face suppression
- age stability
- style coherence
- proportion continuity
- social-IP anatomy read
- low photoreal leakage
