#!/usr/bin/env python3
"""Install the skill into a supported local runtime skills directory."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


RUNTIME_SKILL_DIRS = {
    "codex": Path(".codex") / "skills",
    "claude": Path(".claude") / "skills",
    "agents": Path(".agents") / "skills",
}

IGNORE_NAMES = {
    ".git",
    ".tmp-tests",
    "__pycache__",
    "runs",
}


def read_skill_name(source: Path) -> str:
    skill_md = source / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"SKILL.md not found in {source}")

    content = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid frontmatter in {skill_md}")

    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
    if not name_match:
        raise ValueError(f"Could not read skill name from {skill_md}")

    return name_match.group(1)


def destination_for_runtime(runtime: str, home: Path, skill_name: str) -> Path:
    try:
        suffix = RUNTIME_SKILL_DIRS[runtime]
    except KeyError as exc:
        raise ValueError(f"Unsupported runtime: {runtime}") from exc
    return home / suffix / skill_name


def ignore_filter(_: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORE_NAMES}


def install_skill(
    source: str | Path,
    runtime: str,
    home: str | Path | None = None,
    force: bool = False,
) -> Path:
    source_path = Path(source).resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"Source not found: {source_path}")

    home_path = Path(home).resolve() if home is not None else Path.home()
    skill_name = read_skill_name(source_path)
    destination = destination_for_runtime(runtime, home_path, skill_name)

    if destination.exists():
        if not force:
            raise FileExistsError(f"Destination already exists: {destination}")
        shutil.rmtree(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_path, destination, ignore=ignore_filter)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the research-orchestrator skill into a supported runtime skills directory.",
    )
    parser.add_argument(
        "--runtime",
        required=True,
        choices=sorted(RUNTIME_SKILL_DIRS.keys()),
        help="Target runtime: codex, claude, or agents.",
    )
    parser.add_argument(
        "--source",
        default=str(Path(__file__).resolve().parents[1]),
        help="Source skill directory. Defaults to the repo root.",
    )
    parser.add_argument(
        "--home",
        default=None,
        help="Home directory whose runtime skill folder should be used. Defaults to the current user home.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed copy if present.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    destination = install_skill(
        source=args.source,
        runtime=args.runtime,
        home=args.home,
        force=args.force,
    )
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
