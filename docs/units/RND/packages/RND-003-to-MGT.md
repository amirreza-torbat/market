# بسته RND-003 به MGT

- از: RND | تاریخ: 2026-09-27 | مرجع: `outbox/RND-003.md`
- COVERED پیشنهادی: «کالبدشکافی Made-in-China.com (با حفره PDP) — عضویت Gold/Diamond، حسابرسی ثالث سریال‌دار، Easy Sourcing»
- تسک بعد پیشنهادی: `RND-004` (Global Sources) پس از qa-pass

## تفاوت‌های کلیدی با Alibaba (برای ماتریس RND-008)

| محور | Made-in-China.com | Alibaba.com (RND-002) |
| --- | --- | --- |
| مرکزیت معامله | دایرکتوری + RFQ تطبیقی؛ معامله عمدتاً بیرون از پلتفرم | مارکت‌پلیس معاملاتی با Start Order و Trade Assurance |
| اعتماد | حسابرسی ثالث سریال‌دار (TÜV/SGS) با گزارش سکشن‌بندی‌شده Initial/Re-audit | Gold Supplier + Trade Assurance (سند پولی) |
| اعلان تجاری تأمین‌کننده | فیلترپذیر: Incoterms FOB/CIF/CFR، پرداخت، گواهی با تاریخ، بازارها | مشابه ولی سطح صفحه متفاوت |
| حفره مشترک | PDP هر دو در استخراج متنی بسته بود | — |

## اقدام درخواستی MGT

1. پس از QA: ثبت COVERED و ابلاغ `RND-004`.
2. مسیر ردیف G02 در `registry/sites.csv` از `secondary` به `opened` ارتقا یابد (مشاهده زنده 2026-09-27).
3. بسته‌ها طبق ROUTING به routed/ واحد‌های بسته ارسال شود.
