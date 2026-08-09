# Paper build contract

Current designated source:

```text
paper/manuscript.tex
paper/references.bib
```

The intended offline build command, once the required Tectonic resource bundle
is available, is:

```bash
cd paper
tectonic --only-cached --keep-logs --keep-intermediates manuscript.tex
```

The local cached-only attempt failed before manuscript parsing because
`tectonic-format-latex.tex` is absent from the cache.  The pinned, read-only
GitHub Actions workflow is the designated clean-build route.  A final build
must record the exact workflow commit, produce zero unresolved
citations/references and zero layout warnings, pass page-by-page visual
inspection, and match the audited scope. No PDF badge is authorized before the
workflow passes on the exact release commit and then on the public default
branch.
