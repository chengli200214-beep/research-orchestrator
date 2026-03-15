# Workflow

## 1. Intake

Rewrite the user request into:

- objective
- constraints
- success metric
- known context
- unknowns

If critical information is missing, make the narrowest safe assumptions and label them.

## 2. Ideation

The Researcher Agent should produce:

- 2-5 candidate directions
- likely baselines
- risks and blockers
- a ranked recommendation

Reject directions that are clearly infeasible, untestable, or not aligned with the stated objective.

## 3. Pilot

The Engineer Agent should define the smallest experiment that can falsify or support the chosen direction.

Prefer:

- a toy dataset before a large dataset
- one baseline before many baselines
- one metric that matters before a metric explosion

## 4. Execution and Debugging

When implementation begins:

- keep steps explicit
- isolate one failure at a time
- record failed approaches that should not be retried without new evidence

## 5. Analysis

Interpret results against the predefined success criteria.

Always separate:

- what the result shows
- what the result suggests
- what remains unproven

## 6. Evolution

Close every major step with a short evolution pass:

- retain promising patterns
- retire low-value directions
- define the single best next move

Use the templates in `memory-model.md` instead of free-form summaries.
