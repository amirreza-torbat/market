# NOTIFY FIN-001

- از واحد: FIN
- شناسه تسک: FIN-001
- زمان اعلام: 2026-08-24
- وضعیت نزد مجری: in-qa
- مسیر خروجی: docs/units/FIN/outbox/FIN-001.md
- مسیر بسته‌ها (اگر هست): — (خروجی داده: docs/units/FIN/FIN-001/ شامل payment_matrix_raw.csv، payment_matrix_processed.csv، sensitivity.csv، score.py، build_raw_csv.py)
- خلاصه ۳ خطه آنچه ساخته شد: مقایسه ۱۳ روش پرداخت (TT/LC/confirmed LC/deferred/escrow/CAD/DP/DA/cards/staged/guarantee/credit-insurance/third-country) با روبریک ثابت ۸ بعدی (وزن‌دار) و شاخص‌های خریدار/فروشنده/پلتفرم؛ رتبه‌بندی + تحلیل حساسیت ±۲۰٪؛ ۷ روش غیرقانونی/دورزدن تحریم حذف و در رجیستری prohibited ثبت شد؛ هیچ پیشنهاد دور زدن تحریمی داده نشد.
- آنچه عمداً ساخته نشد (خارج از دامنه): FIN-002 (state machine وجه)، FIN-003 (fees/FX)، FIN-004 (ماتریس کشور×روش)، قیمت‌گذاری نهایی، تفسیر حقوقی تحریم (LEG/CMP).
- درخواست از MGT: پس از qa-pass تسک بعد را ابلاغ کند؛ پیش از آن، زمان‌بندی ابلاغ FIN-002 و رسیدگی CMP/LEG به «محدودیت امارات (TRD-006)» و رجیستری prohibited در دستور قرار گیرد.
- تسک بعد را خودم باز نکردم: بله (FIN-002 و FIN-003 باز نشدند)
