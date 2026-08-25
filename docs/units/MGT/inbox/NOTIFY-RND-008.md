# NOTIFY — RND-008

- **Status:** `in-qa`
- **Branch/Base:** `arena/01a02d71-market` / `6a14529bc365fd75904919960c3dbbb7c2854820`
- **Inputs:** QA-PASS RND-003..007

Deliverables: report; 105-row raw/processed matrix; 7-row fundamentals; 10-row decision log; validator; packages to MGT/PM/ENG/UX/TNS.

Validator expected: 7 sites × 15 capabilities=105, fundamentals=7, decisions=10, errors=0. Evidence coverage is not quality/rank. RND-009 not started; source reports and QA files unchanged.

Run: `PYTHONDONTWRITEBYTECODE=1 python docs/units/RND/outbox/RND-008/validate_synthesis.py`
