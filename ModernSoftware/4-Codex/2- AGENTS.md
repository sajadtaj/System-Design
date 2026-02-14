
## AGENTS.md دقیقاً چه کاری می‌کند؟

* به Codex می‌گوید: ساختار پروژه چیست، کدام مسیرها مهم‌اند، چه تست/لینتی باید اجرا شود، قوانین کدنویسی/PR چیست، محدودیت‌ها و باید/نبایدهای امنیتی یا عملیاتی چیست. ([OpenAI](https://openai.com/index/introducing-codex/?utm_source=chatgpt.com "Introducing Codex"))
* Codex هر بار که اجرا می‌شود، یک «زنجیره دستورالعمل» می‌سازد و این فایل‌ها را در آن زنجیره قرار می‌دهد. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

## کجای پروژه باید باشد؟ روت یا جای دیگر؟

به‌صورت استاندارد:

1. **در روت ریپو** یک `AGENTS.md` می‌گذاری برای قواعد کلی پروژه. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))
2. اگر زیرپروژه/سرویس خاصی قوانین متفاوت دارد، داخل همان پوشه یک `AGENTS.md` یا ترجیحاً `AGENTS.override.md` می‌گذاری تا همان‌جا «نزدیک‌ترین» قوانین اعمال شود. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

Codex از **ریشه ریپو تا پوشه‌ای که داخلش اجرا شده‌ای** پایین می‌آید و در هر پوشه حداکثر یک فایل راهنما را وارد زنجیره می‌کند. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

## چگونه “فعال” می‌شود؟

هیچ فعال‌سازی دستی ندارد. وقتی Codex را اجرا می‌کنی (CLI/IDE که به Codex وصل است)، خودش این فایل‌ها را **قبل از هر کاری** می‌خواند. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))
برای اطمینان هم می‌توانی با دستورهایی مثل اینکه از Codex بخواهی «منابع دستورالعمل فعال» را لیست کند، بررسی کنی چه فایل‌هایی لود شده‌اند. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

## مثل .gitignore است یا مثل bash script؟

هیچ‌کدام، ولی از نظر «ماهیت فایل» به `.gitignore` نزدیک‌تر است تا اسکریپت:

* **مثل bash script نیست** چون اجرا نمی‌شود و هیچ کاری را به‌صورت خودکار در سیستم انجام نمی‌دهد.
* **مثل .gitignore هم نیست** چون قواعدش توسط Git اعمال نمی‌شود. فقط یک **قرارداد/راهنما** است که Codex می‌خواند. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))
  بهترین تشبیه: «README مخصوص agentها» (اما با مکانیزم کشف/اولویت‌بندی مشخص). ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

## لایه‌بندی و اولویت‌ها (نکته‌های مهم)

* Codex علاوه بر ریپو، می‌تواند یک لایه **سراسری (Global)** هم داشته باشد: در مسیر خانگی Codex (پیش‌فرض `~/.codex`) فایل‌های `AGENTS.md` یا `AGENTS.override.md`. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))
* اولویت به این شکل است: سراسری → روت ریپو → پوشه‌های نزدیک‌تر به محل کار؛ و فایل‌های نزدیک‌تر «عملاً بر قبلی‌ها غلبه می‌کنند» چون بعدتر در زنجیره می‌آیند. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))
* محدودیت اندازه هم دارد (پیش‌فرض 32KiB) و اگر زیاد بنویسی ممکن است قطع شود؛ پس کوتاه و عملیاتی بنویس. ([OpenAI Developer Docs](https://developers.openai.com/codex/guides/agents-md/ "Custom instructions with AGENTS.md"))

## چطور استفاده‌اش کنی که واقعاً اثر داشته باشد (نه تزئینی)

اگر AGENTS.md تبدیل به مقاله‌ی طولانی شود، عملاً بی‌اثر می‌شود. باید مثل یک «چک‌لیست اجرایی» باشد:

* دستورهای استاندارد: build / test / lint / format
* قوانین PR و استاندارد کدنویسی (مختصر)
* مسیرهای مهم و مسیرهای ممنوع (مثلاً خروجی‌ها، فایل‌های بزرگ، secrets)
* سیاست وابستگی‌ها (مثلاً “بدون تایید، dependency جدید اضافه نکن”)
* نکات امنیتی/عملیاتی (کلیدها، envها، migrationها)

این دقیقاً همان چیزی است که مستند رسمی OpenAI هم توصیه می‌کند: راهنمایی درباره‌ی ناوبری کدبیس، فرمان‌های تست، و استانداردهای پروژه. ([OpenAI](https://openai.com/index/introducing-codex/?utm_source=chatgpt.com "Introducing Codex"))
