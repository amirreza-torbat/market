# فاز طراحی بازارگاه (Design Phase) — مرجع اصلی

- تاریخ شروع: 2026-09-27 | مالک فاز: PM+DES+ENG (پیش‌نویس) | تصمیم نهایی: صاحب‌کار
- ورودی: همه ۳۸ سند qa-pass + داوری دوم (SECOND-REVIEW-LOG) + SYN-001 handoff
- خروجی: معماری کامل سایت — نیازمندی‌ها، نقشه سایت، تجمیع شواهد، و معماری تک‌تک صفحات
- **قاعده فاز:** هیچ اجرایی (کد) در این فاز نیست؛ فقط سند طراحی

## رجیستری تسک‌های فاز طراحی

| شناسه | تسک | خروجی | وضعیت |
|---|---|---|---|
| DSN-001 | شناسایی نیازها از تحقیق | [REQUIREMENTS.md](REQUIREMENTS.md) | ✅ qa-pass |
| DSN-002 | نقشه سایت و معماری اطلاعات (همه صفحات از قبل) | [SITEMAP.md](SITEMAP.md) | ✅ qa-pass |
| DSN-003 | نقشه تجمیع شواهد → صفحات | [EVIDENCE-MAP.md](EVIDENCE-MAP.md) | ✅ qa-pass |
| DSN-004 | معماری صفحات عمومی (P01–P17) | [pages/PUBLIC-PAGES.md](pages/PUBLIC-PAGES.md) | ✅ qa-pass |
| DSN-005 | معماری صفحات احراز + پنل خریدار (A01–B09) | [pages/PANEL-BUYER.md](pages/PANEL-BUYER.md) | ✅ qa-pass |
| DSN-006 | معماری پنل فروشنده (S01–S09) | [pages/PANEL-SUPPLIER.md](pages/PANEL-SUPPLIER.md) | ✅ qa-pass |
| DSN-007 | معماری کنسول عملیات (O01–O07) | [pages/OPS-CONSOLES.md](pages/OPS-CONSOLES.md) | ✅ qa-pass |
| DSN-008 | صفحات سیستم + فلوهای بین‌صفحه‌ای | [pages/SYSTEM-FLOWS.md](pages/SYSTEM-FLOWS.md) | ✅ qa-pass |
| DSN-009 | ماتریس حالت‌ها/خطاها/گیت‌ها در سطح UI | [pages/STATE-MATRIX.md](pages/STATE-MATRIX.md) | ✅ qa-pass |
| DSN-010 | داوری دوم اسناد طراحی | [DESIGN-SECOND-REVIEW.md](DESIGN-SECOND-REVIEW.md) | ✅ pass با ملاحظه (۴ اصلاح اعمال شد) |

## قواعد فاز

1. هر صفحه یک شناسه پایدار دارد (PG-*)؛ هیچ صفحه‌ای بدون شناسه طراحی نمی‌شود.
2. هر بلوک هر صفحه باید به یک سند accepted ارجاع داشته باشد (قابلیت حسابرسی).
3. گیت انطباق (CMP-002) در هر جریان صفحه‌ای که تراکنش/نمایش داده حساس دارد، صریح است.
4. ضدالگوهای RND-009 در طراحی هر صفحه کنترل می‌شوند (نشان بی‌سند، آمار بی‌تاریخ، کارمزد پنهان).
