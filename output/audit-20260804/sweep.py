#!/usr/bin/env python
"""GramLingo exhaustive browser QA sweep — drives the REAL UI against the dev server.

Pass A per phase: every question answered WRONG (deliberately).
Pass B per phase: every question answered CORRECT.
Verifies feedback, scoring, locking, error log, persistence, and checkpoints a ledger.
"""
import json, os, sys, time, datetime, traceback
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5173/gramlingo/"
ROOT = r"C:/Users/hunin/projects/gramlingo"
OUT = os.path.join(ROOT, "output", "audit-20260804")
EVID = os.path.join(OUT, "evidence")
LEDGER = os.path.join(OUT, "ledger", "sweep-ledger.jsonl")
os.makedirs(EVID, exist_ok=True)
os.makedirs(os.path.join(OUT, "ledger"), exist_ok=True)

EMAIL = os.environ.get("SWEEP_EMAIL", "learner.e2e.20260803@gramlingo.test")
PASS = os.environ.get("SWEEP_PASS", "Grm!E2E-2026-Learner")
USERNAME = EMAIL.split("@")[0]
LS_KEY = "gramlingo_user_state:" + USERNAME

with open(os.path.join(ROOT, "data", "game-data.json"), encoding="utf-8") as f:
    GAME = json.load(f)

MODULES = {m["id"]: m for m in GAME["modules"]}
PHASES = {p["id"]: p for p in GAME["phases"]}

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def ledger_row(row):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

def shot(page, name):
    path = os.path.join(EVID, name)
    try:
        page.screenshot(path=path, full_page=False)
        return os.path.relpath(path, OUT)
    except Exception:
        return ""

def read_user_state(page):
    raw = page.evaluate(f"() => localStorage.getItem('{LS_KEY}')")
    return json.loads(raw) if raw else None

def canonical_correct_indices(q):
    """Indices of options that the app's includes-logic treats as correct."""
    a = q["a"]
    answers = a if isinstance(a, list) else [a]
    opts = q["o"]["en"]
    idxs = []
    for i, opt in enumerate(opts):
        if any((opt in ans) or (ans in opt) for ans in answers):
            idxs.append(i)
    return idxs

def expected_feedback(q, opt_idx):
    ex = q.get("ex", {})
    ex_en = ex.get("en") or []
    tip = (q.get("t") or {}).get("en") or ""
    per = ex_en[opt_idx] if opt_idx < len(ex_en) else ""
    return per or tip or "Tap an option to see its explanation"

def login(page):
    page.goto(BASE, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_selector(".hero-cta", timeout=20000)
    page.click(".hero-cta")
    page.wait_for_selector('input[type="email"]', timeout=10000)
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASS)
    page.click('button:has-text("Continue")')
    page.wait_for_selector(".lp__card", timeout=20000)
    log("logged in, learning path visible")

def open_module(page, module_id):
    card = page.locator(f'.lp__card:has-text("{MODULES[module_id]["name"]["en"]}")').first
    is_open = card.evaluate("el => el.classList.contains('lp__card--open')")
    if not is_open:
        card.click()
        page.wait_for_selector(".lp__panel", timeout=8000)
    # wait for phase buttons
    page.wait_for_function(
        "() => document.querySelectorAll('.lp__phase').length > 0", timeout=8000)

def phase_lock_states(page):
    return page.evaluate("""() => {
        const out = [];
        document.querySelectorAll('.lp__phase').forEach((el, i) => {
            out.push({index: i, text: el.innerText.replace(/\\n/g, ' ').trim(),
                      locked: el.classList.contains('lp__phase--locked'),
                      disabled: el.disabled,
                      done: el.classList.contains('lp__phase--done')});
        });
        return out;
    }""")

def click_phase(page, index):
    try:
        page.locator(".lp__phase").nth(index).click(timeout=4000)
    except Exception:
        pass
    try:
        page.wait_for_selector(".lesson-screen", timeout=4000)
    except Exception:
        pass

