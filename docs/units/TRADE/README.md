# `TRADE` — دپارتمان بازرگانی بین‌الملل

گمرک **یکی از واحدهای این دپارتمان** است، نه کل آن.

پرامپت کپی‌شونده: [`docs/agents/04-TRADE.md`](../../agents/04-TRADE.md)  
بعد از هر outbox: `docs/units/MGT/inbox/NOTIFY-<TASK>.md`

اگر ایجنت تازه‌واردید: JOB → ACTIVITY-LOG → COVERED-TOPICS → CURRENT → بریف inbox.

## واحدهای داخل دپارتمان

| کد | پوشه | قلمرو |
| --- | --- | --- |
| `TRADE/CUS` | [customs/](customs/JOB.md) | اسناد گمرکی مبدأ و مقصد، HS، ترخیص |
| `TRADE/LAW` | [export-law/](export-law/JOB.md) | قوانین و مقررات صادرات ایران و واردات مقصد |
| `TRADE/CTY` | [target-countries/](target-countries/JOB.md) | شرایط کشور هدف: تعرفه، ممنوعه، استاندارد، فرهنگ معامله |
| `TRADE/DOC` | [documentary-cycle/](documentary-cycle/JOB.md) | چرخه اسنادی معامله (پروفرما تا بارنامه و گواهی مبدأ) |

تسک را `MGT` به دپارتمان می‌دهد. در بریف مشخص می‌کند کدام زیرواحد مجری است. ایجنت حق ندارد هر چهار زیرواحد را در یک گزارش سطحی قاطی کند مگر تسک `TRD-001` که نقشه دامنه است.

## نقشه پوشه

```text
TRADE/
  JOB.md PLAYBOOK.md ANALYSIS-RUBRIC.md
  ACTIVITY-LOG.md COVERED-TOPICS.md QUEUE.md CURRENT.md
  inbox/ outbox/ reports/accepted/ packages/
  customs/ export-law/ target-countries/ documentary-cycle/
```
