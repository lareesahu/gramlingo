"""Build the browser curriculum JSON from the canonical CSV files and aviation-missions.json."""

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


def read_json(name: str) -> list[dict[str, object]]:
    with (CONTENT / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def localized(row: dict[str, str], stem: str) -> dict[str, str]:
    return {lang: row.get(f"{stem}_{lang}", "") for lang in LANGUAGES}


def build() -> dict[str, object]:
    module_rows = [row for row in read_csv("modules.csv") if row["status"] == "active"]
    phase_rows = [row for row in read_csv("phases.csv") if row["status"] == "active"]
    question_rows = [row for row in read_csv("questions.csv") if True]

    modules = []
    module_ids: set[str] = set()
    for row in sorted(module_rows, key=lambda item: int(item["sort_order"])):
        module_id = row["module_id"]
        if module_id in module_ids:
            raise ValueError(f"Duplicate module_id: {module_id}")
        module_ids.add(module_id)
        modules.append({
            "id": module_id,
            "name": localized(row, "name"),
            "desc": localized(row, "description"),
            "gramlin": row["gramlin_pose"],
            "icon": row["icon"],
            "sort": int(row["sort_order"]),
        })

    phases_by_id: dict[str, dict[str, object]] = {}
    phase_ids: set[str] = set()
    phase_lock_order: dict[str, list[str]] = {module_id: [] for module_id in module_ids}
    for row in sorted(phase_rows, key=lambda item: int(item["sort_order"])):
        phase_id = row["phase_id"]
        module_id = row["module_id"]
        if module_id not in module_ids:
            raise ValueError(f"Phase {phase_id} references unknown module {module_id}")
        if phase_id in phases_by_id:
            raise ValueError(f"Duplicate phase_id: {phase_id}")
        phases_by_id[phase_id] = {
            "module": module_id, "id": phase_id,
            "name": localized(row, "name"), "s": localized(row, "subtitle"),
            "d": localized(row, "description"), "sort": int(row["sort_order"]), "q": [],
        }
        phase_ids.add(phase_id)
        phase_lock_order[module_id].append(phase_id)

    question_ids: set[str] = set()
    for row in sorted(question_rows, key=lambda item: (item["module_id"], item["phase_id"], int(item["q_num"]))):
        question_id = row["question_id"]
        phase_id = row["phase_id"]
        module_id = row["module_id"]
        phase = phases_by_id.get(f"{module_id}_{phase_id}") or phases_by_id.get(phase_id)
        if phase is None:
            raise ValueError(f"Question {question_id} references unknown phase {phase_id}")
        if phase["module"] != module_id:
            raise ValueError(f"Question {question_id} has the wrong module_id")
        if question_id in question_ids:
            raise ValueError(f"Duplicate question_id: {question_id}")
        question_ids.add(question_id)

        option_letters = [letter for letter in "abcd" if row.get(f"option_{letter}_en", "").strip()]
        options = {lang: [row.get(f"option_{letter}_{lang}", "") for letter in option_letters] for lang in LANGUAGES}
        correct_letters = [value.strip().lower() for value in row["correct_option"].split("|")]
        invalid = [letter for letter in correct_letters if letter not in option_letters]
        if invalid:
            raise ValueError(f"Question {question_id} has invalid correct option: {invalid}")
        answers = [row[f"option_{letter}_en"] for letter in correct_letters]

        explanations: dict[str, list[str]] = {}
        for lang in LANGUAGES:
            fallback = row.get(f"fallback_tip_{lang}", "").strip()
            explanations[lang] = [row.get(f"explanation_{letter}_{lang}", "").strip() or fallback for letter in option_letters]

        phase["q"].append({
            "id": question_id, "type": "multiple_choice_single",
            "q": localized(row, "prompt"), "a": answers[0] if len(answers) == 1 else answers,
            "o": options, "t": localized(row, "fallback_tip"), "ex": explanations,
        })

    # Aviation cloze missions
    aviation_missions = read_json("aviation-missions.json")
    for raw in aviation_missions:
        mid = raw["id"]
        if raw.get("reviewStatus") != "approved":
            raise ValueError(f"Mission {mid}: reviewStatus must be approved")
        raw_type = raw.get("type")
        if raw_type != "cloze":
            continue
        if mid in question_ids:
            raise ValueError(f"Duplicate question_id: {mid}")
        question_ids.add(mid)

        blanks_out = []
        for b in raw["blanks"]:
            if b["word"] not in b["options"]:
                raise ValueError(f"Mission {mid}: answer {b['word']!r} is missing from its options")
            blanks_out.append({"position": b["position"], "word": b["word"], "options": b["options"]})

        phase_id = raw["phaseId"]
        phase = phases_by_id.get(phase_id)
        if phase is None:
            raise ValueError(f"Mission {mid}: unknown phase {phase_id}")

        full = raw["fullSentence"]
        prompt = raw["prompt"]
        scenario = raw["scenario"]
        hint = raw["hint"]

        for locale in ("en", "zh", "es"):
            placeholder_count = prompt[locale].count("_____")
            if placeholder_count != len(blanks_out):
                raise ValueError(
                    f"Mission {mid}: {locale} prompt has {placeholder_count} blanks, expected {len(blanks_out)}"
                )

        phase["q"].append({
            "id": mid, "type": "cloze",
            "q": prompt["en"], "qZh": prompt["zh"], "qEs": prompt["es"],
            "t": hint["en"], "tZh": hint["zh"], "tEs": hint["es"],
            "scenario": scenario["en"], "scenarioZh": scenario["zh"], "scenarioEs": scenario["es"],
            "blanks": blanks_out,
            "fullSentence": full["en"], "fullSentenceZh": full["zh"], "fullSentenceEs": full["es"],
        })

    phases = sorted(phases_by_id.values(), key=lambda phase: (
        next(module["sort"] for module in modules if module["id"] == phase["module"]),
        phase["sort"],
    ))
    return {"title": "GramLingo", "modules": modules, "phases": phases, "phaseLockOrder": phase_lock_order}


if __name__ == "__main__":
    data = build()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    for destination in (ROOT / "data" / "game-data.json", ROOT / "public" / "data" / "game-data.json"):
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    question_count = sum(len(phase["q"]) for phase in data["phases"])
    playable_count = sum(bool(phase["q"]) for phase in data["phases"])
    print(f"Built {len(data['modules'])} modules, {len(data['phases'])} phases, {question_count} questions, {playable_count} playable phases.")
