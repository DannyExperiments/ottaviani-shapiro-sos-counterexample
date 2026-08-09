#!/usr/bin/env bash
set -euo pipefail
python3 scripts/verify_repository.py
python3 -B scripts/build_evidence_bundle.py --check
