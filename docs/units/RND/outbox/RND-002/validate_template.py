#!/usr/bin/env python3
"""Validate the RND D00-D73 evidence schema and build the processed matrix."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
RAW = HERE / "dimensions-raw.csv"
OUTPUT = HERE / "dimensions.csv"
EXPECTED = [f"D{i:02d}" for i in range(74)]
ALLOWED_STATES = {"observed", "observed-not-found"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
NUMERIC_FIELDS = [
    "metric_name", "metric_value", "metric_unit", "metric_currency",
    "metric_period", "metric_territory", "metric_classification",
    "metric_method", "metric_publisher", "source_title", "source_publication_date",
]


def is_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> None:
    with RAW.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["dimension_id"] for row in rows]
    if ids != EXPECTED:
        raise SystemExit(f"dimension sequence mismatch: got {ids}")

    errors: list[str] = []
    processed: list[dict[str, str]] = []
    for row in rows:
        row_errors: list[str] = []
        did = row["dimension_id"]
        if row["evidence_state"] not in ALLOWED_STATES:
            row_errors.append("invalid evidence_state")
        if row["confidence"] not in ALLOWED_CONFIDENCE:
            row_errors.append("invalid confidence")
        if not is_https(row["evidence_url"]):
            row_errors.append("evidence_url must be full HTTPS URL")
        for field in ("field_name", "question", "observed_at", "access_mode", "evidence_type"):
            if not row[field].strip():
                row_errors.append(f"missing {field}")
        if row["evidence_state"] == "observed" and not row["observed_fact"].strip():
            row_errors.append("observed row lacks observed_fact")
        if row["evidence_state"] == "observed-not-found":
            if not row["gap_reason"].strip() or not row["next_method"].strip():
                row_errors.append("not-found row lacks gap_reason or next_method")
        if row["metric_value"].strip():
            for field in NUMERIC_FIELDS:
                if not row[field].strip():
                    row_errors.append(f"numeric claim missing {field}")
        status = "pass" if not row_errors else "fail"
        processed.append({**row, "validation_status": status, "validation_errors": "; ".join(row_errors), "template_version": "RND-D00-D73-v1"})
        errors.extend(f"{did}: {error}" for error in row_errors)

    fields = list(processed[0])
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(processed)

    summary = Counter(row["evidence_state"] for row in rows)
    confidence = Counter(row["confidence"] for row in rows)
    print(f"rows={len(rows)} unique_ids={len(set(ids))} validation_errors={len(errors)}")
    print("evidence_states=" + repr(dict(sorted(summary.items()))))
    print("confidence=" + repr(dict(sorted(confidence.items()))))
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    main()
