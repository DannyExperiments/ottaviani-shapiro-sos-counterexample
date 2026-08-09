# Source-level QA

- TeX brace stack: balanced.
- `begin{document}` / `end{document}`: exactly one each.
- Abstract: four sentences, within the six-sentence limit.
- Author entry: none.
- Paper and margin settings: `amsart`, `a4paper`, one inch.
- Claim-scope scan: the conjectural formula is refuted; the exact extremal
  function and optimality of `1152` are explicitly excluded.
- Exact verifier replay: base count and audited family arithmetic both pass;
  see `VERIFIER_REPLAY_LOG.txt`.
- Private-data scan: no user name, username, email, home path, token, cookie,
  credential, wallet material, or private key detected.
- Frozen PDF SHA-256:
  `32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`.
- PDF scope comparison, metadata, text privacy, embedded-font, and visual
  preflight: `PASS`; see `PDF_PREFLIGHT.md`.
- Designated local TeX and PR-build TeX are byte-identical; the PR build and
  all three rendered pages pass.
