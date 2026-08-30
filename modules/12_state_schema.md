# Module 12 — State Schema v13

```yaml
design_context: FRESH_DESIGN | CONTINUATION
run_id: "20260830T201000-yang02010"
history_access: none | {mode: explicit_single_board, board_id: "B006"}
manifest_path: "state/runs/<run_id>/board-B001-manifest.yaml"
output_root: "output/runs/<run_id>/"

project:
  character_id: "C001"
  active_board_id: "B002"
  next_board_ordinal: 3

role_category: HUMAN | MASCOT
role_category_source: explicit_user_request | clear_human_photo | named_real_person
route: VISUAL_TRAIT_REFERENCE | PERSONA_ONLY | HYBRID_IDENTITY

identity:
  real_reference_available: true|false
  original_real_reference: reference_handle_or_null
  visual_trait_authority: original_real_reference
  literal_resemblance_is_primary_goal: false
  photorealism_is_primary_goal: false
  implicit_trait_amplification: true
  textual_face_dna_primary: false
  age_impression_locked: true|false
  reference_expression_frozen: false
  reference_clothing_frozen: false
  base_vibe: string

boards:
  - board_id: "B001"
    board_ordinal: 1
    generation_id: string
    created_at: string_or_null
    active_board: false
    board_image_ref: image_reference_or_null
    canvas:
      ratio: "1:1"
      grid: "5x5"
    slot_order: ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
    slots:
      "01":
        grid_slot: "01"
        visible_number: "01"
        row: 1
        col: 1
        tile_bbox_normalized: {x0: 0.0, y0: 0.0, x1: 0.2, y1: 0.2}
        carrier_species: string_or_null  # required for MASCOT
        carrier_family: string_or_null   # required for MASCOT; unique within Board
        carrier_archetype: string_or_null
        carrier_rationale: string_or_null
        style_id: "S087"
        family_id: "Fxx"
        selection_bucket: core|adjacent|exploratory|wildcard
        style_name: string
        style_recipe_snapshot: object_or_text
        matched_personality: string
        expression_family: "E01"
        expression_cue: string
        gaze_cue: string
        head_pose_cue: string
        body_pose_cue: string
        empty_hand_gesture: string
        proportion_heads: float
        proportion_profile:
          profile_id: "PP_B001_01"
          body_mode: social_ip
          target_head_count: 4.8
          allowed_variance: 0.3
          head_size_bias: slightly_large
          limb_length_bias: shortened
          torso_leg_balance: compact_stylized
          silhouette_compactness: medium_high
          realistic_anatomy_normalization_allowed: false
        outfit_logic: string
        actual_tile_visual_ref: image_reference_or_null
        render_alignment_score: null
      "02":
        grid_slot: "02"
        visible_number: "02"
        row: 1
        col: 2
        tile_bbox_normalized: {x0: 0.2, y0: 0.0, x1: 0.4, y1: 0.2}
        style_id: "S131"
        style_recipe_snapshot: object_or_text
        actual_tile_visual_ref: image_reference_or_null
        # ... same slot fields

recent_style_history:
  - style_id: "S..."
    board_id: "B..."

quality:
  feature_embodiment_score: null
  template_face_suppression: null
  stylized_identity_read: null
  age_impression_stability: null
  style_coherence: null
  photoreal_leakage: null
  numbering_alignment_pass: null

selection_context:
  current_selected_character_id: null
  current_selected_board_id: null
  current_selected_grid_slot: null

refinements:
  - refinement_id: "R001"
    source:
      character_id: "C001"
      board_id: "B002"
      grid_slot: "02"
      style_id: "S131"
    parent_refinement_id: null
    inherited_proportion_profile_id: "PP_B002_02"
    proportion_profile_changed_by_user: false
    output_image_ref: null
```

## P0 Invariants

1. `visible_number == grid_slot`
2. `(board_id, grid_slot)` 在项目内唯一
3. Board 渲染开始后，slot → style/personality snapshot 不得重排
4. 用户选号时禁止重新运行 Style Selector
5. `01–25` 是当前 Board 的 slot，不是固定 style_id
6. 多 Board 场景必须先解析 board，再解析 slot
7. 用户选中的 Look 绑定 actual rendered tile visual
8. 参考角色角色 Trait 仍绑定 original real reference，而不是 generated tile face
9. 每个 slot 必须有 frozen proportion_profile
10. 单张 refinement 默认必须继承 source slot 的 proportion_profile
11. Original real photo body anatomy 永远不是 IP 身体比例权威
12. FRESH_DESIGN 的 `history_access == none`，且不读取旧 Board。
13. MASCOT Board 的 carrier species 与 carrier family 均在 25 格内唯一。
14. CONTINUATION 只能引用用户点名的单一 Board；新 Board 相对它至少 80% style IDs 与 carrier families 为新增。
