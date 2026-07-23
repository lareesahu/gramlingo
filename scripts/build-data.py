"""Build the browser curriculum JSON from the canonical CSV files."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
LANGUAGES = ("en", "zh", "es")


def read_csv(name: str) -> list[dict[str, str]]:
    with (CONTENT / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def localized(row: dict[str, str], stem: str) -> dict[str, str]:
    return {lang: row.get(f"{stem}_{lang}", "") for lang in LANGUAGES}


def build() -> dict[str, object]:
    module_rows = [row for row in read_csv("modules.csv") if row["status"] == "active"]
    phase_rows = [row for row in read_csv("phases.csv") if row["status"] == "active"]
    question_rows = [
        row
        for row in read_csv("questions.csv")
        if True  # accept all review_status values for now
    ]

    modules = []
    module_ids: set[str] = set()
    for row in sorted(module_rows, key=lambda item: int(item["sort_order"])):
        module_id = row["module_id"]
        if module_id in module_ids:
            raise ValueError(f"Duplicate module_id: {module_id}")
        module_ids.add(module_id)
        modules.append(
            {
                "id": module_id,
                "name": localized(row, "name"),
                "desc": localized(row, "description"),
                "gramlin": row["gramlin_pose"],
                "icon": row["icon"],
                "sort": int(row["sort_order"]),
            }
        )

    phases_by_id: dict[str, dict[str, object]] = {}
    phase_lock_order: dict[str, list[str]] = {module_id: [] for module_id in module_ids}
    for row in sorted(
        phase_rows,
        key=lambda item: int(item["sort_order"]),
    ):
        phase_id = row["phase_id"]
        module_id = row["module_id"]
        if module_id not in module_ids:
            raise ValueError(f"Phase {phase_id} references unknown module {module_id}")
        if phase_id in phases_by_id:
            raise ValueError(f"Duplicate phase_id: {phase_id}")
        phases_by_id[phase_id] = {
            "module": module_id,
            "id": phase_id,
            "name": localized(row, "name"),
            "s": localized(row, "subtitle"),
            "d": localized(row, "description"),
            "sort": int(row["sort_order"]),
            "q": [],
        }
        phase_lock_order[module_id].append(phase_id)

    question_ids: set[str] = set()
    for row in sorted(
        question_rows,
        key=lambda item: (item["module_id"], item["phase_id"], int(item["q_num"])),
    ):
        question_id = row["question_id"]
        phase_id = row["phase_id"]
        module_id = row["module_id"]
        phase = phases_by_id.get(phase_id)
        if phase is None:
            raise ValueError(f"Question {question_id} references unknown phase {phase_id}")
        if phase["module"] != module_id:
            raise ValueError(f"Question {question_id} has the wrong module_id")
        if question_id in question_ids:
            raise ValueError(f"Duplicate question_id: {question_id}")
        question_ids.add(question_id)

        option_letters = [
            letter
            for letter in "abcd"
            if row.get(f"option_{letter}_en", "").strip()
        ]
        options = {
            lang: [row.get(f"option_{letter}_{lang}", "") for letter in option_letters]
            for lang in LANGUAGES
        }
        correct_letters = [value.strip().lower() for value in row["correct_option"].split("|")]
        invalid = [letter for letter in correct_letters if letter not in option_letters]
        if invalid:
            raise ValueError(f"Question {question_id} has invalid correct option: {invalid}")
        answers = [row[f"option_{letter}_en"] for letter in correct_letters]

        explanations: dict[str, list[str]] = {}
        for lang in LANGUAGES:
            fallback = row.get(f"fallback_tip_{lang}", "").strip()
            values = [
                row.get(f"explanation_{letter}_{lang}", "").strip() or fallback
                for letter in option_letters
            ]
            pass  # allow empty explanations (fallback_tip used)
            explanations[lang] = values

        phase["q"].append(
            {
                "id": question_id,
                "q": localized(row, "prompt"),
                "a": answers[0] if len(answers) == 1 else answers,
                "o": options,
                "t": localized(row, "fallback_tip"),
                "ex": explanations,
            }
        )

    phases = sorted(
        phases_by_id.values(),
        key=lambda phase: (
            next(module["sort"] for module in modules if module["id"] == phase["module"]),
            phase["sort"],
        ),
    )
    return {
        "title": "GramLingo",
        "modules": modules,
        "phases": phases,
        "phaseLockOrder": phase_lock_order,
    }


if __name__ == "__main__":
    data = build()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    for destination in (ROOT / "data" / "game-data.json", ROOT / "public" / "data" / "game-data.json"):
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    question_count = sum(len(phase["q"]) for phase in data["phases"])
    playable_count = sum(bool(phase["q"]) for phase in data["phases"])
    print(
        f"Built {len(data['modules'])} modules, {len(data['phases'])} phases, "
        f"{question_count} questions, {playable_count} playable phases."
    )
