#!/usr/bin/env python
"""Focused repro: pass B (all correct) on clauses_subobj with instrumentation."""
import json, time, sys
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
EMAIL = "learner.e2e.20260803@gramlingo.test"
PASS = "Grm!E2E-2026-Learner"
ROOT = r"C:/Users/hunin/projects/gramlingo"

with open(ROOT + "/data/game-data.json", encoding="utf-8") as f:
    GAME = json.load(f)
PHASES = {p["id"]: p for p in GAME["phases"]}
qs = PHASES["clauses_subobj"]["q"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    console_msgs = []
    page.on("console", lambda m: console_msgs.append(f"{m.type}: {m.text}"))
    page.on("pageerror", lambda e: console_msgs.append(f"PAGEERROR: {e}"))

    page.goto(BASE, wait_until="domcontentloaded")
    page.wait_for_selector(".hero-cta", timeout=20000)
    page.click(".hero-cta")
    page.wait_for_selector('input[type="email"]')
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASS)
    page.click('button:has-text("Continue")')
    page.wait_for_selector(".lp__card", timeout=20000)
    print("logged in")

    # open clauses module
    card = page.locator(".lp__card:has-text('Relative Clauses')").first
    if not card.evaluate("el => el.classList.contains('lp__card--open')"):
        card.click()
    page.wait_for_selector(".lp__panel")
    page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")

    # phase index 3 = clauses_subobj
    page.locator(".lp__phase").nth(3).click()
    try:
        page.wait_for_selector(".lesson-screen", timeout=5000)
    except Exception:
        print("FAIL: lesson screen did not open for clauses_subobj")
        print("visible buttons:", [b.inner_text() for b in page.locator("button").all()][:20])
        page.screenshot(path=ROOT + "/output/audit-20260804/evidence/repro_open_fail.png")
        sys.exit(1)
    print("phase opened, count:", page.locator(".lesson-question-count").inner_text())

    for qi, q in enumerate(qs):
        print(f"--- Q{qi} {q['id']}")
        # find correct index
        opts = q["o"]["en"]
        ans = q["a"]
        answers = ans if isinstance(ans, list) else [ans]
        correct_idx = [i for i, o in enumerate(opts) if any(o == a or o in a or a in o for a in answers)][0]
        page.locator(".option-btn").nth(correct_idx).click()
        page.wait_for_timeout(120)
        page.locator(".mc-question-actions button").filter(has_text="Submit").click()
        try:
            page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=6000)
        except Exception:
            print("  FAIL: Next button did not appear after submit")
            print("  card class:", page.locator(".mc-question-card").get_attribute("class"))
            page.screenshot(path=ROOT + f"/output/audit-20260804/evidence/repro_q{qi}_nosubmit.png")
            break
        # feedback
        print("  feedback:", page.locator(".feedback-body").first.inner_text()[:80])
        page.locator("button:has-text('Next')").first.click()
        time.sleep(0.5)
        if qi < len(qs) - 1:
            if page.locator(".lesson-question-count").count():
                print("  advanced to:", page.locator(".lesson-question-count").inner_text())
            else:
                print("  !! lesson-question-count MISSING after Next")
                print("  completion-screen:", page.locator(".completion-screen").count(),
                      "| lp__card:", page.locator(".lp__card").count(),
                      "| welcome:", page.locator(".welcome-screen").count())
                print("  body head:", page.locator("body").inner_text()[:200].replace("\n", " | "))
                page.screenshot(path=ROOT + f"/output/audit-20260804/evidence/repro_q{qi}_afternext.png")
                print("  CONSOLE NOW:")
                for m in console_msgs:
                    print("   ", m[:300])
        else:
            print("  last question -> completion expected")
            if page.locator(".completion-screen").count():
                print("  completion:", page.locator(".star-score").inner_text())
            else:
                print("  !! completion-screen MISSING")

    print("\nCONSOLE:")
    for m in console_msgs:
        print("  ", m[:200])
    browser.close()
