# Handoff RND-002 → QA

- **Task:** `RND-002`
- **Status:** `in-qa`
- **Date:** 2026-08-24
- **Branch:** `arena/01a02d71-market`
- **Source HEAD:** `501abf81566c90e4a37d7e29ffb1bcb1a89e1f83`
- **Dependency verdict:** `QA-PASS-RND-001` at QA commit `35a76ba1ec941a2bac4c3a96404c674a5477995a`

## Deliverables

- `docs/units/RND/outbox/RND-002.md`
- `docs/units/RND/outbox/RND-002/dimensions-raw.csv`
- `docs/units/RND/outbox/RND-002/dimensions.csv`
- `docs/units/RND/outbox/RND-002/validate_template.py`

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-002/validate_template.py
```

Expected:

```text
rows=74 unique_ids=74 validation_errors=0
evidence_states={'observed': 55, 'observed-not-found': 19}
confidence={'high': 53, 'medium': 21}
```

## Required QA assertions

1. IDs are exactly `D00..D73`, ordered and unique.
2. Every row has `observed` or `observed-not-found`.
3. Every evidence URL is full HTTPS; date/type/mode/confidence are populated.
4. Every not-found row has gap reason and next method.
5. Every numeric claim has all eleven metadata fields required by validator.
6. Fact, inference and product implication remain separate.
7. HKTDC is only a fixture; no Alibaba/RND-003 analysis is present.
8. No account, OTP, RFQ, message, order, payment or restricted-path crawl occurred.

## Sampling

Recheck deterministic sample: `D00`, `D10`, `D20`, `D30`, `D40`, `D50`, `D60`, `D73` (8/74 = 10.8%). Recheck all numeric rows: `D05`, `D26`, `D27`, `D40`, `D51`, `D61`, `D69`, `D70`.

## Sensitive distinctions

- certificate verification ≠ shipment inspection;
- PayPal dispute route ≠ escrow;
- country selector includes Iran ≠ service availability/approval;
- return/refund policy field ≠ observed return execution;
- official documentation ≠ direct authenticated UI observation.

## Open QA decisions

- Keep two evidence states with auth/block reason in separate fields, or add a third state?
- Make workflow fields conditional on D11–D50 or mandatory globally?
- Require immutable policy snapshots/hashes in future dossiers?

Do not authorize `RND-003` until this deliverable receives `QA-PASS-RND-002`.
