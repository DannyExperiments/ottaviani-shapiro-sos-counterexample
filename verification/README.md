# Verification

The executable public-safe checks live in [`../checks/`](../checks/). Both are
dependency-free exact integer programs. They corroborate the symbolic proof
and do not replace it.

`scripts/verify_repository.py` additionally checks the frozen PDF and fresh
priority-report hashes, scope markers, visible public-main badge boundary,
release-staging parity, complete file inventory, checksum ledger, and
text-file privacy rules.