def goto_learning_path(page):
    # logo or Back button navigation
    if page.locator(".btn-back").count():
        page.locator(".btn-back").first.click()
    else:
        page.locator(".header-logo").first.click()
    page.wait_for_selector(".lp__card", timeout=8000)

def current_question_count(page):
    try:
        txt = page.locator(".lesson-question-count").inner_text(timeout=3000)
        # e.g. "Question 1 of 5"
        import re
        m = re.search(r"(\d+)\s+of\s+(\d+)", txt)
        return (int(m.group(1)), int(m.group(2))) if m else (None, None)
    except Exception:
        return (None, None)

def answer_mc(page, q, want_correct):
    """Select an option and submit. want_correct=True -> canonical correct; False -> deliberate wrong."""
    opts = q["o"]["en"]
    correct_idx = canonical_correct_indices(q)
    if want_correct:
        target = correct_idx[0]
        target_kind = "correct"
    else:
        wrong = [i for i in range(len(opts)) if i not in correct_idx]
        if not wrong:
            return {"skipped": "no-wrong-option"}
        target = wrong[0]
        target_kind = "wrong"
    # resilient select+submit: retry if the selection does not register
    submitted = False
    for attempt in range(4):
        if not page.locator(".mc-question-card").count():
            return {"lost": "no-question-card"}
        try:
            page.locator(".option-btn").nth(target).click(timeout=4000)
        except Exception:
            return {"lost": "option-click-failed"}
        try:
            page.locator(".mc-question-actions button").filter(has_text="Submit").click(timeout=4000)
            submitted = True
            break
        except Exception:
            page.wait_for_timeout(400)
    if not submitted:
        return {"lost": "submit-never-enabled"}
    page.wait_for_selector(".mc-question-actions button:has-text('Next')", timeout=8000)
    card_cls = page.locator(".mc-question-card").get_attribute("class")
    feedback = page.locator(".feedback").first.inner_text()
    fb_body = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
    opt_classes = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('.option-btn')).map(b => b.className);
    }""")
    return {"target": target, "targetKind": target_kind, "cardCls": card_cls,
            "feedback": feedback, "feedbackBody": fb_body, "optClasses": opt_classes}

def answer_cloze(page, q, want_correct):
    blanks = q["blanks"]
    page.wait_for_selector(".bb-study-panel", timeout=8000)
    page.locator("button:has-text('Hide words & recall')").click()
    page.wait_for_selector(".bb-mem-blank", timeout=8000)
    for b in blanks:
        opts = b["options"]
        word = b["word"]
        pick = word if want_correct else next((w for w in opts if w != word), None)
        if pick is None:
            return {"skipped": "no-wrong-option-for-blank", "blank": b}
        page.get_by_role("button", name=pick, exact=True).first.click()
        page.wait_for_timeout(80)
    page.locator("button:has-text('Check recall')").click()
    page.wait_for_selector("button:has-text('Next sentence')", timeout=8000)
    card_cls = page.locator(".bb-question-card").get_attribute("class")
    feedback = page.locator(".feedback").first.inner_text()
    fb_body = page.locator(".feedback-body").first.inner_text() if page.locator(".feedback-body").count() else ""
    blank_classes = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('.bb-mem-blank')).map(b => b.className);
    }""")
    return {"cardCls": card_cls, "feedback": feedback, "feedbackBody": fb_body, "blankClasses": blank_classes,
            "picked": [b["word"] if want_correct else next((w for w in b["options"] if w != b["word"]), None) for b in blanks]}

def capture_completion(page):
    page.wait_for_selector(".completion-screen", timeout=10000)
    score = page.locator(".star-score").inner_text()
    module_prog = page.locator(".completion-module-progress").inner_text()
    attempted = page.locator(".completion-module-attempted").inner_text()
    unlock = page.locator(".completion-unlock").inner_text() if page.locator(".completion-unlock").count() else ""
    buttons = [b.inner_text().strip() for b in page.locator(".completion-actions button").all()]
    return {"score": score, "moduleProgress": module_prog, "attempted": attempted,
            "unlock": unlock, "buttons": buttons}

