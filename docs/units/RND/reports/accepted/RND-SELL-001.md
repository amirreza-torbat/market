# RND-SELL-001 — Service Blueprint و State Machine سفر فروشنده (۱۶ مرحله)

- واحد: `RND+SUP` | تسک: `RND-SELL-001` | تاریخ: 2026-09-27
- وضعیت گزارش: done (پذیرش MGT 2026-09-27 — رأی QA: reviews/RND-SELL-001-r1.md)
- معیار پذیرش رجیستری: «All 16 stages and failure paths captured» — مراحل ۱۶گانه از §5 نقشه مادر
- **اعلان روش و محدودیت:** walkthrough تعاملی زنده روی رقبا ممکن نشد (بلاک ۴۰۳/تکمیل نشدن فرم‌ها — RND-004/005/006/007)؛ بنابراین blueprint از ترکیب (الف) مشاهده‌های accepted پرونده‌ها (ب) راهنماهای عمومی onboarding با برچسب `عرف/سرنخ` (ج) طراحی state machine برای پلتفرم ما ساخته شد. هر مرحله: هدف/actor/ورودی/وضعیت/خطا/سند/داده شخصی + شاهد. «مشاهده نشد» صادقانه ثبت شده است.

## State Machine فروشنده (وضعیت‌ها)

`guest → registered → contact_verified → kyc_submitted → kyc_approved (یا kyc_rejected→resubmit) → profile_ready → product_listed (×n) → moderation (approved/rejected→fix) → live_seller → rfq_received → quoted → negotiating → pi_signed → payment_secured → preparing_inspected → shipped → delivered → funds_released → rated/renewed`
استثناها: `kyc_rejected`، `moderation_rejected`، `lead_timeout` (RFQ بی‌پاسخ)، `dispute_open`، `payment_failed`، `account_suspended`.

## ۱۶ مرحله (با شاهد پروژه)

| # | مرحله | ورودی→خروجی | خطا/ریزش/جایگزین | داده شخصی | شاهد |
|---|---|---|---|---|---|
| 1 | کشف ارزش/زبان | بازدید→انتخاب EN/AR/RU/FA | زبان نبود→ریزش اولیه | — | RND-007b (هر دو رقیب چندزبانه)؛ TRD-011/008 |
| 2 | ثبت حساب + انتخاب seller | ایمیل/تلفن→حساب | فرم سبک بدون توضیح مسیر تأیید=ریزش (Made in Irani — RND-007b) | ایمیل/تلفن | RND-007b D31؛ RND-004 D31 (Join Free) |
| 3 | تأیید تماس/شرکت | OTP/ایمیل→contact_verified | OTP ناموفق→retry | تلفن/ایمیل | `عرف`؛ IndiaMART OTP+تماس مدیر حساب (`سرنخ` RND-SELL جست‌وجو) |
| 4 | KYC/مدارک | ثبت شرکت/کد اقتصادی/کارت بازرگانی→kyc_submitted | مدارک ناقص→ریزش بزرگ‌ترین نقطه؛ ما الگوی TrustSEAL Pro (اثبات عملیاتی) | مدارک هویتی | TRD-005؛ RND-005 D40؛ CAT-001 |
| 5 | پروفایل شرکت/کارخانه | ظرفیت/تصاویر/گواهی‌ها→profile_ready | اطلاعات ناقص=بی‌اعتمادی خریدار | اطلاعات شرکت | RND-003 D27 (میکروسایت)؛ D41 بخش‌های حسابرسی |
| 6 | افزودن کالا | فیلدهای TRD-014 (HS/گواهی/MOQ/lead time)→product | HS غلط→مسدود اظهار (TRD-004) | — | TRD-014؛ CAT-001؛ RND-003 D25 |
| 7 | قیمت‌گذاری/Incoterm | قیمت پله‌ای+Incoterm→قیمت‌گذاری‌شده | بی‌قاعدگی ارز/Incoterm | — | TRD-003؛ FIN-001؛ RND-003 D60 |
| 8 | انتشار/moderation | ارسال→approved/rejected | رد moderation→اصلاح (نشان بی‌سند=رد — RND-009 ضدالگوی ۱) | — | LEG-003 قاعده ۱ |
| 9 | دریافت/پاسخ RFQ | RFQ ورودی→quote | پاسخ دیر/نپاسخ→lead_timeout | — | RND-003 D32 (Easy Sourcing)؛ TRD-005 (سهمیه buyleads) |
| 10 | نمونه/مذاکره | درخواست نمونه→ارسال/توافق | هزینه نمونه مبهم→ریزش | آدرس خریدار | RND-003 D34 (Buy Sample)؛ RND-004 (فیلتر Buy Sample) |
| 11 | PI/قرارداد | توافق→PI امضاشده | قالب ناقص→اختلاف بعدی | طرف‌ها | LEG-002 (PO/PI)؛ TRD-003 |
| 12 | انتخاب پرداخت | روش FIN-001→payment_secured | کانال غیرمجاز→بلوک CMP | حساب بانکی | FIN-001/002؛ CMP-002 |
| 13 | آماده‌سازی/بازرسی/اسناد | تولید+INSP+اسناد TRD-004→docs_ready | نبود CoC/attestation→توقف (TRD-007) | — | TRD-004/007؛ INS-001 |
| 14 | حمل/تحویل | LOG-001→delivered | صف مرز/تأخیر→delayed | — | LOG-001؛ TRD-008 T12 |
| 15 | آزادسازی وجه | شرط‌های FIN-002→released | اختلاف→dispute_open | — | FIN-002 (۱۰ حالت) |
| 16 | امتیاز/اختلاف/تمدید/تکرار | تجربه→امتیاز+سفارش بعدی | اختلاف حل‌نشده→ریزش دائمی | نظرات | RND-003 D42؛ TRD-014؛ LEG-003 |

## الگوهای ریزش کلیدی (failure paths جمع‌بندی)

1. KYC سنگین/نامشخص در مراحل ۳–۴ (بزرگ‌ترین ریزش — الگوی تعارض رایگان/سختگیری)؛ 2. moderation بی‌معیار (مرحله ۸)؛ 3. lead_timeout مرحله ۹؛ 4. اسناد ناقص مرحله ۱۳؛ 5. اختلاف مرحله ۱۵–۱۶. `پادزهر محصول`: گیت‌های شفاف TRD-014 + سهمیه پاسخ‌دهی + چک‌لیست اسناد مقصد + حل اختلاف قراردادی.

## آنچه مشاهده نشد (صادقانه)

تست تعاملی واقعی ثبت‌نام/انتشار روی رقبا (فرم‌ها ارسال نشد)؛ زمان‌های تأیید واقعی؛ نرخ‌های واقعی ریزش — `سرنخ`های IndiaMART onboarding (تماس مدیر حساب، ۲۴–۴۸ ساعت لیست اولیه) نیاز به تأیید دستی دارد.

## HANDOFF

- به: SUP (onboarding)، PM، TNS، FIN، DES
- خودآزمایی: ۱۶ مرحله همه با خطا/جایگزین ✓؛ هر مرحله شاهد/برچسب ✓؛ مشاهده‌نشدها صادقانه ✓؛ مسیر طبق ابلاغ ✓

## اصلاحات داوری دوم (2026-09-27 — SECOND-REVIEW-LOG)

- ابعاد §5 (actor/سند تولیدشده/هزینه-زمان) هر گام در revision بعد کامل می‌شود؛ پیش از مصرف در SUP-001/CS-001 تکمیل گردد. مقایسه تعاملی Tier A در backlog است.
