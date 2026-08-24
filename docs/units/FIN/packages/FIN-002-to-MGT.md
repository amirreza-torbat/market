# بسته FIN-002 → MGT

- وضعیت: in-qa (آماده داوری QA)
- گزارش: docs/units/FIN/outbox/FIN-002.md
- مدارک: docs/units/FIN/FIN-002/ (state_machine.csv، transitions.csv، ledger_events.csv، constraints.csv، machine_summary.csv، state_machine_diagram.md، build_fsm_data.py، validate_fsm.py — C1..C9 پاس)

## چه ساخته شد
ماشین وضعیت ۱۳ وضعیتی (۱۱ خواسته‌شده + CANCELLED/EXPIRED) با ۱۶ ویژگی هر وضعیت، ۲۳ گذار، ۱۹ رویداد دفتری، ۲۶ گیت انطباق، ۷ کد شرط بازگشت و نقشه شرایط بازرسی/تحویل/اختلاف.

## تصمیم‌های لازم از MGT
1. پیگیری **تأیید کتبی LEG و CMP** برای مدل نگهداشت وجه (گیت G5) — مسدودکننده.
2. تصویب پارامترهای زمان (پیشنهاد FIN): HOLD=۱۸۰ روز؛ VERIFY=۵ روز کاری؛ پنجره پذیرش=۵ روز کاری؛ داوری=۳۰ روز کاری.
3. ابلاغ بسته‌های PM/TRADE/INSP/LEG/CMP/INS.
4. **تا رفع تعلیق امارات (TRD-006) هیچ سفارش/تسویه‌ای به امارات فعال نشود** (قید G2).
5. پس از qa-pass، فقط FIN-003 ابلاغ شود (وابسته به FIN-001؛ LEG-003 آماده نیست → اول LEG-003).

## آنچه عمداً ساخته نشد
FIN-003 (محاسبه کارمزد/FX/chargeback/recon)؛ متن شرط داوری (LEG-003/005)؛ کد نرم‌افزار؛ جدول نرخ.
