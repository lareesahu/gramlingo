"""Translate entries 0-304 from gramlingo zh-batch files to Chinese."""
import json
import os
import re
import sys
import time
import urllib.request

BATCH_FILES = [f"C:/Users/hunin/projects/gramlingo-v3/zh-batch-{i}.json" for i in range(7)]
OUTPUT = "C:/Users/hunin/projects/gramlingo-v3/zh-translate-output.json"

def api_key():
    # Try multiple locations
    locations = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "hermes", ".env"),
        os.path.join(os.environ.get("APPDATA", ""), "hermes", ".env"),
        "C:/Users/hunin/AppData/Local/hermes/.env",
    ]
    for loc in locations:
        try:
            with open(loc, encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if line.startswith("DEEPSEEK_API_KEY="):
                        key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if key:
                            print(f"Found key at {loc} (length={len(key)})")
                            return key
        except FileNotFoundError:
            continue
    raise SystemExit("no DEEPSEEK_API_KEY found")

def call_deepseek(messages, key, model="deepseek-chat"):
    body = json.dumps({"model": model, "messages": messages, "temperature": 0.2}).encode()
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                out = json.loads(resp.read().decode())
            return out["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else ""
            print(f"  HTTP {e.code}: {body[:200]}")
            if e.code == 401 and attempt < 3:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except Exception as exc:
            if attempt == 3:
                raise
            print(f"  Retry {attempt+1}: {exc}")
            time.sleep(5 * (attempt + 1))

def main():
    key = api_key()
    
    # Load all entries
    all_entries = []
    for bf in BATCH_FILES:
        with open(bf, "r", encoding="utf-8") as f:
            all_entries.extend(json.load(f))
    
    print(f"Loaded {len(all_entries)} total entries")
    
    # Take entries 0-304
    target = all_entries[:305]
    print(f"Translating {len(target)} entries (0-304)")
    
    # Load existing output if any
    results = {}
    if os.path.exists(OUTPUT):
        with open(OUTPUT, "r", encoding="utf-8") as f:
            results = json.load(f)
        print(f"Resuming: {len(results)} already translated")
    
    # Process in batches
    BATCH_SIZE = 15
    total_batches = (len(target) + BATCH_SIZE - 1) // BATCH_SIZE
    
    for batch_idx in range(total_batches):
        start = batch_idx * BATCH_SIZE
        end = min(start + BATCH_SIZE, len(target))
        batch = target[start:end]
        
        # Build items only for untranslated entries
        items = []
        for e in batch:
            key = f"{e['phase']}:{e['question']}:{e['option']}"
            if key in results:
                continue
            is_correct = e['options'][e['option']] == e['answer']
            items.append({
                "key": key,
                "en": e['en'],
                "is_correct": is_correct,
                "q_text": e.get('q_text', ''),
                "answer": e.get('answer', ''),
                "option_text": e['options'][e['option']],
                "all_options": e.get('options', [])
            })
        
        if not items:
            print(f"Batch {batch_idx+1}/{total_batches}: already done, skipping")
            continue
        
        sys_prompt = """You are translating English grammar explanations into Chinese for an educational app (GramLingo). 

RULES:
1. For CORRECT answers (is_correct=true): start with '正确！' then provide the Chinese explanation.
2. For WRONG answers: explain concisely why the option is wrong in Chinese.
3. Do NOT add '选项X' prefix — just the explanation text.
4. Use accurate Chinese grammar terms: 一般现在时, 过去完成时, 虚拟语气, 定语从句, 现在完成时, 被动语态, 条件句, 情态动词, 不定式, 动名词, 介词, 连词, 状语从句, 主语, 谓语, 宾语, 补语, etc.
5. Keep the explanation educational and clear.
6. The q_text provides context about what grammar point is being tested.
7. Respond ONLY with a valid JSON object mapping key -> Chinese string. No markdown code blocks.

Example input:
[{"key": "12:0:0", "en": "Base form without -s does not match she.", "is_correct": false, "q_text": "Present simple: he/she/it + verb-s.", "answer": "goes", "option_text": "go", "all_options": ["go", "goes", "going", "is go"]}]

Example output:
{"12:0:0": "动词原形没有加 -s，与主语 she 不匹配。在一般现在时中，he/she/it 作主语时动词需要加 -s。"}"""

        user_payload = json.dumps(items, ensure_ascii=False)
        
        print(f"Batch {batch_idx+1}/{total_batches}: {len(items)} items to translate...")
        
        content = call_deepseek(
            [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_payload},
            ],
            key,
        )
        
        # Extract JSON from response - find outermost { }
        content = content.strip()
        # Remove markdown code fences if present
        content = re.sub(r'^```(?:json)?\s*\n?', '', content)
        content = re.sub(r'\n?```\s*$', '', content)
        
        m = re.search(r'\{.*\}', content, re.S)
        if not m:
            print(f"  BAD RESPONSE (no JSON found): {content[:300]}")
            continue
        
        try:
            batch_results = json.loads(m.group(0))
        except json.JSONDecodeError as exc:
            print(f"  JSON FAIL: {exc} | {content[:300]}")
            continue
        
        # Merge
        results.update(batch_results)
        
        # Save intermediate
        with open(OUTPUT, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"  Done: {len(batch_results)} translated, {len(results)} total saved to {OUTPUT}")
        time.sleep(0.5)
    
    print(f"\nFinal: {len(results)} translations saved to {OUTPUT}")

if __name__ == "__main__":
    main()
