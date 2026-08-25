# NOTIFY — RND-007

- **Status:** `in-qa`
- **Branch/Base:** `arena/01a02d71-market` / `a7b263e0a8c12ea97d1e580347b186a0870c83e3`
- **Dependency:** QA-PASS-RND-006

Deliverables: report, 222-row raw/processed matrix, 30 guest-path rows, validator, and PM/UX/ENG/SUP/BUY packages.

Expected validator: each site 74 rows; TradeKey 41 observed/33 not-found; EC21 58/16; ExportHub 41/33; errors=0; buyer/seller=5/5 per site. Sites are never merged semantically. RND-008 not started.

Run: `PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-007/validate_dossier.py`
