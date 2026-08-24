# Handoff RND-003 → UX

- **Status:** `in-qa`
- **Source report:** `docs/units/RND/outbox/RND-003.md`
- **Path evidence:** `docs/units/RND/outbox/RND-003/guest-paths.csv`

## Buyer path cues

Guest-visible flow: marketplace entry → discovery → PDP → supplier/trust assessment → contact/sample/order CTAs → auth/checkout/payment gates → tracking/delivery/claim documented but not executed.

## Seller path cues

Public/documented flow: seller proposition → plan → business verification → onboarding/store → listing → inquiries → RFQ → protected order → fulfillment/dispute. From verification onward, authenticated UI was not observed.

## UX requirements from evidence

- Show eligibility/gate before destructive or paid actions.
- Keep supplier badge scope and Trade Assurance eligibility explainable.
- Resolve conflicting MOQ/price fields before checkout.
- Display state/error/fallback for shipping, payment and claim.
- Preserve evidence/provenance for order terms and messages.

Mobile, accessibility and performance are explicitly not observed (`D66–D68`) and require separate testing.
