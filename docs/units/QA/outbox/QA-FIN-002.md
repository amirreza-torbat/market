# QA-FIN-002 — داوری مستقل خروجی FIN-002 (ماشین وضعیت وجوه)

- داور: نقش `QA` (بازرس مستقل کیفیت پژوهش)
- نویسنده گزارش: `FIN`
- تاریخ: 2026-08-24
- رأی: **pass**
- شاخه منبع: `origin/arena/01a034a7-market` (read-only)
- commit منبع: `53b3b944d0f8008429bb62166b4d57a8ce9d6c2d`
- canonical docs: `origin/arena/01a029c7-market @ d805abd2151da480ffb21ebe1a6f516c332aa7b0`

## خلاصه

گزارش `FIN-002` (ماشین وضعیت وجه برای جریان hold-release-refund با گیت‌های بازرسی/تحویل/اختلاف) از نظر **بازتولید‌پذیری، کامل‌بودن ابعاد، یکپارچگی گذارها، انطباق/عدم دورزدن تحریم، و وابستگی صحیح به LEG/CMP** تأیید شد.

- **بازتولید:** `build_fsm_data.py` و `validate_fsm.py` هر ۶ خروجی را بایت‌به‌بایت بازتولید کردند؛ C1..C9 پاس.
- **آمار ماشین:** ۱۳ وضعیت (۱۱ خواسته‌شده + `CANCELLED`/`EXPIRED`) × ۱۶ ویژگی (همه پر)؛ ۲۳ گذار؛ ۱۹ رویداد دفتری دوبل؛ ۲۶ گیت انطباق؛ K1–K7.
- **معیار پذیرش (Inspection delivery dispute conditions mapped):** در بخش ۶.۴ و در سطح وضعیت‌های §۵ (trigger/evidence/actor/owner) پوشش داده شد.
- **انطباق:** هیچ state/transition مسیر PR-01..PR-07 یا دورزدن تعلیق امارات را پیاده نمی‌کند؛ گیت‌های G2/G3/G4/G25/G26 حاضرند؛ مسیر ممنوع فقط CANCELLED/EXPIRED→REFUND (C5).
- **LEG-003:** به‌عنوان placeholder/dependency رعایت شده، نه متن حقوقی تصویب‌شده.

## شمارش نقص

| لایه | تعداد شکست | آستانه |
| --- | --- | --- |
| C | 0 | 0 |
| M | 0 | 0 |
| m | 5 (همگی `accepted-nit`؛ غیرمسدود) | <1% یا پذیرش MGT |

## پنج نیت غیرمسدود (accepted-nit؛ ثبت و پذیرش با MGT)

| # | توضیح |
| --- | --- |
| n1 | گزارش `FIN-002` می‌گوید «QA-PASS-FIN-001.md روی هیچ ref محلی/ریموتی یافت نشد»؛ فایل در واقع روی `origin/arena/01a034c3-market @ ab698e2` موجود است (MGT تأیید کرده). نقص فرایندی/پوشش ref. |
| n2 | §5.9 (REFUND transition) می‌گوید «REFUND جزئی → RESOLUTION/RELEASE»، اما `REFUND` پایانه است و تسویه جزئی در `RESOLUTION→RELEASE+REFUND` مدل شده. ناسازگاری توصیفی داخلی (هم‌مرز M). |
| n3 | docstring `build_fsm_data.py` می‌گوید «21 transitions» در حالی که ۲۳ گذار نوشته می‌شود. |
| n4 | جدول §6.4 ستون صریح actor/owner ندارد؛ در §۵.x از طریق actor + legal_dependency پوشش داده می‌شود. |
| n5 | §5.8 (RELEASE transition) «شکست → DISPUTE» بدون یال داده؛ فقط failure-path (وجه می‌ماند). |

## شرایط اجرای next-step

- پس از pass، `MGT` مجاز به ابلاغ `FIN-003` است؛ پیش از آن: تأیید کتبی `LEG`/`CMP` برای مدل نگهداشت وجه (گیت G5)، توزیع بسته‌ها، و ابلاغ `LEG-003`.
- حفظ قید مسدودی امارات (TRD-006) تا ابلاغ رسمی.

## فایل‌ها

- داوری کامل: `docs/units/QA/reviews/FIN-002-r1.md`
- گزارش منبع (read-only): `docs/units/FIN/outbox/FIN-002.md`
