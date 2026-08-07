# Gramlingo Repository Rules (unified 2026-08-07)

## One repo, one folder, two branches

| Role | Branch | Purpose |
|---|---|---|
| **SOURCE** | `v4` | React+TS+Vite source. Edit here. Build here. |
| **DEPLOY** | `v2-restore` | GitHub Pages legacy builder. `index.html` + `assets/` only. |

Both in `C:\Users\hunin\projects\gramlingo` — single folder.

## BRANCH FREEZE (locked 2026-08-07)

**NEVER create a new branch.** Only `v4` and `v2-restore` exist. Do NOT branch for features, experiments, fixes, or "just in case." If Lareesa wants a new branch, she will explicitly say "create a new branch."

## Build + deploy workflow

1. `git checkout v4` — ensure you're on source
2. `npm run build` — tsc 0 errors, vite builds to dist/
3. `git checkout v2-restore` — switch to deploy
4. `rm assets/index-*.{js,css}` — clean old bundle
5. `cp -r dist/assets dist/data dist/favicon.svg dist/icons.svg dist/index.html dist/manifest.json .`
6. `git add index.html assets/` + `git add -u`; commit; push
7. `git checkout v4` — return to source
8. Pages legacy builder takes 5–15 min. Verify live via `curl -s https://lareesahu.github.io/gramlingo/ | grep -o 'index-...'`

## Data rules (CRITICAL)

- `public/data/game-data.json` is the ONLY dataset.
- `name`/`q`/`o`/`t`/`ex` fields are DICTs: `{en, zh, es}`. Never treat as strings.
- `ex` = explanation arrays, one per option. `t` = tip string.
- **Do NOT bulk-rewrite the dataset without: (1) backup, (2) written plan in repo, (3) Lareesa's approval.**

## Repository safety

- Never init a fresh git repo (destroys history).
- Never force-push v2-restore (history must stay linear).
- Never commit `game-data.json` edits on the deploy branch.
- Commit after each verified milestone on v4; deploy commits happen on v2-restore.
- Shell: POSIX paths in bash/MSYS, native paths in tools.
