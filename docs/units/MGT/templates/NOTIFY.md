# قالب اعلام پایان تسک به مدیریت

مجری بعد از گذاشتن فایل در `outbox/` این را می‌سازد:

`docs/units/MGT/inbox/NOTIFY-<TASK-ID>.md`

```md
# NOTIFY <TASK-ID>

- از واحد:
- شناسه تسک:
- زمان اعلام:
- وضعیت نزد مجری: in-qa
- مسیر خروجی: docs/units/<UNIT>/outbox/<TASK-ID>.md
- مسیر بسته‌ها (اگر هست):
- خلاصه ۳ خطه آنچه ساخته شد:
- آنچه عمداً ساخته نشد (خارج از دامنه):
- درخواست از MGT: پس از qa-pass تسک بعد را ابلاغ کند
- تسک بعد را خودم باز نکردم: بله
```

QA از این دو قالب استفاده می‌کند:

`docs/units/MGT/inbox/QA-PASS-<TASK-ID>.md`

```md
# QA-PASS <TASK-ID>
- رأی: docs/units/QA/reviews/<TASK-ID>-r<N>.md
- موضوعات قابل ثبت در COVERED:
- تسک بعد از نظر QA آزاد است؟ بله/خیر (اگر خیر، چرا)
```

`docs/units/MGT/inbox/QA-FAIL-<TASK-ID>.md`

```md
# QA-FAIL <TASK-ID>
- رأی: docs/units/QA/reviews/<TASK-ID>-r<N>.md
- نقص مسدود:
- تسک بعد ممنوع است.
```
