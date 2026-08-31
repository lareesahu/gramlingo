# -*- coding: utf-8 -*-
"""Render GramLingo textbook-style lesson decks (12 modules) + index hub."""
import json, os, re, html, glob, importlib.util, sys

BASE = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE, "content")
DATA = json.load(open(os.path.join(BASE, "..", "..", "public", "data", "game-data.json"), encoding="utf-8"))

def load_lesson(path):
    spec = importlib.util.spec_from_file_location("m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.LESSON

LESSONS = []
for f in sorted(glob.glob(os.path.join(CONTENT_DIR, "m*.py"))):
    LESSONS.append(load_lesson(f))

# order by game-data module sort
sort_map = {m["id"]: m["sort"] for m in DATA["modules"]}
LESSONS.sort(key=lambda l: sort_map.get(l["id"], 99))

# Landing-page card metadata (matches gramlingo.online worlds carousel exactly)
CARD_META = {
    "clauses": ("Relative Clauses", "who · which · that"),
    "prepositions": ("Prepositions", "in · on · at"),
    "tenses": ("Verb Tenses", "past · present · future"),
    "conditionals": ("Conditionals", "if · would · could"),
    "passive": ("Passive Voice", "is done · was made"),
    "reported": ("Reported Speech", "she said that…"),
    "modals": ("Modals", "can · must · might"),
    "determiners": ("Articles & Determiners", "a · an · the"),
    "conjunctions": ("Conjunctions", "and · but · because"),
    "verb_patterns": ("Verb Patterns", "enjoy doing · decide to do"),
    "sentence_structure": ("Sentence Structure", "subject · verb · object"),
    "advanced": ("Advanced Expressions", "idioms that impress"),
}

def esc(s):
    return html.escape(str(s), quote=False).replace("\n", "<br>")

def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()

def pick_questions(module_id, n=3):
    phases = sorted([p for p in DATA["phases"] if p.get("module") == module_id], key=lambda p: p.get("sort", 0))
    qs = [q for p in phases for q in p.get("q", []) if q.get("o", {}).get("en")]
    if not qs:
        return []
    idxs = sorted(set([0, len(qs) // 2, len(qs) - 1]))
    picked = []
    for i in idxs:
        q = qs[i]
        opts = q.get("o", {}).get("en", [])
        ans = q.get("a")
        if isinstance(ans, list):
            ans = ans[0] if ans else None
        ans_i = None
        if ans is not None:
            for j, o in enumerate(opts):
                if norm(o) == norm(ans):
                    ans_i = j
                    break
        picked.append({"q": q.get("q", {}).get("en", ""), "opts": opts, "ans": ans_i, "ans_txt": ans})
        if len(picked) >= n:
            break
    return picked

CSS = r"""
:root{
  --ink:#1b2420; --ink2:#5b6b62; --line:#e6ebe7; --bg:#fbfcfa; --card:#fff;
  --accent:#6aa72e; --accent-soft:#eef6e4; --warn:#b3261e; --warn-soft:#fdf0ee;
  --radius:16px; --shadow:0 1px 2px rgba(20,40,20,.05),0 8px 24px rgba(20,40,20,.06);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans CJK SC",sans-serif;
  background:var(--bg);color:var(--ink);line-height:1.75;-webkit-font-smoothing:antialiased;
}
.wrap{max-width:1000px;margin:0 auto;padding:0 clamp(14px,4vw,28px)}

/* cover */
.cover{
  background:linear-gradient(135deg,var(--accent),color-mix(in srgb,var(--accent) 55%,#000 18%));
  color:#fff;border-radius:0 0 28px 28px;padding:clamp(36px,7vw,72px) 0 clamp(28px,5vw,48px);
  position:relative;overflow:hidden;
}
.cover::after{content:"";position:absolute;right:-80px;top:-80px;width:min(260px,38vw);height:min(260px,38vw);border-radius:50%;background:rgba(255,255,255,.10)}
.kicker{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;opacity:.85;margin-bottom:14px;font-weight:600}
.cover h1{font-size:clamp(26px,5vw,40px);line-height:1.25;font-weight:800;letter-spacing:-.01em}
.cover h1 .zh{display:block;font-size:.62em;font-weight:600;opacity:.9;margin-top:6px}
.cover .desc{margin-top:16px;max-width:640px;font-size:clamp(14px,2.4vw,16.5px);opacity:.95}
.cover .desc .zh{display:block;opacity:.82;font-size:.95em;margin-top:4px}
.objectives{margin-top:24px;display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.objectives div{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);border-radius:12px;padding:10px 14px;font-size:13.5px;backdrop-filter:blur(4px)}
.objectives b{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;opacity:.75;margin-bottom:2px}

/* toc */
.toc{position:sticky;top:0;z-index:50;background:rgba(251,252,250,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.toc .wrap{display:flex;gap:8px;overflow-x:auto;padding-top:10px;padding-bottom:10px;scrollbar-width:none}
.toc .wrap::-webkit-scrollbar{display:none}
.toc a{white-space:nowrap;font-size:12.5px;font-weight:600;color:var(--ink2);text-decoration:none;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:5px 13px;transition:.15s}
.toc a:hover{border-color:var(--accent);color:var(--accent)}
.toc a.on{background:var(--accent);border-color:var(--accent);color:#fff}

/* sections */
main{padding:clamp(24px,5vw,44px) 0 20px}
.phase{scroll-margin-top:64px;margin-bottom:clamp(28px,5vw,44px)}
.phase-head{display:flex;align-items:baseline;gap:10px;margin-bottom:14px;border-bottom:2px solid var(--line);padding-bottom:10px}
.phase-num{flex:none;background:var(--accent);color:#fff;font-weight:800;font-size:12.5px;border-radius:8px;padding:3px 9px;letter-spacing:.04em}
.phase-head h2{font-size:clamp(19px,3.2vw,24px);font-weight:800}
.phase-head .zh{font-size:clamp(13px,2vw,15px);color:var(--ink2);font-weight:600}

.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:clamp(16px,3vw,24px);margin-bottom:14px}
.card h3{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:10px;display:flex;align-items:center;gap:8px}
.concept{font-size:clamp(14.5px,2.6vw,16px)}
.concept .zh{display:block;color:var(--ink2);margin-top:6px;font-size:.95em}

.rules{display:grid;gap:0}
.rule{display:grid;grid-template-columns:110px 1fr;gap:4px 14px;padding:11px 4px;border-bottom:1px dashed var(--line)}
.rule:last-child{border-bottom:0}
.rule b{grid-column:1;grid-row:1/3;font-size:12.5px;color:var(--accent);background:var(--accent-soft);align-self:start;border-radius:8px;padding:3px 10px;text-align:center}
.rule .en{font-size:14.5px}
.rule .zh{color:var(--ink2);font-size:13.5px}

.ex{border-left:3px solid var(--accent);padding:10px 14px;background:var(--accent-soft);border-radius:0 10px 10px 0;margin-bottom:8px}
.ex .en{font-weight:600;font-size:14.5px}
.ex .zh{color:var(--ink2);font-size:13.5px}

.mistakes{background:var(--warn-soft);border:1px solid #f3d3cf}
.mistakes h3{color:var(--warn)}
.mistake{padding:9px 12px;border-bottom:1px dashed #f0c9c4;font-size:13.8px}
.mistake:last-child{border-bottom:0}
.mistake .zh{display:block;color:#8a5a55;font-size:13px;margin-top:2px}

/* practice */
.practice .p-q{margin-bottom:12px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--card)}
.practice details summary{cursor:pointer;list-style:none;padding:14px 16px;display:flex;gap:10px;align-items:flex-start}
.practice details summary::-webkit-details-marker{display:none}
.practice details[open] summary{border-bottom:1px dashed var(--line)}
.practice .qnum{flex:none;background:var(--ink);color:#fff;font-size:11px;font-weight:700;border-radius:7px;padding:3px 8px;margin-top:3px}
.practice .qtext{font-size:14.5px;font-weight:600}
.practice .opts{padding:8px 16px 14px}
.practice .opt{display:block;width:100%;text-align:left;font:inherit;font-size:13.8px;padding:7px 10px;border-radius:8px;margin-top:6px;background:#f4f7f4;border:1px solid var(--line);cursor:pointer}
.practice .opt:focus-visible,.toc a:focus-visible,.nav-prev-next a:focus-visible,.toplink:focus-visible{outline:3px solid #1b2420;outline-offset:2px}
.practice .opt[aria-pressed="true"]{border-color:var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 25%,transparent)}
.practice .opt.right{background:#e8f5dc;border-color:#b7d992;font-weight:700}
.practice .opt.right::after{content:" ✓ correct";color:#1e7a34;font-size:12px;font-weight:700}
.practice .hint{padding:10px 16px;font-size:12.5px;color:var(--ink2);border-top:1px dashed var(--line);background:#fafcfa}

/* footer */
footer{border-top:1px solid var(--line);margin-top:20px;padding:26px 0 40px}
.nav-prev-next{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:22px}
.nav-prev-next a{flex:1;min-width:200px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 18px;text-decoration:none;color:var(--ink);box-shadow:var(--shadow);transition:.15s}
.nav-prev-next a:hover{border-color:var(--accent);transform:translateY(-1px)}
.nav-prev-next .dir{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2)}
.nav-prev-next .t{font-weight:700;font-size:14.5px;margin-top:2px}
.credit{font-size:12.5px;color:var(--ink2);text-align:center}
.credit a{color:var(--accent);text-decoration:none;font-weight:600}
.toplink{display:inline-block;margin-top:10px;font-size:12.5px;color:var(--accent);text-decoration:none;font-weight:600}

@media print{
  .toc,footer .nav-prev-next,.toplink{display:none}
  body{background:#fff}
  .cover{border-radius:0}
  .phase{page-break-inside:avoid}
}
@media (max-width:640px){
  .rule{grid-template-columns:1fr}
  .rule b{grid-row:auto;justify-self:start;margin-bottom:2px}
  .objectives{grid-template-columns:1fr}
}

/* GramLingo landing-page visual language */
@font-face{font-family:Baloo2;src:url('assets/fonts/baloo2-latin.woff2') format('woff2');font-weight:600 800;font-display:swap}
@font-face{font-family:DMSans;src:url('assets/fonts/dmsans-latin.woff2') format('woff2');font-weight:400 700;font-display:swap}
:root{--ink:#2d1b10;--ink2:#6f5b4d;--line:#e8d5c4;--bg:#fff5ee;--card:#fff;--accent:#ff8c42;--accent-soft:#fff0e5;--warn:#b94b4b;--warn-soft:#fff1ed;--radius:20px;--shadow:0 3px 0 rgba(45,27,16,.1),0 12px 28px rgba(117,70,40,.08);--ease-bounce:cubic-bezier(.34,1.56,.64,1)}
body{font-family:DMSans,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink)}
h1,h2,h3{font-family:Baloo2,DMSans,sans-serif}
.cover{background:linear-gradient(135deg,#ff8c42,#e86f35);color:var(--ink);border-radius:0 0 32px 32px}
.cover::after{right:clamp(18px,9vw,120px);top:28px;width:130px;height:130px;background:url('assets/gramlingo-logo.png') center/contain no-repeat;opacity:.95;transform:rotate(5deg)}
.cover::before{content:"";position:absolute;inset:auto -80px -130px auto;width:340px;height:340px;border-radius:50%;background:rgba(255,255,255,.2)}
.cover h1{font-size:clamp(30px,5vw,48px);line-height:1.1}
.objectives div{background:rgba(255,255,255,.55);border:2px solid rgba(45,27,16,.12);border-radius:14px;box-shadow:0 3px 0 rgba(45,27,16,.08)}
.toc{background:rgba(255,250,246,.94);border-color:var(--line)}
.toc a{border:2px solid var(--line)}
.toc a.on{background:var(--accent);border-color:var(--ink);color:var(--ink)}
.phase-num{background:var(--accent);color:var(--ink);border:2px solid var(--ink);border-radius:999px}
.card{border:2px solid var(--line);box-shadow:var(--shadow)}
.rule b{color:var(--ink);background:var(--accent-soft);border:1px solid var(--line);border-radius:999px}
.ex{border:1px solid #ffd2b2;border-left:5px solid var(--accent);background:var(--accent-soft);border-radius:0 12px 12px 0}
.practice .opt{background:#fffaf6;border:2px solid var(--line);border-radius:10px}
.practice .opt[aria-pressed="true"]{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,140,66,.22)}
.nav-prev-next a{border:2px solid var(--line)}
@media (max-width:640px){.cover::after{right:12px;top:20px;width:84px;height:84px;opacity:.7}}
.hub .cover{padding-bottom:clamp(34px,6vw,58px)}
.hub .cover h1{max-width:none}
.hub .cover .sub{max-width:680px;margin-top:14px}
.hub .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;padding:clamp(26px,5vw,48px) 0}
.hub .module-card{display:block;overflow:hidden;background:var(--card);border:2px solid var(--line);border-radius:20px;color:var(--ink);text-decoration:none;box-shadow:var(--shadow);transition:transform .15s,box-shadow .15s,border-color .15s}
.hub .module-card:hover{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 5px 0 rgba(45,27,16,.12),0 18px 34px rgba(117,70,40,.12)}
.hub .module-card img{display:block;width:100%;aspect-ratio:3/1.25;object-fit:cover}
.hub .module-card-body{padding:16px 18px 18px}
.hub .module-card-body .num{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:700}
.hub .module-card-body h2{font-size:20px;line-height:1.2;margin-top:6px}
.hub .module-card-body .zh{display:block;color:var(--ink2);font-size:15px;margin-top:3px}
.hub .module-card-body p{margin-top:9px;color:var(--ink2);font-size:13.5px}
.hub footer{border-top:1px solid var(--line);padding:24px 0 40px;text-align:center;color:var(--ink2);font-size:12.5px}
.hub footer a{color:var(--accent);font-weight:700;text-decoration:none}
.lesson-nav{height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 clamp(16px,4vw,32px);background:rgba(255,245,238,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:100}
.cover::after{display:none}
.lesson-nav{height:70px;padding:0 clamp(18px,5vw,52px);gap:18px}.lesson-brand img{width:126px}.lesson-nav-links{gap:4px;flex:1;justify-content:center}.lesson-nav-link{border:2px solid transparent;color:var(--ink);font-size:13px;padding:8px 13px}.lesson-nav-link:hover{border-color:var(--ink);background:#fff}.lesson-nav-link--active{border-color:var(--ink);background:var(--card)}.lesson-nav-link--cta{background:var(--accent);border-color:var(--ink);box-shadow:0 3px 0 var(--ink)}.lesson-nav-link--cta:hover{background:#ffb788}.lesson-language{display:flex;align-items:center;border:2px solid var(--ink);border-radius:999px;background:var(--card);overflow:hidden;font-size:12px;font-weight:700}.lesson-language span{padding:7px 9px}.lesson-language--active{background:var(--accent)}
.cover{background:radial-gradient(circle at 88% 20%,rgba(255,183,136,.35),transparent 28%),var(--bg);color:var(--ink);border:0}.cover .kicker{display:inline-block;border:2px solid var(--accent);border-radius:999px;padding:6px 12px;opacity:1;letter-spacing:.1em}.cover h1{color:var(--ink)}.cover .desc{color:var(--ink2)}.objectives div{background:var(--card);border:2px solid var(--ink);box-shadow:3px 3px 0 var(--ink)}.hub .cover{padding-top:clamp(34px,7vw,70px)}.hub-gramlin{position:absolute;right:clamp(24px,12vw,160px);bottom:-8px;width:150px;filter:drop-shadow(0 5px 0 rgba(45,27,16,.15));animation:lesson-float 4s ease-in-out infinite}.hub .cover .wrap{position:relative}.hub .cover h1{max-width:700px}.hub .cover .sub{max-width:680px}.hub .module-card{border:2px solid var(--ink);box-shadow:4px 4px 0 var(--ink)}.hub .module-card:hover{border-color:var(--ink);box-shadow:6px 7px 0 var(--ink);transform:translate(-2px,-4px)}
.lesson-brand{display:inline-flex;align-items:center;height:48px}.lesson-brand img{display:block;width:132px;height:auto}.lesson-nav-links{display:flex;align-items:center;gap:8px}.lesson-nav-link{color:var(--ink);font-size:13px;font-weight:600;padding:8px 12px;border-radius:999px;transition:background .15s,color .15s}.lesson-nav-link:hover,.lesson-nav-link--active{background:var(--accent-soft);color:var(--ink)}
.hub .cover{border-radius:0 0 32px 32px}.hub .cover::after{background:url('assets/gramlingo-logo.png') center/contain no-repeat}.hub .module-gallery-section{padding:clamp(40px,8vw,72px) 0}.hub .gallery-wrap{max-width:980px}.hub .module-gallery{gap:16px;padding:8px 4px 14px}.hub .module-card{width:260px;border-radius:10px;border:1px solid #f0e5d8;box-shadow:none}.hub .module-card:hover{transform:translateY(-4px);box-shadow:0 8px 24px rgba(45,27,16,.1)}.hub .module-card-cover{aspect-ratio:3/4}.hub .module-card-body h2{font-family:Baloo2,DMSans,sans-serif;font-size:16px;min-height:2.6em;margin:0 0 4px}.hub .module-card-body{padding:16px}.hub .module-card-body p{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.hub .module-card-body p.zh{margin-top:3px}.lesson-nav-link:focus-visible,.lesson-brand:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.cover .wrap{position:relative}
.cover-art{position:absolute;right:clamp(14px,5vw,64px);top:clamp(56px,9vw,96px);width:clamp(96px,15vw,190px);aspect-ratio:1/1;object-fit:cover;border:2px solid var(--ink);border-radius:16px;box-shadow:4px 4px 0 var(--ink);animation:lesson-float 4s ease-in-out infinite;pointer-events:none}
.cover h1{max-width:min(700px,calc(100% - 170px))}
.cover .desc{max-width:min(620px,calc(100% - 150px))}
.hub .module-gallery{display:flex;gap:16px;overflow-x:auto;padding:14px 6px 22px;scroll-snap-type:x mandatory}
.hub .module-gallery::-webkit-scrollbar{height:8px}
.hub .module-gallery::-webkit-scrollbar-thumb{background:var(--line);border-radius:99px}
.hub .gallery-wrap{max-width:980px;margin:0 auto;padding:0 24px}
.hub .module-gallery-hint{text-align:right;color:var(--ink2);font-size:12px;font-weight:800;margin:0 8px 2px}
.hub .module-card{flex:0 0 220px;background:var(--card);border:3px solid var(--ink);border-radius:18px;box-shadow:0 4px 0 rgba(45,27,16,.3);scroll-snap-align:start;text-decoration:none;color:var(--ink);overflow:hidden;transition:transform .25s cubic-bezier(.22,.61,.36,1),box-shadow .25s ease}
.hub .module-card:hover{transform:translateY(-5px)}
.hub .module-card-cover{aspect-ratio:1/1;overflow:hidden;border-radius:15px 15px 0 0}
.hub .module-card-cover img{width:100%;height:100%;object-fit:cover;aspect-ratio:auto}
.hub .module-card-body{padding:14px 16px}
.hub .module-card-body h2{font-family:Baloo2,DMSans,sans-serif;font-weight:800;font-size:15px;margin:0;min-height:0;line-height:1.25}
.hub .module-card-body p{font-size:12px;color:var(--ink2);margin-top:4px;display:block;-webkit-line-clamp:unset}
.hub .section-heading{font-size:clamp(22px,3.4vw,30px);line-height:1.15;margin:0 auto;max-width:980px;padding:0 24px}
.hub .section-sub{color:var(--ink2);margin:10px auto 0;max-width:980px;padding:0 24px;font-size:clamp(14px,2vw,16px)}
.hub-link{display:inline-block;margin-bottom:18px;font-size:13px;font-weight:700;color:var(--ink);background:var(--accent-soft);border:2px solid var(--ink);border-radius:999px;padding:8px 14px;text-decoration:none;box-shadow:0 2px 0 var(--ink);transition:background .15s,transform .15s}
.hub-link:hover{background:var(--accent)}
.hub-link:active{transform:translateY(2px);box-shadow:none}
.lesson-brand img{animation:logo-settle .6s var(--ease-bounce)}
@keyframes lesson-float{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(2deg)}}
@keyframes logo-settle{from{opacity:0;transform:translateY(-5px) scale(.96)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.cover-art,.lesson-brand img{animation:none}}
@media (max-width:900px){.lesson-nav-links{overflow-x:auto;justify-content:flex-end}.lesson-nav-link{white-space:nowrap}.lesson-language{display:none}.hub-gramlin{right:18px;width:110px}}
@media (max-width:640px){.lesson-nav{height:58px;padding:0 10px}.lesson-brand img{width:104px}.lesson-nav-links{gap:0}.lesson-nav-link{font-size:11px;padding:7px 8px}.lesson-nav-link:not(.lesson-nav-link--active):not(.lesson-nav-link--cta){display:none}.hub-gramlin{display:none}.cover h1{padding-right:0}}
@media (max-width:640px){.cover-art{display:none}.cover h1{max-width:none}.cover .desc{max-width:none}.hub .section-heading,.hub .section-sub{padding:0 18px}}
"""

def render_lesson(lesson, idx):
    pid = lesson["id"]
    phases_html = []
    for n, p in enumerate(lesson["phases"], 1):
        rules = "".join(
            f'<div class="rule"><b>{esc(r["label"])}</b><div class="en">{esc(r["en"])}</div><div class="zh">{esc(r["zh"])}</div></div>'
            for r in p.get("rules", []))
        exs = "".join(
            f'<div class="ex"><div class="en">{esc(e["en"])}</div><div class="zh">{esc(e["zh"])}</div></div>'
            for e in p.get("examples", []))
        mis = "".join(
            f'<div class="mistake">{esc(m["en"])}<span class="zh">{esc(m["zh"])}</span></div>'
            for m in p.get("mistakes", []))
        concept = p.get("concept", {})
        phases_html.append(f'''
      <section class="phase" id="{esc(p["id"])}">
        <div class="phase-head">
          <span class="phase-num">{idx:02d}-{n:02d}</span>
          <h2>{esc(p["name"])}</h2>
          <span class="zh">{esc(p["zh"])}</span>
        </div>
        <div class="card"><h3>💡 概念 Concept</h3><div class="concept">{esc(concept.get("en",""))}<span class="zh">{esc(concept.get("zh",""))}</span></div></div>
        <div class="card"><h3>📐 规则 Rules</h3><div class="rules">{rules}</div></div>
        <div class="card"><h3>✏️ 例句 Examples</h3>{exs}</div>
        <div class="card mistakes"><h3>⚠️ 常见错误 Common Mistakes</h3>{mis}</div>
      </section>''')

    # practice questions from the real bank
    practice = pick_questions(pid, 3)
    prac_html = ""
    if practice:
        items = []
        for i, q in enumerate(practice, 1):
            opts = "".join(
                f'<button type="button" class="opt{" right" if j == q["ans"] else ""}" aria-pressed="false">{esc(o)}</button>'
                for j, o in enumerate(q["opts"]))
            items.append(f'''
        <div class="p-q">
          <details>
            <summary><span class="qnum">Q{i}</span><span class="qtext">{esc(q["q"])}</span></summary>
            <div class="opts">{opts}</div>
            <div class="hint">Tap an option to reveal the answer · 点击选项查看答案</div>
          </details>
        </div>''')
        prac_html = f'''
      <section class="phase practice" id="practice">
        <div class="phase-head"><span class="phase-num">PR</span><h2>Practice 课堂练习</h2><span class="zh">from the GramLingo question bank</span></div>
        {''.join(items)}
      </section>'''

    toc = "".join(
        f'<a href="#{esc(p["id"])}">{n:02d}. {esc(p["name"])} / {esc(p["zh"])}</a>'
        for n, p in enumerate(lesson["phases"], 1)) + '<a href="#practice">Practice 练习</a>'

    prev_l = LESSONS[idx - 1] if idx > 0 else None
    next_l = LESSONS[idx + 1] if idx < len(LESSONS) - 1 else None
    nav = ""
    if prev_l:
        nav += f'<a href="{prev_l["id"]}.html"><div class="dir">← Previous 上一模块</div><div class="t">{esc(prev_l["name"])} {esc(prev_l["zh"])}</div></a>'
    else:
        nav += f'<a href="index.html"><div class="dir">← All lessons 返回目录</div><div class="t">All modules 全部模块</div></a>'
    if next_l:
        nav += f'<a href="{next_l["id"]}.html"><div class="dir">Next 下一模块 →</div><div class="t">{esc(next_l["name"])} {esc(next_l["zh"])}</div></a>'
    else:
        nav += f'<a href="index.html"><div class="dir">All lessons 返回目录 →</div><div class="t">All modules 全部模块</div></a>'

    objs = "".join(
        f'<div><b>Objective {n} 目标</b>{esc(o["en"])} · {esc(o["zh"])}</div>'
        for n, o in enumerate(lesson.get("objectives", []), 1))

    phases = "".join(phases_html)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Module {idx:02d} · {esc(lesson["name"])} — GramLingo Lessons / 语法课件</title>
<link rel="stylesheet" href="lessons.css">
</head>
<body data-accent="{esc(lesson.get("accent","#6aa72e"))}">
<nav class="lesson-nav" aria-label="Primary navigation">
  <a class="lesson-brand" href="index.html"><img src="assets/gramlingo-logo.webp" alt="GramLingo"></a>
  <div class="lesson-nav-links">
    <a class="lesson-nav-link" href="https://gramlingo.online/#sec-worlds">Worlds / 世界</a>
    <a class="lesson-nav-link" href="https://gramlingo.online/#sec-how">How it works / 如何学习</a>
    <a class="lesson-nav-link lesson-nav-link--active" href="index.html">Lessons / 课件</a>
    <a class="lesson-nav-link lesson-nav-link--cta" href="https://app.gramlingo.online">Start the quest / 开始冒险</a>
  </div>
</nav>
<header class="cover">
  <div class="wrap">
    <div class="kicker">GramLingo · Module {idx:02d} / 12 · 模块 {idx:02d} / 12</div>
    <h1>{esc(lesson.get("icon",""))} {esc(lesson["name"])}<span class="zh">{esc(lesson["zh"])}</span></h1>
    <img class="cover-art" src="assets/covers/cover-{esc(pid)}.webp" alt="" loading="eager">
    <div class="desc">{esc(lesson["desc"]["en"])}<span class="zh">{esc(lesson["desc"]["zh"])}</span></div>
    <div class="objectives">{objs}</div>
  </div>
</header>
<nav class="toc"><div class="wrap">{toc}</div></nav>
<main class="wrap">
  {phases}
  {prac_html}
</main>
<footer class="wrap">
  <a class="hub-link" href="index.html">← All lessons / 全部课件</a>
  <div class="nav-prev-next">{nav}</div>
  <div class="credit">GramLingo · Module {idx:02d} / 12 · Bilingual lessons EN + 中文 / 双语教案<br>Built with care by <a href="https://pulse-branding.com">Pulse Branding</a></div>
  <a class="toplink" href="#top">↑ Back to top 返回顶部</a>
</footer>
<script>
document.documentElement.style.setProperty('--accent', document.body.dataset.accent);
document.querySelectorAll('.practice .opt').forEach(function (button) {{
  button.addEventListener('click', function () {{
    var group = button.closest('.opts');
    group.querySelectorAll('.opt').forEach(function (option) {{
      option.setAttribute('aria-pressed', option === button ? 'true' : 'false');
    }});
  }});
}});
var links=[].slice.call(document.querySelectorAll('.toc a'));
var secs=links.map(function(a){{return document.querySelector(a.getAttribute('href'));}});
window.addEventListener('scroll',function(){{
  var y=window.scrollY+90,best=-1;
  secs.forEach(function(s,i){{if(s&&s.offsetTop<=y)best=i;}});
  links.forEach(function(a,i){{a.classList.toggle('on',i===best);}});
}},{{passive:true}});
</script>
</body>
</html>'''

def render_index():
    cards = []
    for i, l in enumerate(LESSONS, 1):
        phases_n = len(l["phases"])
        cards.append(f'''
      <a class="card" style="--accent:{esc(l.get("accent","#6aa72e"))}" href="{l["id"]}.html">
        <div class="num">Module {i:02d} · {phases_n} 节</div>
        <div class="t">{esc(l.get("icon",""))} {esc(l["name"])} <span class="zh">{esc(l["zh"])}</span></div>
        <div class="d">{esc(l["desc"]["en"])}</div>
        <div class="go">打开课件 →</div>
      </a>''')
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GramLingo 语法课件 · 全部 12 个模块</title>
<style>
:root{{--ink:#1b2420;--ink2:#5b6b62;--line:#e6ebe7;--bg:#fbfcfa;--card:#fff;--accent:#6aa72e;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans CJK SC",sans-serif;background:var(--bg);color:var(--ink);line-height:1.7}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 clamp(14px,4vw,28px)}}
.cover{{background:linear-gradient(135deg,#4e9f2f,#2f6b1e);color:#fff;border-radius:0 0 28px 28px;padding:clamp(36px,7vw,64px) 0 40px}}
.kicker{{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;opacity:.85;margin-bottom:14px;font-weight:600}}
.cover h1{{font-size:clamp(26px,5vw,40px);font-weight:800}}
.cover .sub{{margin-top:12px;max-width:620px;opacity:.92;font-size:clamp(14px,2.4vw,16px)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;padding:clamp(24px,5vw,40px) 0 24px}}
.card{{--a:var(--accent);display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;text-decoration:none;color:var(--ink);box-shadow:0 1px 2px rgba(20,40,20,.05),0 8px 24px rgba(20,40,20,.05);transition:.15s}}
.card:hover{{transform:translateY(-2px);border-color:var(--a);box-shadow:0 10px 30px rgba(20,40,20,.10)}}
.num{{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--a);font-weight:700;margin-bottom:8px}}
.t{{font-size:17px;font-weight:800;line-height:1.3}}
.t .zh{{color:var(--ink2);font-weight:600;font-size:14px;margin-left:4px}}
.d{{margin-top:8px;font-size:13px;color:var(--ink2);min-height:36px}}
.go{{margin-top:12px;font-size:12.5px;font-weight:700;color:var(--a)}}
footer{{border-top:1px solid var(--line);padding:24px 0 40px;font-size:12.5px;color:var(--ink2);text-align:center}}
footer a{{color:#4e9f2f;text-decoration:none;font-weight:600}}
</style>
</head>
<body>
<header class="cover">
  <div class="wrap">
    <div class="kicker">GramLingo · 12 Modules · 92 Lessons</div>
    <h1>语法课件目录</h1>
    <div class="sub">GramLingo 全部 12 个语法模块的教材式课件，双语（English + 中文），每节包含概念、规则、例句、常见错误与课堂练习。</div>
  </div>
</header>
<main class="wrap"><div class="grid">{''.join(cards)}</div></main>
<footer>Built with care by <a href="https://pulse-branding.com">Pulse Branding</a></footer>
</body>
</html>'''

def render_index():
    cards = []
    for l in LESSONS:
        name, keyword = CARD_META[l["id"]]
        cards.append(f'''\n      <a class="module-card" href="{l["id"]}.html">
        <div class="module-card-cover"><img src="assets/covers/cover-{l["id"]}.webp" width="512" height="512" alt="{esc(name)}" loading="lazy"></div>
        <div class="module-card-body">
          <h2>{esc(name)}</h2>
          <p>{esc(keyword)}</p>
        </div>
      </a>''')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Grammar lessons / 语法课件 · GramLingo</title>
<link rel="stylesheet" href="lessons.css">
</head>
<body class="hub">
<nav class="lesson-nav" aria-label="Primary navigation">
  <a class="lesson-brand" href="index.html"><img src="assets/gramlingo-logo.webp" alt="GramLingo"></a>
  <div class="lesson-nav-links">
    <a class="lesson-nav-link" href="https://gramlingo.online/#sec-worlds">Worlds / 世界</a>
    <a class="lesson-nav-link" href="https://gramlingo.online/#sec-how">How it works / 如何学习</a>
    <a class="lesson-nav-link lesson-nav-link--active" href="index.html">Lessons / 课件</a>
    <a class="lesson-nav-link lesson-nav-link--cta" href="https://app.gramlingo.online">Start the quest / 开始冒险</a>
  </div>
</nav>
<header class="cover">
  <div class="wrap">
    <div class="kicker">GramLingo · 12 modules · 92 lessons / 12 个模块 · 92 节课</div>
    <img class="hub-gramlin" src="assets/gramlin/peekaboo-gramlin.png" alt="" aria-hidden="true">
    <h1>Grammar lessons <span class="zh">语法课件目录</span></h1>
    <div class="sub">Build clear grammar intuition through short explanations, examples, common mistakes, and practice.<br><span class="zh">用简短讲解、例句、常见错误与练习，建立清晰的语法直觉。</span></div>
  </div>
</header>
<main><section class="module-gallery-section"><h2 class="section-heading">Choose a grammar world / 选择语法世界</h2><p class="section-sub">Short, visual lessons that make grammar stick. / 简短、直观，让语法真正留下来。</p><div class="gallery-wrap"><div class="module-gallery-hint">Drag to explore / 拖动浏览 →</div><div class="module-gallery">{''.join(cards)}</div></div></section></main>
<footer>Learn by playing at <a href="https://app.gramlingo.online">app.gramlingo.online</a> · Built with care by <a href="https://pulse-branding.com">Pulse Branding</a></footer>
</body>
</html>'''

def main():
    os.makedirs(BASE, exist_ok=True)
    with open(os.path.join(BASE, "lessons.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    for i, l in enumerate(LESSONS):
        out = os.path.join(BASE, l["id"] + ".html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(render_lesson(l, i + 1))
        print("wrote", os.path.basename(out))
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    print("wrote index.html")
    print("total lessons:", len(LESSONS))

if __name__ == "__main__":
    main()
