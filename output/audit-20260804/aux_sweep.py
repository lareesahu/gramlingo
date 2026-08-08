#!/usr/bin/env python
"""Auxiliary learner: covers the clauses phases blocked by D7 using the workaround.

Uses a FRESH learner account (created via the normal signup flow):
- clauses_subobj: q04 answered wrong in pass B to avoid the D7 crash, phase completes at 83%
- then clauses_oblq/gen/rest/prod run fully (wrong+correct paths)
Also verifies the fresh account sees ZERO inherited progress (isolation).
"""
import json, os, sys, time, datetime
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
ROOT = r"C:/Users/hunin/projects/gramlingo"
OUT = os.path.join(ROOT, "output", "audit-20260804")
EVID = os.path.join(OUT, "evidence")
AUX_EMAIL = "isolation.e2e.20260804@gramlingo.test"
AUX_PASS = "Grm!E2E-2026-Aux"
AUX_USER = AUX_EMAIL.split("@")[0]
AUX_LS = "gramlingo_user_state:" + AUX_USER
LEDGER = os.path.join(OUT, "ledger", "aux-ledger.jsonl")

with open(os.path.join(ROOT, "data", "game-data.json"), encoding="utf-8") as f:
    GAME = json.load(f)
PHASES = {p["id"]: p for p in GAME["phases"]}
MODULES = {m["id"]: m for m in GAME["modules"]}

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def row(r):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

def read_state(page):
    raw = page.evaluate(f"() => localStorage.getItem('{AUX_LS}')")
    return json.loads(raw) if raw else None

