#!/usr/bin/env python
"""Careful re-run of reported module phases: reported_time + verbs/tense/embedded/prod.

Uses poll-until-changed waits to avoid the advance race that flaked the sweep.
"""
import json, os, datetime
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
ROOT = r"C:/Users/hunin/projects/gramlingo"
OUT = os.path.join(ROOT, "output", "audit-20260804")
LEDGER = os.path.join(OUT, "ledger", "reported-ledger.jsonl")
EMAIL = "learner.e2e.20260803@gramlingo.test"
PASS = "Grm!E2E-2026-Learner"
USER = EMAIL.split("@")[0]
LS_KEY = "gramlingo_user_state:" + USER

with open(os.path.join(ROOT, "data", "game-data.json"), encoding="utf-8") as f:
    GAME = json.load(f)
PHASES = {p["id"]: p for p in GAME["phases"]}
MODULE_NAME = "Reported Speech"

def row(r):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

def log(m):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}", flush=True)

def state(page):
    raw = page.evaluate(f"() => localStorage.getItem('{LS_KEY}')")
    return json.loads(raw) if raw else None

def correct_idx(q):
    a = q["a"]; answers = a if isinstance(a, list) else [a]
    opts = q["o"]["en"]
    return [i for i, o in enumerate(opts) if any(o == x or o in x or x in o for x in answers)]

def qcount(page):
    try:
        import re
        t = page.locator(".lesson-question-count").inner_text(timeout=1500)
        m = re.search(r"(\d+)\s+of\s+(\d+)", t)
        return (int(m.group(1)), int(m.group(2))) if m else (None, None)
    except Exception:
        return (None, None)

def advance_wait(page, expected_next):
    """Click the exact Next button, poll until question count == expected_next (or completion)."""
    try:
        page.get_by_role("button", name="Next →", exact=True).click(timeout=5000)
    except Exception:
        try:
            page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
        except Exception:
            pass
    for _ in range(30):
        if page.locator(".completion-screen").count():
            return "completion"
        c = qcount(page)
        if c and c[0] == expected_next:
            return "ok"
        page.wait_for_timeout(200)
    return "timeout:" + str(qcount(page))

def answer_one(page, q, want_correct):
    ci = correct_idx(q)
    if want_correct:
        target = ci[0]
    else:
        wrong = [i for i in range(len(q["o"]["en"])) if i not in ci]
        target = wrong[0] if wrong else ci[0]
    # click option and VERIFY selection registered (selected class) before submit
    for _ in range(5):
        page.locator(".option-btn").nth(target).click()
        page.wait_for_timeout(150)
        cls = page.locator(".option-btn").nth(target).get_attribute("class")
        if "option-btn--selected" in cls or page.locator(".mc-question-actions button:has-text('Submit')").count():
            break
        page.wait_for_timeout(200)
    page.locator(".mc-question-actions button").filter(has_text="Submit").click()
    page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
    card = page.locator(".mc-question-card").get_attribute("class")
    fb = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
    return {"target": target, "cardCls": card, "feedback": fb[:120]}

def run_phase(page, pid, open_panel=False):
    phase = PHASES[pid]
    qs = phase["q"]
    order = GAME["phaseLockOrder"][phase["module"]]
    log(f"--- {pid} ({len(qs)} qs)")
    if not page.locator(".lesson-screen").count():
        if not page.locator(".lp__panel").count():
            page.locator(".header-logo").first.click()
            page.wait_for_selector(".lp__card")
        card = page.locator(f".lp__card:has-text('{MODULE_NAME}')").first
        if not card.evaluate("el => el.classList.contains('lp__card--open')"):
            card.click()
        page.wait_for_selector(".lp__panel")
        page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")
        btn = page.locator(".lp__phase").nth(order.index(pid))
        if btn.is_disabled():
            log(f"  !! {pid} LOCKED — skipping")
            row({"kind": "phase", "phase": pid, "status": "blocked", "reason": "locked"})
            return False
        btn.click()
        page.wait_for_selector(".lesson-screen", timeout=8000)
    page.wait_for_timeout(400)
    # pass A all wrong
    for qi, q in enumerate(qs):
        r = answer_one(page, q, want_correct=False)
        row({"kind": "question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "A",
             "wrongUsed": q["o"]["en"][r["target"]], "wrongRejected": "card--wrong" in r["cardCls"],
             "feedback": r["feedback"]})
        adv = advance_wait(page, qi + 2)
        row({"kind": "advance", "phase": pid, "qidx": qi, "pass": "A", "state": adv})
        if adv != "ok":
            log(f"  !! advance issue pass A q{qi}: {adv}")
            if adv == "completion":
                break
    page.wait_for_selector(".completion-screen", timeout=10000)
    scoreA = page.locator(".star-score").inner_text()
    row({"kind": "phase", "phase": pid, "pass": "A", "status": "ok", "score": scoreA})
    log(f"  pass A score={scoreA}")
    # pass B all correct
    page.locator(".completion-actions button").filter(has_text="Retry").first.click()
    page.wait_for_selector(".lesson-screen", timeout=8000)
    page.wait_for_timeout(400)
    for qi, q in enumerate(qs):
        r = answer_one(page, q, want_correct=True)
        row({"kind": "question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "B",
             "correctUsed": q["o"]["en"][r["target"]], "accepted": "card--correct" in r["cardCls"],
             "feedback": r["feedback"]})
        adv = advance_wait(page, qi + 2)
        row({"kind": "advance", "phase": pid, "qidx": qi, "pass": "B", "state": adv})
        if adv != "ok":
            log(f"  !! advance issue pass B q{qi}: {adv}")
            if adv == "completion":
                break
    page.wait_for_selector(".completion-screen", timeout=10000)
    scoreB = page.locator(".star-score").inner_text()
    row({"kind": "phase", "phase": pid, "pass": "B", "status": "ok", "score": scoreB})
    log(f"  pass B score={scoreB}")
    # error log check
    st = state(page)
    errs = [e for e in st["errorLog"] if e["phaseId"] == pid] if st else []
    row({"kind": "errorlog", "phase": pid, "afterB": len(errs)})
    # home
    if page.locator(".completion-actions button:has-text('Home')").count():
        page.locator(".completion-actions button").filter(has_text="Home").first.click()
        page.wait_for_selector(".lp__card", timeout=8000)
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

    for pid in ["reported_time", "reported_verbs", "reported_tense", "reported_embedded", "reported_prod"]:
        ok = run_phase(page, pid)
        if not ok:
            log(f"  {pid} not run (locked) — stopping")
            break

    st = state(page)
    log(f"final: progress={len(st['progress'])} errors={len(st['errorLog'])}")
    row({"kind": "final", "progressCount": len(st["progress"]), "errorLogCount": len(st["errorLog"])})
    browser.close()
