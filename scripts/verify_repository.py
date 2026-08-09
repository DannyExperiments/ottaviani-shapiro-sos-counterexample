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
        ".gitattributes",
        ".gitignore",
        ".github/workflows/pdf.yml",
        ".github/workflows/replay.yml",
        ".github/workflows/verify.yml",
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
        "evidence/RELEASE_HARDENING_AUDIT_2026-08-09.md",
        "evidence/PRIVACY_AND_SECRET_SCAN.md",
        "audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md",
        "proof/PROBLEM_AND_PROOF.md",
        "checks/verify_k2_l10.py",
        "checks/verify_even_family_counts.py",
        "formalization/FORMALIZATION_FEASIBILITY_AND_DEPENDENCIES.md",
        "release/RELEASE_CHECKLIST.md",
        "release/RELEASE_NOTES_v1.0.0.md",
        "release/README.md",
        "release/EVIDENCE_BUNDLE.zip",
        "release/EVIDENCE_BUNDLE.sha256",
        "release/RELEASE_ASSET_SHA256SUMS.txt",
        "scripts/build_evidence_bundle.py",
        "paper/manuscript.tex",
        "paper/manuscript.pdf",
        "paper/references.bib",
        "paper/BUILD.md",
        "paper/BUILD_LOG.txt",
        "paper/BUILD_STATUS.md",
        "paper/PDF_PREFLIGHT.md",
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


def verify_workflows() -> None:
    pdf = (ROOT / ".github/workflows/pdf.yml").read_text(encoding="utf-8")
    for marker in [
        "pull_request:",
        "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
        "xu-cheng/latex-action@6549dc21effb2730855a1281407ecfcececc6c1b",
        "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02",
        "if-no-files-found: error",
        "retention-days: 7",
    ]:
        if marker not in pdf:
            fail(f"PDF workflow hardening marker missing: {marker}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "actions/workflows/pdf.yml/badge.svg" not in readme:
        fail("staged PDF badge definition missing")
    if "<!--" not in readme.split("actions/workflows/pdf.yml/badge.svg", 1)[0]:
        fail("PDF badge must remain hidden before the public rerun")


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
        "MANUSCRIPT_PASS",
        "PRIORITY_AUDIT_PASS_QUALIFIED",
        "apparently new after documented search through 2026-08-09, moderate confidence",
        "generic/product-grid/SOS ingredients are prior art",
        "absolute priority unclaimed",
        "PUBLIC_CANDIDATE_PASS_VISIBILITY_PENDING",
    ]:
        if marker.lower() not in joined.lower():
            fail(f"scope marker missing: {marker}")

    build_status = (ROOT / "paper/BUILD_STATUS.md").read_text(encoding="utf-8")
    for marker in [
        "TEX_SOURCE_QA: PASS",
        "PDF_COMPILED: YES",
        "PDF_VISUAL_PREFLIGHT: PASS",
        "PUBLIC_PR_REBUILD: PASS",
        "PUBLIC_PR_REBUILD_HEAD: 7c2eb4031131923f98fe4779f17a6d6578fea1ea",
        "PUBLIC_PR_REBUILD_RUN: 31295131872",
        "PUBLIC_DEFAULT_BRANCH_REBUILD: PENDING",
        "PDF_BADGE: HIDDEN",
    ]:
        if marker not in build_status:
            fail(f"manuscript build boundary missing: {marker}")

    preflight = (ROOT / "paper/PDF_PREFLIGHT.md").read_text(encoding="utf-8")
    for marker in [
        "PDF_SCOPE_COMPARISON: PASS",
        "EXACT_MAXIMUM_BOUNDARY: PASS",
        "PDF_TEXT_PRIVACY_SCAN: PASS",
        "PDF_EMBEDDED_FONT_SCAN: PASS",
        "PDF_VISUAL_PREFLIGHT: PASS",
    ]:
        if marker not in preflight:
            fail(f"PDF preflight marker missing: {marker}")


def verify_frozen_artifacts() -> None:
    expected = {
        "paper/manuscript.pdf":
            "32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110",
        "audits/public_safe_reports/LITERATURE_PRIORITY_AUDIT.md":
            "4a9062c610a4e322e195c47a094ca6721ec84c1b55f7ad78410cc863a61a4030",
        "audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md":
            "fbfe8c2ad56cfaced4f1442b854a62e53dcd5efa9f29d73989ba1f53fdb3d163",
    }
    for relative, digest in expected.items():
        if sha256(ROOT / relative) != digest:
            fail(f"frozen artifact hash mismatch: {relative}")

    pdf = (ROOT / "paper/manuscript.pdf").read_bytes()
    if not pdf.startswith(b"%PDF-"):
        fail("frozen manuscript is not a PDF")


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
    expected_files: set[str] = set()
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts:
            continue
        if path.is_symlink():
            fail(f"symlink is forbidden: {relative.as_posix()}")
        if not path.is_file():
            continue
        if "__pycache__" in relative.parts or path.suffix in {".pyc", ".pyo"}:
            fail(f"generated Python cache is forbidden: {relative.as_posix()}")
        if path != ledger:
            expected_files.add(relative.as_posix())

    entries: dict[str, str] = {}
    for number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError:
            fail(f"malformed checksum line {number}")
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            fail(f"malformed checksum hash on line {number}")
        if relative in entries:
            fail(f"duplicate checksum entry: {relative}")
        entries[relative] = expected
        path = ROOT / relative
        if not path.is_file():
            fail(f"checksum target missing: {relative}")
        if sha256(path) != expected:
            fail(f"checksum mismatch: {relative}")
    if set(entries) != expected_files:
        missing = sorted(expected_files - set(entries))
        extra = sorted(set(entries) - expected_files)
        fail(f"checksum inventory mismatch; missing={missing}, extra={extra}")


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
    verify_workflows()
    verify_scope()
    verify_frozen_artifacts()
    verify_privacy()
    replay()
    verify_ledger()
    print("REPOSITORY_INTEGRITY=PASS")
    print("SCOPE_BOUNDARY=PASS")
    print("PRIVATE_DATA_SCAN=PASS")
    print("EXACT_VERIFIER_REPLAY=PASS")


if __name__ == "__main__":
    main()
