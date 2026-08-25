# NOTIFY — RND-005

- **Task:** `RND-005`
- **Owner:** `RND`
- **Status:** `in-qa`
- **Date:** 2026-08-24
- **Branch:** `arena/01a02d71-market`
- **Base:** `bee39b63ec2789eb10c54d7c10d0f9db0d54e894`
- **Dependency:** `QA-PASS-RND-004`

## Deliverables

Report `docs/units/RND/outbox/RND-005.md`; raw/processed dimensions, guest paths and validator in adjacent `RND-005/`; packages to PM/UX/ENG/SUP/BUY.

## QA summary

- dimensions=74; errors=0; observed=62; not-found=12
- confidence high=60; medium=14
- buyer path=10; seller path=9
- metrics=8; sample=8/74; mismatch=0
- no account/inquiry/RFQ/order/payment/shipment/dispute
- STS escrow wording recorded, but Iran legal/financial feasibility not approved
- RND-006 not started; RND-001..004/QA/template unchanged

Run: `PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-005/validate_dossier.py`
