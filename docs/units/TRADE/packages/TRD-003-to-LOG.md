# بسته TRD-003 → LOG

- تاریخ: 2026-09-27
- منبع: `docs/units/TRADE/outbox/TRD-003.md` (in-qa) — یافته ۱ و ۲

## نقاط اتصال فریت/رهگیری به مدل وضعیت (پیشنهاد)

| رخداد متصدی/فورواردر (event) | وضعیت سفارش هدف | فیلد ثبت |
| --- | --- | --- |
| booking confirmed | `inland_transport` | شماره booking، فورواردر |
| gate-in ترمینال مبدأ | `declaring` / `declared` | شماره کانتینر، انبار |
| on-board date (B/L) | `origin_loaded` | شماره B/L، تاریخ on-board، متصدی |
| ETD | `in_transit` | ETD/ETA، مسیر |
| transshipment / ترانزیت | زیررخداد `in_transit` | بندر/مرز ترانزیت، مدت |
| ATA بندر/مرز مقصد | `arrived` | ATA، بسته ورود مقصد |
| customs release مقصد | `arrived` → آماده تحویل | شماره پروانه ورود مقصد |
| POD امضا | `در_مقصد` | POD (رسید تحویل) |

## قواعد اتصال

- رخداد گمشده: اگر on-board بدون ثبت B/L رخ داد، وضعیت `origin_loaded` ثبت نشود؛ فریت فقط با سند حمل جلو می‌رود.
- پیغام گمرک (سبز/زرد/قرمز از EPL — TRD-004) فقط بازتاب شود؛ زمان قطعی وعده نشود.
- استثناها از eventهای متصدی: exception notice → `customs_hold`/`damaged`/`delayed` با timestamp.
- EDI/API فورواردر و track&trace متصدی منبع رخداد؛ ادعای فورواردر ≠ سند حمل — سند ملاک (سرنخ/عرف).

## فیلدهای پیشنهادی برای PIM/سفارش

carrier، B/L/AWB/CMR number، container no، ETD/ETA، milestone code، POD file، exception flag + timestamp.
