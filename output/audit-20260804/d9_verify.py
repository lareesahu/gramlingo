#!/usr/bin/env python
"""D9 verification: for affected questions, deliberately pick the app-accepted-but-intended-wrong option
and confirm the app marks it CORRECT (card--correct), awarding a point that should not be awarded."""
import json, os, datetime
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
ROOT = r"C:/Users/hunin/projects/gramlingo"
OUT = os.path.join(ROOT, "output", "audit-20260804")
LEDGER = os.path.join(OUT, "ledger", "d9-ledger.jsonl")
EMAIL = "learner.e2e.20260803@gramlingo.test"
PASS = "Grm!E2E-2026-Learner"

with open(os.path.join(ROOT, "data", "game-data.json"), encoding="utf-8") as f:
    GAME = json.load(f)
PHASES = {p["id"]: p for p in GAME["phases"]}

def row(r):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

def log(m):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}", flush=True)

def intended_idx(q):
    a = q["a"]; answers = a if isinstance(a, list) else [a]
    return [j for j, o in enumerate(q["o"]["en"]) if o in answers]

def app_accepts(o, answers):
    return any(o == a or o in a or a in o for a in answers)

# (module, phase, qidx, extraOptionToTest)
TARGETS = [
    ("tenses", "tenses_present", 0, "go"),
    ("tenses", "tenses_present", 1, "having"),
    ("tenses", "tenses_past", 1, "cook"),
    ("conditionals", "conditionals_zero", 0, "will heat ... boils"),
    ("passive", "passive_recognition", 1, "broke"),
    ("passive", "passive_formation", 0, "deliver"),
    ("reported", "reported_embedded", 1, "where the"),
    ("modals", "modals_permission", 1, "can"),
    ("determiners", "determiners_articles", 0, "a"),
    ("verb_patterns", "verb_patterns_gerunds", 0, "read"),
    ("advanced", "advanced_substitution", 1, "did"),
    ("clauses", "clauses_gen", 0, "whom"),
]

def advance(page):
    try:
        page.get_by_role("button", name="Next →", exact=True).click(timeout=4000)
    except Exception:
        try:
            page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
        except Exception:
            return False
    return True

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    page.goto(BASE, wait_until="domcontentloaded")
    page.wait_for_selector(".hero-cta", timeout=20000)
    page.click(".hero-cta")
    page.wait_for_selector('input[type="email"]')
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASS)
    page.click('button:has-text("Continue")')
    page.wait_for_selector(".lp__card", timeout=20000)
    log("logged in")

    for mod_id, pid, qidx, extra in TARGETS:
        phase = PHASES[pid]
        q = phase["q"][qidx]
        opts = q["o"]["en"]
        intended = intended_idx(q)
        if extra not in opts:
            log(f"{pid} q{qidx}: extra {extra!r} NOT in options {opts}")
            continue
        if not any(app_accepts(o, q["a"] if isinstance(q["a"], list) else [q["a"]]) for o in [extra]):
            log(f"{pid} q{qidx}: app does NOT accept {extra!r}??")
            continue
        # navigate to phase
        mod_name = next(m["name"]["en"] for m in GAME["modules"] if m["id"] == mod_id)
        page.locator(".header-logo").first.click()
        page.wait_for_selector(".lp__card")
        card = page.locator(f".lp__card:has-text('{mod_name}')").first
        if not card.evaluate("el => el.classList.contains('lp__card--open')"):
            card.click()
        page.wait_for_selector(".lp__panel")
        page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")
        order = GAME["phaseLockOrder"][mod_id]
        btn = page.locator(".lp__phase").nth(order.index(pid))
        if btn.is_disabled():
            log(f"{pid}: LOCKED, skip")
            row({"kind": "d9", "phase": pid, "qidx": qidx, "status": "blocked", "reason": "locked"})
            continue
        btn.click()
        page.wait_for_selector(".lesson-screen", timeout=8000)
        page.wait_for_timeout(400)
        # answer questions before target CORRECTLY
        ok = True
        for qi in range(qidx):
            qq = phase["q"][qi]
            t = intended_idx(qq)[0]
            page.locator(".option-btn").nth(t).click()
            page.wait_for_timeout(120)
            page.locator(".mc-question-actions button").filter(has_text="Submit").click()
            try:
                page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=6000)
            except Exception:
                log(f"{pid}: could not submit pre-question {qi}")
                ok = False
                break
            if not advance(page):
                ok = False
                break
            page.wait_for_timeout(300)
        if not ok:
            row({"kind": "d9", "phase": pid, "qidx": qidx, "status": "blocked", "reason": "pre-question"})
            continue
        # now answer the TARGET with the D9 extra option
        ei = opts.index(extra)
        page.locator(".option-btn").nth(ei).click()
        page.wait_for_timeout(150)
        sel_cls = page.locator(".option-btn").nth(ei).get_attribute("class")
        page.locator(".mc-question-actions button").filter(has_text="Submit").click()
        try:
            page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=6000)
        except Exception:
            row({"kind": "d9", "phase": pid, "qidx": qidx, "status": "blocked", "reason": "submit"})
            log(f"{pid} q{qidx}: submit failed")
            page.goto(BASE); page.wait_for_selector(".lp__card", timeout=20000)
            continue
        card_cls = page.locator(".mc-question-card").get_attribute("class")
        fb = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
        opt_cls = page.evaluate("() => Array.from(document.querySelectorAll('.option-btn')).map(b => b.className)")
        accepted = "card--correct" in card_cls
        row({"kind": "d9", "phase": pid, "qidx": qidx, "qid": q["id"],
             "extraOption": extra, "extraIndex": ei,
             "intended": [opts[i] for i in intended],
             "appAcceptedWrong": accepted,
             "cardCls": card_cls, "feedback": fb[:100],
             "optionClasses": opt_cls,
             "status": "verified" if accepted else "not-accepted"})
        log(f"{pid} q{qidx}: picked {extra!r} -> app says {'CORRECT (D9!)' if accepted else 'wrong'} | fb={fb[:60]!r}")
        # finish the phase quickly (answer rest correctly) to not leave it mid-phase
        for qi in range(qidx + 1, len(phase["q"])):
            qq = phase["q"][qi]
            t = intended_idx(qq)[0]
            page.locator(".option-btn").nth(t).click()
            page.wait_for_timeout(100)
            page.locator(".mc-question-actions button").filter(has_text="Submit").click()
            try:
                page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=6000)
            except Exception:
                break
            if not advance(page):
                break
            page.wait_for_timeout(200)
        page.wait_for_timeout(800)
        # back to learning path
        if page.locator(".completion-screen").count():
            if page.locator(".completion-actions button:has-text('Home')").count():
                page.locator(".completion-actions button").filter(has_text="Home").first.click()
                page.wait_for_selector(".lp__card", timeout=8000)
        else:
            page.locator(".btn-back").first.click()
            page.wait_for_selector(".lp__card", timeout=8000)

    browser.close()
    log("D9 verification complete")
