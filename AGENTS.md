# Gramlingo Repository Rules (corrected 2026-08-07)

## Canonical source vs deploy repo

| Role | Path | Repo/branch | Purpose |
|---|---|---|---|
| **SOURCE (canonical, writable)** | `C:\Users\hunin\projects\gramlingo-v3` | its own git (remote `lareesahu/gramlingo`) | React+TS+Vite source. Edit here. Build here. |
| **DEPLOY (build output only)** | `C:\Users\hunin\projects\gramlingo` | git, branch `v2-restore` (Pages) + `gh-pages` | Contains ONLY `index.html` + `assets/` from dist. Never edit source here. |

## Build + deploy workflow (verified 2026-08-06/07 — see PROVEN_WORKFLOWS.md)

1. Ensure `gramlingo-v3/.env.local` has `VITE_SUPABASE_URL` + `VITE_SUPABASE_PUBLISHABLE_KEY` (copy from `gramlingo/.env.local` if missing).
2. `npm run build` in gramlingo-v3 (tsc 0 errors).
3. In deploy repo: `rm assets/index-*.{js,css}`; copy `dist/index.html` + `dist/assets/index-*.{js,css}`.
4. `git add index.html assets/` + `git add -u`; commit; `git push origin v2-restore` AND `git push origin HEAD:gh-pages --force`.
5. Pages legacy builder takes 5–15 min. Verify live bundle via `curl -s https://lareesahu.github.io/gramlingo/ | grep -o 'index-...'`.

## Data rules (CRITICAL — do not violate)

- `public/data/game-data.json` is the ONLY dataset. 282 questions, 92 phases.
- The `name`/`q`/`o`/`t`/`ex` fields are DICTs: `{en, zh, es}`. Never treat them as strings.
- `ex` = explanation arrays, one string PER OPTION. `t` = tip string.
- **Do NOT bulk-rewrite the dataset without: (1) a backup copy, (2) a written plan in this repo, (3) Lareesa's approval.** LLM bulk translation of game-data.json is a rejected approach (2026-08-07) — the data is the curriculum, not a scratch file.

## Shell rules

- This repo is on Windows; prefer PowerShell-native tooling but Hermes terminal uses bash/MSYS. Use POSIX paths (`/c/Users/...`) in terminal, native paths in tools.

## Repository safety

- Never init a fresh git repo here (would destroy history).
- Never force-push v2-restore (history must stay linear). gh-pages force-push is the deploy mechanism.
- Never commit `game-data.json` edits in the deploy repo.
- Commit after each verified milestone in the SOURCE repo; deploy commits happen in the DEPLOY repo.
