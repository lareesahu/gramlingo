#!/usr/bin/env python
"""Capture full pageerror stack for clauses_subobj crash."""
import json, sys
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
EMAIL = "learner.e2e.20260803@gramlingo.test"
PASS = "Grm!E2E-2026-Learner"
ROOT = r"C:/Users/hunin/projects/gramlingo"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    stacks = []
    page.on("pageerror", lambda e: stacks.append(f"{e}\n{e.stack}"))

    page.goto(BASE, wait_until="domcontentloaded")
    page.wait_for_selector(".hero-cta", timeout=20000)
    page.click(".hero-cta")
    page.wait_for_selector('input[type="email"]')
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASS)
    page.click('button:has-text("Continue")')
    page.wait_for_selector(".lp__card", timeout=20000)

    card = page.locator(".lp__card:has-text('Relative Clauses')").first
    if not card.evaluate("el => el.classList.contains('lp__card--open')"):
        card.click()
    page.wait_for_selector(".lp__panel")
    page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")

    # Need phase 4 (clauses_subobj). Click through: it's unlocked. Index 3.
    page.locator(".lp__phase").nth(3).click()
    page.wait_for_selector(".lesson-screen")

    # Answer Q1-Q4 correct quickly
    answers = [0, 1, 1, 3]  # indexes for q01..q04
    for qi, ans in enumerate(answers):
        page.locator(".option-btn").nth(ans).click()
        page.wait_for_timeout(100)
        page.locator(".mc-question-actions button").filter(has_text="Submit").click()
        page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=6000)
        page.locator("button:has-text('Next')").first.click()
        page.wait_for_timeout(600)
        print(f"q{qi}: stacks={len(stacks)}", flush=True)
        if stacks:
            break

    if stacks:
        print("\n===== FULL PAGEERROR STACK =====")
        print(stacks[-1])
    else:
        print("no crash this run")
    # also dump runtime question data from the app
    print("\n--- runtime phase data (via app import attempt) ---")
    try:
        # React internals not easily accessible; instead dump the raw JSON q05
        with open(ROOT + "/data/game-data.json", encoding="utf-8") as f:
            data = json.load(f)
        for ph in data["phases"]:
            if ph["id"] == "clauses_subobj":
                for i, q in enumerate(ph["q"]):
                    print(i, q["id"], "keys:", sorted(q.keys()))
                    print("   a=", repr(q.get("a")), "o=", repr(q.get("o")))
                    print("   ex=", repr(q.get("ex"))[:200])
    except Exception as e:
        print("dump err", e)
    browser.close()
