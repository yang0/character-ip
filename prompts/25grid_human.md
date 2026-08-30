# Prompt Template — HUMAN CHARACTER BOARD (V13)

Use case: stylized-character-ip
Asset type: dynamic 25-style human character exploration board
Canvas: strict 1:1 square

Role category: `HUMAN` only. Use only after the Role Category Gate resolves to `HUMAN`.

Design context: use only the supplied frozen run-scoped Manifest. For `FRESH_DESIGN`, do not infer, retrieve, or reuse any prior Board, image, style history, or output.

## Board Manifest / Number Binding — P0

Use the frozen 25-slot manifest exactly in `01 → 25` order. Do not reorder styles or candidates.

Visible numbers are immutable and row-major:

```text
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

## Human Contract

- Every tile is a full-body human character IP, never an animal or mascot carrier.
- Preserve the frozen personality, expression, pose, silhouette, outfit and style recipe.
- When a real reference photo exists, use it only for visual traits and age impression; fully redraw the head and body in the selected style.
- Use compact square social-IP anatomy; no photo-head mismatch, no generic template face, no realistic fashion-model anatomy.

## Output

- one single 5×5 image-generation pass
- 25 equal cells, one complete full-body human character per cell
- semi-transparent numbers 01–25; no style names, personality labels or extra text
- style changes must transform the character, not only the background
