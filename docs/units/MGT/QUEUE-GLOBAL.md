# صف جهانی مدیریت

خطوط موازی مجاز: `RND` ∥ `TRADE` ∥ `LEG` ∥ `FIN` ∥ `CMP` (به‌روزرسانی MGT 2026-09-27: بهانه بسته‌بودن LEG/FIN/CMP — نبود بسته RND — رفع شد؛ بسته‌های نهایی RND-009 آماده است)
داخل هر خط: سری. تسک بعد فقط با `qa-pass`.

جزئیات داخل:

- [`../RND/QUEUE.md`](../RND/QUEUE.md) — تکمیل شد
- [`../TRADE/QUEUE.md`](../TRADE/QUEUE.md) — تکمیل شد
- [`../LEG/QUEUE.md`](../LEG/QUEUE.md) — باز شد (LEG-001)
- [`../FIN/QUEUE.md`](../FIN/QUEUE.md) — باز شد (FIN-001)
- [`../CMP/QUEUE.md`](../CMP/QUEUE.md) — باز شد (CMP-001)

واحدهای `SEO` `DES` `PM` و بقیه: صف اجرایی بسته است تا خروجی LEG/FIN/CMP و SELL/BUY برسد. بستهٔ RND برایشان در `routed/` می‌ماند.

پرامپت چهار خط باز: `docs/agents/README.md`
