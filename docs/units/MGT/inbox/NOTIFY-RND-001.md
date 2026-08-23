# NOTIFY — RND-001

- **Task ID:** `RND-001`
- **Owner:** `RND`
- **Status:** `in-qa`
- **Date:** 2026-08-23
- **Branch:** `arena/01a02d71-market`
- **Dependencies:** none

## Deliverables

- Scope report: `docs/units/RND/outbox/RND-001.md`
- Processed registry: `docs/units/RND/registry/sites.csv`
- Raw candidate log: `docs/units/RND/outbox/RND-001/candidates-raw.csv`
- Reproducible scoring: `docs/units/RND/outbox/RND-001/score_registry.py`
- Activity log: `docs/units/RND/ACTIVITY-LOG.md`

## Acceptance summary

- All seven required competitor categories are represented.
- 41 included records resolve to 41 unique canonical domains.
- One exact `www` alias duplicate is retained in the raw log and excluded from the processed registry.
- Tier distribution: A=15, B=22, C=4.
- Missing observations and low-confidence legal identities are explicit; no missing traffic rank was treated as zero traffic.

## QA request

Re-run the scoring script, verify category/domain assertions, spot-check the documented 10% sample and category leaders, and review the open questions and the activity-log inconsistency recorded in the report. Do not route a subsequent RND task until QA disposition.
