# رجیستر رسمی تسک‌های ابلاغ‌شده

فقط `MGT` وضعیت را تغییر می‌دهد. مرجع برنامه: [`../../research/task-registry.csv`](../../research/task-registry.csv) (canonical: `01a029c7@d805abd`)

| واحد مجری | تسک | وضعیت | مبنا/وابستگی | تاریخ آخرین ثبت |
| --- | --- | --- | --- | --- |
| `RND` | `RND-001` | `qa-pass` | `QA-PASS-RND-001` (inbox canonical)؛ outbox روی `01a02d71@2e9b2e9` | 2026-08-22 |
| `RND` | `RND-002` | `qa-pass` | `QA-PASS-RND-002` rev2 (inbox canonical)؛ outbox روی `01a02d71@2e9b2e9` | 2026-08-24 |
| `RND` | `RND-003` | `in-qa` | `NOTIFY-RND-003` @ `01a02d71@2e9b2e9`؛ وابستگی‌ها RND-001/002 ✓ qa-pass؛ اجرا با دستور کارفرما پس از قفل 01a034a2 (override ثبت شد) | 2026-08-24 |
| `TRADE` | `TRD-001` | `qa-pass` | `QA-PASS-TRD-001` (inbox canonical + تبار 01a034bd/01a034a2) | 2026-08-24 |
| `TRADE` | `TRD-002` | `qa-pass` | `QA-PASS-TRD-002` (inbox canonical)؛ outbox canonical | 2026-08-24 |
| `TRADE` | `TRD-003` | `issued` | بریف در `TRADE/inbox/TRD-003.md` (canonical)؛ **هنوز outbox وجود ندارد** — در انتظار تحویل | 2026-08-24 |
| `TRADE` | `TRD-004` | `in-qa` | `NOTIFY-TRD-004` (inbox canonical)؛ outbox canonical | 2026-08-24 |
| `TRADE` | `TRD-005` | `in-qa` | `NOTIFY-TRD-005` (inbox canonical)؛ **وابستگی registry: TRD-004 که qa-pass نشده — پرچ (اجرای owner-directed)** | 2026-08-24 |
| `TRADE` | `TRD-006` | `in-qa` | `NOTIFY-TRD-006` (inbox canonical)؛ تعلیق امارات = گیت مسدودکننده؛ بسته‌های CMP/LEG route شد | 2026-08-24 |
| `FIN` | `FIN-001` | `qa-pass` | `QA-PASS-FIN-001` @ `01a034c3@ab698e2`؛ اعتبارسنجی مستقل MGT در این شیفت (بازتولید بایت‌به‌بایت) | 2026-08-24 |
| `FIN` | `FIN-002` | `in-qa` | `NOTIFY-FIN-002` @ `01a034a7@53b3b94`؛ FIN-001 ✓ qa-pass؛ **وابستگی `LEG-003` شروع‌نشده — استثنا باز، برای QA پرچخورده** | 2026-08-24 |
| `LEG` | `LEG-001` | `in-qa` | `NOTIFY-LEG-001` @ `01a034a6@bf43b53`؛ وابستگی ندارد | 2026-08-24 |

## تسک‌های بعدی — مسدود (ابلاغ ممنوع تا رفع blocker)

| واحد | تسک | Blocker |
| --- | --- | --- |
| `RND` | `RND-004` | `RND-003` در in-qa |
| `TRADE` | `TRD-007` (عراق) | `TRD-006` در in-qa + گیت تعلیق امارات |
| `FIN` | `FIN-003` | `FIN-002` در in-qa + **`LEG-003` شروع‌نشده** (طبق بسته FIN-002-to-MGT: اول LEG-003) |
| `LEG` | `LEG-002` | `LEG-001` در in-qa |
| `LEG` | `LEG-003` | `LEG-001` در in-qa (+TRD-001 ✓) |

## آماده ابلاغ — در انتظار دستور صریح کارفرما (در این شیفت ابلاغ نشد)

- `CMP-001` (P0، بدون وابستگی) — پرامپت موجود؛ دستور فعلی کارفرما مصادف با ابلاغ آن نیست.
- `CMP-002` (P0، وابستگی `TRD-002` ✓ qa-pass) — مانند بالا.

## قاعده اجرا

`MGT` فقط پس از ثبت پذیرش QA وضعیت را آزاد می‌کند. وجود commit یا فایل در شاخه دیگر به‌تنهایی نه qa-pass است و نه ابلاغ. «done» فقط پس از qa-pass و ثبت در `COVERED-TOPICS` مجاز است.
