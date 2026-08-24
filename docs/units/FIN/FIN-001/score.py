#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIN-001 payment-scoring script (reproducible).
Reads raw qualitative matrix (payment_matrix_raw.csv), applies the FIXED rubric
weights, computes weighted totals and party suitability indices, runs a
deterministic +/-20% weight sensitivity and writes the processed CSV.

Run:  python3 docs/units/FIN/FIN-001/score.py
"""
import csv
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "payment_matrix_raw.csv")
OUT = os.path.join(BASE, "payment_matrix_processed.csv")
SENS = os.path.join(BASE, "sensitivity.csv")

# ---- Fixed rubric (defined in FIN-001.md, section "روبریک ثابت") ----
WEIGHTS = {
    "d1": 0.25,  # seller payment assurance
    "d2": 0.15,  # low total cost
    "d3": 0.10,  # fast settlement
    "d4": 0.10,  # buyer protection / refundability
    "d5": 0.10,  # integrity / anti-fraud
    "d6": 0.15,  # compliance & availability (sanctions)
    "d7": 0.10,  # inspection & delivery integration
    "d8": 0.05,  # domestic (Iran) legal basis
}
assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9, "weights must sum to 1"

# Party suitability index formulas (also fixed; sums to 1.0 each)
BUYER_W = {"d4": 0.30, "d3": 0.20, "d2": 0.20, "d6": 0.15, "d7": 0.15}
SELLER_W = {"d1": 0.30, "d6": 0.20, "d5": 0.15, "d8": 0.15, "d3": 0.10, "d2": 0.10}
PLATFORM_W = {"d6": 0.25, "d7": 0.25, "d5": 0.20, "d8": 0.15, "d2": 0.15}


DIM_KEYS = {
    "d1": "d1_seller_payment_assurance",
    "d2": "d2_low_cost",
    "d3": "d3_fast_settlement",
    "d4": "d4_buyer_protection",
    "d5": "d5_integrity_anti_fraud",
    "d6": "d6_compliance_availability",
    "d7": "d7_inspection_delivery_link",
    "d8": "d8_iran_legal_basis",
}
assert set(DIM_KEYS) == set(WEIGHTS)


def load_rows():
    with open(RAW, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def weighted(row, w):
    return sum(int(row[DIM_KEYS[k]]) * wt for k, wt in w.items()) / sum(w.values())


def main():
    rows = load_rows()
    if not rows:
        sys.exit("no rows in raw file")
    processed = []
    for r in rows:
        total = weighted(r, WEIGHTS) * 20.0  # 1..5 scale -> 0..100
        processed.append({
            "method_id": r["method_id"],
            "method_en": r["method_en"],
            "weighted_score_0_100": round(total, 2),
            "buyer_index_0_100": round(weighted(r, BUYER_W) * 20.0, 2),
            "seller_index_0_100": round(weighted(r, SELLER_W) * 20.0, 2),
            "platform_index_0_100": round(weighted(r, PLATFORM_W) * 20.0, 2),
        })

    # ranks (1 = best / highest)
    for key in ("weighted_score_0_100", "buyer_index_0_100",
                "seller_index_0_100", "platform_index_0_100"):
        order = sorted(processed, key=lambda x: x[key], reverse=True)
        for i, p in enumerate(order, start=1):
            p["rank_" + key] = i

    # ---- sensitivity: +-20% relative on each weight (renormalised) ----
    sens_rows = []
    for r in rows:
        base_total = weighted(r, WEIGHTS) * 20.0
        lo, hi = base_total, base_total
        for k in WEIGHTS:
            for factor in (0.8, 1.2):
                w = dict(WEIGHTS)
                w[k] = w[k] * factor
                t = weighted(r, w) * 20.0
                lo = min(lo, t)
                hi = max(hi, t)
        sens_rows.append({
            "method_id": r["method_id"],
            "base_score": round(base_total, 2),
            "min_under_pm20": round(lo, 2),
            "max_under_pm20": round(hi, 2),
            "band_width": round(hi - lo, 2),
        })
    # rank stability under perturbations
    rank_bands = defaultdict(lambda: [11, 0])
    for pert in range(17):  # base + 16 one-at-a-time perturbations of each weight (8*2)
        w = dict(WEIGHTS)
        if pert > 0:
            k = list(WEIGHTS)[(pert - 1) // 2]
            factor = 0.8 if (pert - 1) % 2 == 0 else 1.2
            w[k] = w[k] * factor
        scored = sorted(
            ((r["method_id"], weighted(r, w) * 20.0) for r in rows),
            key=lambda x: x[1], reverse=True)
        for rank, (mid, _) in enumerate(scored, start=1):
            band = rank_bands[mid]
            band[0] = min(band[0], rank)
            band[1] = max(band[1], rank)
    for s in sens_rows:
        s["rank_min"] = rank_bands[s["method_id"]][0]
        s["rank_max"] = rank_bands[s["method_id"]][1]

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=list(processed[0].keys()))
        wtr.writeheader()
        wtr.writerows(sorted(processed, key=lambda x: x["weighted_score_0_100"],
                             reverse=True))
    with open(SENS, "w", encoding="utf-8", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=list(sens_rows[0].keys()))
        wtr.writeheader()
        wtr.writerows(sens_rows)

    # console summary
    print(f"rows scored: {len(rows)}; sensitivity perturbations: 17 per method")
    order = sorted(processed, key=lambda x: x["weighted_score_0_100"], reverse=True)
    print("RANK | ID | TOTAL | BUYER | SELLER | PLATFORM | rank band")
    for p in order:
        s = next(x for x in sens_rows if x["method_id"] == p["method_id"])
        print(f"{p['rank_weighted_score_0_100']:>4} | {p['method_id']} | "
              f"{p['weighted_score_0_100']:>6.2f} | {p['buyer_index_0_100']:>6.2f} | "
              f"{p['seller_index_0_100']:>6.2f} | {p['platform_index_0_100']:>6.2f} | "
              f"{s['rank_min']}-{s['rank_max']}")
    print(f"\nwrote: {OUT}\nwrote: {SENS}")


if __name__ == "__main__":
    main()
