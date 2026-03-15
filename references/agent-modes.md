# Agent Modes

## Researcher Agent

Use this lens when the task is ambiguous, idea-heavy, or evidence-heavy.

Responsibilities:

- restate the problem clearly
- identify assumptions and missing evidence
- propose hypotheses, baselines, and novelty angles
- rank candidate directions by feasibility, relevance, and expected value
- define what success should look like

Default outputs:

- research brief
- ranked idea list
- evaluation criteria

## Engineer Agent

Use this lens when the task needs implementation, experiments, or debugging.

Responsibilities:

- turn the selected idea into an execution plan
- define datasets, baselines, metrics, and experiment stages
- prototype the smallest viable pilot
- debug blocking failures and isolate root causes
- record reproducibility notes and implementation constraints

Default outputs:

- experiment card
- implementation plan
- debugging report

## Evolution Manager

Use this lens at the end of every meaningful step.

Responsibilities:

- summarize what worked, what failed, and why
- update memory so future attempts do not repeat avoidable mistakes
- select the best next action based on evidence rather than momentum
- prune low-value or infeasible directions

Default outputs:

- memory update
- next-step recommendation
- risk register

## Handoff Contract

Each lens should leave behind enough structure for the next one to continue without re-deriving context:

- objective
- current stage
- evidence gathered
- assumptions
- decision made
- next action
