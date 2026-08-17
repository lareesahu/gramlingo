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
.practice .opt{font-size:13.8px;padding:7px 10px;border-radius:8px;margin-top:6px;background:#f4f7f4;border:1px solid var(--line)}
.practice .opt.right{background:#e8f5dc;border-color:#b7d992;font-weight:700}
.practice .opt.right::after{content:" ✓ 正确答案";color:var(--accent);font-size:12px;font-weight:700}
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
                f'<div class="opt{" right" if j == q["ans"] else ""}">{esc(o)}</div>'
                for j, o in enumerate(q["opts"]))
            items.append(f'''
        <div class="p-q">
          <details>
            <summary><span class="qnum">Q{i}</span><span class="qtext">{esc(q["q"])}</span></summary>
            <div class="opts">{opts}</div>
            <div class="hint">点击选项上方文字已展开答案 · 正确答案由 GramLingo 题库提供</div>
          </details>
        </div>''')
        prac_html = f'''
      <section class="phase practice" id="practice">
        <div class="phase-head"><span class="phase-num">PR</span><h2>课堂练习 Practice</h2><span class="zh">选自 GramLingo 题库</span></div>
        {''.join(items)}
      </section>'''

    toc = "".join(
        f'<a href="#{esc(p["id"])}">{n:02d}. {esc(p["name"])}</a>'
        for n, p in enumerate(lesson["phases"], 1)) + '<a href="#practice">练习</a>'

    prev_l = LESSONS[idx - 1] if idx > 0 else None
    next_l = LESSONS[idx + 1] if idx < len(LESSONS) - 1 else None
    nav = ""
    if prev_l:
        nav += f'<a href="{prev_l["id"]}.html"><div class="dir">← 上一模块</div><div class="t">{esc(prev_l["name"])} {esc(prev_l["zh"])}</div></a>'
    else:
        nav += f'<a href="index.html"><div class="dir">← 返回目录</div><div class="t">全部模块</div></a>'
    if next_l:
        nav += f'<a href="{next_l["id"]}.html"><div class="dir">下一模块 →</div><div class="t">{esc(next_l["name"])} {esc(next_l["zh"])}</div></a>'
    else:
        nav += f'<a href="index.html"><div class="dir">返回目录 →</div><div class="t">全部模块</div></a>'

    objs = "".join(
        f'<div><b>目标 {n}</b>{esc(o["en"])} · {esc(o["zh"])}</div>'
        for n, o in enumerate(lesson.get("objectives", []), 1))

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Module {idx:02d} · {esc(lesson["name"])} — GramLingo 语法课件</title>
<style>{CSS}</style>
</head>
<body data-accent="{esc(lesson.get("accent","#6aa72e"))}">
<header class="cover">
  <div class="wrap">
    <div class="kicker">GramLingo 语法课件 · Module {idx:02d} / 12</div>
    <h1>{esc(lesson.get("icon",""))} {esc(lesson["name"])}<span class="zh">{esc(lesson["zh"])}</span></h1>
    <div class="desc">{esc(lesson["desc"]["en"])}<span class="zh">{esc(lesson["desc"]["zh"])}</span></div>
    <div class="objectives">{objs}</div>
  </div>
</header>
<nav class="toc"><div class="wrap">{toc}</div></nav>
<main class="wrap">
  {phases_html}
  {prac_html}
</main>
<footer class="wrap">
  <div class="nav-prev-next">{nav}</div>
  <div class="credit">GramLingo 语法课件 · Module {idx:02d} / 12 · 双语教案 EN + 中文<br>Built with care by <a href="https://pulsebranding.com">Pulse Branding</a></div>
  <a class="toplink" href="#top">↑ 返回顶部</a>
</footer>
<script>
document.documentElement.style.setProperty('--accent', document.body.dataset.accent);
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
<footer>Built with care by <a href="https://pulsebranding.com">Pulse Branding</a></footer>
</body>
</html>'''

def main():
    os.makedirs(BASE, exist_ok=True)
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
