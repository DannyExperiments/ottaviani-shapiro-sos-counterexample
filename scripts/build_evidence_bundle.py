#!/usr/bin/env python3
"""Build or check the deterministic sanitized public evidence bundle."""

from __future__ import annotations

import argparse
import hashlib
import io
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release/EVIDENCE_BUNDLE.zip"
SIDECAR = ROOT / "release/EVIDENCE_BUNDLE.sha256"
ASSET_LEDGER = ROOT / "release/RELEASE_ASSET_SHA256SUMS.txt"
PREFIX = "POLY-2200006_PUBLIC_EVIDENCE_V1/"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)

ALLOWLIST = (
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
    "proof/PROBLEM_AND_PROOF.md",
    "audits/README.md",
    "audits/public_safe_reports/MATHEMATICAL_AUDIT.md",
    "audits/public_safe_reports/LITERATURE_PRIORITY_AUDIT.md",
    "audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md",
    "evidence/README.md",
    "evidence/PRIVACY_AND_SECRET_SCAN.md",
    "evidence/RELEASE_HARDENING_AUDIT_2026-08-09.md",
    "checks/verify_k2_l10.py",
    "checks/verify_even_family_counts.py",
    "verification/README.md",
    "formalization/README.md",
    "formalization/FORMALIZATION_FEASIBILITY_AND_DEPENDENCIES.md",
    "formalization/lean/README.md",
    "formalization/aristotle/REQUEST.md",
    "formalization/aristotle/DEPENDENCY_MAP.md",
    "paper/manuscript.tex",
    "paper/manuscript.pdf",
    "paper/references.bib",
    "paper/README.md",
    "paper/BUILD.md",
    "paper/BUILD_STATUS.md",
    "paper/BUILD_LOG.txt",
    "paper/PDF_PREFLIGHT.md",
    "paper/SOURCE_COMPARISON.md",
    "paper/SOURCE_QA.md",
    "paper/CLAIM_SCOPE_AND_LIMITATIONS.md",
    "paper/HOSTILE_MANUSCRIPT_AUDIT_PROMPT.md",
    "paper/VERIFIER_REPLAY_LOG.txt",
    "release/README.md",
    "release/RELEASE_CHECKLIST.md",
    "release/RELEASE_NOTES_v1.0.0.md",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replay_readme() -> bytes:
    return b"""# Replay the public evidence bundle

This archive is a deterministic, sanitized evidence subset. It contains no raw
chat transcript, private receipt, local path, credential, screenshot, or
third-party source PDF. After extraction, change into
`POLY-2200006_PUBLIC_EVIDENCE_V1` and run:

```bash
shasum -a 256 -c BUNDLE_SHA256SUMS.txt
python3 checks/verify_k2_l10.py
python3 checks/verify_even_family_counts.py
```

The checksum command verifies the exact archived bytes. The two dependency-free
scripts replay exact integer counts and are corroborating evidence; they do not
replace the symbolic proof, peer review, or proof-assistant verification.
"""


def manifest(member_names: list[str]) -> bytes:
    lines = [
        "# Public evidence bundle manifest",
        "",
        "Bundle ID: `POLY-2200006_PUBLIC_EVIDENCE_V1`.",
        "",
        "Every archived member is a regular file with a fixed ZIP timestamp and",
        "mode. `BUNDLE_SHA256SUMS.txt` hashes every member except itself.",
        "",
        "## Members",
        "",
    ]
    lines.extend(f"- `{name}`" for name in sorted(member_names))
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_bytes() -> bytes:
    missing = [relative for relative in ALLOWLIST if not (ROOT / relative).is_file()]
    if missing:
        raise SystemExit("missing bundle members: " + ", ".join(missing))

    payloads = {relative: (ROOT / relative).read_bytes() for relative in ALLOWLIST}
    payloads["REPLAY_README.md"] = replay_readme()
    names = sorted([*payloads, "BUNDLE_MANIFEST.md", "BUNDLE_SHA256SUMS.txt"])
    payloads["BUNDLE_MANIFEST.md"] = manifest(names)
    payloads["BUNDLE_SHA256SUMS.txt"] = "".join(
        f"{sha256(payloads[name])}  {name}\n"
        for name in sorted(payloads)
    ).encode("utf-8")

    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(payloads):
            info = zipfile.ZipInfo(PREFIX + name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payloads[name])
    return buffer.getvalue()


def sidecar_text(bundle: bytes) -> str:
    return f"{sha256(bundle)}  EVIDENCE_BUNDLE.zip\n"


def asset_ledger_text(bundle: bytes) -> str:
    assets = {
        "ottaviani-shapiro-sos-counterexample-v1.0.0.pdf":
            (ROOT / "paper/manuscript.pdf").read_bytes(),
        "ottaviani-shapiro-sos-counterexample-v1.0.0.tex":
            (ROOT / "paper/manuscript.tex").read_bytes(),
        "references.bib": (ROOT / "paper/references.bib").read_bytes(),
        "CITATION.cff": (ROOT / "CITATION.cff").read_bytes(),
        "ottaviani-shapiro-sos-counterexample-public-evidence-v1.0.0.zip":
            bundle,
    }
    return "".join(
        f"{sha256(assets[name])}  {name}\n" for name in sorted(assets)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    bundle = build_bytes()
    sidecar = sidecar_text(bundle)
    asset_ledger = asset_ledger_text(bundle)
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_bytes() != bundle:
            raise SystemExit("EVIDENCE_BUNDLE_OUT_OF_DATE")
        if not SIDECAR.is_file() or SIDECAR.read_text(encoding="utf-8") != sidecar:
            raise SystemExit("EVIDENCE_BUNDLE_SIDECAR_OUT_OF_DATE")
        if (
            not ASSET_LEDGER.is_file()
            or ASSET_LEDGER.read_text(encoding="utf-8") != asset_ledger
        ):
            raise SystemExit("RELEASE_ASSET_LEDGER_OUT_OF_DATE")
        print("DETERMINISTIC_EVIDENCE_BUNDLE: PASS")
        return

    OUTPUT.write_bytes(bundle)
    SIDECAR.write_text(sidecar, encoding="utf-8")
    ASSET_LEDGER.write_text(asset_ledger, encoding="utf-8")
    print(f"WROTE {OUTPUT.relative_to(ROOT)}")
    print(f"SHA256 {sha256(bundle)}")


if __name__ == "__main__":
    main()