def advance_after_answer(page):
    """Click Next, then wait for the next question OR completion. Returns 'ok'|'completion'|'lost'."""
    try:
        try:
            page.get_by_role("button", name="Next →", exact=True).click(timeout=5000)
        except Exception:
            try:
                page.get_by_role("button", name="Next sentence →", exact=True).click(timeout=3000)
            except Exception:
                pass
    except Exception:
        pass
    try:
        page.wait_for_selector(".lesson-question-count", timeout=6000)
        return "ok"
    except Exception:
        pass
    # not a lesson question anymore
    if page.locator(".completion-screen").count():
        return "completion"
    if page.locator(".lp__card").count():
        return "lost-learningpath"
    return "lost-unknown"

def recover_to_learning_path(page):
    """Reload; cloud session restore lands on learning path. Returns True if recovered."""
    try:
        page.goto(BASE, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_selector(".lp__card", timeout=20000)
        return True
    except Exception:
        return False

def click_completion_button(page, text):
    page.locator(".completion-actions button").filter(has_text=text).first.click()

def phase_already_done(pid):
    """True if ledger already contains a pass-B phase row for this phase."""
    if not os.path.exists(LEDGER):
        return False
    with open(LEDGER, encoding="utf-8") as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("kind") == "phase" and r.get("phase") == pid and r.get("pass") == "B":
                return True
    return False

def main():
    start = time.time()
    run_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    console_errors = []
    stats = {"modules": 0, "phases": 0, "questions_tested": 0, "wrong_paths": 0,
             "correct_paths": 0, "failures": 0, "blocked": 0}
    defects = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        page = ctx.new_page()
        page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: console_errors.append(str(e)))

        login(page)

        # pre-sweep: capture current cloud state from localStorage
        pre_state = read_user_state(page)
        log(f"pre-sweep state: progress={len(pre_state['progress'])} errorLog={len(pre_state['errorLog'])}")

        # order: iterate modules by sort, phases by lock order
        mods = sorted(GAME["modules"], key=lambda m: m["sort"])
        phase_limit = int(os.environ.get("SWEEP_PHASE_LIMIT", "0") or 0)
        module_filter = os.environ.get("SWEEP_MODULES", "")
        phases_done = 0
        for mod in mods:
            mid = mod["id"]
            if module_filter and mid not in module_filter.split(","):
                continue
            order = GAME["phaseLockOrder"][mid]
            playable = [pid for pid in order if len(PHASES[pid]["q"]) > 0]
            if not playable:
                continue
            stats["modules"] += 1
            log(f"=== MODULE {mid} ({len(playable)} playable phases) ===")

            # Enter module; record lock states BEFORE any completion this module
            goto_learning_path(page)
            open_module(page, mid)
            lock_before = phase_lock_states(page)
            # first phase must be unlocked; others locked (unless previously completed)
            for st in lock_before:
                pid = order[st["index"]]
                prev_done = st["index"] > 0 and (PHASES[order[st["index"]-1]] or True)
            ledger_row({"kind": "module-enter", "module": mid, "run": run_id,
                        "lockStates": lock_before})

            for pid in playable:
                if phase_limit and phases_done >= phase_limit:
                    break
                if os.environ.get("SWEEP_RESUME") and phase_already_done(pid):
                    log(f"skip (already done): {pid}")
                    continue
                phases_done += 1
                phase = PHASES[pid]
                qs = phase["q"]
                stats["phases"] += 1
                log(f"--- PHASE {pid} ({len(qs)} qs) ---")

                # ensure we are on learning path with module open
                if not page.locator(".lesson-screen").count():
                    if not page.locator(".lp__panel").count():
                        goto_learning_path(page)
                        open_module(page, mid)
                # click the phase in the open panel by order index
                pidx = order.index(pid)
                click_phase(page, pidx)
                if not page.locator(".lesson-screen").count():
                    # phase is locked/unavailable -> record blocked and skip
                    ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                                "status": "blocked", "blockReason": "phase-unreachable-locked",
                                "expectedCount": len(qs)})
                    stats["blocked"] += 1
                    goto_learning_path(page)
                    open_module(page, mid)
                    continue

                # displayed question count check
                idx, total = current_question_count(page)
                if total != len(qs):
                    ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                                "status": "fail", "issue": "question-count-mismatch",
                                "expectedCount": len(qs), "observedCount": total})
                    stats["failures"] += 1

                phase_rows = []
                phase_console_before = len(console_errors)
                stPre = read_user_state(page)
                prevBest = 0
                prevAttempts = 0
                for p in (stPre["progress"] if stPre else []):
                    if p["phaseId"] == pid:
                        prevBest = p.get("bestScore", 0)
                        prevAttempts = p.get("attempts", 0)

                # ── PASS A: all wrong ──
                passA_correct = 0
                passA_rows = []
                for qi, q in enumerate(qs):
                    qtype = q["type"]
                    row = {"kind": "question", "module": mid, "phase": pid, "qidx": qi,
                           "qid": q.get("id"), "type": qtype, "pass": "A",
                           "prompt": q.get("q", {}).get("en", q.get("q")) if isinstance(q.get("q"), dict) else q.get("q"),
                           "expectedAnswer": q["a"] if qtype == "multiple_choice_single" else "|".join(b["word"] for b in q["blanks"]),
                           "expectedWrongFeedback": expected_feedback(q, 0) if qtype == "multiple_choice_single" else q["fullSentence"],
                           "expectedCorrectFeedback": expected_feedback(q, canonical_correct_indices(q)[0]) if qtype == "multiple_choice_single" else q["fullSentence"]}
                    stats["questions_tested"] += 1
                    if qtype == "multiple_choice_single":
                        res = answer_mc(page, q, want_correct=False)
                    else:
                        res = answer_cloze(page, q, want_correct=False)
                    stats["wrong_paths"] += 1
                    if res.get("skipped"):
                        row["status"] = "blocked"
                        row["blockReason"] = res["skipped"]
                        row["observedWrongFeedback"] = ""
                        stats["blocked"] += 1
                    elif res.get("lost"):
                        row["status"] = "blocked"
                        row["blockReason"] = "ui-state-lost-" + res["lost"]
                        row["observedWrongFeedback"] = ""
                        stats["blocked"] += 1
                        shot(page, f"{mid}_{pid}_q{qi}_passA_lost.png")
                        adv = advance_after_answer(page)
                        row["advanceState"] = adv
                        if adv != "ok":
                            break
                    else:
                        row["wrongUsed"] = q["o"]["en"][res["target"]] if qtype == "multiple_choice_single" else "|".join(res["picked"])
                        row["observedWrongFeedback"] = res["feedbackBody"] or res["feedback"]
                        row["cardCls"] = res["cardCls"]
                        row["optClasses"] = res.get("optClasses")
                        row["wrongRejected"] = ("card--wrong" in (res["cardCls"] or ""))
                        if qtype == "multiple_choice_single":
                            if not row["wrongRejected"]:
                                # app treated wrong answer as correct -> possible defect
                                row["defectCandidate"] = "wrong-answer-accepted"
                                if q["id"] not in [d["qid"] for d in defects]:
                                    defects.append({"qid": q["id"], "module": mid, "phase": pid,
                                                    "issue": "wrong-answer-accepted", "wrongUsed": row["wrongUsed"]})
                                passA_correct += 1
                        else:
                            row["wrongRejected"] = ("bb-mem-blank--wrong" in (res["blankClasses"] or [])) or ("card--wrong" in (res["cardCls"] or ""))
                        exp = row["expectedWrongFeedback"]
                        obs = row["observedWrongFeedback"]
                        row["wrongFeedbackMatch"] = (exp in obs) if exp else True
                    phase_rows.append(row)
                    # advance
                    adv = advance_after_answer(page)
                    row["advanceState"] = adv
                    is_last = (qi == len(qs) - 1)
                    if adv == "completion":
                        if not is_last:
                            row["advanceIssue"] = f"premature completion after question {qi+1} of {len(qs)}"
                            stats["failures"] += 1
                            shot(page, f"{mid}_{pid}_q{qi}_passA_advance_{adv}.png")
                        break
                    elif adv != "ok":
                        row["advanceIssue"] = f"unexpected state after Next: {adv}"
                        stats["failures"] += 1
                        shot(page, f"{mid}_{pid}_q{qi}_passA_advance_{adv}.png")
                        break
                    elif not is_last:
                        idx2, _ = current_question_count(page)
                        if idx2 not in (None, qi + 2):
                            row["advanceIssue"] = f"expected question {qi+2}, saw {idx2}"
                            stats["failures"] += 1

                # completion after pass A
                expectedA = round((passA_correct / len(qs)) * 100) if len(qs) else 0
                if not page.locator(".completion-screen").count():
                    recovered = recover_to_learning_path(page)
                    ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                                "pass": "A", "status": "failed",
                                "defectId": "D7-mc-crash-blank-page",
                                "attemptScoreExpected": expectedA,
                                "recovered": recovered})
                    stats["failures"] += 1
                    for r in phase_rows:
                        ledger_row(r)
                    if recovered:
                        open_module(page, mid)
                    continue
                compA = capture_completion(page)
                expectedDisplayA = max(prevBest, expectedA)
                ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                            "pass": "A", "attemptScoreExpected": expectedA,
                            "attemptScoreObserved": compA["score"],
                            "displayScoreExpected": expectedDisplayA,
                            "prevBest": prevBest, "prevAttempts": prevAttempts,
                            "completion": compA, "status": "info"})
                # record passA rows
                for r in phase_rows:
                    r["completionA"] = compA["score"]
                    ledger_row(r)

                # error log check after pass A
                stA = read_user_state(page)
                errsA = [e for e in stA["errorLog"] if e["phaseId"] == pid] if stA else []
                ledger_row({"kind": "errorlog-check", "module": mid, "phase": pid, "pass": "A",
                            "run": run_id, "entriesForPhase": len(errsA), "entries": errsA})
                expectedErrCount = sum(1 for r in phase_rows if r.get("wrongRejected") and not r.get("skipped"))
                # note: entries may include earlier attempts of the same phase (dedupe increments)
                ledger_row({"kind": "errorlog-expected", "module": mid, "phase": pid, "pass": "A",
                            "run": run_id, "newWrongQuestions": expectedErrCount})

                # ── PASS B: all correct (Retry) ──
                click_completion_button(page, "Retry")
                page.wait_for_selector(".lesson-screen", timeout=8000)
                passB_correct = 0
                passB_rows = []
                for qi, q in enumerate(qs):
                    qtype = q["type"]
                    row = {"kind": "question", "module": mid, "phase": pid, "qidx": qi,
                           "qid": q.get("id"), "type": qtype, "pass": "B",
                           "prompt": q.get("q", {}).get("en", q.get("q")) if isinstance(q.get("q"), dict) else q.get("q"),
                           "expectedAnswer": q["a"] if qtype == "multiple_choice_single" else "|".join(b["word"] for b in q["blanks"]),
                           "expectedCorrectFeedback": expected_feedback(q, canonical_correct_indices(q)[0]) if qtype == "multiple_choice_single" else q["fullSentence"]}
                    stats["correct_paths"] += 1
                    # D7 workaround: if the correct option index of this question >= next question's
                    # option count, answering correctly would crash the app on the next render.
                    next_q = qs[qi + 1] if qi + 1 < len(qs) else None
                    workaround = False
                    if (os.environ.get("SWEEP_CRASH_WORKAROUND")
                            and qtype == "multiple_choice_single"
                            and next_q and next_q.get("type") == "multiple_choice_single"
                            and canonical_correct_indices(q)
                            and canonical_correct_indices(q)[0] >= len(next_q["o"]["en"])):
                        workaround = True
                        row["workaroundD7"] = True
                    if qtype == "multiple_choice_single":
                        res = answer_mc(page, q, want_correct=not workaround)
                        if workaround:
                            row["workaroundNote"] = "answered WRONG on this question to avoid D7 crash on next question"
                        if res.get("lost"):
                            row["status"] = "blocked"
                            row["blockReason"] = "ui-state-lost-" + res["lost"]
                            stats["blocked"] += 1
                            shot(page, f"{mid}_{pid}_q{qi}_passB_lost.png")
                            adv = advance_after_answer(page)
                            row["advanceState"] = adv
                            if adv != "ok":
                                break
                            passB_rows.append(row)
                            continue
                        row["correctUsed"] = q["o"]["en"][res["target"]]
                        row["observedCorrectFeedback"] = res["feedbackBody"] or res["feedback"]
                        row["cardCls"] = res["cardCls"]
                        row["optClasses"] = res.get("optClasses")
                        row["accepted"] = "card--correct" in (res["cardCls"] or "")
                        if row["accepted"]:
                            passB_correct += 1
                        row["correctFeedbackMatch"] = row["expectedCorrectFeedback"] in row["observedCorrectFeedback"] if row["expectedCorrectFeedback"] else True
                        # stale wrong styling check
                        row["staleWrongStyling"] = any("option-btn--wrong" in c for c in res.get("optClasses", []))
                    else:
                        res = answer_cloze(page, q, want_correct=True)
                        row["correctUsed"] = "|".join(res["picked"])
                        row["observedCorrectFeedback"] = res["feedbackBody"] or res["feedback"]
                        row["cardCls"] = res["cardCls"]
                        row["blankClasses"] = res.get("blankClasses")
                        row["accepted"] = "card--correct" in (res["cardCls"] or "")
                        if row["accepted"]:
                            passB_correct += 1
                        row["correctFeedbackMatch"] = row["expectedCorrectFeedback"] in row["observedCorrectFeedback"]
                        row["staleWrongStyling"] = any("bb-mem-blank--wrong" in c for c in res.get("blankClasses", []))
                    passB_rows.append(row)
                    # advance
                    adv = advance_after_answer(page)
                    row["advanceState"] = adv
                    is_last = (qi == len(qs) - 1)
                    if adv == "completion":
                        if not is_last:
                            row["advanceIssue"] = f"premature completion after question {qi+1} of {len(qs)}"
                            stats["failures"] += 1
                            shot(page, f"{mid}_{pid}_q{qi}_passB_advance_{adv}.png")
                        break
                    elif adv != "ok":
                        row["advanceIssue"] = f"unexpected state after Next: {adv}"
                        stats["failures"] += 1
                        shot(page, f"{mid}_{pid}_q{qi}_passB_advance_{adv}.png")
                        break
                    elif not is_last:
                        idx2, _ = current_question_count(page)
                        if idx2 not in (None, qi + 2):
                            row["advanceIssue"] = f"expected question {qi+2}, saw {idx2}"
                            stats["failures"] += 1
                # completion after pass B
                expectedB = round((passB_correct / len(qs)) * 100) if len(qs) else 0
                if not page.locator(".completion-screen").count():
                    recovered = recover_to_learning_path(page)
                    ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                                "pass": "B", "status": "failed",
                                "defectId": "D7-mc-crash-blank-page",
                                "attemptScoreExpected": expectedB,
                                "recovered": recovered})
                    stats["failures"] += 1
                    for r in passB_rows:
                        ledger_row(r)
                    if recovered:
                        open_module(page, mid)
                    continue
                compB = capture_completion(page)
                expectedDisplayB = max(prevBest, expectedB)
                ledger_row({"kind": "phase", "module": mid, "phase": pid, "run": run_id,
                            "pass": "B", "attemptScoreExpected": expectedB,
                            "attemptScoreObserved": compB["score"],
                            "displayScoreExpected": expectedDisplayB,
                            "prevBest": prevBest, "completion": compB,
                            "status": "info"})
                for r in passB_rows:
                    r["completionB"] = compB["score"]
                    ledger_row(r)

                # error log check after pass B (errors for this phase should be removed)
                stB = read_user_state(page)
                errsB = [e for e in stB["errorLog"] if e["phaseId"] == pid] if stB else []
                ledger_row({"kind": "errorlog-check", "module": mid, "phase": pid, "pass": "B",
                            "run": run_id, "entriesForPhase": len(errsB), "entries": errsB})

                # progress state checks
                stP = read_user_state(page)
                pp = next((p for p in stP["progress"] if p["phaseId"] == pid), None)
                ledger_row({"kind": "progress", "module": mid, "phase": pid, "run": run_id,
                            "phaseProgress": pp, "totalProgress": len(stP["progress"]),
                            "errorLogTotal": len(stP["errorLog"])})

                # phase console errors
                if len(console_errors) > phase_console_before:
                    ledger_row({"kind": "console-errors", "module": mid, "phase": pid, "run": run_id,
                                "errors": console_errors[phase_console_before:]})

                # advance to next phase: click Next Phase when available, else Home
                order_idx = order.index(pid)
                next_phase_id = order[order_idx + 1] if order_idx + 1 < len(order) else None
                next_phase_empty = next_phase_id and len(PHASES[next_phase_id]["q"]) == 0
                if next_phase_empty:
                    ledger_row({"kind": "empty-phase-in-lock-chain", "module": mid, "phase": pid,
                                "nextPhase": next_phase_id, "run": run_id,
                                "issue": "next-phase-in-order-has-zero-questions"})
                    click_completion_button(page, "Home")
                    page.wait_for_selector(".lp__card", timeout=8000)
                    open_module(page, mid)
                elif page.locator(".completion-actions button:has-text('Next Phase')").count():
                    click_completion_button(page, "Next Phase")
                    page.wait_for_selector(".lesson-screen", timeout=8000)
                else:
                    click_completion_button(page, "Home")
                    page.wait_for_selector(".lp__card", timeout=8000)
                    # open module again for next phase
                    open_module(page, mid)
                # end phase loop

            # module done — record module progress from state
            stM = read_user_state(page)
            mod_prog = stM["progress"]
            ledger_row({"kind": "module-done", "module": mid, "run": run_id,
                        "progressEntries": mod_prog})

        # ── RELOAD PERSISTENCE CHECK ──
        log("reload persistence check...")
        page.wait_for_timeout(3500)  # let debounced cloud sync flush
        page.reload()
        page.wait_for_selector(".lp__card", timeout=20000)
        banner = page.locator(".lp__banner-stats").inner_text()
        stReload = read_user_state(page)
        ledger_row({"kind": "persistence", "run": run_id, "check": "reload",
                    "banner": banner, "progressCount": len(stReload["progress"]),
                    "errorLogCount": len(stReload["errorLog"])})
        log(f"after reload: banner='{banner}' progress={len(stReload['progress'])} errors={len(stReload['errorLog'])}")

        # ── LOGOUT / LOGIN PERSISTENCE CHECK ──
        log("logout/login persistence check...")
        page.locator(".header-btn--profile").click()
        page.wait_for_timeout(300)
        page.locator(".dropdown-option:has-text('Log Out')").click()
        page.wait_for_selector(".hero-cta", timeout=10000)
        # re-login
        page.click(".hero-cta")
        page.wait_for_selector('input[type="email"]', timeout=10000)
        page.fill('input[type="email"]', EMAIL)
        page.fill('input[type="password"]', PASS)
        page.click('button:has-text("Continue")')
        page.wait_for_selector(".lp__card", timeout=20000)
        banner2 = page.locator(".lp__banner-stats").inner_text()
        stRelogin = read_user_state(page)
        ledger_row({"kind": "persistence", "run": run_id, "check": "logout-login",
                    "banner": banner2, "progressCount": len(stRelogin["progress"]),
                    "errorLogCount": len(stRelogin["errorLog"])})
        log(f"after relogin: banner='{banner2}' progress={len(stRelogin['progress'])} errors={len(stRelogin['errorLog'])}")

        browser.close()

    # summary
    elapsed = time.time() - start
    summary = {"run": run_id, "elapsedSec": round(elapsed, 1), "stats": stats,
               "consoleErrorsTotal": len(console_errors), "consoleErrorsSample": console_errors[:30],
               "defectsCandidate": defects}
    with open(os.path.join(OUT, "ledger", "sweep-summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    log(f"SWEEP DONE in {round(elapsed,1)}s: {json.dumps(stats)}")
    log(f"console errors: {len(console_errors)}; candidate defects: {len(defects)}")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
