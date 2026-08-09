# Reproducibility

Requirements: Python 3.10 or later; no third-party Python packages.

Run the complete public-safe verification:

```bash
bash scripts/verify.sh
```

This also checks that `release/EVIDENCE_BUNDLE.zip`, its sidecar, and the
release-asset ledger are byte-for-byte reproducible. To check that layer
directly, run:

```bash
python3 -B scripts/build_evidence_bundle.py --check
```

The archive contains an internal manifest, SHA-256 ledger, and replay README.
It is a public-safe subset; raw audit transcripts and private receipts remain
outside the repository.

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
`32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`.
Its source comparison, metadata checks, privacy text extraction, embedded-font
check, and page-by-page visual preflight pass; see `paper/PDF_PREFLIGHT.md`.

The historical cached-only Tectonic attempt is recorded in
`paper/BUILD_LOG.txt`; it stopped before TeX parsing because the local resource
cache was incomplete. `paper/BUILD.md` and the pinned, read-only
`.github/workflows/pdf.yml` define the clean public rebuild gate. Do not
display a PDF-build badge before a passing public default-branch run.
