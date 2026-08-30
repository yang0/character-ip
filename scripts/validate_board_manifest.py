#!/usr/bin/env python3
"""Validate the v13 design-context and mascot-carrier board invariants."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


SLOT_IDS = [f"{index:02d}" for index in range(1, 26)]
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("manifest root must be a mapping")
    return data


def slot_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    slots = manifest.get("slots")
    if not isinstance(slots, dict):
        return {}
    return {str(key).zfill(2): value for key, value in slots.items() if isinstance(value, dict)}


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(manifest: dict[str, Any], manifest_path: Path, reference: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    context = manifest.get("design_context")
    run_id = manifest.get("run_id")
    access = manifest.get("history_access")
    board_id = manifest.get("board_id")

    if context not in {"FRESH_DESIGN", "CONTINUATION"}:
        errors.append("design_context must be FRESH_DESIGN or CONTINUATION")
    if not nonempty(run_id) or not RUN_ID_RE.fullmatch(run_id):
        errors.append("run_id must contain only letters, digits, underscores, and hyphens")

    normalized_path = manifest_path.as_posix()
    if context == "FRESH_DESIGN":
        if board_id != "B001":
            errors.append("FRESH_DESIGN must start at board_id B001")
        if access != "none":
            errors.append("FRESH_DESIGN must record history_access: none")
        if nonempty(run_id) and f"state/runs/{run_id}/" not in normalized_path:
            errors.append("FRESH_DESIGN manifest must live under state/runs/<run_id>/")
        output_root = manifest.get("output_root")
        if not nonempty(output_root) or f"output/runs/{run_id}/" not in output_root.replace("\\", "/"):
            errors.append("FRESH_DESIGN output_root must be output/runs/<run_id>/")
    elif context == "CONTINUATION":
        if not isinstance(access, dict) or access.get("mode") != "explicit_single_board" or not nonempty(access.get("board_id")):
            errors.append("CONTINUATION requires explicit_single_board history_access with board_id")
        if reference is None:
            errors.append("CONTINUATION validation requires --reference-manifest")

    slots = slot_map(manifest)
    if list(sorted(slots)) != SLOT_IDS:
        errors.append("slots must contain exactly 01 through 25")
        return errors

    for index, slot_id in enumerate(SLOT_IDS, start=1):
        slot = slots[slot_id]
        if str(slot.get("grid_slot", "")).zfill(2) != slot_id:
            errors.append(f"slot {slot_id} grid_slot must equal {slot_id}")
        expected_row, expected_col = divmod(index - 1, 5)
        if slot.get("row") != expected_row + 1 or slot.get("col") != expected_col + 1:
            errors.append(f"slot {slot_id} must be row {expected_row + 1}, col {expected_col + 1}")
        if not nonempty(slot.get("style_id")):
            errors.append(f"slot {slot_id} requires non-empty style_id")

    if manifest.get("role_category") == "MASCOT":
        fields = ("carrier_species", "carrier_family", "carrier_archetype", "carrier_rationale")
        for slot_id in SLOT_IDS:
            for field in fields:
                if not nonempty(slots[slot_id].get(field)):
                    errors.append(f"slot {slot_id} requires non-empty {field}")

        for field in ("carrier_species", "carrier_family"):
            values = [slots[slot_id].get(field, "").strip().casefold() for slot_id in SLOT_IDS if nonempty(slots[slot_id].get(field))]
            if len(values) != len(set(values)):
                errors.append(f"MASCOT {field} values must be unique within the Board")

    image_ref = manifest.get("board_image_ref")
    if context == "FRESH_DESIGN" and image_ref is not None:
        output_root = str(manifest.get("output_root", "")).replace("\\", "/")
        if not isinstance(image_ref, str) or not image_ref.replace("\\", "/").startswith(output_root):
            errors.append("FRESH_DESIGN board_image_ref must stay under output_root")

    if context == "CONTINUATION" and reference is not None:
        current_slots, reference_slots = slot_map(manifest), slot_map(reference)
        if list(sorted(reference_slots)) != SLOT_IDS:
            errors.append("reference manifest must contain exactly 01 through 25 slots")
        else:
            for field in ("style_id", "carrier_family"):
                current = {str(current_slots[slot_id].get(field, "")).casefold() for slot_id in SLOT_IDS}
                previous = {str(reference_slots[slot_id].get(field, "")).casefold() for slot_id in SLOT_IDS}
                new_ratio = len(current - previous) / 25
                if new_ratio < 0.80:
                    errors.append(f"CONTINUATION requires at least 80% new {field} values; got {new_ratio:.0%}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--reference-manifest", type=Path)
    args = parser.parse_args()
    try:
        manifest = load_manifest(args.manifest)
        reference = load_manifest(args.reference_manifest) if args.reference_manifest else None
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate(manifest, args.manifest.resolve(), reference)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: manifest satisfies v13 design-context and carrier-diversity invariants")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
