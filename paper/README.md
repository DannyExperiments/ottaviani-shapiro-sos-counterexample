# Manuscript gate

`manuscript.tex` is the designated manuscript source. It follows
the PRZ presentation standard: `amsart`, A4 paper, one-inch margins, no author
entry, and a four-sentence abstract. It states the certified `1152>1024`
refutation and the strongest audited lower-bound family, while explicitly
leaving the exact extremal maximum open.

The frozen output is [`manuscript.pdf`](manuscript.pdf), SHA-256
`32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`.
Source-level formatting, theorem scope, privacy, exact verifier QA, PDF
metadata, embedded fonts, and page-by-page visual inspection pass. The
cached-only local Tectonic attempt remains recorded as an environment failure.
The release-hardening PR build and the public default-branch workflow pass;
public-main artifact parity also passes.

Read `CLAIM_SCOPE_AND_LIMITATIONS.md`, `SOURCE_COMPARISON.md`, `SOURCE_QA.md`,
`VERIFIER_REPLAY_LOG.txt`, `PDF_PREFLIGHT.md`, and `BUILD_STATUS.md` before
treating the files as a release candidate. The visible PDF-build badge and
target were anonymously tested after the clean public-main workflow passed.
