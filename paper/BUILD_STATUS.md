# Build status

```text
TEX_SOURCE_QA: PASS
TECTONIC_BINARY: PRESENT (0.16.9)
LOCAL_TEX_RESOURCE_BUNDLE: MISSING
CACHED_ONLY_COMPILE_HISTORY: BLOCKED_BEFORE_TEX_PARSING
FINAL_ARTIFACT_INTEGRATED: YES
PDF_COMPILED: YES
PDF_SHA256: 3622e8746ce08f94d4d42a6b0acb5628c10945c2afe2c8c7d03a35f42ba026a4
PDF_PAGE_COUNT: 3
PDF_PAGE_SIZE: A4
PDF_SCOPE_COMPARISON: PASS
PDF_TEXT_PRIVACY_SCAN: PASS
PDF_EMBEDDED_FONT_SCAN: PASS
PDF_VISUAL_PREFLIGHT: PASS
PUBLIC_DEFAULT_BRANCH_REBUILD: PENDING
PDF_BADGE: HIDDEN
```

The historical cached-only attempt stopped before parsing the manuscript
because the local Tectonic resource cache lacked `tectonic-format-latex.tex`.
The frozen PDF is now integrated and separately verified. The repository's
pinned, read-only GitHub Actions workflow remains the clean public rebuild
route. Its badge remains hidden until it passes on the public default branch.
