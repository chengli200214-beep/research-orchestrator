#!/usr/bin/env python3
"""Create a deterministic Research Orchestrator research run workspace."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "research-run"


def build_files(topic: str) -> dict[str, str]:
    today = date.today().isoformat()
    return {
        "brief.md": f"""# Research Brief

- Topic: {topic}
- Created: {today}
- Objective:
- Constraints:
- Background:
- Candidate directions:
- Recommended direction:
- Risks:
- Success metric:
""",
        "experiment.md": f"""# Experiment Card

- Topic: {topic}
- Hypothesis:
- Baseline:
- Pilot scope:
- Dataset or inputs:
- Metrics:
- Implementation steps:
- Failure checkpoints:
""",
        "results.md": f"""# Results Memo

- Topic: {topic}
- What was tested:
- What happened:
- Evidence:
- Interpretation:
- Limitations:
- Decision:
- Next step:
""",
        "paper-outline.md": f"""# Paper Outline

- Topic: {topic}

1. Problem and motivation
2. Proposed approach
3. Experimental setup
4. Results
5. Analysis and limitations
6. Future work
""",
        "memory/ideation.md": f"""# Ideation Memory

- Topic: {topic}
- Objective:
- Promising directions:
- Rejected directions:
- Why rejected:
- Novelty cues:
- Evaluation criteria:
- Open questions:
""",
        "memory/experimentation.md": f"""# Experimentation Memory

- Topic: {topic}
- Experiment or task:
- Pilot scope:
- Successful tactics:
- Failed tactics:
- Failure modes:
- Best observed result:
- Reproducibility notes:
- Next recommended step:
""",
    }


def create_run(topic: str, root: str | Path | None = None, force: bool = False) -> Path:
    base_dir = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    run_dir = base_dir / "runs" / slugify(topic)

    if run_dir.exists() and not force:
        raise FileExistsError(f"Run already exists: {run_dir}")

    run_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in build_files(topic).items():
        file_path = run_dir / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    return run_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a Research Orchestrator workspace under runs/<topic-slug>/.",
    )
    parser.add_argument("topic", help="Research topic or task title")
    parser.add_argument(
        "--root",
        default=None,
        help="Root directory that should receive the runs/ folder. Defaults to the repo root.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing run directory by regenerating the default files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = create_run(args.topic, root=args.root, force=args.force)
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
