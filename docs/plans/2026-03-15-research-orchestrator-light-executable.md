# Research Orchestrator Light Executable Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add lightweight executable scaffolding so the `research-orchestrator` skill can create research workspaces, memory files, and output templates locally.

**Architecture:** Keep the skill workflow in `SKILL.md` and `references/`, then add a small Python CLI in `scripts/` that generates a deterministic run folder under `runs/<topic-slug>/`. Use standard-library-only Python and `unittest` so the repo stays portable and self-contained.

**Tech Stack:** Markdown, Python 3 standard library, unittest

---

### Task 1: Add a failing scaffold test

**Files:**
- Create: `C:\Users\EGO\research-orchestrator\tests\test_init_research_run.py`

**Step 1: Write the failing test**

Add a `unittest` case that imports or executes the future scaffolding script and asserts that a generated run contains:
- `brief.md`
- `experiment.md`
- `results.md`
- `paper-outline.md`
- `memory/ideation.md`
- `memory/experimentation.md`

**Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -v`
Expected: FAIL because the scaffolding module or script does not exist yet.

### Task 2: Implement the research run scaffolder

**Files:**
- Create: `C:\Users\EGO\research-orchestrator\scripts\init_research_run.py`

**Step 1: Write minimal implementation**

Implement:
- a `slugify()` helper
- a `build_files()` helper returning the default output files
- a `create_run()` function that creates `runs/<topic-slug>/`
- a CLI accepting `topic`, optional `--root`, and optional `--force`

**Step 2: Run tests to verify they pass**

Run: `python -m unittest discover -s tests -v`
Expected: PASS

### Task 3: Wire the skill documentation to the executable path

**Files:**
- Modify: `C:\Users\EGO\research-orchestrator\SKILL.md`
- Modify: `C:\Users\EGO\research-orchestrator\README.md`
- Create: `C:\Users\EGO\research-orchestrator\references\execution.md`

**Step 1: Update SKILL.md**

Add:
- when to use the scaffolding script
- the exact command
- where generated output appears

**Step 2: Update README.md**

Add:
- executable features
- usage examples
- install and local activation steps

**Step 3: Add execution reference**

Document:
- generated directory tree
- expected files
- safe overwrite behavior

### Task 4: Install and verify locally

**Files:**
- Modify: `C:\Users\EGO\.codex\skills\research-orchestrator\...` (copy from repo)

**Step 1: Install**

Copy the completed repo folder into the local Codex skills directory.

**Step 2: Verify**

Run:
- `python -m unittest discover -s tests -v`
- `python C:\Users\EGO\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\EGO\research-orchestrator`
- `python C:\Users\EGO\research-orchestrator\scripts\init_research_run.py "demo topic" --root C:\Users\EGO\research-orchestrator`

Expected:
- tests pass
- skill validates
- a run folder is generated with the expected files
