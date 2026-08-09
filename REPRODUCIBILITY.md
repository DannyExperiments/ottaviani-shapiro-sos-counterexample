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

The designated manuscript source is `paper/manuscript.tex`. The frozen output
is `paper/manuscript.pdf`, a three-page A4 PDF with SHA-256
`3622e8746ce08f94d4d42a6b0acb5628c10945c2afe2c8c7d03a35f42ba026a4`.
Its source comparison, metadata checks, privacy text extraction, embedded-font
check, and page-by-page visual preflight pass; see `paper/PDF_PREFLIGHT.md`.

The historical cached-only Tectonic attempt is recorded in
`paper/BUILD_LOG.txt`; it stopped before TeX parsing because the local resource
cache was incomplete. `paper/BUILD.md` and the pinned, read-only
`.github/workflows/pdf.yml` define the clean public rebuild gate. Do not
display a PDF-build badge before a passing public default-branch run.
