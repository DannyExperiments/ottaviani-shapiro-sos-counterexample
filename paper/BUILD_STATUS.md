# Build status

```text
TEX_SOURCE_QA: PASS
TECTONIC_BINARY: PRESENT (0.16.9)
LOCAL_TEX_RESOURCE_BUNDLE: MISSING
CACHED_ONLY_COMPILE_HISTORY: BLOCKED_BEFORE_TEX_PARSING
FINAL_ARTIFACT_INTEGRATED: YES
PDF_COMPILED: YES
PDF_SHA256: 32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110
PDF_PAGE_COUNT: 3
PDF_PAGE_SIZE: A4
PDF_SCOPE_COMPARISON: PASS
PDF_TEXT_PRIVACY_SCAN: PASS
PDF_EMBEDDED_FONT_SCAN: PASS
PDF_VISUAL_PREFLIGHT: PASS
PUBLIC_PR_REBUILD: PASS
PUBLIC_PR_REBUILD_HEAD: 7c2eb4031131923f98fe4779f17a6d6578fea1ea
PUBLIC_PR_REBUILD_RUN: 31295131872
PUBLIC_PR_ARTIFACT_ZIP_SHA256: 03bf4d9e1c4b62027e54dad850c9ffbb28c28ded7aff440385bffa2462e90ddd
PUBLIC_DEFAULT_BRANCH_REBUILD: PENDING
PDF_BADGE: HIDDEN
```

The historical cached-only attempt stopped before parsing the manuscript
because the local Tectonic resource cache lacked `tectonic-format-latex.tex`.
The exact PDF rebuilt by the pinned, read-only GitHub Actions workflow on the
release-hardening PR is now integrated and separately verified. The badge
remains hidden until the workflow passes on the public default branch.
