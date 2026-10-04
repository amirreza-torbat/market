# RND-BUY-001 — Service Blueprint و State Machine سفر خریدار (۱۳ مرحله)

- واحد: `RND+BUY` | تسک: `RND-BUY-001` | تاریخ: 2026-09-27
- وضعیت گزارش: done (پذیرش MGT 2026-09-27 — رأی QA: reviews/RND-BUY-001-r1.md)
- معیار پذیرش رجیستری: «All 13 stages and failure paths captured» — مراحل ۱۳گانه از §6 نقشه مادر
- اعلان روش: مثل SELL-001 — ترکیب مشاهده‌های accepted (مسیر مهمان همه رقبا ثبت شده: RND-003 D30، RND-004/005/006/007) + `عرف/سرنخ` + طراحی state machine پلتفرم ما. تمرکز بریف: کشف، اعتماد، RFQ، پیشنهاد، پرداخت، حمل، claim — با زمان/کلیک/ابهام تا حد مشاهده‌پذیر.

## State Machine خریدار

`guest → searching → comparing → registered/KYB → rfq_posted (یا direct_inquiry) → quotes_received → negotiating/sampling → po_signed → payment_secured → inspection_insured → shipped/tracking → delivered_accepted (یا claim) → funds_released → rated/repeat`
استثناها: `no_results`، `seller_unverified`، `quote_timeout`، `payment_failed`، `customs_hold`، `damaged`، `claim_open`.

## ۱۳ مرحله (با شاهد پروژه)

| # | مرحله | مشاهده/طراحی | خطا/ریزش | شاهد |
|---|---|---|---|---|
| 1 | ورود SEO/دعوت | دایرکتوری شهر/دسته (الگوی IndiaMART — RND-005 D55)؛ SEO باز (ضدالگوی GS 403) | — | RND-005 D55؛ RND-004 D71 |
| 2 | جست‌وجو/فیلتر | فیلترهای TRD-014 (کشور/گواهی/ظرفیت/مجوز) — رقبا: Business Type/R&D/Certification (RND-003 D22) | no_results→گسترش | RND-003/004 D22 |
| 3 | مقایسه/اعتبارسنجی فروشنده | کارت + پروفایل + گواهی سریال‌دار (الگوی MIC) + پرونده انطباق عمومی (خلأ ما) | seller_unverified→هشدار | RND-003 D27/D40-41؛ RND-007a |
| 4 | ثبت‌نام/KYB خریدار | سبک؛ KYB برای سفارش‌های تجاری | فرم سنگین زودهنگام=ریزش (الگوی رقبا: اقدام پشت دیوار — RND-008 یافته ۴) | RND-008؛ LEG-003 |
| 5 | RFQ یا خرید مستقیم | فرم RFQ (الگوی MIC ۴گام — RND-003 D32) + Get Best Price | فرم مبهم→quote ضعیف | RND-003/005/006 D32 |
| 6 | دریافت/مقایسه پیشنهادها | جدول مقایسه (قیمت/Incoterm/زمان/مجوز) — Inquiry Basket الگو | quote_timeout→یادآوری | RND-003 D32/D16؛ RND-005 |
| 7 | چت/ترجمه/نمونه | چت + ترجمه + Buy Sample (RND-003 D33/D34) | ترجمه ضعیف→سوءتفاهم | RND-003 D33 |
| 8 | تأیید مشخصات/PO | PO از قالب LEG-002 + فیلدهای TRD-014 | مغایرت مشخصات→claim بعدی | LEG-002؛ TRD-014 |
| 9 | ارز/پرداخت/escrow-LC | انتخاب روش FIN-001 + ماشین FIN-002 + گیت CMP | payment_failed/compliance_hold | FIN-001/002؛ CMP-002 |
| 10 | بازرسی/بیمه | انتخاب INSP + بیمه INS-001 بر اساس Incoterm | پوشش گپ→هشدار | INS-001؛ INSP-001 (بعدی) |
| 11 | اسناد/حمل/رهگیری | اسناد TRD-004/007 + رهگیری LOG-001 | customs_hold→اطلاع‌رسانی | TRD-004؛ LOG-001 |
| 12 | تحویل/پذیرش/claim | پنجره پذیرش + قالب ادعا LEG-002 | damaged→claim_open | FIN-002؛ LEG-002 |
| 13 | آزادسازی/امتیاز/تکرار | FIN-002 released + امتیاز دوطرفه | اختلاف حل‌نشده→ریزش | FIN-002؛ RND-003 D42 |

## الگوهای ریزش و ابهام (فشرده)

1. دیوار لاگین زودهنگام تماس (همه رقبا) — فرصت ما: استعلام مهمان‌پذیر (RND-008 یافته ۴)؛ 2. ابهام قیمت/حمل (بدون Incoterm/زمان واقعی — TRD-008 صف بازرگان)؛ 3. اعتماد بی‌سند (ضدالگو RND-009)؛ 4. quote_timeout بی‌پیگیری؛ 5. اختلاف بدون مسیر قراردادی (الگوی TradeKey — RND-006).

## مقایسه اجباری Tier A (محدودیت صادقانه)

زمان تا اولین پاسخ/تعداد کلیک واقعی نیازمند تست تعاملی است — ثبت نشد (بلاک/فرم ارسال نشد)؛ آنچه مقایسه شد: تعداد گام ساختاری RFQ (MIC ۴گام مستند)، فیلترها، مسیرهای تماس، پوشش پرداخت. تست تعاملی در backlog.

## HANDOFF

- به: BUY (persona/KYB خریدار)، PM، TNS، FIN، CS
- خودآزمایی: ۱۳ مرحله همه با خطا/جایگزین ✓؛ شاهد/برچسب هر مرحله ✓؛ محدودیت تعاملی صادقانه ✓؛ مسیر طبق ابلاغ ✓

## اصلاحات داوری دوم (2026-09-27 — SECOND-REVIEW-LOG)

- مقایسه Tier A ساختاری است؛ تست تعاملی (زمان پاسخ/کلیک/mobile) در backlog — نباید «مقایسه کامل» تلقی شود. ارجاع رو‌به‌جلو به INSP-001 باز است.
