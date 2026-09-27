# بسته TRD-003 → MGT

- تاریخ: 2026-09-27
- خروجی کامل: `docs/units/TRADE/outbox/TRD-003.md` (in-qa)
- مفقودی: نسخه قبلی این تسک (outbox + NOTIFY) مفقود بود؛ این نسخه بازسازی شد.

## مصرف مدیر

مدل وضعیت حمل آماده است: **۱۳ حالت از پذیرش تا تحویل + ۵ استثنا** (customs_hold، docs_rejected، damaged، delayed، compliance_hold). ۷ نام از پرونده‌های in-qa قفل است (accepted/permit_pending/docs_prep/declared/in_transit/arrived/در_مقصد) و ۶ نام «پیشنهادی» است — حکم با PM.

معیار پذیرش برآورده شد: مسئولیت حقوقی هر حالت و همه دست‌به‌دست‌ها صریح در جدول یافته ۱/۴.

**پیشنهاد COVERED (حکم با MGT):**

- Covered (پلتفرم داخلی): accepted، docs_prep، declaring، declared، origin_loaded، in_transit، arrived، در_مقصد + ۵ فلگ استثنا.
- Partial (داده از همکار): sample/producing (مایل‌استون تأیید نمونه)، permit_pending (فقط شناسه مجوز از TRD-005)، inland_transport (فورواردر).
- Not covered (خارج پلتفرم): جزئیات ترخیص واردات مقصد (TRD-006 به بعد)، فرایند داخلی بانک‌ها — فقط وضعیت اسناد.

## تصمیم‌های خواسته‌شده

1. تصویب نام‌های ۶‌گانه پیشنهادی یا اصلاح (PM/فنی).
2. رأی روی COVERED بالا (پیش از ابلاغ TRD-007).
3. تهیه نسخه رسمی Incoterms 2020 و UCP600 — صفحات رایگان ICC جزئیات ماده‌ای ندارند (منابع ۱-۳ outbox).
4. ترتیب TRD-007 (عراق) پس از qa-pass این تسک؛ گیت G2 (تحریم امارات از TRD-006) تا رفع رسمی پابرجاست.

تسک بعدی را خودم باز نکردم.
