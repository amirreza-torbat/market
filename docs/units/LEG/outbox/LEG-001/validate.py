#!/usr/bin/env python3
"""LEG-001 — اعتبارسنجی تکرارپذیر ماتریس مسئولیت و منابع.

بررسی‌ها:
  1. ساختار: ۷ مدل × ۱۰ بُعد = ۷۰ ردیف بدون خانه خالی.
  2. همه source_id های استفاده‌شده در ماتریس باید در sources.csv تعریف شده باشند.
  3. مقادیر confidence و type فقط از مجموعه مجاز.
  4. همه منابع باید URL و تاریخ دسترسی داشته باشند.
  5. نمونه‌گیری ۱۰٪ (۷ ردیف) برای کنترل مجدد و ثبت در لاگ.

اجرا:  python3 validate.py
خروجی: نتیجه در ترمینال + نوشتن reconciliation-log.md
"""
import csv
import io
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MATRIX = os.path.join(HERE, "model-liability-matrix.csv")
SOURCES = os.path.join(HERE, "sources.csv")
LOG = os.path.join(HERE, "reconciliation-log.md")

MODELS = {"M1", "M2", "M3", "M4", "M5", "M6", "M7"}
DIMS = {
    "تعهدات پلتفرم",
    "مسئولیت در برابر فروشنده",
    "مسئولیت در برابر خریدار",
    "مسئولیت کیفیت کالا",
    "مسئولیت پرداخت",
    "مسئولیت اطلاعات نادرست",
    "مسئولیت تحریم و انطباق",
    "مسئولیت اسناد و لجستیک",
    "ریسک‌های قراردادی",
    "قانون حاکم و حوزه قضایی",
}
CONF = {"بالا", "متوسط", "پایین"}
TYPES = {"واقعیت-قانون", "واقعیت-مشاهده", "استنباط", "برآورد"}

errors = []
notes = []


def load(path):
    with io.open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


rows = load(MATRIX)
srcs = load(SOURCES)
src_ids = {s["source_id"] for s in srcs}

# 1) ساختار
if len(rows) != 70:
    errors.append(f"تعداد ردیف {len(rows)} است؛ انتظار ۷۰.")
seen = set()
for r in rows:
    key = (r["model_id"], r["dimension"])
    if key in seen:
        errors.append(f"ردیف تکراری: {key}")
    seen.add(key)
    if r["model_id"] not in MODELS:
        errors.append(f"model_id ناشناخته: {r['model_id']}")
    if r["dimension"] not in DIMS:
        errors.append(f"بُعد ناشناخته: {r['dimension']}")
    if not r["summary_fa"].strip():
        errors.append(f"خلاصه خالی: {key}")
    if r["confidence"] not in CONF:
        errors.append(f"confidence نامعتبر در {key}: {r['confidence']}")
    if r["type"] not in TYPES:
        errors.append(f"type نامعتبر در {key}: {r['type']}")
missing = {(m, d) for m in MODELS for d in DIMS} - seen
if missing:
    errors.append(f"خانه‌های غایب: {sorted(missing)}")

# 2) ارجاع منبع
used = set()
for r in rows:
    ids = [x.strip() for x in r["source_ids"].split(",") if x.strip()]
    if not ids:
        errors.append(f"بدون منبع: {r['model_id']}/{r['dimension']}")
    for i in ids:
        used.add(i)
        if i not in src_ids:
            errors.append(f"منبع استفاده‌شده اما تعریف‌نشده: {i}")
unused = src_ids - used
if unused:
    notes.append(f"منابع تعریف‌شده ولی استفاده‌نشده: {', '.join(sorted(unused))}")

# 3) منابع: URL و تاریخ
for s in srcs:
    if not s["url"].startswith("http"):
        errors.append(f"منبع {s['source_id']} بدون URL معتبر.")
    if s["access_date"] != "2026-08-24":
        errors.append(f"منبع {s['source_id']} تاریخ دسترسی غیر از 2026-08-24 دارد.")

# 4) نمونه ۱۰٪ = ۷ ردیف با seed ثابت برای تکرارپذیری
random.seed(1404)
sample = random.sample(rows, 7)
notes.append("نمونه ۱۰٪ برای بازبینی دستی (باید با منبع کنترل شود):")
for r in sample:
    notes.append(
        f"  - {r['model_id']} / {r['dimension']} → منابع {r['source_ids']} (اطمینان: {r['confidence']})"
    )

line = "=" * 60
report = [
    "# Reconciliation & self-check log — LEG-001",
    "",
    "- تاریخ اجرا: 2026-08-24",
    f"- ردیف‌های ماتریس: {len(rows)} (انتظار 70)",
    f"- منابع تعریف‌شده: {len(srcs)}؛ استفاده‌شده: {len(used)}",
    f"- منابع بدون استفاده: {', '.join(sorted(unused)) or '—'}",
    f"- خطاها: {len(errors)}",
    "",
    "## خطاها",
]
report += [f"- {e}" for e in errors] or ["- بدون خطا"]
report += ["", "## یادداشت‌ها و نمونه ۱۰٪"] + notes + ["", line]

with io.open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("\n".join(report))
sys.exit(1 if errors else 0)
