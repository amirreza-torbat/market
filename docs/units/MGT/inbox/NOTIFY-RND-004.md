# NOTIFY — RND-004

- **Task:** `RND-004`
- **Owner:** `RND`
- **Status:** `in-qa`
- **Date:** 2026-08-24
- **Branch:** `arena/01a02d71-market`
- **Base:** `2e9b2e980fdf4739806d42571d8b713d2ca4eafd`
- **Dependency:** `QA-PASS-RND-003`
- **Template:** `RND-D00-D73-v1.1`

## Deliverables

- `docs/units/RND/outbox/RND-004.md`
- `docs/units/RND/outbox/RND-004/dimensions-raw.csv`
- `docs/units/RND/outbox/RND-004/dimensions.csv`
- `docs/units/RND/outbox/RND-004/guest-paths.csv`
- `docs/units/RND/outbox/RND-004/validate_dossier.py`
- `docs/units/RND/packages/RND-004-to-{PM,UX,ENG,SUP,BUY}.md`

## QA summary

- 74 unique ordered dimensions; structural errors=0.
- observed=60; observed-not-found=14.
- confidence high=45; medium=29.
- buyer guest path=10; seller public/documented path=8.
- numeric claims=8 with complete metadata.
- sample=8/74 (10.8%); mismatch=0.
- no account, inquiry, RFQ, order, PayPal, shipment or complaint submitted.
- verification was not treated as a product guarantee; Buyer Protection was not labeled escrow.
- RND-005 not started; RND-002/RND-003/QA/template unchanged.

## QA command

`PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-004/validate_dossier.py`

Recheck sample `D00,D10,D20,D30,D40,D50,D60,D73`, all numeric rows, seller/product category inconsistency, Ready-to-Order current-status caveat and payment/protection terminology.
