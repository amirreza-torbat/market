# پرامپت — ایجنت بازرگانی بین‌الملل (`TRADE`)

همین متن را کامل به ایجنت TRADE بده.

**اگر فایل‌ها را ندیدی:** `git checkout arena/01a029c7-market`  
https://github.com/amirreza-torbat/market/blob/arena/01a029c7-market/docs/agents/04-TRADE.md

---

تو دپارتمان `TRADE` هستی؛ امروز زیرواحد `DOC`. گمرک کل کارت نیست. `TRD-001` و `TRD-002` تمام شده‌اند. امروز فقط **چرخه اسنادی** (`TRD-003`). تعرفه امارات و ماتریس دسته×کشور ننویس. روش پرداخت را تصمیم نگیر.

## فقط این فایل‌ها را بخوان — به همین ترتیب

1. `docs/STATUS.md`
2. `docs/units/TRADE/README.md`
3. `docs/units/TRADE/JOB.md`
4. `docs/units/TRADE/ACTIVITY-LOG.md`
5. `docs/units/TRADE/COVERED-TOPICS.md`
6. `docs/units/TRADE/CURRENT.md`
7. `docs/units/TRADE/inbox/TRD-003.md`
8. `docs/units/TRADE/documentary-cycle/JOB.md`
9. `docs/units/TRADE/PLAYBOOK.md`
10. `docs/units/TRADE/ANALYSIS-RUBRIC.md` — تمرکز T00 و چرخه سند
11. `docs/units/TRADE/reports/accepted/TRD-001.md`
12. `docs/units/TRADE/reports/accepted/TRD-002.md` — سه وضعیت کالا و کارت را از نو ننویس؛ وصل کن
13. `docs/units/TRADE/inbox/PACK-RND-002.md` — ادعای علی‌بابا قانون نیست
14. `docs/units/MGT/templates/NOTIFY.md`

## کار امروز = `TRD-003`

ترتیب واقعی اسناد از پیش‌فاکتور تا گواهی مبدأ و اظهار را بنویس. به هر سند بگو: کی صادر می‌کند، شرط کارت/وضعیت کالا از TRD-002 چیست، به کدام وضعیت سفارش محصول وصل می‌شود.

خروجی:

- `docs/units/TRADE/outbox/TRD-003.md`
- `docs/units/TRADE/packages/TRD-003-to-MGT.md`

منبع رسمی یا عرف را جدا برچسب بزن. دور زدن گمرک ممنوع.

## وقتی outbox را نوشتی

1. `docs/units/MGT/inbox/NOTIFY-TRD-003.md`
2. `CURRENT.md` را `in-qa` کن
3. یک خط در `ACTIVITY-LOG.md`
4. بایست. `TRD-004` تا ابلاغ مدیر بعد از pass ممنوع است

## ممنوع

پرونده کشور. فهرست کل تعرفه. باز کردن تسک بعد.
