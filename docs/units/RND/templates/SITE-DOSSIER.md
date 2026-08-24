# SITE-DOSSIER — قالب استاندارد پرونده سایت

- **Template version:** `RND-D00-D73-v1.1`
- **اصلاح:** `m-DIM`
- **وضعیت:** منتظر QA
- **کاربرد:** پرونده مستند هر پلتفرم؛ این فایل حاوی یافته واقعی درباره هیچ سایت خاصی نیست.

## قواعد استفاده

1. برای هر سایت، بخش‌های `D00` تا `D73` را بدون حذف نگه دارید.
2. زیر **هر بُعد**، برای **هر قابلیت یا بخش مستقل** یک «Capability/Section Record» کامل پر کنید. اگر یک بُعد سه قابلیت دارد، block همان بُعد باید سه بار تکرار شود؛ تجمیع چند قابلیت در یک record ممنوع است.
3. هیچ‌یک از ۱۲ فیلد ساختاری را حذف نکنید. اگر داده مشاهده نشد، مقدار را `مشاهده نشد` بنویسید و علت، مسیر بررسی و روش بعدی را در Evidence Record همان قابلیت ثبت کنید.
4. `page/module` باید محل رخداد را مشخص کند؛ `entity`, `event`, `state` و `error/exception` نباید در توضیح کلی گم شوند.
5. واقعیت مشاهده‌شده، استنباط و پیشنهاد محصول را جدا نگه دارید. URL کامل، تاریخ دسترسی و confidence برای هر record اجباری است.
6. هیچ ورود، ارسال فرم، پرداخت یا crawl خارج از Terms/robots بدون مجوز صریح انجام نشود.

## مشخصات پرونده

| فیلد | مقدار |
|---|---|
| Task ID | `<!-- TASK-ID -->` |
| Site | `<!-- canonical name -->` |
| Canonical URL | `<!-- full HTTPS URL -->` |
| Observer | `RND` |
| Observation date | `<!-- YYYY-MM-DD -->` |
| Region/device/access mode | `<!-- region; desktop/mobile; guest/auth -->` |
| Terms/robots status | `<!-- observed status + URLs -->` |
| Scope exclusions | `<!-- explicit exclusions -->` |

## Evidence state vocabulary

- `observed`: قابلیت/وضعیت با مشاهده مستقیم یا سند رسمی پشتیبانی شد.
- `observed-not-found`: در دامنه و access mode تعریف‌شده شاهد کافی پیدا نشد؛ به معنی نبود قطعی قابلیت نیست.

---
## D00 — `positioning_audience_geography`

**سؤال معیار:** What is the platform position, audience, geography, category breadth and proposition?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D00.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D01 — `home_page`

**سؤال معیار:** What does the guest homepage expose?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D01.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D02 — `global_navigation`

**سؤال معیار:** Are core destinations visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D02.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D03 — `search_entry`

**سؤال معیار:** What search scopes and input constraints are visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D03.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D04 — `search_results`

**سؤال معیار:** What result layout and count appear for a reproducible query?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D04.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D05 — `category_taxonomy`

**سؤال معیار:** Is a category hierarchy visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D05.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D06 — `filters`

**سؤال معیار:** Are filters evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D06.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D07 — `sorting`

**سؤال معیار:** Which sort controls and defaults exist?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D07.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D08 — `listing_card`

**سؤال معیار:** What appears on a guest product card?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D08.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D09 — `product_detail`

**سؤال معیار:** Which product fields/actions appear?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D09.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D10 — `supplier_detail`

**سؤال معیار:** Which supplier fields/actions appear?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D10.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D11 — `registration_entry`

**سؤال معیار:** Is registration entry visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D11.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D12 — `buyer_registration`

**سؤال معیار:** What buyer registration inputs are documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D12.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D13 — `supplier_enrollment`

**سؤال معیار:** What supplier enrollment path is public?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D13.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D14 — `login`

**سؤال معیار:** Which login mechanisms are documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D14.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D15 — `role_selection`

**سؤال معیار:** Is an explicit buyer/seller role-selection screen shown?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D15.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D16 — `email_verification`

