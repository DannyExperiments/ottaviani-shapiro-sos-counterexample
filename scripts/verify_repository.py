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
        ".github/workflows/publish-v1.0.0.yml",
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
        "release/staging/v1.0.0/CITATION.cff",
        "release/staging/v1.0.0/ottaviani-shapiro-sos-counterexample-public-evidence-v1.0.0.zip",
        "release/staging/v1.0.0/ottaviani-shapiro-sos-counterexample-v1.0.0.pdf",
        "release/staging/v1.0.0/ottaviani-shapiro-sos-counterexample-v1.0.0.tex",
        "release/staging/v1.0.0/references.bib",
        "release/staging/v1.0.0/SHA256SUMS.txt",
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
    badge_block = "\n".join([
        "[![Verify public evidence](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml)",
        "[![Verifier replay](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml)",
        "[![PDF build](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/pdf.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/pdf.yml)",
    ])
    if not readme.startswith(
        "# A counterexample to the Ottaviani--Shapiro isolated-zero conjecture\n\n"
        + badge_block
    ):
        fail("three public-main workflow badges must be visible below the title")
    if "actions/workflows/lean" in readme.lower():
        fail("Lean badge is forbidden without a scope-matched kernel theorem")

    publish = (
        ROOT / ".github/workflows/publish-v1.0.0.yml"
    ).read_text(encoding="utf-8")
    for marker in [
        "workflow_dispatch:",
        "Require exact public main tip",
        "test \"$GITHUB_SHA\" = \"$default_tip\"",
        "bash scripts/verify.sh",
        "sha256sum -c SHA256SUMS.txt",
        "--target \"$GITHUB_SHA\"",
        "Verify published release and re-downloaded assets",
        "--jq .immutable",
        "gh release download v1.0.0 --dir redownload",
    ]:
        if marker not in publish:
            fail(f"release workflow hardening marker missing: {marker}")
    if "push:" in publish:
        fail("release publication must be manually dispatched after final-main CI")


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
        "PUBLIC_MAIN_CI_PASS_RELEASE_PENDING",
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
        "PUBLIC_DEFAULT_BRANCH_REBUILD: PASS",
        "PUBLIC_DEFAULT_BRANCH_HEAD: 78a6a49461df990abf01a8d5089fcd074002fd36",
        "PUBLIC_DEFAULT_BRANCH_PDF_RUN: 31296200849",
        "PUBLIC_DEFAULT_BRANCH_PDF_JOB: 93201578150",
        "PUBLIC_DEFAULT_BRANCH_ARTIFACT_ID: 9033026233",
        "PUBLIC_DEFAULT_BRANCH_ARTIFACT_DIGEST: sha256:a796fa661318c52403d61e62450f8228123dd622e5c0c2c2ab62248bfc0a68ac",
        "PUBLIC_DEFAULT_BRANCH_ARTIFACT_PARITY: PASS",
        "PDF_BADGE: VISIBLE_PASSING",
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
        "31296200849",
        "93201578150",
        "9033026233",
    ]:
        if marker not in preflight:
            fail(f"PDF preflight marker missing: {marker}")

    release_audit = (
        ROOT / "evidence/RELEASE_HARDENING_AUDIT_2026-08-09.md"
    ).read_text(encoding="utf-8")
    for marker in [
        "PUBLIC_REPOSITORY_ANONYMOUS_ACCESS: PASS",
        "PUBLIC_DEFAULT_BRANCH_HEAD: 78a6a49461df990abf01a8d5089fcd074002fd36",
        "PUBLIC_DEFAULT_BRANCH_TREE: 6677b47d7da528c4bad8252b608529e187f73bac",
        "PUBLIC_MAIN_VERIFY_RUN: 31296200851",
        "PUBLIC_MAIN_VERIFY_JOB: 93201578108",
        "PUBLIC_MAIN_VERIFY_CHECK: Verify public evidence",
        "PUBLIC_MAIN_REPLAY_RUN: 31296200854",
        "PUBLIC_MAIN_REPLAY_JOB: 93201578158",
        "PUBLIC_MAIN_REPLAY_CHECK: Replay exact counterexample checks",
        "PUBLIC_MAIN_PDF_RUN: 31296200849",
        "PUBLIC_MAIN_PDF_JOB: 93201578150",
        "PUBLIC_MAIN_PDF_CHECK: Rebuild manuscript PDF",
        "WORKFLOW_BADGES_VISIBLE_AND_ANONYMOUSLY_TESTED: PASS",
    ]:
        if marker not in release_audit:
            fail(f"public-main release audit marker missing: {marker}")


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


