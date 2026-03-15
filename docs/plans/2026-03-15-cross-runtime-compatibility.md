# Research Orchestrator Cross Runtime Compatibility Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make `research-orchestrator` portable across Claude Code, Codex, and OpenClaw/Agents with clear install instructions and a deterministic install script.

**Architecture:** Keep one shared skill package and add a small Python installer that copies the repo into the correct runtime-specific skills directory. Put runtime-specific notes in a reference file and keep `SKILL.md` runtime-agnostic.

**Tech Stack:** Markdown, Python 3 standard library, unittest

---

### Task 1: Add a failing runtime install test

**Files:**
- Create: `C:\Users\EGO\research-orchestrator\tests\test_install_skill.py`

**Step 1: Write the failing test**

Add a `unittest` case that:
- loads `scripts/install_skill.py`
- calls an install function with a repo source path
- targets `codex`, `claude`, and `agents`
- asserts the destination path matches the runtime conventions
- asserts `SKILL.md` exists at the installed destination

**Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -v`
Expected: FAIL because `install_skill.py` does not exist yet.

### Task 2: Implement the runtime installer

**Files:**
- Create: `C:\Users\EGO\research-orchestrator\scripts\install_skill.py`

**Step 1: Write minimal implementation**

Implement:
- a runtime-to-directory mapping for `codex`, `claude`, and `agents`
- a function that resolves the install destination
- a copy routine with safe overwrite support
- a CLI with `--runtime`, `--home`, `--source`, and `--force`

**Step 2: Run tests to verify they pass**

Run: `python -m unittest discover -s tests -v`
Expected: PASS

### Task 3: Document compatibility

**Files:**
- Modify: `C:\Users\EGO\research-orchestrator\README.md`
- Modify: `C:\Users\EGO\research-orchestrator\SKILL.md`
- Create: `C:\Users\EGO\research-orchestrator\references\runtime-compatibility.md`

**Step 1: Update README**

Add:
- install instructions for Claude Code, Codex, and OpenClaw/Agents
- a single install script example per runtime
- runtime-specific invocation notes where relevant

**Step 2: Update SKILL.md**

Link to the runtime compatibility reference.

**Step 3: Add reference**

Document:
- supported runtimes
- install paths
- which files are required versus optional metadata

### Task 4: Verify source package behavior

**Files:**
- Verify only

**Step 1: Run full tests**

Run: `python -m unittest discover -s tests -v`
Expected: PASS

**Step 2: Validate the skill**

Run: `python C:\Users\EGO\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\EGO\research-orchestrator`
Expected: `Skill is valid!`

**Step 3: Verify install script behavior**

Run:
- `python C:\Users\EGO\research-orchestrator\scripts\install_skill.py --runtime codex --home C:\Users\EGO\research-orchestrator\.tmp-tests\compat-root --force`
- `python C:\Users\EGO\research-orchestrator\scripts\install_skill.py --runtime claude --home C:\Users\EGO\research-orchestrator\.tmp-tests\compat-root --force`
- `python C:\Users\EGO\research-orchestrator\scripts\install_skill.py --runtime agents --home C:\Users\EGO\research-orchestrator\.tmp-tests\compat-root --force`

Expected:
- `compat-root\.codex\skills\research-orchestrator\SKILL.md` exists
- `compat-root\.claude\skills\research-orchestrator\SKILL.md` exists
- `compat-root\.agents\skills\research-orchestrator\SKILL.md` exists
