#!/usr/bin/env python
"""Lower-score-does-not-overwrite + error-log dedupe/repeat test on the primary learner."""
import json, os, sys, datetime
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
ROOT = r"C:/Users/hunin/projects/gramlingo"
OUT = os.path.join(ROOT, "output", "audit-20260804")
LEDGER = os.path.join(OUT, "ledger", "retest-ledger.jsonl")
EMAIL = "learner.e2e.20260803@gramlingo.test"
PASS = "Grm!E2E-2026-Learner"
USER = EMAIL.split("@")[0]
LS_KEY = "gramlingo_user_state:" + USER

with open(os.path.join(ROOT, "data", "game-data.json"), encoding="utf-8") as f:
    GAME = json.load(f)
PHASES = {p["id"]: p for p in GAME["phases"]}

def row(r):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

def state(page):
    raw = page.evaluate(f"() => localStorage.getItem('{LS_KEY}')")
    return json.loads(raw) if raw else None

def correct_idx(q):
    a = q["a"]; answers = a if isinstance(a, list) else [a]
    opts = q["o"]["en"]
    return [i for i, o in enumerate(opts) if any(o == x or o in x or x in o for x in answers)]

def run_all_wrong(page, phase_id):
    qs = PHASES[phase_id]["q"]
    for qi, q in enumerate(qs):
        ci = correct_idx(q)
        wrong = [i for i in range(len(q["o"]["en"])) if i not in ci]
        target = wrong[0] if wrong else ci[0]
        page.locator(".option-btn").nth(target).click()
        page.locator(".mc-question-actions button").filter(has_text="Submit").click()
        page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
        try:
            page.get_by_role("button", name="Next →", exact=True).click(timeout=5000)
        except Exception:
            try:
                page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
            except Exception:
                pass
        page.wait_for_timeout(250)

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
    print("logged in", flush=True)

    target_phase = "prepositions_prep_place"  # completed at 100% by the sweep
    before = state(page)
    pp_before = next((p for p in before["progress"] if p["phaseId"] == target_phase), None)
    print("before:", pp_before, flush=True)
    row({"kind": "retest-before", "phase": target_phase, "progress": pp_before})

    # open prepositions module -> click phase 1 (index 0)
    card = page.locator(".lp__card:has-text('Prepositions')").first
    if not card.evaluate("el => el.classList.contains('lp__card--open')"):
        card.click()
    page.wait_for_selector(".lp__panel")
    page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")
    page.locator(".lp__phase").nth(0).click()
    page.wait_for_selector(".lesson-screen")

    # run ALL WRONG (score should be 0% -> lower than bestScore 100)
    run_all_wrong(page, target_phase)
    page.wait_for_selector(".completion-screen", timeout=10000)
    score_shown = page.locator(".star-score").inner_text()
    stars = page.locator(".stars").inner_text()
    print("completion after all-wrong retry: score shown =", score_shown, "stars =", repr(stars), flush=True)
    row({"kind": "retest-lower-score", "phase": target_phase, "scoreShown": score_shown, "stars": stars,
         "expectedBestKept": "100%", "expectedStars": "★ ★ ★"})

    # verify state: bestScore must remain 100, attempts +1
    page.wait_for_timeout(2500)  # flush debounce
    after = state(page)
    pp_after = next((p for p in after["progress"] if p["phaseId"] == target_phase), None)
    print("after:", pp_after, flush=True)
    row({"kind": "retest-after", "phase": target_phase, "progress": pp_after})

    # ---- error-log dedupe test: answer one question wrong TWICE in a row (two retries) ----
    # Retry phase, answer q0 wrong, quit to learning path, re-enter, answer q0 wrong again -> attemptCount should be 2
    page.locator(".completion-actions button").filter(has_text="Retry").first.click()
    page.wait_for_selector(".lesson-screen", timeout=8000)
    q0 = PHASES[target_phase]["q"][0]
    ci = correct_idx(q0)
    wrong = [i for i in range(len(q0["o"]["en"])) if i not in ci]
    page.locator(".option-btn").nth(wrong[0]).click()
    page.locator(".mc-question-actions button").filter(has_text="Submit").click()
    page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
    page.locator("button:has-text('Next')").first.click()
    page.wait_for_timeout(300)
    # now quit back to learning path (Back)
    page.locator(".btn-back").first.click()
    page.wait_for_selector(".lp__card", timeout=8000)
    page.wait_for_timeout(2500)
    st1 = state(page)
    errs1 = [e for e in st1["errorLog"] if e["phaseId"] == target_phase]
    print("errors after 1st wrong:", errs1, flush=True)
    row({"kind": "retest-errordedupe-1", "phase": target_phase, "entries": errs1})

    # re-enter phase, answer q0 wrong again
    card = page.locator(".lp__card:has-text('Prepositions')").first
    if not card.evaluate("el => el.classList.contains('lp__card--open')"):
        card.click()
    page.wait_for_selector(".lp__panel")
    page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")
    page.locator(".lp__phase").nth(0).click()
    page.wait_for_selector(".lesson-screen")
    ci = correct_idx(q0)
    wrong = [i for i in range(len(q0["o"]["en"])) if i not in ci]
    page.locator(".option-btn").nth(wrong[0]).click()
    page.locator(".mc-question-actions button").filter(has_text="Submit").click()
    page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
    page.wait_for_timeout(800)
    st2 = state(page)
    errs2 = [e for e in st2["errorLog"] if e["phaseId"] == target_phase]
    q0_errs = [e for e in errs2 if e["questionIndex"] == 0]
    print("errors after 2nd wrong:", errs2, flush=True)
    row({"kind": "retest-errordedupe-2", "phase": target_phase, "entries": errs2,
         "q0Entry": q0_errs[0] if q0_errs else None,
         "duplicateCheck": len(q0_errs) == 1})

    browser.close()
