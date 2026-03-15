# Research Orchestrator Skill

`research-orchestrator` is a portable AI research workflow skill inspired by the EvoScientist project and paper.
It is designed to work across Claude Code, Codex, and OpenClaw-style `SKILL.md` runtimes from one shared repository.

## Quick Start

1. Install into your target runtime with `scripts/install_skill.py`
2. Invoke `$research-orchestrator`
3. Optionally scaffold a workspace with `scripts/init_research_run.py`

## Supported Runtimes

| Runtime | Skill Path | Install Command |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/research-orchestrator` | `python .\scripts\install_skill.py --runtime claude --force` |
| Codex | `~/.codex/skills/research-orchestrator` | `python .\scripts\install_skill.py --runtime codex --force` |
| OpenClaw/Agents | `~/.agents/skills/research-orchestrator` | `python .\scripts\install_skill.py --runtime agents --force` |

## What This Repo Is

This repo extracts the most reusable parts of EvoScientist:

- a research-oriented role system
- an end-to-end workflow for ideation, experimentation, analysis, and writing
- memory templates for preserving good and bad research directions
- structured output formats for research artifacts
- a local scaffold command for repeatable research workspaces

## What This Repo Is Not

This repo does not try to clone the full EvoScientist runtime.
It does not include:

- a multi-agent execution service
- provider orchestration
- chat platform integrations
- persistent vector memory infrastructure
- automated experiment runners

Instead, it turns EvoScientist into a single reusable skill package that can be installed into multiple agent runtimes.

## Skill Design

The skill uses three agent lenses adapted from EvoScientist:

- `Researcher Agent (RA)`: frames the problem, proposes hypotheses, and ranks directions
- `Engineer Agent (EA)`: turns the chosen direction into code, experiments, and debugging steps
- `Evolution Manager (EMA)`: summarizes lessons, records memory, and decides what to try next

The repo also preserves EvoScientist's two key memory ideas:

- `Ideation Memory`: promising and rejected directions
- `Experimentation Memory`: implementation tactics, failure modes, and reproducible wins

## Repo Structure

```text
research-orchestrator/
|-- SKILL.md
|-- README.md
|-- docs/
|   `-- plans/
|-- scripts/
|   |-- install_skill.py
|   `-- init_research_run.py
|-- tests/
|   |-- test_install_skill.py
|   `-- test_init_research_run.py
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- agent-modes.md
    |-- execution.md
    |-- memory-model.md
    |-- output-templates.md
    |-- runtime-compatibility.md
    `-- workflow.md
```

## Installation

### Claude Code

```powershell
python .\scripts\install_skill.py --runtime claude --force
```

Manual path:

```text
~/.claude/skills/research-orchestrator
```

### Codex

```powershell
python .\scripts\install_skill.py --runtime codex --force
```

Manual path:

```text
~/.codex/skills/research-orchestrator
```

### OpenClaw or Agents

```powershell
python .\scripts\install_skill.py --runtime agents --force
```

Manual path:

```text
~/.agents/skills/research-orchestrator
```

### Invocation

When the runtime supports explicit skill invocation, use `$research-orchestrator`.
For runtimes that auto-load skills from descriptions, install the whole folder unchanged so `SKILL.md` discovery still works.

## Publish to GitHub

If you want to publish this repo, you have two options:

### Dry Run the Publish Flow

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\publish_github.ps1 -Repo yourname/research-orchestrator -DryRun
```

### Publish for Real

1. Log in first:

```powershell
gh auth login
```

2. Make sure git identity is configured:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

3. Run the publish script:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\publish_github.ps1 -Repo yourname/research-orchestrator -Visibility public
```

The script will:

- initialize git if needed
- create the first commit when there are staged changes
- create the GitHub repo with `gh repo create`
- push `main` to `origin`

## Example Prompts

- `Use $research-orchestrator to turn this research idea into three testable experiments with ranked risks.`
- `Use $research-orchestrator to debug this training pipeline and record what we should not retry.`
- `Use $research-orchestrator to synthesize these results into a workshop paper outline with open questions.`
- `Use $research-orchestrator to compare baselines, define metrics, and propose the smallest viable pilot.`

## Local Scaffold Command

Create a research workspace with starter files:

```powershell
python .\scripts\init_research_run.py "graph neural network baseline"
```

This generates:

```text
runs/graph-neural-network-baseline/
|-- brief.md
|-- experiment.md
|-- results.md
|-- paper-outline.md
`-- memory/
    |-- ideation.md
    `-- experimentation.md
```

Use `--root` to place the run in a different workspace and `--force` to regenerate an existing slug.

## Authoring Notes

- `SKILL.md` stays compact and trigger-focused.
- Detailed instructions live in `references/` to keep the main skill lightweight.
- `agents/openai.yaml` provides UI-facing metadata for skill catalogs.
- `scripts/install_skill.py` handles runtime-specific installation without maintaining multiple copies of the skill.
- `scripts/init_research_run.py` provides the lightweight executable path without requiring an external service.
- `scripts/publish_github.ps1` packages the local repo into a GitHub publish flow.


