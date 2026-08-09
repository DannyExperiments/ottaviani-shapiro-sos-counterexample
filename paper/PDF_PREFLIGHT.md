# Frozen PDF preflight

Execution date: 2026-08-09.

## Identity

```text
FILE: paper/manuscript.pdf
SHA256: 32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110
SIZE_BYTES: 251329
PRODUCER: pdfTeX-1.40.29
PAGES: 3
PAGE_SIZE: A4 (595.276 x 841.89 points)
ENCRYPTED: NO
FORMS: NONE
JAVASCRIPT: NO
AUTHOR_METADATA: EMPTY
```

The file is the exact `manuscript.pdf` member from successful GitHub Actions
run `31295131872`, PR head
`7c2eb4031131923f98fe4779f17a6d6578fea1ea`. The downloaded artifact ZIP had
SHA-256 `03bf4d9e1c4b62027e54dad850c9ffbb28c28ded7aff440385bffa2462e90ddd`.
The workflow source blob matches the designated local TeX source exactly.

The same PDF workflow passed on public `main` at commit
`78a6a49461df990abf01a8d5089fcd074002fd36` in run `31296200849`, job
`93201578150`. Artifact `9033026233` has API-recorded digest
`sha256:a796fa661318c52403d61e62450f8228123dd622e5c0c2c2ab62248bfc0a68ac`;
source/artifact parity passed.

## Scope comparison

The extracted PDF contains the exact headline witness `1152>1024=2^10`, the
audited even-degree family, and the explicit closing boundary that the work
does not determine the exact extremal function, prove optimality of `1152`,
provide a matching upper bound, or classify extremizers.

```text
PDF_SCOPE_COMPARISON: PASS
EXACT_MAXIMUM_BOUNDARY: PASS
NO_LEAN_CLAIM: PASS
NO_DOI_CLAIM: PASS
NO_PEER_REVIEW_CLAIM: PASS
```

## Privacy and document safety

Poppler text extraction was scanned for user-home paths, private temporary
paths, raw ChatGPT URLs, Codex attachment paths, email addresses, tokens,
cookies, wallet/private-key markers, and sandbox URIs. No match was found.

All 22 reported fonts are embedded and subsetted with Unicode mappings.

```text
PDF_TEXT_PRIVACY_SCAN: PASS
PDF_METADATA_SCAN: PASS
PDF_EMBEDDED_FONT_SCAN: PASS
```

## Visual inspection

All three pages were rendered and inspected at original detail. The title,
abstract, theorem/proof flow, equations, headers, page numbers, references,
and final scope paragraph are readable. No clipping, overlap, broken glyph,
black box, malformed equation, or excessive display fragmentation was found.
The section heading `A general even-degree family` is visually separated from
the following introductory sentence and theorem; the earlier crowding is
absent in this rebuilt artifact.

```text
PDF_VISUAL_PREFLIGHT: PASS
```

This preflight authorizes the frozen local artifact. The public-default-branch
workflow and artifact-parity gate also passed, so the PDF badge is visible; its
image and target were anonymously tested and report passing. No Lean or DOI
badge is authorized.
