# `RND` — تحقیق و توسعه و تحلیل رقبا

اگر ایجنت تازه‌وارد این واحد هستید، همین فایل را اول بخوانید. سپس به ترتیب پایین بروید. **تحلیل ننویسید قبل از خواندن لاگ.**

## ترتیب ورود اجباری (۱۵ دقیقه اول)

1. [JOB.md](JOB.md) — چه کاره هستید و چه کاره نیستید
2. [ACTIVITY-LOG.md](ACTIVITY-LOG.md) — قبلاً چه شده
3. [COVERED-TOPICS.md](COVERED-TOPICS.md) — چه موضوعی بسته است
4. [CURRENT.md](CURRENT.md) — تنها کار مجاز امروز
5. بریف داخل `inbox/` با همان شناسه
6. [PLAYBOOK.md](PLAYBOOK.md) و [ANALYSIS-RUBRIC.md](ANALYSIS-RUBRIC.md) وقتی تسک کالبدشکافی بود

## نقشه پوشه

```text
RND/
  README.md                 ← شما اینجا هستید
  JOB.md
  PLAYBOOK.md
  ANALYSIS-RUBRIC.md        ← از رنگ تا استراتژی کلان
  ACTIVITY-LOG.md
  COVERED-TOPICS.md
  QUEUE.md                  ← صف یکی‌پس‌ازدیگری
  CURRENT.md
  inbox/                    ← بریف‌های MGT
  outbox/                   ← تحویل برای QA
  reports/accepted/         ← فقط بعد از qa-pass
  packages/                 ← داده برای واحدهای دیگر
  registry/                 ← فهرست سایت‌های شناسایی‌شده
  templates/
```

پرامپت کپی‌شونده: [`docs/agents/03-RND.md`](../../agents/03-RND.md)

بعد از هر outbox: `docs/units/MGT/inbox/NOTIFY-<TASK>.md`

## قانون طلایی این واحد

همه واحدهای محصول (`DES`, `SEO`, `PM`, `SUP`, `FIN`, ...) باید از **بسته داده همین واحد** تغذیه شوند. تحلیل سلیقه‌ای واحد دیگر روی رقیب، بدون ارجاع به بسته `RND`، معتبر نیست.

پس گزارش شما باید قابل‌برش باشد: رنگ برای `DES`، دسته برای `PIM`، خدمت برای `PM`، اعتماد برای `TNS`.
