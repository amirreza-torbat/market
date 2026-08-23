#!/usr/bin/env python3
"""Build the canonical RND-001 site registry from the raw candidate log.

No network calls are made. Scores are explicit research judgments stored in the raw
CSV; this script validates them, resolves included canonical domains, computes total
scores and assigns tiers.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
RAW = HERE / "candidates-raw.csv"
OUTPUT = HERE.parents[1] / "registry" / "sites.csv"
REQUIRED_CATEGORIES = {"C1", "C2", "C3", "C4", "C5", "C6", "C7"}


def canonical_domain(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    return host.removeprefix("www.")


def tier(total: int) -> str:
    if total >= 7:
        return "A"
    if total >= 5:
        return "B"
    return "C"


def main() -> None:
    with RAW.open(encoding="utf-8", newline="") as handle:
        raw = list(csv.DictReader(handle))

    included = [row for row in raw if row["decision"] == "include"]
    domains = [canonical_domain(row["canonical_url"]) for row in included]
    duplicates = [domain for domain, count in Counter(domains).items() if count > 1]
    if duplicates:
        raise SystemExit(f"unresolved canonical-domain duplicates: {duplicates}")

    covered = {row["category_code"] for row in included}
    if covered != REQUIRED_CATEGORIES:
        raise SystemExit(
            f"category coverage mismatch: missing={REQUIRED_CATEGORIES-covered}, "
            f"extra={covered-REQUIRED_CATEGORIES}"
        )

    output_fields = [
        "site_id", "canonical_name", "category_code", "category_name",
        "canonical_url", "canonical_domain", "aliases", "owner_operator",
        "owner_verification", "country_or_territory", "languages",
        "marketplace_model", "specialization", "geography", "access_status",
        "login_requirement", "robots_terms_status", "observation_limitations",
        "traffic_proxy", "traffic_rank",
        "traffic_rank_date", "traffic_source_url", "traffic_score",
        "specialty_score", "geography_score", "model_score", "total_score",
        "tier", "primary_source_url", "source_type", "accessed_at",
        "confidence", "notes",
    ]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, lineterminator="\n")
        writer.writeheader()
        for index, row in enumerate(included, start=1):
            scores = [int(row[key]) for key in (
                "traffic_score", "specialty_score", "geography_score", "model_score"
            )]
            if any(score not in (0, 1, 2) for score in scores):
                raise SystemExit(f"invalid score for {row['canonical_name']}: {scores}")
            total = sum(scores)
            domain = canonical_domain(row["canonical_url"])
            writer.writerow({
                "site_id": f"S{index:03d}",
                "canonical_name": row["canonical_name"],
                "category_code": row["category_code"],
                "category_name": row["category_name"],
                "canonical_url": row["canonical_url"],
                "canonical_domain": domain,
                "aliases": row["aliases"],
                "owner_operator": row["owner_operator"],
                "owner_verification": row["owner_verification"],
                "country_or_territory": row["country_or_territory"],
                "languages": row["languages"],
                "marketplace_model": row["marketplace_model"],
                "specialization": row["specialization"],
                "geography": row["geography"],
                "access_status": row["access_status"],
                "login_requirement": row["login_requirement"],
                "robots_terms_status": "not tested; no automated crawling performed",
                "observation_limitations": row["notes"] or "public landing/index evidence only; authenticated workflow not tested",
                "traffic_proxy": "Tranco rank (lower is stronger; not a visit count)",
                "traffic_rank": row["traffic_rank"],
                "traffic_rank_date": row["traffic_rank_date"],
                "traffic_source_url": row["traffic_source_url"],
                "traffic_score": scores[0],
                "specialty_score": scores[1],
                "geography_score": scores[2],
                "model_score": scores[3],
                "total_score": total,
                "tier": tier(total),
                "primary_source_url": row["primary_source_url"],
                "source_type": row["source_type"],
                "accessed_at": row["accessed_at"],
                "confidence": row["confidence"],
                "notes": row["notes"],
            })

    print(f"wrote {len(included)} unique sites to {OUTPUT}")
    print("category counts:", dict(sorted(Counter(r["category_code"] for r in included).items())))
    print("tier counts:", dict(sorted(Counter(tier(sum(int(r[k]) for k in ('traffic_score','specialty_score','geography_score','model_score'))) for r in included).items())))


if __name__ == "__main__":
    main()
