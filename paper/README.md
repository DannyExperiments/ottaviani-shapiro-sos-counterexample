# Manuscript gate

`manuscript.tex` is the designated manuscript source. It follows
the PRZ presentation standard: `amsart`, A4 paper, one-inch margins, no author
entry, and a four-sentence abstract. It states the certified `1152>1024`
refutation and the strongest audited lower-bound family, while explicitly
leaving the exact extremal maximum open.

The frozen output is [`manuscript.pdf`](manuscript.pdf), SHA-256
`3622e8746ce08f94d4d42a6b0acb5628c10945c2afe2c8c7d03a35f42ba026a4`.
Source-level formatting, theorem scope, privacy, exact verifier QA, PDF
metadata, embedded fonts, and page-by-page visual inspection pass. The
cached-only local Tectonic attempt remains recorded as an environment failure;
the public default-branch workflow rerun remains pending.

Read `CLAIM_SCOPE_AND_LIMITATIONS.md`, `SOURCE_COMPARISON.md`, `SOURCE_QA.md`,
`VERIFIER_REPLAY_LOG.txt`, `PDF_PREFLIGHT.md`, and `BUILD_STATUS.md` before
treating the files as a release candidate. Do not display a PDF-build badge
until a clean public default-branch workflow passes.
