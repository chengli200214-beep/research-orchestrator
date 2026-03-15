# Execution

## Purpose

Use the local scaffolding command when you want the skill to start from a concrete workspace instead of a blank conversation.

## Command

```powershell
python .\scripts\init_research_run.py "your topic here"
```

You can also choose a different destination root:

```powershell
python .\scripts\init_research_run.py "your topic here" --root C:\path\to\workspace
```

## Generated Layout

```text
runs/<topic-slug>/
|-- brief.md
|-- experiment.md
|-- results.md
|-- paper-outline.md
`-- memory/
    |-- ideation.md
    `-- experimentation.md
```

## Behavior

- The command creates deterministic starter files for a research run.
- Existing runs are protected by default.
- Use `--force` only when you want to regenerate the starter files for the same slug.

## Suggested Flow

1. Run the scaffold command.
2. Invoke `$research-orchestrator` with the generated files as working context.
3. Update `memory/ideation.md` after idea ranking.
4. Update `memory/experimentation.md` after implementation or analysis.
