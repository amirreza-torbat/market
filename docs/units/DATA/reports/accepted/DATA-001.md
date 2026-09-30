# DATA-001 — تاکسونومی رویداد و دیکشنری KPI

- واحد: `DATA` | تسک: `DATA-001` | تاریخ: 2026-09-27
- وضعیت گزارش: done (پذیرش MGT 2026-09-27 — رأی QA + داوری دوم: reviews/SYN-001-second-review.md)
- معیار پذیرش رجیستری: «event taxonomy + KPI dictionary — Funnels SLA trust and financial events defined»
- ورودی (accepted): FIN-003 (LedgerEvent ۶گانه)، ENG-001 (ماژول‌ها)، TRD-003 (حالت‌ها)، RND-008 (بنچمارک)، CS-001 (SLA)

## ۱) تاکسونومی رویداد (Event taxonomy — pyramid: base/intermediate/business)

| لایه | نمونه رویدادها |
|---|---|
| پایه (UI) | page_view، search_performed، filter_applied، rfq_started، rfq_submitted |
| واسط | quote_received، quote_viewed، sample_requested، po_signed، payment_initiated |
| کسب‌وکار (پایه مالی — FIN-003) | PAYMENT_RECORDED، FUNDS_HELD/RELEASED/PARTIAL، REFUND_ISSUED، FEE_APPLIED، COMPLIANCE_HOLD_ON/OFF |

`قاعده`: هر رویداد: نام، موجودیت، actor، خواص، منبع قانونی ذخیره (LEG-004)؛ append-only برای مالی (FIN-003).

## ۲) قیف‌ها (Funnels)

| قیف | مراحل (از رویدادها) | منبع |
|---|---|---|
| خریدار | ورود→جست‌وجو→مقایسه→RFQ→quote→PO→پرداخت→تحویل→تکرار | RND-BUY-001 ۱۳ مرحله |
| فروشنده | ورود→ثبت→KYC→لیست→RFQ پاسخ→PI→حمل→آزادسازی→تمدید | RND-SELL-001 ۱۶ مرحله |
| اختلاف | ادعا→مستندات→حکم→اجرا | TNS-001 §4 |

## ۳) دیکشنری KPI (هر KPI: تعریف/فرمول/منبع رویداد)

| KPI | تعریف | اتصال |
|---|---|---|
| زمان تا اولین پاسخ RFQ | میانگین فاصله rfq_submitted تا اولین quote | SLA CS-001؛ بنچمارک «۲ ساعت» IndiaMART (`سرنخ` RND-003 D32) |
| نرخ گذراندن گیت CMP | سهم hold/reject/escalate | CMP-002 |
| نرخ PSI pass | pass کل PSIها | INSP-001 |
| مدت آزادسازی وجه | funds_held تا released | FIN-002 |
| نرخ اختلاف/برگشت | dispute_open نسبت به delivered | TNS-001 |
| SLA تیکت | درصد پاسخ در مهلت | CS-001 |
| نرخ تکرار سفارش | سفارش دوم/اول | RND-SELL-001 مرحله ۱۶ |

## ۴) SLA و اعتماد به‌عنوان KPI

SLAهای CS-001 (اولین پاسخ) و گیت‌ها به‌صورت KPI پایش می‌شوند؛ اهداف عددی را PM/MGT می‌گذارد (اینجا فقط تعریف).

## ۵) T14

رویدادهای جدید؛ تغییر تعریف KPI (نسخه‌بندی تعریف!) — دیکشنری نسخه‌دار است.

## منابع

FIN-003، ENG-001، TRD-003، RND-SELL/BUY-001، CS-001، TNS-001، RND-003 — accepted 2026-09-27.

## HANDOFF

- به: MGT، PM، ENG
- خودآزمایی: Funnels/SLA/trust/financial چهارگانه ✓؛ رویدادها از FIN-003/ENG-001 ✓؛ مسیر طبق ابلاغ ✓
