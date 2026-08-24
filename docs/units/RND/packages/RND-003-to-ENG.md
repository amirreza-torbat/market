# Handoff RND-003 → ENG

- **Status:** `in-qa`
- **Data:** `docs/units/RND/outbox/RND-003/dimensions.csv`
- **Paths:** `docs/units/RND/outbox/RND-003/guest-paths.csv`

## Candidate bounded contexts

Identity/BusinessVerification; Supplier/Storefront; Catalog/PIM; Search; RFQ/Quotation; Messaging; Sample; Order/Contract; PaymentProtection; Logistics/Shipment; Inspection; Review; Claim/Dispute; Notification; Moderation; Policy/Audit.

## State/event implications

Use the explicit `entity`, `event`, `state`, `error_exception`, `document`, `personal_data`, `risk`, and `handoff` columns. Do not collapse payment protection into escrow. Keep external provider/integration lifecycle versioned; Alibaba logistics evidence shows a deprecation/transition risk.

## Controls

- provenance and conflict rules for seller-entered values;
- regional capability flags;
- immutable order/message evidence references;
- policy/version references on enforcement decisions;
- no KPI assumption without DATA telemetry.
