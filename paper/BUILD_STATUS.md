# Build status

```text
TEX_SOURCE_QA: PASS
TECTONIC_BINARY: PRESENT (0.16.9)
LOCAL_TEX_RESOURCE_BUNDLE: MISSING
CACHED_ONLY_COMPILE: BLOCKED
PINNED_PRIVATE_GITHUB_CI_BUILD: PRE_EDITORIAL_SOURCE_PASS
CURRENT_EXACT_SOURCE_RERUN: PENDING_AFTER_CLARITY_ONLY_WORDING_REPAIR
PDF_COMPILED: NO
PDF_PAGE_COUNT: NOT_AVAILABLE
PDF_VISUAL_PREFLIGHT: NOT_RUN
```

The cached-only attempt stopped before parsing the manuscript because the
local Tectonic resource cache does not contain `tectonic-format-latex.tex`.
This is an environment/runtime blocker, not a TeX or mathematical failure.

The repository's pinned, read-only private GitHub Actions workflow provides
the clean build route without modifying the local TeX environment.  Its first
hosted build passed on the immediately preceding source.  Two clarity-only
wording substitutions now require an exact-source rerun before any final PDF,
build badge, or visual-preflight claim is authorized.
