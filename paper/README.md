# Manuscript gate

`manuscript.tex` is the designated private manuscript candidate. It follows
the PRZ presentation standard: `amsart`, A4 paper, one-inch margins, no author
entry, and a four-sentence abstract. It states the certified `1152>1024`
refutation and the strongest audited lower-bound family, while explicitly
leaving the exact extremal maximum open.

Source-level formatting, theorem-scope, privacy, and exact verifier QA pass.
This is not yet a frozen or visually inspected release manuscript: no final
PDF is integrated. The cached-only local Tectonic attempt stopped before TeX
parsing because the local resource bundle is missing.  The pinned, read-only
private GitHub Actions route compiled the immediately preceding source; the
exact current source requires a fresh hosted rerun after two clarity-only
wording repairs.

Read `CLAIM_SCOPE_AND_LIMITATIONS.md`, `SOURCE_COMPARISON.md`, `SOURCE_QA.md`,
`VERIFIER_REPLAY_LOG.txt`, and `BUILD_STATUS.md` before treating the source as
a release candidate. Do not display a PDF-build badge until a clean public
default-branch workflow passes and the resulting PDF is visually inspected.