def verify_release_staging() -> None:
    staging = ROOT / "release/staging/v1.0.0"
    sources = {
        "CITATION.cff": ROOT / "CITATION.cff",
        "ottaviani-shapiro-sos-counterexample-public-evidence-v1.0.0.zip":
            ROOT / "release/EVIDENCE_BUNDLE.zip",
        "ottaviani-shapiro-sos-counterexample-v1.0.0.pdf":
            ROOT / "paper/manuscript.pdf",
        "ottaviani-shapiro-sos-counterexample-v1.0.0.tex":
            ROOT / "paper/manuscript.tex",
        "references.bib": ROOT / "paper/references.bib",
    }
    actual_names = {
        path.name for path in staging.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.txt"
    }
    if actual_names != set(sources):
        fail(
            "release staging inventory mismatch; "
            f"expected={sorted(sources)}, actual={sorted(actual_names)}"
        )
    for name, source in sources.items():
        if sha256(staging / name) != sha256(source):
            fail(f"release staging asset mismatch: {name}")
    if (
        (staging / "SHA256SUMS.txt").read_text(encoding="utf-8")
        != (ROOT / "release/RELEASE_ASSET_SHA256SUMS.txt").read_text(encoding="utf-8")
    ):
        fail("release staging checksum ledger is out of date")


def verify_public_state_language() -> None:
    current_surfaces = [
        "README.md",
        "STATUS.md",
        "CLAIMS_EVIDENCE_MATRIX.md",
        "PROVENANCE.md",
        "REPRODUCIBILITY.md",
        "verification/README.md",
        "paper/BUILD.md",
        "paper/BUILD_LOG.txt",
        "paper/BUILD_STATUS.md",
        "paper/PDF_PREFLIGHT.md",
        "paper/README.md",
        "release/README.md",
        "release/RELEASE_CHECKLIST.md",
        "release/RELEASE_NOTES_v1.0.0.md",
        "evidence/PRIVACY_AND_SECRET_SCAN.md",
        "evidence/RELEASE_HARDENING_AUDIT_2026-08-09.md",
    ]
    stale = [
        "PUBLIC_CANDIDATE_PASS_VISIBILITY_PENDING",
        "PUBLIC_DEFAULT_BRANCH_REBUILD: PENDING",
        "PDF_BADGE: HIDDEN",
        "Activate these badges only after",
        "repository remains private",
        "human changes repository visibility to public",
        "badges remain hidden",
        "badges stay hidden",
        "workflow badges remain hidden",
        "public default-branch rebuild pending",
        "post-visibility gates",
    ]
    for relative in current_surfaces:
        lowered = (ROOT / relative).read_text(encoding="utf-8").lower()
        for fragment in stale:
            if fragment.lower() in lowered:
                fail(f"stale public-state language in {relative}: {fragment}")

    required_pending = {
        "README.md": [
            "A release link and DOI badge will be added only after the immutable",
            "release and DOI deposits exist.",
        ],
        "STATUS.md": [
            "no immutable versioned GitHub",
            "release setting were live-verified on 2026-08-10",
            "An immutable `v1.0.0` release, DOI publication",
        ],
        "release/README.md": [
            "No immutable release exists yet.",
            "Default-branch protection and repository release immutability were",
            "The immutable tag/release, DOI publication",
        ],
        "release/RELEASE_NOTES_v1.0.0.md": [
            "remain staged Version 1.0.0 notes until an immutable `v1.0.0` tag",
            "No DOI has been deposited.",
        ],
        "release/RELEASE_CHECKLIST.md": [
            "- [x] Default branch protected against force push and deletion",
            "- [x] Repository release immutability enabled for future releases",
            "- [ ] Immutable `v1.0.0` release created and assets re-hashed",
            "- [ ] DOI collision scan repeated and DOI deposit verified",
        ],
    }
    for relative, markers in required_pending.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for marker in markers:
            if " ".join(marker.split()) not in normalized_text:
                fail(f"release/DOI pending boundary missing in {relative}: {marker}")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    # CFF is YAML, so a DOI may appear below a nested mapping such as
    # ``preferred-citation``.  Match the key at every indentation depth; the
    # pre-deposit repository must not claim any DOI until the verified DOI
    # metadata update deliberately changes this release-phase guard.
    if re.search(r"(?mi)^[ \t]*doi[ \t]*:", citation):
        fail("CITATION.cff must not claim a DOI before a verified DOI deposit")
    for relative in current_surfaces:
        text = (ROOT / relative).read_text(encoding="utf-8")
        if "/releases/tag/v1.0.0" in text:
            fail(f"immutable release URL asserted before release creation: {relative}")


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
    verify_release_staging()
    verify_public_state_language()
    verify_privacy()
    replay()
    verify_ledger()
    print("REPOSITORY_INTEGRITY=PASS")
    print("SCOPE_BOUNDARY=PASS")
    print("PRIVATE_DATA_SCAN=PASS")
    print("EXACT_VERIFIER_REPLAY=PASS")
    print("PUBLIC_MAIN_BADGES_AND_RELEASE_STAGING=PASS")


if __name__ == "__main__":
    main()
