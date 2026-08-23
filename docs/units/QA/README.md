# `QA` — کنترل کیفیت خروجی ایجنت

این واحد کالای فیزیکی را بازرسی نمی‌کند. بازرسی کالا کد `INSP` است.  
`QA` فقط می‌پرسد: **آیا ایجنت کار ابلاغ‌شده را کامل، مستند، غیرتکراری و قابل‌اتکا انجام داده؟**

| فایل | کار |
| --- | --- |
| [JOB.md](JOB.md) | شرح وظایف |
| [LOOP.md](LOOP.md) | حلقه کیفیت تا خطای زیر ۱٪ |
| [RUBRIC.md](RUBRIC.md) | روبریک نمره‌دهی و نقص‌ها |
| [ACTIVITY-LOG.md](ACTIVITY-LOG.md) | تاریخچه رأی‌ها |
| [templates/VERDICT.md](templates/VERDICT.md) | قالب رأی |
| [reviews/](reviews/README.md) | برگه‌های رأی |

کالای در انتظار رأی: `docs/units/<UNIT>/outbox/`

پرامپت: [`docs/agents/02-QA.md`](../../agents/02-QA.md)  
بعد از رأی: `QA-PASS-*` یا `QA-FAIL-*` در `docs/units/MGT/inbox/`
