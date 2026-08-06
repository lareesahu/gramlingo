# Gramlingo Repository Rules

## Canonical repository

The only writable Gramlingo repository is:

C:\Users\hunin\projects\gramlingo

Do not search for, edit, copy from, restore from, compare against, or run builds inside any other folder whose name contains "gramlingo" unless the user explicitly requests recovery work.

## Required startup checks

Before editing anything, run:

1. Get-Location
2. git status
3. git branch --show-current
4. git rev-parse HEAD
5. 
pm run build

Stop immediately if:

- the current path is not C:\Users\hunin\projects\gramlingo
- Git is in detached HEAD state
- the branch is not the designated working branch
- package.json is missing
- the baseline build fails before any modifications

Do not repair a missing file until confirming that it belongs to this repository and this version.

## Shell rules

Use Windows PowerShell commands only.

Do not use:

- /c/Users/... paths
- sync
- Unix cp, m, grep, or sed
- mixed PowerShell and Git Bash syntax

## Repository safety

- Never create another Gramlingo repository or recovery folder.
- Never clone Gramlingo inside another Gramlingo folder.
- Never copy dist into any directory inside this repository.
- Never use git reset --hard, force-push, delete branches, or overwrite main.
- Make one named branch for the task.
- Commit after each verified milestone.
- Do not edit generated files in dist.
- Do not treat a successful build as proof that the product behavior is correct.

## Scope discipline

Before implementation, identify:

- the exact files to edit
- the approved baseline behavior
- the acceptance tests
- what must remain unchanged

After each meaningful change, run the smallest relevant test.
Before completion, run the full build and relevant Playwright tests.

If three consecutive repair attempts fail for the same issue, stop editing. Report:

- the original error
- the attempted fixes
- current Git diff
- current branch and commit
- the likely root cause

Do not begin a rebuild from scratch unless the user explicitly requests one.
