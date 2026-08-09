#!/usr/bin/env python3
"""Regenerate the deterministic public manifest and checksum ledger."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git"}
EXCLUDED_NAMES = {"SHA256SUMS.txt", "MANIFEST.md"}


def files() -> list[Path]:
    current: list[Path] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            raise SystemExit(f"refusing to freeze symlink: {relative.as_posix()}")
        if not path.is_file():
            continue
        if "__pycache__" in relative.parts or path.suffix in {".pyc", ".pyo"}:
            raise SystemExit(f"refusing to freeze generated Python cache: {relative.as_posix()}")
        if path.name not in EXCLUDED_NAMES:
            current.append(path)
    return sorted(current)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    current = files()
    manifest_lines = [
        "# Public-candidate manifest",
        "",
        "Generated from the sanitized allowlist. Raw/private evidence is excluded.",
        "The manifest lists every regular repository file. `SHA256SUMS.txt` hashes every",
        "regular file except itself.",
        "",
    ]
    listed = sorted(current + [ROOT / "MANIFEST.md", ROOT / "SHA256SUMS.txt"])
    manifest_lines.extend(f"- `{path.relative_to(ROOT).as_posix()}`" for path in listed)
    (ROOT / "MANIFEST.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    hashed = sorted(current + [ROOT / "MANIFEST.md"])
    ledger = "".join(
        f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in hashed
    )
    (ROOT / "SHA256SUMS.txt").write_text(ledger, encoding="utf-8")


if __name__ == "__main__":
    main()
