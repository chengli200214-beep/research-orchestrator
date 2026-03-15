---
name: research-orchestrator
description: Use when planning or executing research-heavy work with AI support, including literature review, hypothesis generation, experiment design, prototype implementation, debugging, result analysis, and paper or report drafting.
---

# Research Orchestrator

## Overview

This skill distills the EvoScientist project into a single Codex skill for end-to-end research work.
It treats each task through three lenses: Researcher Agent, Engineer Agent, and Evolution Manager.

## When to Use

- The user has a research question but not yet a testable plan.
- The task mixes literature review, implementation, debugging, analysis, and writing.
- The work benefits from retaining failed directions and reusing successful strategies.
- The user wants a structured research artifact instead of ad-hoc brainstorming.

For detailed role behavior, read [references/agent-modes.md](references/agent-modes.md).
For memory structures, read [references/memory-model.md](references/memory-model.md).
For output formats, read [references/output-templates.md](references/output-templates.md).
For local scaffolding, read [references/execution.md](references/execution.md).
For runtime-specific installation, read [references/runtime-compatibility.md](references/runtime-compatibility.md).

## Workflow Decision Tree

- If the task is open-ended or idea-heavy, start with the Researcher Agent, then close with the Evolution Manager.
- If the task is implementation-heavy or blocked by code, start with the Engineer Agent, then close with the Evolution Manager.
- If the task already has results and needs interpretation or writing, combine the Researcher Agent and Engineer Agent, then close with the Evolution Manager.
- If the task spans multiple phases, run the full loop below.

## Core Loop

1. Frame the objective
   - Rewrite the request as a goal, constraints, and success metric.
   - State assumptions explicitly when the problem is under-specified.
2. Run the Researcher Agent
   - Generate hypotheses, baselines, novelty angles, and evidence gaps.
   - Rank candidate directions before selecting one.
3. Run the Engineer Agent
   - Translate the selected direction into an executable experiment or implementation plan.
   - Prefer a cheap pilot before a costly run.
4. Run the Evolution Manager
   - Distill what to keep, what to avoid, and what to test next.
   - Update ideation memory and experimentation memory with the templates in `references/memory-model.md`.
5. Produce the artifact
   - Use a suitable format from `references/output-templates.md`.
   - Separate evidence, assumptions, limitations, and next steps.

## Operating Rules

- Evidence first. Distinguish sourced facts from hypotheses.
- Run the smallest viable experiment before scaling up.
- Preserve failure knowledge instead of retrying rejected directions blindly.
- Define evaluation criteria before implementation whenever possible.
- When code exists, inspect it before proposing architecture changes.
- When external facts matter, browse and cite sources.
- When evidence is weak or missing, say so directly.

## Common Deliverables

- research brief
- ranked hypothesis list
- experiment plan
- pilot implementation plan
- debugging report
- results memo
- paper or report outline

## Local Execution

When you want a concrete workspace before running the workflow, create one with:

```powershell
python .\scripts\init_research_run.py "your topic here"
```

This creates `runs/<topic-slug>/` with:

- `brief.md`
- `experiment.md`
- `results.md`
- `paper-outline.md`
- `memory/ideation.md`
- `memory/experimentation.md`

## References

- [references/agent-modes.md](references/agent-modes.md)
- [references/workflow.md](references/workflow.md)
- [references/memory-model.md](references/memory-model.md)
- [references/output-templates.md](references/output-templates.md)
- [references/execution.md](references/execution.md)
- [references/runtime-compatibility.md](references/runtime-compatibility.md)
