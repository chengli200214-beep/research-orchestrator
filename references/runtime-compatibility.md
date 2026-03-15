# Runtime Compatibility

## Supported Runtimes

This skill is designed to work as one shared package across:

- Claude Code
- Codex
- OpenClaw or other `~/.agents/skills/` runtimes

## Required Files

These files are the portable core:

- `SKILL.md`
- `references/`
- `scripts/`

## Optional Runtime Metadata

- `agents/openai.yaml` is useful for runtimes that read UI-facing metadata.
- Runtimes that only read `SKILL.md` can ignore `agents/openai.yaml`.

## Install Paths

- Claude Code: `~/.claude/skills/research-orchestrator`
- Codex: `~/.codex/skills/research-orchestrator`
- OpenClaw or Agents: `~/.agents/skills/research-orchestrator`

## Portable Installer

Use the installer from the repo root:

```powershell
python .\scripts\install_skill.py --runtime claude --force
python .\scripts\install_skill.py --runtime codex --force
python .\scripts\install_skill.py --runtime agents --force
```

Use `--home` when you want to install into a different root for testing.

## Invocation Notes

- When the runtime supports explicit skill invocation, use `$research-orchestrator`.
- When the runtime uses auto-loading based on skill descriptions, keep the repo name and `SKILL.md` together so discovery still works.
