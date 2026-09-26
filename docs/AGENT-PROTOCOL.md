# پروتکل ایجنت‌ها

## هویت

یک ایجنت در هر نوبت یک کد واحد. پوشه کار فقط `docs/units/<CODE>/`.

## منبع حقیقت (اولویت)

1. `docs/STATUS.md`
2. `docs/units/MGT/ISSUED.md`
3. `docs/units/<CODE>/CURRENT.md` و بریف `inbox/`
4. `docs/units/<CODE>/ACTIVITY-LOG.md` و `COVERED-TOPICS.md`
5. `docs/RFP.md`
6. `docs/ORGANIZATION.md` (نقشه کلان؛ خانه عملیاتی نیست)

`docs/research/TASK-BOARD.md` منسوخ است.

## حلقه کار

```text
MGT ابلاغ → اجرا → self-check → outbox
         → NOTIFY در docs/units/MGT/inbox/
         → QA رأی → QA-PASS یا QA-FAIL در همان inbox
   fail: همان تسک
   pass: MGT تسک بعد را ابلاغ می‌کند + بسته RND را route می‌کند
```

بدون فایل `NOTIFY-*` کار تمام‌شده حساب نمی‌شود.

وضعیت مجاز تسک:

`queued` | `issued` | `doing` | `in-qa` | `qa-fail` | `qa-pass`

کلمه `done` فقط روی موضوع در `COVERED-TOPICS` بعد از `qa-pass`.

## ممنوع

- دو تسک همزمان در یک واحد
- تکرار موضوع `done`
- ساخت محصول قبل از بسته‌های تحقیق
- دور زدن تحریم یا گمرک
- پاک کردن لاگ واحد دیگر
- رأی QA روی کار خود به‌عنوان pass نهایی

## هandoff

بسته جدا در `packages/` برای واحد مصرف‌کننده. گزارش خام را به طراح حواله نکنید.
