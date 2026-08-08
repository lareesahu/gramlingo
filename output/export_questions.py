#!/usr/bin/env python
"""Export all GramLingo questions (MC + cloze) with answers, options, tips, and
explanations (en/zh/es) to a single XLSX workbook."""
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

SRC = r"C:/Users/hunin/projects/gramlingo/data/game-data.json"
OUT = r"C:/Users/hunin/projects/gramlingo/output/question-export-20260806.xlsx"

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)

modules = {m["id"]: m for m in data["modules"]}

wb = Workbook()
ws = wb.active
ws.title = "All Questions"

headers = [
    "Module", "Phase", "Phase ID", "Q#", "Question ID", "Type",
    "Question EN", "Question ZH", "Question ES",
    "Options EN", "Options ZH", "Options ES",
    "Correct Answer", "Tip EN", "Tip ZH", "Tip ES",
    "Explanation EN", "Explanation ZH", "Explanation ES",
    "Cloze: Scenario EN", "Cloze: Blanks (word@pos)", "Cloze: Full Sentence EN",
]
ws.append(headers)

hdr_fill = PatternFill(start_color="FF1F2937", end_color="FF1F2937", fill_type="solid")
hdr_font = Font(color="FFFFFFFF", bold=True, size=11)
for c, _ in enumerate(headers, start=1):
    cell = ws.cell(row=1, column=c)
    cell.fill = hdr_fill
    cell.font = hdr_font
    cell.alignment = Alignment(vertical="center")

def join_opts(o):
    if isinstance(o, dict):
        return " | ".join(o.get("en", []) or [])
    if isinstance(o, list):
        return " | ".join(str(x) for x in o)
    return str(o) if o else ""

def opts_lang(o, lang):
    if isinstance(o, dict):
        return " | ".join(o.get(lang, []) or [])
    return ""

def fmt_ans(a):
    if isinstance(a, list):
        return " | ".join(str(x) for x in a)
    return str(a) if a is not None else ""

def fmt_ex(ex):
    if isinstance(ex, list):
        return "\n".join(f"{i+1}. {x}" for i, x in enumerate(ex))
    return ""

row = 2
for p in data["phases"]:
    mod_id = p.get("module", "")
    mod_name = modules.get(mod_id, {}).get("name", {}).get("en", mod_id)
    phase_name = p.get("name", {}).get("en", p.get("id", ""))
    qs = p.get("q", [])
    for i, q in enumerate(qs, start=1):
        qtype = q.get("type", "")
        qtext = q.get("q", "")
        if isinstance(qtext, dict):
            q_en = qtext.get("en", "")
            q_zh = qtext.get("zh", "")
            q_es = qtext.get("es", "")
        else:
            q_en = qtext or ""
            q_zh = q.get("qZh", q_en) or q_en
            q_es = q.get("qEs", q_en) or q_en

        o_en = join_opts(q.get("o"))
        o_zh = opts_lang(q.get("o"), "zh")
        o_es = opts_lang(q.get("o"), "es")
        ans = fmt_ans(q.get("a"))
        t = q.get("t") or {}
        t_en = t.get("en", "") if isinstance(t, dict) else str(t or "")
        t_zh = t.get("zh", "") if isinstance(t, dict) else (q.get("tZh", "") or "")
        t_es = t.get("es", "") if isinstance(t, dict) else (q.get("tEs", "") or "")
        ex = q.get("ex") or {}
        ex_en = fmt_ex(ex.get("en")) if isinstance(ex, dict) else fmt_ex(ex)
        ex_zh = fmt_ex(ex.get("zh")) if isinstance(ex, dict) else ""
        ex_es = fmt_ex(ex.get("es")) if isinstance(ex, dict) else ""

        scenario = q.get("scenario", "")
        if isinstance(scenario, dict):
            scenario = scenario.get("en", "")
        blanks = q.get("blanks")
        blanks_str = ""
        if isinstance(blanks, list):
            blanks_str = " | ".join(f"{b.get('word','')}@{b.get('position','')}" for b in blanks)
        full = q.get("fullSentence", "")
        if isinstance(full, dict):
            full = full.get("en", "")

        ws.append([
            mod_name, phase_name, p.get("id", ""), i, q.get("id", ""), qtype,
            q_en, q_zh, q_es,
            o_en, o_zh, o_es,
            ans, t_en, t_zh, t_es,
            ex_en, ex_zh, ex_es,
            scenario, blanks_str, full,
        ])
        row += 1

# Column widths (rough per-content)
widths = [14, 22, 18, 6, 20, 14, 40, 40, 40, 40, 40, 40, 22, 28, 28, 28, 55, 55, 55, 30, 30, 55]
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Freeze header + wrap text
ws.freeze_panes = "A2"
wrap = Alignment(wrap_text=True, vertical="top")
for r in range(2, row):
    for c in range(1, len(headers) + 1):
        ws.cell(row=r, column=c).alignment = wrap

wb.save(OUT)
print(f"Saved {OUT}")
print(f"Rows: {row - 1} questions")
