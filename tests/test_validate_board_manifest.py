from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_board_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_board_manifest", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def fresh_manifest() -> dict:
    slots = {}
    for index in range(1, 26):
        slot_id = f"{index:02d}"
        row, col = divmod(index - 1, 5)
        slots[slot_id] = {
            "grid_slot": slot_id,
            "row": row + 1,
            "col": col + 1,
            "style_id": f"S{index:03d}",
            "carrier_species": f"species-{index}",
            "carrier_family": f"family-{index}",
            "carrier_archetype": f"archetype-{index}",
            "carrier_rationale": f"rationale-{index}",
        }
    return {
        "design_context": "FRESH_DESIGN",
        "run_id": "run-a",
        "history_access": "none",
        "board_id": "B001",
        "output_root": "output/runs/run-a/",
        "role_category": "MASCOT",
        "slots": slots,
    }


class ValidateBoardManifestTests(unittest.TestCase):
    def test_fresh_manifest_passes_without_history(self) -> None:
        manifest = fresh_manifest()
        path = Path("state/runs/run-a/board-B001-manifest.yaml")
        self.assertEqual(VALIDATOR.validate(manifest, path), [])

    def test_duplicate_family_fails(self) -> None:
        manifest = fresh_manifest()
        manifest["slots"]["02"]["carrier_family"] = "family-1"
        errors = VALIDATOR.validate(manifest, Path("state/runs/run-a/board-B001-manifest.yaml"))
        self.assertTrue(any("carrier_family" in error for error in errors))

    def test_fresh_history_access_fails(self) -> None:
        manifest = fresh_manifest()
        manifest["history_access"] = {"mode": "explicit_single_board", "board_id": "B006"}
        errors = VALIDATOR.validate(manifest, Path("state/runs/run-a/board-B001-manifest.yaml"))
        self.assertTrue(any("history_access" in error for error in errors))

    def test_continuation_requires_eighty_percent_new_values(self) -> None:
        reference = fresh_manifest()
        continuation = fresh_manifest()
        continuation.update({
            "design_context": "CONTINUATION",
            "run_id": "run-b",
            "history_access": {"mode": "explicit_single_board", "board_id": "B001"},
            "board_id": "B002",
            "output_root": "output/runs/run-b/",
        })
        errors = VALIDATOR.validate(continuation, Path("state/runs/run-b/board-B002-manifest.yaml"), reference)
        self.assertTrue(any("80% new style_id" in error for error in errors))

    def test_continuation_passes_with_eighty_percent_new_values(self) -> None:
        reference = fresh_manifest()
        continuation = fresh_manifest()
        continuation.update({
            "design_context": "CONTINUATION",
            "run_id": "run-b",
            "history_access": {"mode": "explicit_single_board", "board_id": "B001"},
            "board_id": "B002",
            "output_root": "output/runs/run-b/",
        })
        for index in range(1, 21):
            slot = continuation["slots"][f"{index:02d}"]
            slot["style_id"] = f"NEW-{index}"
            slot["carrier_family"] = f"new-family-{index}"
        self.assertEqual(
            VALIDATOR.validate(continuation, Path("state/runs/run-b/board-B002-manifest.yaml"), reference),
            [],
        )