def canonical_correct_indices(q):
    a = q["a"]; answers = a if isinstance(a, list) else [a]
    opts = q["o"]["en"]
    return [i for i, o in enumerate(opts) if any(o == x or o in x or x in o for x in answers)]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    console_errs = []
    page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: console_errs.append(str(e)))

    # Signup/login via the real UI
    page.goto(BASE, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_selector(".hero-cta", timeout=20000)
    page.click(".hero-cta")
    page.wait_for_selector('input[type="email"]')
    page.fill('input[type="email"]', AUX_EMAIL)
    page.fill('input[type="password"]', AUX_PASS)
    page.click('button:has-text("Continue")')
    page.wait_for_selector(".lp__card", timeout=25000)
    banner = page.locator(".lp__banner-stats").inner_text()
    st = read_state(page)
    log(f"aux account logged in. banner='{banner}' progress={len(st['progress']) if st else 'NA'} errors={len(st['errorLog']) if st else 'NA'}")
    row({"kind": "aux-account", "username": AUX_USER, "banner": banner,
         "progressCount": len(st["progress"]) if st else None,
         "errorLogCount": len(st["errorLog"]) if st else None})

    # Open clauses module; verify isolation: only phase 1 unlocked, ZERO completed
    card = page.locator(".lp__card:has-text('Relative Clauses')").first
    if not card.evaluate("el => el.classList.contains('lp__card--open')"):
        card.click()
    page.wait_for_selector(".lp__panel")
    page.wait_for_function("() => document.querySelectorAll('.lp__phase').length > 0")
    lockstates = page.evaluate("""() => Array.from(document.querySelectorAll('.lp__phase')).map((el,i)=>({i, locked: el.classList.contains('lp__phase--locked'), disabled: el.disabled}))""")
    row({"kind": "aux-isolation", "clausesLockStates": lockstates})
    log(f"clauses lock states: {lockstates}")

    # ---- clauses_subobj with workaround ----
    def run_phase(pid, workaround_q04=False):
        phase = PHASES[pid]
        qs = phase["q"]
        order = GAME["phaseLockOrder"][phase["module"]]
        log(f"--- {pid} ({len(qs)} qs) workaround={workaround_q04}")
        if not page.locator(".lesson-screen").count():
            # ensure module open
            if not page.locator(".lp__panel").count():
                page.locator(".header-logo").first.click()
                page.wait_for_selector(".lp__card")
                card = page.locator(".lp__card:has-text('Relative Clauses')").first
                if not card.evaluate("el => el.classList.contains('lp__card--open')"):
                    card.click()
                page.wait_for_selector(".lp__panel")
            page.locator(".lp__phase").nth(order.index(pid)).click()
            try:
                page.wait_for_selector(".lesson-screen", timeout=4000)
            except Exception:
                log(f"  !! cannot open {pid} (locked?)")
                row({"kind": "aux-phase", "phase": pid, "status": "blocked"})
                return
        # pass A wrong
        for qi, q in enumerate(qs):
            qtype = q["type"]
            if qtype == "multiple_choice_single":
                ci = canonical_correct_indices(q)
                wrong = [i for i in range(len(q["o"]["en"])) if i not in ci]
                if not wrong:
                    row({"kind": "aux-question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "A", "status": "blocked", "reason": "no-wrong-option"})
                    page.get_by_role("button", name="Next →", exact=True).click()
                    page.wait_for_timeout(300)
                    continue
                target = wrong[0]
                page.locator(".option-btn").nth(target).click()
                page.locator(".mc-question-actions button").filter(has_text="Submit").click()
                page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
                fb = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
                cardcls = page.locator(".mc-question-card").get_attribute("class")
                row({"kind": "aux-question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "A",
                     "type": qtype, "wrongUsed": q["o"]["en"][target], "wrongRejected": "card--wrong" in cardcls,
                     "feedback": fb[:120]})
            else:
                page.locator("button:has-text('Hide words & recall')").click()
                page.wait_for_selector(".bb-mem-blank")
                for b in q["blanks"]:
                    pick = next((w for w in b["options"] if w != b["word"]), None)
                    page.get_by_role("button", name=pick, exact=True).first.click()
                    page.wait_for_timeout(60)
                page.locator("button:has-text('Check recall')").click()
                page.wait_for_selector("button:has-text('Next sentence')", timeout=8000)
                cardcls = page.locator(".bb-question-card").get_attribute("class")
                row({"kind": "aux-question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "A",
                     "type": qtype, "wrongRejected": "card--wrong" in cardcls})
            try:
                page.get_by_role("button", name="Next →", exact=True).click(timeout=5000)
            except Exception:
                try:
                    page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
                except Exception:
                    pass
            page.wait_for_timeout(250)
        # completion
        try:
            page.wait_for_selector(".completion-screen", timeout=8000)
        except Exception:
            log(f"  !! no completion after pass A for {pid}")
            row({"kind": "aux-phase", "phase": pid, "pass": "A", "status": "failed"})
            page.goto(BASE); page.wait_for_selector(".lp__card", timeout=20000)
            return
        scoreA = page.locator(".star-score").inner_text()
        row({"kind": "aux-phase", "phase": pid, "pass": "A", "status": "ok", "score": scoreA})
        # retry -> pass B correct (with workaround for q04 if set)
        page.locator(".completion-actions button").filter(has_text="Retry").first.click()
        page.wait_for_selector(".lesson-screen", timeout=8000)
        correct_count = 0
        for qi, q in enumerate(qs):
            qtype = q["type"]
            if qtype == "multiple_choice_single":
                ci = canonical_correct_indices(q)
                workaround = workaround_q04 and qi == 3
                target = (ci[0] if ci else 0) if not workaround else next((i for i in range(len(q["o"]["en"])) if i not in ci), 0)
                page.locator(".option-btn").nth(target).click()
                page.locator(".mc-question-actions button").filter(has_text="Submit").click()
                page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
                cardcls = page.locator(".mc-question-card").get_attribute("class")
                accepted = "card--correct" in cardcls
                if accepted: correct_count += 1
                fb = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
                row({"kind": "aux-question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "B",
                     "type": qtype, "correctUsed": q["o"]["en"][target], "accepted": accepted,
                     "workaround": workaround, "feedback": fb[:120]})
            else:
                page.locator("button:has-text('Hide words & recall')").click()
                page.wait_for_selector(".bb-mem-blank")
                for b in q["blanks"]:
                    page.get_by_role("button", name=b["word"], exact=True).first.click()
                    page.wait_for_timeout(60)
                page.locator("button:has-text('Check recall')").click()
                page.wait_for_selector("button:has-text('Next sentence')", timeout=8000)
                cardcls = page.locator(".bb-question-card").get_attribute("class")
                if "card--correct" in cardcls: correct_count += 1
                row({"kind": "aux-question", "phase": pid, "qidx": qi, "qid": q["id"], "pass": "B",
                     "type": qtype, "accepted": "card--correct" in cardcls})
            try:
                page.get_by_role("button", name="Next →", exact=True).click(timeout=5000)
            except Exception:
                try:
                    page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
                except Exception:
                    pass
            page.wait_for_timeout(250)
        try:
            page.wait_for_selector(".completion-screen", timeout=8000)
        except Exception:
            log(f"  !! no completion after pass B for {pid}")
            row({"kind": "aux-phase", "phase": pid, "pass": "B", "status": "failed"})
            page.goto(BASE); page.wait_for_selector(".lp__card", timeout=20000)
            return
        scoreB = page.locator(".star-score").inner_text()
        expectedB = round(correct_count / len(qs) * 100)
        row({"kind": "aux-phase", "phase": pid, "pass": "B", "status": "ok",
             "score": scoreB, "expectedB": expectedB, "correctCount": correct_count, "total": len(qs)})
        log(f"  passB score={scoreB} expected={expectedB}")
        # advance: Home then next phase handled by caller
        if page.locator(".completion-actions button:has-text('Home')").count():
            page.locator(".completion-actions button").filter(has_text="Home").first.click()
            page.wait_for_selector(".lp__card", timeout=8000)

    # run clauses_subobj with workaround, then the rest
    run_phase("clauses_subobj", workaround_q04=True)
    for pid in ["clauses_oblq", "clauses_gen", "clauses_rest", "clauses_prod"]:
        run_phase(pid, workaround_q04=False)

    # final state
    st = read_state(page)
    row({"kind": "aux-final", "progressCount": len(st["progress"]) if st else None,
         "errorLogCount": len(st["errorLog"]) if st else None,
         "consoleErrors": console_errs[:20]})
    log(f"final aux state: progress={len(st['progress']) if st else None} errors={len(st['errorLog']) if st else None} consoleErrs={len(console_errs)}")
    browser.close()
