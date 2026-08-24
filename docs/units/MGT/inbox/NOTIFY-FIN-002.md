# NOTIFY FIN-002

- از واحد: FIN
- شناسه تسک: FIN-002
- زمان اعلام: 2026-08-24
- وضعیت نزد مجری: in-qa
- مسیر خروجی: docs/units/FIN/outbox/FIN-002.md
- مسیر بسته‌ها: docs/units/FIN/packages/FIN-002-to-MGT.md، FIN-002-to-PM.md، FIN-002-to-TRADE.md، FIN-002-to-INSP.md، FIN-002-to-LEG.md، FIN-002-to-CMP.md، FIN-002-to-INS.md
- خلاصه ۳ خطه آنچه ساخته شد: ماشین وضعیت وجوه ۱۳ وضعیتی (AUTHORIZE→HOLD→VERIFY→INSPECT→SHIP→DELIVERY→ACCEPT→RELEASE/REFUND/DISPUTE/RESOLUTION + CANCELLED/EXPIRED) با ۱۶ ویژگی هر وضعیت (trigger/actor/input/output/evidence/permission/timeout/transition/failure/refund/dispute/ledger/audit/compliance/legal/insurance)، ۲۳ گذار، ۱۹ رویداد دفتری دوبل، ۲۶ گیت انطباق، ۷ کد شرط بازگشت (K1–K7) و نقشه شرایط بازرسی/تحویل/اختلاف؛ اعتبارسنجی خودکار C1–C9 پاس؛ تعلیق امارات (TRD-006) و رجیستری prohibited (FIN-001) به‌عنوان constraint (G2/G3/G4/G25/G26) ثبت شد و هیچ مسیر دورزدن/غیرقانونی طراحی نشد.
- آنچه عمداً ساخته نشد (خارج از دامنه): FIN-003 (fees/FX/chargeback/recon)؛ متن شرط داوری (LEG-003/005)؛ تأیید کتبی LEG+CMP برای مدل نگهداشت وجه (مسدودکننده G5)؛ کد نرم‌افزار؛ قیمت‌گذاری.
- درخواست از MGT: پس از qa-pass تسک بعد را ابلاغ کند؛ پیش از آن: (۱) پیگیری تأیید LEG/CMP برای مدل نگهداشت وجه، (۲) توزیع بسته‌ها، (۳) ابلاغ LEG-003 قبل از FIN-003، (۴) حفظ قید مسدودی امارات تا ابلاغ رسمی.
- تسک بعد را خودم باز نکردم: بله (FIN-003 باز نشد)
