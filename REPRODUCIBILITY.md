# Reproducibility

Requirements: Python 3.10 or later; no third-party Python packages.

Run the complete public-safe verification:

```bash
python3 scripts/verify_repository.py
```

Run the mathematical corroboration directly:

```bash
python3 checks/verify_k2_l10.py
python3 checks/verify_even_family_counts.py
```

The scripts verify exact integer sign-slice data and counts. They are
corroborating evidence only. The proof does not depend on bounded
enumeration.

The designated private manuscript source is `paper/manuscript.tex`, and its
source-level QA passes. No final PDF is integrated. The cached-only Tectonic
attempt is recorded in `paper/BUILD_LOG.txt`; it stopped before TeX parsing
because the resource cache is incomplete. `paper/BUILD.md` and the pinned,
read-only `.github/workflows/pdf.yml` define the clean-build gate. Do not
display a PDF-build badge before the exact release commit rebuilds and its PDF
passes visual preflight, followed by a passing public default-branch run.