**سؤال معیار:** How is email verified?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D16.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D17 — `mobile_verification`

**سؤال معیار:** How is mobile verified?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D17.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D18 — `company_onboarding`

**سؤال معیار:** Is company information collected?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D18.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D19 — `kyc_kyb_documents`

**سؤال معیار:** Which exact KYB documents are mandatory at registration?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D19.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D20 — `password_recovery`

**سؤال معیار:** What recovery path is documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D20.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D21 — `dashboard`

**سؤال معیار:** Is a supplier dashboard evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D21.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D22 — `company_profile`

**سؤال معیار:** Can suppliers maintain a profile?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D22.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D23 — `catalog_management`

**سؤال معیار:** Is catalog/showroom management evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D23.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D24 — `product_creation`

**سؤال معیار:** Is product creation evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D24.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D25 — `product_specifications`

**سؤال معیار:** Are structured specifications displayed?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D25.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D26 — `price_moq`

**سؤال معیار:** Are price and MOQ visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D26.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D27 — `capacity_lead_time`

**سؤال معیار:** Are capacity and lead time visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D27.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D28 — `rfq_creation`

**سؤال معیار:** Can a buyer submit an RFQ?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D28.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D29 — `rfq_response`

**سؤال معیار:** Can suppliers view/respond to RFQs?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D29.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D30 — `messaging`

**سؤال معیار:** Is messaging/file exchange evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D30.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D31 — `quotation`

**سؤال معیار:** Is quotation workflow evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D31.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D32 — `sample_workflow`

**سؤال معیار:** Is a platform-managed sample workflow visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D32.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D33 — `negotiation`

**سؤال معیار:** Is negotiation supported?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D33.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D34 — `order_creation`

**سؤال معیار:** Is an order flow documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D34.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D35 — `po_pi_documents`

**سؤال معیار:** Are platform-generated PO or pro-forma invoice documents evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D35.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D36 — `checkout`

**سؤال معیار:** What checkout steps are documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D36.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D37 — `payment_methods`

**سؤال معیار:** Which payment methods are stated?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D37.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D38 — `escrow_buyer_protection`

**سؤال معیار:** Is escrow or platform-held funds evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D38.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D39 — `notifications`

**سؤال معیار:** Are notification surfaces visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D39.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D40 — `order_status`

**سؤال معیار:** Which order states are documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D40.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D41 — `shipping_quote`

**سؤال معیار:** How is shipping price handled?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D41.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D42 — `carrier_freight`

**سؤال معیار:** Are logistics integrations/settings evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D42.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D43 — `incoterms`

**سؤال معیار:** Are Incoterms structured in product/order UI?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D43.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D44 — `trade_documents`

**سؤال معیار:** Are invoice, packing list, COO or bill-of-lading workflows shown?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D44.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D45 — `shipment_tracking`

**سؤال معیار:** Is platform shipment tracking evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D45.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D46 — `inspection`

**سؤال معیار:** Is transactional inspection ordering evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D46.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D47 — `delivery_confirmation`

**سؤال معیار:** Is buyer delivery acceptance evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D47.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D48 — `returns_refunds`

**سؤال معیار:** Are return/refund terms captured?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D48.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D49 — `claims`

**سؤال معیار:** Where can post-payment issues be raised?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D49.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D50 — `dispute_resolution`

**سؤال معیار:** Is dispute resolution native or external?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D50.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D51 — `supplier_verification`

**سؤال معیار:** How is supplier/certificate verification evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D51.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D52 — `buyer_verification`

**سؤال معیار:** What buyer KYB/verification badge exists?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D52.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D53 — `badges_certifications`

**سؤال معیار:** Where are trust marks shown?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D53.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D54 — `ratings_reviews`

**سؤال معیار:** Are buyer ratings/reviews visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D54.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D55 — `fraud_reporting`

**سؤال معیار:** Is a dedicated fraud/report action visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D55.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D56 — `moderation`

**سؤال معیار:** Are prohibited conduct and enforcement rights documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D56.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D57 — `customer_support`

