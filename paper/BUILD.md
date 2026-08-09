# Paper build contract

Current designated source and frozen artifact:

```text
paper/manuscript.tex
paper/references.bib
paper/manuscript.pdf
```

The integrated PDF has SHA-256
`32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`.
It was produced by pdfTeX 1.40.29, has three A4 pages, and passed the scope,
metadata, text-privacy, embedded-font, and page-by-page visual checks recorded
in `PDF_PREFLIGHT.md`.

The intended offline build command, once the required Tectonic resource bundle
is available, is:

```bash
cd paper
tectonic --only-cached --keep-logs --keep-intermediates manuscript.tex
```

The historical local cached-only attempt failed before manuscript parsing
because `tectonic-format-latex.tex` was absent from the cache. That environment
failure does not invalidate the integrated artifact. The pinned, read-only
GitHub Actions workflow rebuilt the exact designated source successfully on
the release-hardening PR. No PDF badge is authorized before the workflow also
passes on the public default branch.
