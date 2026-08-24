#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIN-002 data builder (reproducible).
Authors the raw CSV artifacts of the funds state machine:
  state_machine.csv   (13 states x 17 fields, incl. the 16 required attributes)
  transitions.csv     (21 transitions with trigger/guard/actor)
  ledger_events.csv   (double-entry event catalogue, ownership -> FIN-003)
  constraints.csv     (sanctions/prohibited/regulatory/approval gates)
Run:  python3 docs/units/FIN/FIN-002/build_fsm_data.py
"""
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))

STATE_FIELDS = [
    "state_id", "state_en", "state_fa", "is_terminal",
    "trigger", "actor", "input", "output", "evidence", "permission",
    "timeout", "transition", "failure_path", "refund_condition",
    "dispute_condition", "ledger_event", "audit_log", "compliance_gate",
    "legal_dependency", "insurance_dependency", "notes",
]
REQ_ATTRS = [
    "trigger", "actor", "input", "output", "evidence", "permission",
    "timeout", "transition", "failure_path", "refund_condition",
    "dispute_condition", "ledger_event", "audit_log", "compliance_gate",
    "legal_dependency", "insurance_dependency",
]

STATES = [
 {
  "state_id":"AUTHORIZE","state_en":"Authorize","state_fa":"مجوز پرداخت","is_terminal":"0",
  "trigger":"خریدار «پرداخت» را برای سفارش قفل‌شده (PO تأییدشده) تأیید می‌کند؛ روش پرداخت از فهرست مجاز FIN-001 انتخاب شده است",
  "actor":"خریدار (شروع‌کننده) + سیستم پرداخت/درگاه یا بانک حواله",
  "input":"شناسه سفارش؛ مبلغ و ارز؛ روش پرداخت (کد M-از FIN-001)؛ جزئیات حساب مقصد/ذی‌نفع؛ لینک PO/پروفرما",
  "output":"مرجع پرداخت (ref) + وضعیت «در انتظار واریز» (بدون جابه‌جایی وجوه)",
  "evidence":"رسید درگاه یا سند حواله (اسکرین‌شات MT103/اعلان بانکی)؛ رکورد PO؛ نتیجه اولیه سندبازار",
  "permission":"روش در فهرست مجاز؛ عدم تطابق با رجیستری prohibited (PR-01..PR-07)؛ مقصد در فهرست کشورهای فعال (امارات = مسدود طبق TRD-006)؛ سندبازار اولیه طرفین",
  "timeout":"پارامتر پیشنهادی FIN: ۲۴ ساعت (درگاه) یا ۳ روز کاری (حواله)؛ پس از آن → CANCELLED (بدون کسر وجه). تأیید نهایی: PM/LEG",
  "transition":"→ HOLD (پرداخت موفق)؛ → CANCELLED (شکست/انقضا)",
  "failure_path":"خطای درگاه/رجوع حواله/عدم تطبیق سندبازار → CANCELLED با پیام شفاف؛ هیچ وجهی جابه‌جا نمی‌شود مگر از مسیر REFUND",
  "refund_condition":"لغو پیش از ورود وجوه → بدون کارمزد؛ هیچ مبلغی هنوز برداشت نهایی نشده",
  "dispute_condition":"ندارد (پیش از شروع؛ هر مغایرت = CANCELLED)؛ در صورت واریز اشتباه از مسیر غیرمجاز → انجماد + گزارش CMP (بدون آزادسازی)",
  "ledger_event":"L01,L02",
  "audit_log":"AUD-001: actor، روش، مبلغ، ارز، مرجع، هش اسناد",
  "compliance_gate":"G1,G2,G3,G4",
  "legal_dependency":"LEG-001 (نقش حقوقی پلتفرم)؛ LEG-003 (PO/پرداخت)؛ تأیید مدل پرداخت توسط LEG و CMP (پیش‌شرط فعال‌سازی درگاه)",
  "insurance_dependency":"ندارد",
  "notes":"گاهی قفل تعهد؛ موج اول کشورها: امارات مسدود = این حالت برای آن مقصد قابل ورود نیست"
 },
 {
  "state_id":"HOLD","state_en":"Hold","state_fa":"نگهداشت وجه (حساب امانی)","is_terminal":"0",
  "trigger":"تأیید واریز/قفل وجوه در حساب امانی نزد بانک (طبق توافق‌نامه امانی) یا کانال نگهداشت مورد تأیید LEG/CMP",
  "actor":"سیستم/امین (پلتفرم) + بانک نگهدارنده (حساب امانی) + CMP (نظارت)",
  "input":"شناسه تراکنش؛ مبلغ؛ ارز؛ شناسه حساب امانی؛ ارکان قرارداد پایه؛ اطلاعات هویتی پرداخت‌کننده/متعهد (ماده ۱۵ دستورالعمل امانی)",
  "output":"موجودی قفل‌شده (hold) + شناسه escrow + بدهی پلتفرم در حساب امانی",
  "evidence":"اعلان/صورتحساب بانکی؛ توافق‌نامه امانی؛ تأیید هویت پرداخت‌کننده؛ مطابقت مبلغ با PO",
  "permission":"**مدل نگهداشت وجه = مسدودکننده تا تأیید کتبی LEG و CMP**؛ حساب امانی فعال؛ رعایت دوره آزمایشی دستورالعمل امانی (تا پایان ۱۴۰۴)؛ بانک نگهدارنده غیرمسدود",
  "timeout":"پارامتر پیشنهادی FIN: حداکثر ۱۸۰ روز نگهداشت؛ تمدید فقط با تأیید MGT+LEG؛ انقضا → EXPIRED",
  "transition":"→ VERIFY (قفل موفق)؛ → EXPIRED (انقضا)",
  "failure_path":"عدم وصول وجوه → CANCELLED؛ مغایرت مبلغ/حساب → انجماد دستی (کارشناس، بدون جابه‌جایی) تا رفع مغایرت",
  "refund_condition":"لغو توافقی پیش از VERIFY → REFUND کامل؛ عدم امکان قفل → بازگشت خودکار (CANCELLED→REFUND)",
  "dispute_condition":"ندارد (وجه بدون ریسک کالا؛ اختلاف بعد از واریز اشتباه = مسیر CMP)",
  "ledger_event":"L02",
  "audit_log":"AUD-002: زمان قفل، مبلغ، ارز، بانک، هش توافق‌نامه",
  "compliance_gate":"G5,G6,G7",
  "legal_dependency":"دستورالعمل ناظر بر حساب امانی CBI (مصوب ۱۶/۰۶/۱۴۰۴، آزمایشی تا پایان ۱۴۰۴)؛ **تأیید LEG برای مدل نگهداشت**؛ LEG-001؛ تأیید CMP",
  "insurance_dependency":"ندارد",
  "notes":"هیچ آزادسازی بدون دستور امین؛ هیچ برداشت برای مقاصد دیگر مجاز نیست"
 },
 {
  "state_id":"VERIFY","state_en":"Verify","state_fa":"احراز و سندبازار","is_terminal":"0",
  "trigger":"ورود وجوه به HOLD؛ شروع فرایند انطباق (KYC/KYB + سندبازار + کنترل کالا) پیش از هر تعهد عملیاتی",
  "actor":"سیستم خودکار + CMP (تصمیم انطباق)؛ FIN (فقط استثنای ثبت‌شده)؛ TRADE (طبقه‌بندی کالا)",
  "input":"اسناد KYB دو طرف؛ ذی‌نفع نهایی؛ بانک‌ها/فورواردر؛ HS/شرح کالا؛ مدارک مبدأ؛ شناسه مجوز (TRD-004/005)؛ داده TBML",
  "output":"پرونده انطباق: وضعیت verified / blocked / در انتظار تکمیل؛ گواهی سندبازار؛ برچسب کشور مقصد",
  "evidence":"نتیجه screening علیه فهرست‌های OFAC SDN/EU/UN؛ گواهی KYB؛ شناسه مجوز مبدأ؛ تطبیق اسناد با کالا (anti-TBML)",
  "permission":"فقط ابزار سندبازار تأییدشده CMP؛ **عدم پذیرش اسناد غیرواقعی**؛ هیچ مسیر «جایگزین» برای گریز از تعلیق امارات یا PR تعریف نمی‌شود",
  "timeout":"پارامتر پیشنهادی FIN: ۲ روز کاری استاندارد؛ سقف ۵ روز کاری؛ پس از آن (بدون تصمیم مستند) → EXPIRED→REFUND",
  "transition":"→ INSPECT (تأیید)؛ → CANCELLED (رد انطباق)",
  "failure_path":"رد سندبازار/تحریم → CANCELLED + گزارش CMP؛ مدارک ناقص → بازگشت به VERIFY (همان حالت، بدون جابه‌جایی وجه)",
  "refund_condition":"رد انطباق → REFUND کامل (وجه هرگز به فروشنده نرفته)؛ بدون جریمه",
  "dispute_condition":"اعتراض به رد انطباق → بررسی CMP (وجه در HOLD می‌ماند)؛ خروجی: ادامه VERIFY یا CANCELLED",
  "ledger_event":"L03",
  "audit_log":"AUD-003: فهرست لیست‌های بررسی‌شده، نتیجه، امضاکننده",
  "compliance_gate":"G1,G2,G3,G4,G8,G9,G10",
  "legal_dependency":"CMP-001 (سندبازار)؛ CMP-002 (کالای حساس/دوکاربرده)؛ LEG-003؛ LEG-004 (داده شخصی)؛ LEG-005 (حوزه قضایی)",
  "insurance_dependency":"ندارد",
  "notes":"گیت مسدودکننده: مقصد=امارات → هرگز VERIFY نمی‌شود (از AUTHORIZE مسدود)"
 },
 {
  "state_id":"INSPECT","state_en":"Inspect","state_fa":"بازرسی (پیش‌تولید/حین‌تولید/پیش‌حمل)","is_terminal":"0",
  "trigger":"پس از VERIFY؛ صدور درخواست بازرسی مطابق INSP-001 (نوع، زمان، معیار از PO)",
  "actor":"INSP (بازرس تأییدشده) + پلتفرم (ضبط و توزیع شواهد)؛ TRADE (مشخصات کالا)",
  "input":"درخواست بازرسی؛ مشخصات PO؛ معیار کیفیت/کمیّت؛ آدرس/زمان؛ کد سفارش",
  "output":"گزارش بازرسی دیجیتال با نتیجه pass / fail / hold + بسته شواهد",
  "evidence":"گزارش امضاشده؛ عکس/ویدئو/آزمون؛ شناسه بازرس؛ تطبیق با PO؛ نتیجه در قالب «سند بانکی» (پل FIN-001 F6)",
  "permission":"بازرس/نهاد تأییدشده (INSP-001)؛ قالب گزارش = سند قابل‌ارائه در LC/وصولی/اسکرو؛ بدون تأیید خارج از مسیر",
  "timeout":"پارامتر پیشنهادی FIN: ۵ روز کاری گزارش؛ سقف ۱۰ روز کاری؛ پس از آن → DISPUTE (یا REFUND توافقی). تصمیم نهایی: INSP",
  "transition":"→ SHIP (pass)؛ → REFUND (fail + توافق)؛ → DISPUTE (اختلاف کیفیت)",
  "failure_path":"fail → DISPUTE (در صورت ادعای خریدار) یا REFUND (توافق/فسخ توافقی)؛ گزارش ناقص → بازگشت به INSPECT",
  "refund_condition":"fail تأییدشده + توافق → REFUND کامل؛ انصراف خریدار پیش از حمل → REFUND منهای هزینه‌های واقعی قابل‌اثبات (تأیید LEG)",
  "dispute_condition":"ادعای عدم تطابق کیفیت/کمیّت (مستند به گزارش) از خریدار → DISPUTE؛ ادعای جعلی‌بودن گزارش از فروشنده → DISPUTE (بازبینی مستقل)",
  "ledger_event":"L04,L11",
  "audit_log":"AUD-004: شناسه گزارش، هش، امضا، تصمیم",
  "compliance_gate":"G11,G12",
  "legal_dependency":"LEG-003 (معیار کیفیت/عهده‌داری)؛ INSP-001 (قالب/رویه بازرسی)",
  "insurance_dependency":"بیمه مسئولیت بازرس: «داده در دسترس نبود» (نیازمند استعلام INSP/INS؛ خارج از این تسک)",
  "notes":"گزارش بازرسی باید خروجی INSP و ورودی اسنادی SHIP/RELEASE باشد"
 },
 {
  "state_id":"SHIP","state_en":"Ship","state_fa":"حمل (خروج از گمرک مبدأ)","is_terminal":"0",
  "trigger":"نتیجه INSPECT=pass؛ صدور اسناد حمل و اظهار گمرک مبدأ؛ ثبت Incoterms (TRD-003)",
  "actor":"فروشنده/فورواردر (اجرا) + گمرک مبدأ (اظهار) + پلتفرم (ثبت وضعیت)",
  "input":"بارنامه/CMR/AWB (on board)؛ گواهی مبدأ؛ اظهار/کوتاژ گمرکی؛ بیمه‌نامه حمل؛ مشخصات Incoterms؛ شناسه مجوز",
  "output":"status SHIPPED + بسته اسناد حمل (برای انتقال به مقصد)",
  "evidence":"B/L یا AWB یا CMR با یادداشت on board؛ گواهی مبدأ؛ بیمه‌نامه؛ کوتاژ؛ تطبیق فاکتور/پکینگ/بارنامه (TRD-003)",
  "permission":"حمل‌کننده و کشور ترانزیت سندبازاری؛ کالای مجاز (نه دوکاربرده بدون مجوز)؛ **عدم استفاده از شرکت‌های حمل مسدود (IRISL و مشمولان Annex EU 267/2012)**؛ مقصد مجاز",
  "timeout":"پارامتر پیشنهادی FIN: ۳۰ روز از تأیید بازرسی برای بارگیری (قابل تغییر در قرارداد)؛ عدم بارگیری → DISPUTE یا REFUND توافقی",
  "transition":"→ DELIVERY (بارگیری)؛ → DISPUTE (تأخیر/نقض)؛ → REFUND (فسخ توافقی پیش از حمل)",
  "failure_path":"رد گمرک مبدأ/مقصد؛ تحریم/توقف مسیر؛ امتناع حمل‌کننده → DISPUTE (بررسی) یا CANCELLED→REFUND در صورت غیرممکن‌بودن ادامه",
  "refund_condition":"فسخ توافقی پیش از حمل → REFUND منهای هزینه‌های قابل‌اثبات؛ **توقف مسیر به دلیل تحریم → REFUND کامل** (بدون جریمه؛ تأیید LEG)",
  "dispute_condition":"تأخیر بیش از مهلت؛ مغایرت اسناد با کالا (اظهارشده)؛ رد گمرکی → DISPUTE",
  "ledger_event":"L05,L12",
  "audit_log":"AUD-005: شماره بارنامه، تاریخ، گمرک، بیمه",
  "compliance_gate":"G13,G14,G15",
  "legal_dependency":"TRD-003 (Incoterms/فورواردر)؛ LEG-003 (شرط حمل)؛ قوانین گمرک مبدأ/مقصد؛ EU 267/2012 (حمل مسدود)",
  "insurance_dependency":"INS-001: بیمه‌نامه حمل مطابق Incoterms (ذی‌نفع طبق قرارداد) — برای کالای مشمول، پیش‌نیاز ورود به DELIVERY",
  "notes":"بدون بیمه‌نامه معتبر برای کالای مشمول → ورود به DELIVERY مجاز نیست"
 },
 {
  "state_id":"DELIVERY","state_en":"Delivery","state_fa":"تحویل (ورود/رسید مقصد)","is_terminal":"0",
  "trigger":"ثبت شواهد تحویل/ورود به مقصد (POD، اظهار گمرک مقصد، نتیجه ترکینگ)",
  "actor":"حمل‌کننده/فورواردر (شواهد) + گمرک مقصد + پلتفرم (ثبت)",
  "input":"POD/رسید تحویل؛ اظهارنامه ورود مقصد؛ ترکینگ؛ نتیجه بازرسی گمرکی مقصد (در صورت)",
  "output":"status DELIVERED + خلاصه اسناد مقصد",
  "evidence":"POD/رسید؛ اظهارنامه ورود؛ ترکینگ؛ عکس/گزارش پذیرش انبار مقصد (فیلدها از TRD-006/TRD-003)",
  "permission":"مقصد مجاز (امارات مسدود)؛ تطبیق با Incoterms؛ ورود فقط پس از ترخیص/تأیید گمرکی مقصد",
  "timeout":"پارامتر پیشنهادی FIN: تحویل تا ۷ روز کاری پس از ETA (ترکینگ)؛ عدم تحویل → DISPUTE",
  "transition":"→ ACCEPT (تحویل سالم)؛ → DISPUTE (گم‌شدن/آسیب/نقص/تأخیر حمل)",
  "failure_path":"گم‌شدن/آسیب/نقص → DISPUTE + اقدام بیمه حمل (INS)؛ رد گمرکی مقصد → DISPUTE/REFUND بر اساس علت",
  "refund_condition":"عدم تحویل در مهلت (با شواهد) → REFUND کامل؛ آسیب جزئی → DISPUTE (کاهش قیمت/تعمیر/جایگزینی)",
  "dispute_condition":"آسیب/نقص/کمیّت در زمان تحویل (POD + گزارش) → DISPUTE؛ اختلاف روی علت → شواهد حمل و بیمه",
  "ledger_event":"L06",
  "audit_log":"AUD-006: POD، تاریخ، گمرک، تریپ",
  "compliance_gate":"G16,G17",
  "legal_dependency":"LEG-003 (نحوه تحویل/رسید)؛ INCOTERMS؛ قوانین گمرک مقصد",
  "insurance_dependency":"فعال‌سازی احتمالی مطالبه بیمه حمل (در صورت خسارت)؛ سند خسارت برای DISPUTE",
  "notes":"«تحویل» فقط با شواهد؛ تأیید خریدار در ACCEPT است نه DELIVERY"
 },
 {
  "state_id":"ACCEPT","state_en":"Accept","state_fa":"پذیرش (یا پذیرش ضمنی)","is_terminal":"0",
  "trigger":"ورود به وضعیت تحویل‌شده؛ شروع پنجره پذیرش خریدار (زمان‌بندی طبق قرارداد)",
  "actor":"خریدار (تصریح) + سیستم (پذیرش ضمنی/مرور زمان)",
  "input":"اعلام پذیرش/عدم پذیرش؛ گزارش بازرسی مقصد (در صورت)؛ اسناد POD",
  "output":"پذیرش (بازکردن مسیر RELEASE) یا اعتراض مستند (مسیر DISPUTE)",
  "evidence":"پذیرش صریح یا گذشت پنجره (deemed acceptance)؛ گزارش بازرسی مقصد؛ ثبت‌های AUD-007",
  "permission":"فقط خریدارِ ثبت‌شده در سفارش؛ شرط deemed acceptance باید در LEG-003/قرارداد باشد؛ اعتراض فقط با شاهد",
  "timeout":"پارامتر پیشنهادی FIN: ۵ روز کاری پنجره پذیرش (LEG تصمیم نهایی)؛ پس از آن پذیرش ضمنی",
  "transition":"→ RELEASE (پذیرش/ضمنی)؛ → DISPUTE (اعتراض مستند)",
  "failure_path":"اعتراض خریدار → DISPUTE (وجه در HOLD می‌ماند)؛ هیچ آزادسازی پیش از خاتمه اعتراض",
  "refund_condition":"پس از DISPUTE/RESOLUTION در صورت رد کیفیت مستند → REFUND (کل یا جزئی طبق حکم)",
  "dispute_condition":"هر اعتراض رسمی خریدار در پنجره (کیفیت/کمیّت/زمان/اسناد) با شاهد اولیه → DISPUTE؛ اعتراض بدون شاهد → رد (ثبت در AUD)",
  "ledger_event":"L07",
  "audit_log":"AUD-007: زمان پنجره، اقدام، نتیجه",
  "compliance_gate":"G18",
  "legal_dependency":"LEG-003 (شرایط پذیرش/کمیّت)؛ LEG-005 (حوزه قضایی اختلاف)",
  "insurance_dependency":"در مدل پرداخت معوق (M04/M08): بیمه اعتبار صادراتی می‌تواند مرجع ریسک عدم‌پذیرش باشد (پیش‌نیاز: FIN-001 M12)",
  "notes":"پذیرش ضمنی = عبور زمان؛ هر اعتراض پس از پایان پنجره خارج از ماشین (مسیر حقوقی)"
 },
 {
  "state_id":"RELEASE","state_en":"Release","state_fa":"آزادسازی به فروشنده","is_terminal":"1",
  "trigger":"ACCEPT یا حکم RESOLUTION به‌نفع فروشنده؛ صدور دستور پرداخت امین",
  "actor":"امین/سیستم + بانک (اجرای پرداخت)؛ FIN (ثبت تسویه)",
  "input":"دستور پرداخت امین (مطابق توافق‌نامه امانی)؛ تأیید سندبازار نهایی؛ اطلاعات حساب فروشنده؛ کد تسویه",
  "output":"واریز به فروشنده + تسویه کارمزدها + ثبت وضعیت «رفع تعهد ارزی» (هم‌راستا با مسیر مجاز)",
  "evidence":"تأییدیه بانک پرداخت؛ سند آزادسازی؛ فاکتور نهایی؛ کوتاژ/مدارک نیما (در مسیر مجاز)",
  "permission":"آزادسازی = تنها با دستور امین؛ **مدل تأییدشده LEG/CMP**؛ حساب فروشنده غیرمسدود؛ سندبازار مجدد (لغو تحریم جدید)؛ کارمزد طبق قرارداد",
  "timeout":"پارامتر پیشنهادی FIN: پرداخت T+2 روز کاری پس از پذیرش؛ شکست پرداخت → retry (حداکثر ۲ بار)؛ ۳ شکست → DISPUTE (با قفل وجه)",
  "transition":"→ پایانه (released)؛ شکست → retry در RELEASE یا → DISPUTE (خطای بانک/مسیر)",
  "failure_path":"رد پرداخت بانک/مسدودی حساب فروشنده/تغییر سندبازار → retry یا DISPUTE؛ هیچ آزادسازی ناقص/بدون تسویه",
  "refund_condition":"پس از آزادسازی فقط از مسیر حقوقی (خارج از ماشین)؛ خطای سامانه‌ای (واژگونی پرداخت بدون مبنا) → اصلاح با تأیید MGT+LEG",
  "dispute_condition":"ادعای پس از آزادسازی = خارج از ماشین (مرجع LEG-005)؛ ماشین در این نقطه می‌بندد",
  "ledger_event":"L08,L10,L12",
  "audit_log":"AUD-008: دستور امین، مرجع بانک، زمان، کارمزد",
  "compliance_gate":"G1,G18,G19,G20",
  "legal_dependency":"LEG-001 (مسئولیت امانت)؛ LEG-003؛ دستورالعمل امانی؛ تأیید LEG/CMP",
  "insurance_dependency":"در صورت پوشش بیمه اعتبار برای معوق: هماهنگی با صندوق پیش از تسویه (سند)",
  "notes":"پایانه ماشین؛ تسویه کارمزد/FX/مالیات = مالک FIN-003"
 },
 {
  "state_id":"REFUND","state_en":"Refund","state_fa":"بازگشت وجه به خریدار","is_terminal":"1",
  "trigger":"تصمیم REFUND از هر حالت پیش از RELEASE؛ حکم DISPUTE/RESOLUTION؛ انقضا (EXPIRED→REFUND)؛ لغو (CANCELLED→REFUND)",
  "actor":"امین/سیستم + بانک؛ CMP (سندبازار مقصد بازگشت)",
  "input":"دستور بازگشت؛ حساب مبدأ خریدار؛ کد علت (K1..K7)؛ اسناد تصمیم؛ در صورت جزئی: محاسبه سهم",
  "output":"بازگشت وجه + بستن سفارش + ثبت علت",
  "evidence":"تأییدیه بانک بازگشت؛ قرارداد/حکم؛ کد علت؛ محاسبات منصفانه",
  "permission":"فقط با علت مستند؛ **بازگشت به حساب مبدأ و ذی‌نفع اصلی**؛ هیچ مسیر بازگشت غیرمجاز؛ هیچ «جبران» با ارز/مکان دیگر بدون تأیید LEG/CMP",
  "timeout":"پارامتر پیشنهادی FIN: T+5 روز کاری پس از دستور؛ شکست → retry (۲ بار)؛ ۳ شکست → گزارش MGT + قفل دستی",
  "transition":"→ پایانه (refunded)؛ در REFUND جزئی → RESOLUTION (تسویه باقی) یا RELEASE (سهم فروشنده)",
  "failure_path":"شکست بانک/معتبر نبودن حساب مقصد → retry؛ سپس قفل دستی (بدون جابه‌جایی) + گزارش",
  "refund_condition":"K1 لغو پیش از ورود؛ K2 رد انطباق؛ K3 فسخ توافقی؛ K4 fail بازرسی؛ K5 عدم تحویل؛ K6 حکم RESOLUTION؛ K7 انقضای HOLD/VERIFY",
  "dispute_condition":"اختلاف روی «میزان» بازگشت (جزئی) → RESOLUTION؛ بازگشت فقط پس از خاتمه اختلاف",
  "ledger_event":"L09,L13",
  "audit_log":"AUD-009: علت، مرجع بانک، زمان، کد",
  "compliance_gate":"G21,G22",
  "legal_dependency":"LEG-003 (مرجوعی/فسخ)؛ LEG-001؛ دستورالعمل امانی",
  "insurance_dependency":"در خسارت بیمه‌شده: subrogation/هماهنگی با بیمه‌گر پیش از بازگشت (سند)",
  "notes":"REFUND جزئی: از مسیر RESOLUTION با تسویه دوبخشی"
 },
 {
  "state_id":"DISPUTE","state_en":"Dispute","state_fa":"اختلاف (قفل وجه)","is_terminal":"0",
  "trigger":"اعتراض رسمی هر طرف (کیفیت/کمیّت/تأخیر/اسناد/نقص تحویل) با شاهد اولیه؛ از INSPECT/SHIP/DELIVERY/ACCEPT یا شکست RELEASE",
  "actor":"طرفین + پلتفرم/داور مرحله اول + INSP (نظر فنی)؛ LEG (در صورت ارجاع)",
  "input":"درخواست داوری + شواهد (گزارش بازرسی/POD/قرارداد/مکاتبات) + مبلغ در اختلاف",
  "output":"پرونده اختلاف + نتیجه مرحله: حل، ارجاع، توافق",
  "evidence":"گزارش بازرسی؛ POD؛ قرارداد؛ مکاتبات؛ گزارش تطبیق اسناد؛ رأی/توافق",
  "permission":"فقط با قفل کامل وجه؛ هیچ آزادسازی تا خاتمه؛ داوری طبق شرط LEG-003/005؛ پلتفرم داور مرحله اول است نه مرجع نهایی",
  "timeout":"پارامتر پیشنهادی FIN: مذاکره ۱۰ روز کاری؛ سپس ارجاع به RESOLUTION؛ عدم پاسخ = deemed rejection (ثبت)",
  "transition":"→ RESOLUTION (بدون توافق)؛ → RELEASE (توافق/پذیرش)؛ → REFUND (توافق/بازگشت)",
  "failure_path":"عدم ارائه شاهد از مدعی → بستن اعتراض (بازگشت به مسیر قبلی)؛ امتناع از پاسخ → deemed؛ هر دو → RESOLUTION",
  "refund_condition":"توافق بازگشت (کل/جزئی) → REFUND (با سهم‌بندی)",
  "dispute_condition":"ورود: ادعا + شاهد اولیه + کد موضوع؛ آستانه/فرم داوری = پیشنهاد LEG (خارج از این تسک)",
  "ledger_event":"L14,L15",
  "audit_log":"AUD-010: درخواست، شواهد، مذاکرات، نتیجه",
  "compliance_gate":"G23",
  "legal_dependency":"LEG-003 (شرایط اختلاف)؛ LEG-005 (داوری/قانون حاکم)؛ CMP (در صورت ادعای تقلب)",
  "insurance_dependency":"بیمه حمل/اعتبار: مرجع فنی خسارت؛ سند subrogation در صورت وجود",
  "notes":"وجه در HOLD باقی می‌ماند؛ هیچ «تسویه پنهان» یا جبران خارجی مجاز نیست"
 },
 {
  "state_id":"RESOLUTION","state_en":"Resolution","state_fa":"حل نهایی (میانجی/داوری)","is_terminal":"1",
  "trigger":"عدم توافق در DISPUTE؛ ارجاع به مرحله نهایی طبق شرط داوری قرارداد (LEG-005)",
  "actor":"مرجع تعیین‌شده (داور/میانجی) + طرفین + پلتفرم (اجرای حکم)",
  "input":"پرونده کامل + رأی/توافق‌نامه؛ محاسبه تسویه (کل/جزئی)",
  "output":"حکم نهایی: release کامل / refund کامل / جزئی+جزئی",
  "evidence":"رأی کتبی؛ توافق‌نامه؛ محاسبه؛ تطبیق با قانون حاکم",
  "permission":"پلتفرم فقط مجری حکم است؛ هیچ اصلاح/تخفیف/شرط اضافه بدون رأی؛ اجرا از مسیرهای مجاز",
  "timeout":"پارامتر پیشنهادی FIN: ۳۰ روز کاری برای داوری ساده؛ طبق قرارداد/قانون حاکم؛ پس از آن متناسب با LEG-005",
  "transition":"→ RELEASE (به‌نفع فروشنده)؛ → REFUND (به‌نفع خریدار)؛ → REFUND+RELEASE (تسویه جزئی دوبخشی)",
  "failure_path":"عدم اجرای حکم → escalation به MGT + مرجع حقوقی (خارج از ماشین)",
  "refund_condition":"طبق حکم (کل/جزئی)؛ تسویه جزئی با سهم‌بندی مستند",
  "dispute_condition":"حکم نهایی است؛ ادعای بعدی = خارج از ماشین",
  "ledger_event":"L16,L17,L18",
  "audit_log":"AUD-011: رأی، امضا، محاسبه، اجرا",
  "compliance_gate":"G24,G25",
  "legal_dependency":"LEG-005؛ LEG-003؛ قانون حاکم/داوری",
  "insurance_dependency":"حصه خسارت بیمه‌گر (در صورت) پیش از تسویه؛ سند",
  "notes":"پایانه؛ هیچ مسیر غیرقانونی به‌عنوان «حل» مجاز نیست"
 },
 {
  "state_id":"CANCELLED","state_en":"Cancelled","state_fa":"لغو (بستن بدون آزادسازی)","is_terminal":"0",
  "trigger":"شکست AUTHORIZE/VERIFY؛ رد انطباق؛ لغو پیش از HOLD/SHIP؛ تشخیص تحریم/PR؛ خطای بانکی غیرقابل رفع",
  "actor":"سیستم (خودکار برای انقضا) + CMP/MGT (تصمیمی)؛ طرفین (لغو توافقی)",
  "input":"کد علت؛ اسناد؛ در صورت وجه: دستور بازگشت",
  "output":"بستن سفارش + (در صورت وجود وجه) مسیر REFUND",
  "evidence":"کد علت + مستندات + تأیید CMP در موارد انطباقی",
  "permission":"هیچ بستنی با وجه بدون REFUND؛ **هیچ مسیر جایگزین غیرقانونی**؛ تعلیق امارات/PR = مسدود مستقیم، بدون workaround",
  "timeout":"فوری (تصمیمی) یا خودکار پس از timeout های AUTHORIZE/VERIFY",
  "transition":"→ REFUND (در صورت وجود وجه در HOLD)؛ بدون خروج دیگر",
  "failure_path":"— (پایانه بستن)؛ هر ناهماهنگی دستی → گزارش MGT",
  "refund_condition":"هر وجه نگهداری‌شده → بازگشت کامل (K1/K2/K3/K7)",
  "dispute_condition":"ندارد",
  "ledger_event":"L19",
  "audit_log":"AUD-012: کد علت، امضا، زمان",
  "compliance_gate":"G26",
  "legal_dependency":"LEG-003 (فسخ)؛ CMP-003",
  "insurance_dependency":"—",
  "notes":"مسدودی مقصد/تحریم = CANCELLED، نه «مسیر جایگزین»"
 },
 {
  "state_id":"EXPIRED","state_en":"Expired","state_fa":"انقضا (timeout)","is_terminal":"0",
  "trigger":"انقضای مهلت HOLD (۱۸۰ روز) یا VERIFY (۵ روز کاری) بدون تصمیم مستند",
  "actor":"سیستم خودکار (فقط انقضا) + FIN (ثبت) + MGT (اطلاع)",
  "input":"کد timeout؛ مبلغ؛ زمان‌ها",
  "output":"بستن + REFUND خودکار (در صورت وجوه)",
  "evidence":"timestamps سیستم؛ گزارش خودکار",
  "permission":"فقط برای timeout (خودکار)؛ هیچ انقضای دستی؛ تمدید فقط با تأیید MGT+LEG پیش از انقضا",
  "timeout":"مطابق تعریف حالت (HOLD: ۱۸۰ روز؛ VERIFY: ۵ روز کاری)",
  "transition":"→ REFUND (خودکار)؛ بدون خروج دیگر",
  "failure_path":"—؛ در صورت شکست REFUND → قفل دستی + گزارش",
  "refund_condition":"K7: بازگشت کامل بدون جریمه (تقصیر زمان نیست)",
  "dispute_condition":"ندارد",
  "ledger_event":"L19",
  "audit_log":"AUD-012: کد timeout، زمان‌ها",
  "compliance_gate":"G26",
  "legal_dependency":"دستورالعمل امانی (مهلت)؛ LEG-003",
  "insurance_dependency":"—",
  "notes":"پیشنهادهای زمان = پارامترهای قراردادی؛ تأیید LEG/PM"
 },
]

TRANSITIONS = [
 # from, to, trigger, guard, actor, note
 ("AUTHORIZE","HOLD","واریز/قفل موفق وجه (درگاه یا حواله)","روش مجاز؛ سندبازار اولیه؛ مقصد فعال","خریدار/سیستم/بانک","ورود به نگهداشت امانی"),
 ("AUTHORIZE","CANCELLED","شکست پرداخت/انقضای مهلت/رد سندبازار اولیه","بدون وجه جابه‌جا شده","سیستم/CMP","بستن فارغ از وجه"),
 ("HOLD","VERIFY","قفل وجوه تأیید شد","تأیید LEG/CMP برای مدل نگهداشت؛ حساب امانی فعال","امین/سیستم","شروع احراز"),
 ("HOLD","EXPIRED","انقضای ۱۸۰ روز نگهداشت","بدون تصمیم مستند تمدید","سیستم خودکار","بازگشت خودکار در راه"),
 ("VERIFY","INSPECT","نتیجه سندبازار = verified","کالا مجاز؛ مقصد مجاز؛ شناسه مجوز","CMP/سیستم","آماده بازرسی"),
 ("VERIFY","CANCELLED","رد سندبازار/تحریم/PR","کد CMP","CMP","بستن + گزارش"),
 ("INSPECT","SHIP","نتیجه بازرسی = pass","گزارش معتبر؛ قالب سند","INSP/سیستم","شروع حمل"),
 ("INSPECT","REFUND","نتیجه بازرسی = fail + توافق","کد K4","طرفین/سیستم","بازگشت کامل"),
 ("INSPECT","DISPUTE","ادعای عدم تطابق (کیفیت/کمیّت)","شاهد اولیه + کد موضوع","خریدار/سیستم","قفل وجه"),
 ("SHIP","DELIVERY","بارنامه on board + بیمه + اظهار گمرک","Incoterms مجاز؛ حمل‌کننده سندبازاری؛ بیمه معتبر (کالای مشمول)","فروشنده/فورواردر/سیستم","مدارک مقصد"),
 ("SHIP","DISPUTE","تأخیر/نقض/رد گمرکی/مغایرت اسناد","شاهد (کد موضوع)","طرفین/سیستم","قفل وجه"),
 ("SHIP","REFUND","فسخ توافقی پیش از حمل","کد K3 + هزینه‌های قابل‌اثبات","طرفین/سیستم","بازگشت منهای هزینه واقعی"),
 ("DELIVERY","ACCEPT","POD/اظهار ورود مقصد ثبت شد","مقصد مجاز؛ گمرک مقصد تأیید","سیستم/حمل‌کننده","شروع پنجره پذیرش"),
 ("DELIVERY","DISPUTE","گم‌شدن/آسیب/نقص/تأخیر","شاهد POD+گزارش","طرفین/سیستم","قفل وجه + بیمه"),
 ("ACCEPT","RELEASE","پذیرش صریح یا ضمنی","پنجره تمام؛ سندبازار نهایی","سیستم/خریدار","آزادسازی"),
 ("ACCEPT","DISPUTE","اعتراض مستند خریدار","شاهد + کد موضوع","خریدار/سیستم","قفل وجه"),
 ("DISPUTE","RESOLUTION","عدم توافق در مذاکره (۱۰ روز کاری)","شرط داوری LEG-005","طرفین/مرجع","داوری"),
 ("DISPUTE","RELEASE","توافق/پذیرش (به‌نفع فروشنده)","توافق‌نامه","طرفین/سیستم","آزادسازی"),
 ("DISPUTE","REFUND","توافق/بازگشت (به‌نفع خریدار)","توافق‌نامه","طرفین/سیستم","بازگشت"),
 ("RESOLUTION","RELEASE","حکم به‌نفع فروشنده","رأی کتبی؛ سندبازار نهایی","مرجع/سیستم","پایانه"),
 ("RESOLUTION","REFUND","حکم به‌نفع خریدار","رأی کتبی","مرجع/سیستم","پایانه"),
 ("CANCELLED","REFUND","وجود وجه در HOLD هنگام بستن","کد علت (K1/K2/K7)","سیستم","بازگشت کامل"),
 ("EXPIRED","REFUND","انقضای مهلت (خودکار)","کد K7","سیستم","بازگشت کامل"),
]

# resolution partial: same REFUND+RELEASE pair — represented by RESOLUTION->REFUND then RESOLUTION->RELEASE both used in one settlement (documented in ledger L17/L18)

LEDGER_EVENTS = [
 # event_id, state, side, debit_account, credit_account, amount_rule, trigger, owner, note
 ("L01","AUTHORIZE","info","—","—","مبلغ سفارش (ارز قرارداد)","ثبت درخواست پرداخت","FIN-003","ثبت، بدون جابه‌جایی"),
 ("L02","HOLD","debit/credit","escrow_pool (بانک امانی)","platform_liability (escrow)","مبلغ قفل‌شده = مبلغ سفارش","قفل وجوه","FIN-003","تعادل دوطرفه"),
 ("L03","VERIFY","info","—","—","—","نتیجه سندبازار","FIN-003","ثبت پرونده"),
 ("L04","INSPECT","info","—","—","—","نتیجه بازرسی","FIN-003","ثبت گزارش"),
 ("L05","SHIP","info","—","—","—","اسناد حمل","FIN-003","ثبت بسته اسناد"),
 ("L06","DELIVERY","info","—","—","—","POD/اظهار ورود","FIN-003","ثبت تحویل"),
 ("L07","ACCEPT","info","—","—","—","پذیرش/ضمنی","FIN-003","ثبت پذیرش"),
 ("L08","RELEASE","debit/credit","platform_liability (escrow)","seller_receivable / payout","مبلغ خالص = مبلغ سفارش − کارمزدها","دستور امین","FIN-003","آزادسازی"),
 ("L09","REFUND","debit/credit","platform_liability (escrow)","buyer_refund_pool","مبلغ بازگشت (کل/جزئی)","دستور بازگشت","FIN-003","بازگشت"),
 ("L10","RELEASE","fee","seller_receivable","platform_revenue","کارمزد پلتفرم (قرارداد)","تسویه","FIN-003","کارمزد"),
 ("L11","INSPECT","fee","escrow_pool","inspector_receivable","هزینه بازرسی (در صورت)","گزارش بازرسی","FIN-003","هزینه بازرسی"),
 ("L12","SHIP","fee","escrow_pool","insurer_receivable","حق بیمه حمل (در صورت)","صدور بیمه‌نامه","FIN-003","حق بیمه"),
 ("L13","REFUND","fee","—","—","کارمزد بازگشت (طبق قرارداد؛ خطای پلتفرم = صفر)","بازگشت","FIN-003","پیشنهاد: بدون کارمزد برای کدهای پلتفرمی"),
 ("L14","DISPUTE","info","—","—","مبلغ در اختلاف","ورود اختلاف","FIN-003","قفل اختلاف"),
 ("L15","DISPUTE","reserve","escrow_pool","dispute_reserve","سهم در اختلاف (در صورت جزئی)","قفل اختلاف","FIN-003","رزرو"),
 ("L16","RESOLUTION","info","—","—","محاسبه حکم","حکم","FIN-003","ثبت حکم"),
 ("L17","RESOLUTION","debit/credit","dispute_reserve","seller_receivable","سهم فروشنده طبق حکم","تسویه داوری","FIN-003","بخش فروشنده"),
 ("L18","RESOLUTION","debit/credit","dispute_reserve","buyer_refund_pool","سهم خریدار طبق حکم","تسویه داوری","FIN-003","بخش خریدار"),
 ("L19","CANCELLED/EXPIRED","info","—","—","—","بستن/انقضا","FIN-003","ثبت خاتمه"),
]

CONSTRAINTS = [
 # gate_id, type, source_ref, applies_to, gate_behavior, legal_dependency, note
 ("G1","sanctions","OFAC SDN / EU 267/2012 Annexes؛ FIN-001 S5,S7","ALL (هر تراکنش)","بلوک در صورت تطبیق؛ هیچ‌گونه معامله با طرف مسدود","LEG/CMP-001","سندبازار در ورود و آزادسازی"),
 ("G2","sanctions","تعلیق تجارت/مبادلات مالی امارات با ایران — TRD-006","AUTHORIZE,VERIFY,SHIP,DELIVERY","مقصد=امارات → مسدود مطلق؛ بدون استثنا تا ابلاغ رسمی","LEG/CMP؛ TRD-006","ثبت به‌عنوان constraint؛ هیچ مسیر جایگزین ممنوع است"),
 ("G3","prohibited","FIN-001 رجیستری PR-01..PR-07","ALL","روش مطابق PR → غیرقابل انتخاب/بلوک","CMP/LEG","رجیستری prohibited به‌عنوان گیت"),
 ("G4","prohibited","ITSR §560.203 (ممنوعیت دور زدن)؛ EU 267/2012","ALL","هر الگوی «نشان‌سازی مجدد/پنهان‌سازی» → بلوک + گزارش","LEG/CMP","عدم طراحی هر مسیر گریز"),
 ("G5","regulatory","دستورالعمل حساب امانی CBI (مصوب ۱۶/۰۶/۱۴۰۴)","HOLD,RELEASE,REFUND","فقط با تأیید کتبی LEG و CMP (مسدودکننده)","LEG؛ دستورالعمل امانی","مدل نگهداشت بدون تأیید = غیرقابل فعال‌سازی"),
 ("G6","regulatory","بانک نگهدارنده غیرمسدود","HOLD","بانک مسدود → بلوک؛ هیچ‌جاگزینی غیرمجاز","CMP","بانک حساب امانی سندبازاری"),
 ("G7","regulatory","ماده ۱۱ (AML/CFT) و ماده ۱۵ (هویت پرداخت‌کننده)","HOLD,REFUND","عدم تطبیق هویت → بلوک/بازگشت","LEG","قابلیت ردیابی الزامی"),
 ("G8","regulatory","CMP-002 (کالای حساس/دوکاربرده)","VERIFY,SHIP","کالای مشمول بدون مجوز → بلوک","CMP","کنترل صادرات"),
 ("G9","regulatory","کشور ترانزیت مجاز (سندبازاری)","SHIP","ترانزیت مسدود → بلوک/توقف","CMP","فورواردر سندبازاری"),
 ("G10","regulatory","EU 267/2012 Annex (IRISL و حمل‌کننده‌های مسدود)","SHIP","حمل‌کننده مسدود → بلوک","CMP/LEG","عدم استفاده از ناوگان مسدود"),
 ("G11","product","INSP-001 (بازرس تأییدشده)","INSPECT","بازرس غیرتأیید → بلوک","INSP/LEG","قالب گزارش استاندارد"),
 ("G12","product","انطباق مقصد (ESMA/MoIAT/Montaji برای مقاصد مشمول)","INSPECT","نداشتن انطباق → بلوک (برای مقاصد غیرمعلق مجاز)","TRADE/LEG","مطابق TRD-006؛ امارات فعلاً مسدود"),
 ("G13","product","تطبیق اسناد حمل (فاکتور/پکینگ/بارنامه) — TRD-003","SHIP","مغایرت اسناد → بلوک/ارجاع","TRADE","چک‌لیست پیش از ارسال"),
 ("G14","regulatory","گمرک مبدأ (اظهار/کوتاژ)","SHIP","اظهار ناقص → بلوک","TRADE","کوتاژ برای رفع تعهد ارزی"),
 ("G15","sanctions","بازبینی مسیر/حمل‌کننده در لحظه حمل (تکمیل G9/G10)","SHIP","تغییر/توقف مسیر → بلوک","CMP","کنترل لحظه‌ای"),
 ("G16","sanctions","مقصد مجاز (فهرست فعال؛ امارات مسدود)","DELIVERY","مقصد غیرمجاز → بلوک","CMP/LEG","—"),
 ("G17","product","تطبیق Incoterms/اسناد مقصد","DELIVERY","مغایرت → بلوک/ارجاع","TRADE/LEG","—"),
 ("G18","sanctions","سندبازار مجدد پیش از پرداخت","ACCEPT,RELEASE","هر تطبیق جدید → بلوک/بازگشت","CMP","قبل از هر پول"),
 ("G19","sanctions","مسیر پرداخت مجاز (نه بانک مسدود)","RELEASE","—","CMP","—"),
 ("G20","regulatory","رفع تعهد ارزی (مصوبه ۱۳۹۷/۱۳۹۸؛ سامانه نیما/سنا)","RELEASE","ثبت وضعیت رفع تعهد؛ عدم ثبت → هشدار/بلوک جزئی","CBI/TRADE","مشترک همه روش‌ها"),
 ("G21","regulatory","بازگشت به حساب مبدأ/ذی‌نفع اصلی","REFUND","تغییر ذی‌نفع → بلوک","CMP/LEG","—"),
 ("G22","sanctions","سندبازار حساب مقصد بازگشت","REFUND","—","CMP","—"),
 ("G23","legal","LEG-003/LEG-005 (شرط داوری)","DISPUTE","بدون شرط داوری → پرونده ناقص","LEG","—"),
 ("G24","legal","اجرای حکم + سندبازار نهایی","RESOLUTION","—","LEG/CMP","—"),
 ("G25","prohibited","هیچ تسویه به مسیر غیرمجاز (PR)","RESOLUTION","—","LEG/CMP","—"),
 ("G26","prohibited","رجیستری prohibited + تعلیق امارات (constraint)","CANCELLED,EXPIRED","بستن بدون workaround؛ وجه فقط از REFUND","CMP/LEG","ثبت constraint"),
]

def write_csv(name, fields, rows, tuples=False):
    with open(os.path.join(BASE, name), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            if tuples:
                w.writerow(dict(zip(fields, r)))
            else:
                w.writerow({k: r.get(k, "") for k in fields})
    print(f"wrote {name}: {len(rows)} rows")

def main():
    write_csv("state_machine.csv", STATE_FIELDS, STATES)
    write_csv("transitions.csv", ["from_state","to_state","trigger","guard","actor","note"], TRANSITIONS, tuples=True)
    write_csv("ledger_events.csv", ["event_id","state","side","debit_account","credit_account","amount_rule","trigger","owner","note"], LEDGER_EVENTS, tuples=True)
    write_csv("constraints.csv", ["gate_id","type","source_ref","applies_to","gate_behavior","legal_dependency","note"], CONSTRAINTS, tuples=True)

if __name__ == "__main__":
    main()