**سؤال معیار:** Is support accessible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D57.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D58 — `support_sla`

**سؤال معیار:** Are response/resolution SLAs published?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D58.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D59 — `trust_education`

**سؤال معیار:** Does platform educate buyers about verification?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D59.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D60 — `enforcement_account_controls`

**سؤال معیار:** Are account/content controls documented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D60.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D61 — `language_localization`

**سؤال معیار:** Which language/localization capabilities are visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D61.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D62 — `currency`

**سؤال معیار:** Which currencies are displayed?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D62.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D63 — `country_region`

**سؤال معیار:** How is region represented?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D63.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D64 — `seo_metadata`

**سؤال معیار:** Are basic SEO signals visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D64.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D65 — `url_patterns`

**سؤال معیار:** Are page-type URL patterns stable and descriptive?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D65.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D66 — `mobile_responsive`

**سؤال معیار:** Is mobile behavior validated?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D66.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D67 — `accessibility`

**سؤال معیار:** Are WCAG/keyboard/screen-reader outcomes validated?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D67.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D68 — `performance`

**سؤال معیار:** Are load/performance metrics measured?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D68.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D69 — `revenue_model`

**سؤال معیار:** What monetization is publicly evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D69.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D70 — `advertising_promoted_listings`

**سؤال معیار:** Are paid exposure products evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D70.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D71 — `promotions_merchandising`

**سؤال معیار:** Are promotions/editorial merchandising visible?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D71.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D72 — `api_integrations`

**سؤال معیار:** Are APIs or integrations evidenced?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D72.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
## D73 — `data_content_policies`

**سؤال معیار:** Which data/content policies apply?

> اگر این بُعد بیش از یک قابلیت/بخش دارد، block زیر را برای هر مورد جداگانه duplicate کنید.

### D73.1 — Capability/Section Record

| فیلد استاندارد | مقدار اجباری برای همین قابلیت/بخش |
|---|---|
| actor | `<!-- نقش آغازگر/مصرف‌کننده/اپراتور -->` |
| input | `<!-- داده، اقدام یا پیش‌شرط ورودی -->` |
| output | `<!-- نتیجه قابل مشاهده/سند/تغییر وضعیت -->` |
| page/module | `<!-- URL/نام صفحه و ماژول دقیق -->` |
| entity | `<!-- موجودیت‌های درگیر؛ مثال: Account, RFQ, Order -->` |
| event | `<!-- رویداد دامنه‌ای/سیستمی؛ مثال: RFQSubmitted -->` |
| state | `<!-- before → after؛ اگر مشاهده نشد صریح بنویسید -->` |
| error/exception | `<!-- خطا، edge case، fallback یا observed-not-found -->` |
| document | `<!-- سند ورودی/خروجی؛ در صورت نبود: مشاهده نشد -->` |
| personal data | `<!-- نوع داده شخصی و ضرورت؛ در صورت نبود: مشاهده نشد -->` |
| risk | `<!-- ریسک اعتماد/حقوقی/مالی/عملیاتی/داده -->` |
| handoff | `<!-- مالک بعدی + شرط handoff -->` |

#### Evidence Record همین قابلیت/بخش

| فیلد شاهد | مقدار |
|---|---|
| evidence state | `<!-- observed / observed-not-found -->` |
| observed fact | `<!-- فقط واقعیت مشاهده‌شده -->` |
| evidence URL | `<!-- full HTTPS URL -->` |
| evidence type | `<!-- direct UI / official support / policy / supplier content / secondary lead -->` |
| observed at | `<!-- YYYY-MM-DD -->` |
| access mode | `<!-- guest/auth; region; device -->` |
| confidence | `<!-- high / medium / low + علت -->` |
| gap reason | `<!-- برای observed-not-found اجباری -->` |
| next method | `<!-- روش بعدی مجاز و قابل بازتولید -->` |
| inference | `<!-- جدا از واقعیت -->` |
| product implication | `<!-- پیشنهاد، جدا از واقعیت -->` |

<!-- برای قابلیت/بخش بعدی در همین بُعد، کل Capability/Section Record و Evidence Record را تکرار کنید. -->

---
