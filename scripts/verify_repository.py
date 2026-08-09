#!/usr/bin/env python3
"""Dependency-free integrity, scope, privacy, and verifier checks."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_required_files() -> None:
    required = [
        "README.md",
        "STATUS.md",
        "PROBLEM_AND_PROOF.md",
        "CITATION.cff",
        "AI_DISCLOSURE.md",
        "PROVENANCE.md",
        "CLAIMS_EVIDENCE_MATRIX.md",
        "REPRODUCIBILITY.md",
        "LICENSE_STATUS.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "proof/PROBLEM_AND_PROOF.md",
        "checks/verify_k2_l10.py",
        "checks/verify_even_family_counts.py",
        "formalization/FORMALIZATION_FEASIBILITY_AND_DEPENDENCIES.md",
        "release/RELEASE_CHECKLIST.md",
        "paper/manuscript.tex",
        "paper/references.bib",
        "paper/BUILD.md",
        "paper/BUILD_LOG.txt",
        "paper/BUILD_STATUS.md",
        "paper/CLAIM_SCOPE_AND_LIMITATIONS.md",
        "paper/SOURCE_COMPARISON.md",
        "paper/SOURCE_QA.md",
        "paper/HOSTILE_MANUSCRIPT_AUDIT_PROMPT.md",
        "paper/VERIFIER_REPLAY_LOG.txt",
        "MANIFEST.md",
        "SHA256SUMS.txt",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"required file missing: {relative}")


def verify_scope() -> None:
    joined = "\n".join(
        (ROOT / relative).read_text(encoding="utf-8")
        for relative in ["README.md", "proof/PROBLEM_AND_PROOF.md", "STATUS.md"]
    )
    for marker in [
        "1152 > 2^10",
        "exact extremal function",
        "exact maximum remains open",
        "((l-1)(k-1)/4)",
        "MANUSCRIPT_HOSTILE_SOURCE_AUDIT_PASS",
    ]:
        if marker.lower() not in joined.lower():
            fail(f"scope marker missing: {marker}")

    build_status = (ROOT / "paper/BUILD_STATUS.md").read_text(encoding="utf-8")
    for marker in [
        "TEX_SOURCE_QA: PASS",
        "PDF_COMPILED: NO",
        "PDF_VISUAL_PREFLIGHT: NOT_RUN",
    ]:
        if marker not in build_status:
            fail(f"manuscript build boundary missing: {marker}")


def verify_privacy() -> None:
    forbidden = [
        re.compile("chatgpt" + r"\.com/(c|share|s|t)/", re.I),
        re.compile("sandbox" + r":/", re.I),
        re.compile("/" + r"Users/[A-Za-z0-9._-]+/"),
        re.compile(r"\\" + r"Users\\[A-Za-z0-9._-]+\\"),
        re.compile("/private" + r"/var/", re.I),
        re.compile(r"\." + r"codex/", re.I),
        re.compile("codex" + r"/attachments", re.I),
        re.compile(r"(?:ghp|github_pat|sk)-[A-Za-z0-9_-]{16,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    text_suffixes = {
        ".md", ".tex", ".bib", ".py", ".yml", ".yaml", ".txt",
        ".json", ".cff", ".toml", ".sh",
    }
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or not path.is_file():
            continue
        if path.name == "SHA256SUMS.txt" or path.suffix.lower() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in forbidden:
            if pattern.search(text):
                fail(f"private/secret pattern in {relative}: {pattern.pattern}")


def verify_ledger() -> None:
    ledger = ROOT / "SHA256SUMS.txt"
    for number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError:
            fail(f"malformed checksum line {number}")
        path = ROOT / relative
        if not path.is_file():
            fail(f"checksum target missing: {relative}")
        if sha256(path) != expected:
            fail(f"checksum mismatch: {relative}")


def replay() -> None:
    for script in ["verify_k2_l10.py", "verify_even_family_counts.py"]:
        result = subprocess.run(
            [sys.executable, str(ROOT / "checks" / script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if "PASS" not in result.stdout and "CERTIFIED_COUNTEREXAMPLE=YES" not in result.stdout:
            fail(f"unexpected verifier output: {script}")


def main() -> None:
    verify_required_files()
    verify_scope()
    verify_privacy()
    replay()
    verify_ledger()
    print("REPOSITORY_INTEGRITY=PASS")
    print("SCOPE_BOUNDARY=PASS")
    print("PRIVATE_DATA_SCAN=PASS")
    print("EXACT_VERIFIER_REPLAY=PASS")


if __name__ == "__main__":
    main()
