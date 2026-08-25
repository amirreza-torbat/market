# NOTIFY — RND-006

- **Status:** `in-qa`
- **Owner:** `RND`
- **Date:** 2026-08-24
- **Branch/Base:** `arena/01a02d71-market` / `5cc9bd1271cda8bd00ede5b04c355aa1775d0a25`
- **Dependency:** QA-PASS-RND-005

Deliverables: `outbox/RND-006.md`, adjacent raw/processed/path/validator, packages to PM/UX/ENG/SUP/BUY.

QA expected: 74 dimensions; 52 observed; 22 observed-not-found; 0 errors; high=51, medium=23; buyer=10, seller=8; metrics=8. Validate regional lead-marketplace limitation, TrustSEAL verification-vs-visibility, payment-protection non-escrow wording and no RND-007.

Run: `PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-006/validate_dossier.py`
