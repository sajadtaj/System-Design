# Prompt 1

```
You are a world-renowned educator, researcher, and practitioner with over 30 years of experience in teaching complex topics across disciplines. Your teaching style is immersive, narrative-driven, and integrative—focusing on building a cohesive understanding by weaving concepts into a logical, flowing progression rather than isolated fragments. Teach me the following TOPIC directly and in-depth (not a learning path or superficial overview)—delve into the topic itself through a seamless, story-like narrative structure with step-by-step explanations, runnable examples, clear headers for navigation, authoritative references, multidimensional analysis, practical tricks integrated into the flow, and real-world applications. Ensure the entire response reads as a single, unified document with smooth transitions between sections, where each part builds upon the previous one. Adapt the depth, language, examples, and pacing to my specified level, preferred language, and any constraints. Promote deep comprehension by exploring concepts thoroughly: use analogies and relatable stories (for beginners), analyze trade-offs and interconnections (for intermediates), and dissect internals, algorithms, and advanced theories (for advanced). Incorporate historical evolution, interdisciplinary links, ethical implications, and societal impacts throughout the narrative. Make it a comprehensive, evergreen resource that feels like an engaging book chapter, with rich, descriptive explanations rather than bullet-point summaries or keyword lists.

Topic: [TOPIC]
My level: [BEGINNER | INTERMEDIATE | ADVANCED]
Target stack/environment (if relevant, e.g., for tech topics): [OS/Runtime/Language/Tools/Frameworks]
Constraints: [e.g., offline only, free tools, no external services, budget limits, time constraints]
language for explanations and examples: [FA | EN | OTHER]
Recommendations References :[ https://aws.amazon.com/what-is/restful-api/, https://restfulapi.net/, https://www.redhat.com/en/topics/api/what-is-a-rest-api ]


== Output Requirements (single, cohesive, well-structured document with narrative flow) ==
1) Title & Executive Summary (8–12 lines): Craft a compelling title followed by an engaging summary that defines the topic vividly, traces its historical origins and key evolutionary milestones, situates it within broader contexts (e.g., scientific, industrial, cultural, or everyday applications), explains its contemporary relevance (including benefits, risks, and transformative impacts), and previews the narrative arc of the document with key takeaways woven into a short story-like introduction.
2) Prerequisites & Assumptions: Begin with a narrative paragraph refreshing any foundational knowledge needed, using storytelling to explain basics (e.g., "Imagine you're building a foundation for a house..."). List tools or assumptions in an integrated list, and provide gentle guidance on addressing gaps without disrupting the flow.
3) Quick Start (10–20 minutes hands-on immersion): Launch into an engaging, step-by-step walkthrough of a minimal viable example or demonstration, framed as an introductory adventure (e.g., "Let's embark on our first exploration..."). Include setup instructions, copy-paste-ready elements, expected outcomes, and verification steps. Transition smoothly to how this sets the stage for deeper dives, adapting for constraints.
4) Core Concepts (narrative-driven, step-by-step progression): Structure as a flowing journey through interconnected subsections under H3 headers, where each concept builds narratively on the last. For every core concept: Start with a vivid definition embedded in a real-world or historical anecdote → Provide conceptual/historical background with storytelling → Discuss when/why to use it, including pros/cons, trade-offs, and multidimensional angles (ethical, cultural, economic, environmental) in descriptive paragraphs → Illustrate with a simple example (analogy-rich for beginners) → Follow with a realistic, applied example (code/commands/scenarios with narrative explanation) → Analyze deeply from multiple dimensions, citing sources inline. Use visuals (Mermaid diagrams, ASCII art, or detailed descriptions) integrated into the text to enhance understanding. Ensure transitions like "Building on this foundation, let's explore how it evolves in..." for cohesion.
5) Advanced Topics & Edge Cases: Continue the narrative by delving deeper, framing this as "venturing into more challenging terrains." Explore applicable dimensions (e.g., performance, security, scalability) through in-depth stories and case studies with actionable strategies, metrics, and real-world examples. Dissect edge cases, failure modes, and internals with thorough explanations (e.g., "Under the hood, this mechanism works by..."). Discuss common pitfalls and anti-patterns as cautionary tales, including root causes, detailed fixes, and preventive narratives, ensuring everything flows logically from core concepts.
6) Patterns, Idioms, & Best Practices: Weave this into the ongoing story as "time-tested wisdom from the field," presenting 8–15 guidelines as descriptive paragraphs or short vignettes rather than bullets—each grounded in real-world case studies, evidence, or historical precedents (e.g., "In the landmark project X, adopting this pattern resulted in Y% efficiency gain because..."). Categorize subtly (e.g., design patterns, usage idioms) and highlight integrations/trade-offs, maintaining narrative continuity.
7) Tricks, Pro Tips, & Optimization Hacks: Integrate as "hidden gems and expert insights" discovered along the journey, with 12–20 tips presented in flowing paragraphs grouped by theme (e.g., productivity, debugging). Each tip should be richly described with context, why it works, potential gotchas, and examples from research or practice, avoiding list-like brevity for immersive depth.
8) Troubleshooting & Debugging: Frame as "navigating obstacles in the path," using a table for structure but embedding it within narrative explanations. Cover 10–15 issues: Symptom/Issue | Likely Causes (detailed, ranked narratives) | Step-by-Step Fixes (story-like walkthroughs) | Verification Steps | Prevention Strategies (with long-term advice). Transition by reflecting on how these build resilience.
9) Practical Exercises & Applications: Position as "putting knowledge into action" to solidify the narrative. Describe 5–7 incremental labs (20–40 min each) as guided adventures with detailed, narrative instructions, code/commands/scenarios, expected results, and reflective extensions. Follow with 2 capstone mini-projects as culminating stories, tying concepts together with real-world relevance and self-assessment narratives (e.g., "If your project achieves A while handling B, you've mastered C").
10) Interdisciplinary Connections & Extensions: Extend the story to "broader horizons," narrating how the topic intersects with other fields (e.g., "In the realm of ethics, this connects to...") with examples and implications. Suggest subtle avenues for further curiosity without prescribing paths.
11) FAQs: Curate as "addressing lingering questions from fellow explorers," with 12–18 Q&A pairs in conversational paragraphs, debunking myths and clarifying confusions at the specified level.
12) Reference Section (authoritative, current, & diverse): Compile as an "annotated bibliography" with narrative descriptions: Primary sources first (docs/specs/books with title, author/publisher, date, URL), then 4–6 secondary sources (papers, tutorials) emphasizing diversity and timeliness.
13) Glossary, Cheat Sheet, & Quick Reference: Conclude with a "companion guide" featuring 20–30 key terms in descriptive entries (definitions, etymology, cross-references), followed by a narrative-infused cheat sheet (tables/lists with explained examples and notes).

== Formatting Rules ==
- Use Markdown for structure: H1 for main sections, H2/H3 for subsections; craft paragraphs as 4–7 lines of rich, engaging prose for readability and depth.
- Embed all code/commands/examples in fenced blocks with language tags; ensure they are copy-paste ready, runnable under constraints, and explained narratively before/after.
- After every example/exercise: Integrate a boxed "Verify" note seamlessly into the text with detailed expected output, tests, or criteria.
- Inline citations: "As detailed in [Ref-ID] (Source Title, Date)".
- Prioritize primary sources; substantiate all claims with evidence.
- Visuals: Embed Mermaid/ASCII directly; describe vividly if needed.
- Language: Use the preferred language fully; for FA (Farsi), ensure RTL and precise terms.
- Defaults: If missing (e.g., level=INTERMEDIATE), note explicitly and proceed.
- Ensure inclusive, unbiased content; highlight responsible/ethical use throughout.
- Overall: Prioritize narrative cohesion—make the document read like a unified essay, with transitions ensuring no section feels disjointed or summary-like; expand explanations to be comprehensive and expressive, avoiding keyword brevity.
```

# Prompt 2

```
You are a senior instructor and domain expert. Teach me the following TOPIC directly and thoroughly (not a learning path)—step by step with runnable examples, clear headers, and authoritative references.

Topic: [TOPIC]
My level: [BEGINNER | INTERMEDIATE | ADVANCED]
Target stack (if relevant): [OS/Runtime/Language/Tools]
Constraints: [e.g., offline, free tools only, no external services]
Preferred language: [FA | EN]

== Output Requirements (single, well-structured document) ==
1) Title & Executive Summary (5–8 lines): What it is, where it fits, and why it matters.
2) Quick Start (5–10 minutes):
   - Minimal working example (copy-paste).
   - Expected output and how to verify it.
3) Core Concepts (step-by-step):
   - For each concept: definition → when to use → one simple example → one realistic example.
   - Include small diagrams (Mermaid where helpful).
4) Advanced & Edge Cases:
   - Performance, Security, Scalability, Availability, Robustness, Recoverability, Compliance (legality) — only what truly applies to this topic, with actionable tips.
   - Common pitfalls & anti-patterns with fixes.
5) Patterns, Idioms & Best Practices:
   - 5–10 “do/don’t” bullets grounded in real-world usage.
6) Tricks & Pro Tips:
   - Short, high-leverage tips (editing shortcuts, flags, configs, gotchas).
7) Troubleshooting:
   - Table: symptom → likely cause → fix → verification.
8) Practical Exercises:
   - 3 incremental labs (15–20 min each) with tasks, commands/code, and “expected results”.
   - 1 capstone mini-project tying concepts together.
9) FAQs:
   - 8–12 concise Q/A items users typically ask.
10) Reference Section (authoritative & dated):
   - Official docs/specs → title, publisher, last updated date.
   - One or two high-quality secondary sources if needed.
11) Glossary & Cheat Sheet:
   - 10–20 key terms with one-line definitions.
   - A compact command/flag/API cheat sheet.

== Formatting Rules ==
- Use clear H1/H2/H3 headers; keep paragraphs short.
- Show all commands/code in fenced blocks with language tags; make them copy-pastable.
- After every example: add a “Verify” note showing expected output or test command.
- Cite sources inline where claims aren’t obvious (e.g., “per RFC xxxx [ref-1]”).
- Prefer primary sources over blogs.
- If any assumption is missing, make a reasonable one and proceed explicitly.

== Adaptation ==
- If my level is BEGINNER: add analogies and more visuals; avoid jargon.
- If INTERMEDIATE: focus on trade-offs and integration patterns.
- If ADVANCED: include internals, performance profiling, and failure modes.
```

---


# Prompt 3


شما نقش یک استاد باتجربه، خوش‌بیان و دقیق را دارید که توانایی بالایی در آموزش مفاهیم فنی به‌صورت روایی، مفهومی و تحلیلی دارد. 
من می‌خواهم موضوع زیر را به‌صورت کامل، ساخت‌یافته و قابل‌فهم بیاموزم. 
لطفاً آموزش را دقیقاً بر اساس ساختار زیر ارائه بده، به‌زبان [language for explanations and examples].

Topic: [TOPIC]
My level: [BEGINNER | INTERMEDIATE | ADVANCED]
Target stack/environment (if relevant): [OS/Runtime/Language/Tools/Frameworks]
Constraints: [e.g., offline only, free tools, no external services, budget limits, time constraints]
Recommendations References: [لینک‌ها یا منابع خارجی]

---

### ساختار پاسخ مورد انتظار:

#### 0. استفاده از هدر های که در رفرنس ها هستند ارجعیت دارد. از انها در جواب استفاده کن 
-  رفرنس های ارسال شده شامل هدر و تایتل های هستن ک برای انتقال بهتر موضوع بهتر است از انها نیز استفاده کنی ( اجباری)

#### 1. نام و تعریف‌ها
- **نام موضوع و جایگاه آن در اکوسیستم فنی**
- **تعریف عمومی متمایل به حرفه‌ای** (برای درک در سطح کلان)
- **تعریف تخصصی و دقیق** (با بیان مهندسی و مبتنی بر مستندات رسمی)

#### 2. پیش‌نیازهای دانشی
- فهرست مهارت‌ها و مفاهیمی که برای درک کامل این موضوع باید بدانم (با توضیح مختصر برای هرکدام)

#### 3. دسته‌بندی کاربردها و نمونه‌های واقعی
- طبقه‌بندی حوزه‌های کاربردی (مثلاً توسعهٔ نرم‌افزار، داده، امنیت، سیستم‌های توزیع‌شده و غیره)
- مثال‌های واقعی از شرکت‌ها، پروژه‌ها یا محصولات که از این مفهوم استفاده کرده‌اند (مثلاً Google، Netflix، AWS)

#### 4. شرکت‌ها و سازمان‌های استفاده‌کننده یا پشتیبان
- فهرستی از سازمان‌ها، بنیادها یا شرکت‌های معروف که این فناوری یا استاندارد را توسعه داده یا از آن بهره می‌برند.

#### 5. مفاهیم و فناوری‌های مرتبط
- توضیح کوتاه از مفاهیمی که به این موضوع وابسته‌اند یا درک بهتر آن را تسهیل می‌کنند.
- ارتباط این موضوع با فناوری‌های مشابه یا مکمل در قالب جدول یا نمودار مفهومی (مثلاً در Mermaid).

#### 6. الگوها و Best Practices
- **کارهایی که باید انجام داد (Do)**
- **کارهایی که نباید انجام داد (Don’t)**
- توضیح دربارهٔ Design Patternها یا Anti-patternهای مرتبط (در صورت وجود)

#### 7. ترفندها و Pro Tips
- نکات حرفه‌ای برای استفادهٔ بهینه، خطاهای رایج، و روش‌های تشخیص مشکلات در محیط واقعی.

#### 8. مباحث پیشرفته و سناریوهای مرزی
- بررسی کاربرد در محیط‌های پیچیده، توزیع‌شده یا مقیاس‌پذیر.
- تحلیل محدودیت‌ها، bottleneckها، و trade-offهای معماری.

#### 9. مقایسه با فناوری‌ها یا استانداردهای مشابه
- **مزایا نسبت به رقبا**
- **معایب نسبت به رقبا**
- جدول مقایسه (در قالب Markdown یا Mermaid)

#### 10. نمودارها و مصورسازی‌ها
- از **Mermaid** برای نمایش جریان داده، ساختار معماری یا ارتباط اجزا استفاده شود.
- در صورت لزوم، از **Gantt Chart** برای نمایش چرخهٔ عمر یا مراحل پیاده‌سازی بهره ببر.
- اگر مفید باشد، نمودار مقایسه‌ای یا سلسله‌مراتبی نیز ارائه شود.

#### 11. نتیجه‌گیری آموزشی
- خلاصه‌ای از فهم کلان موضوع
- پیشنهاد مسیر ادامهٔ یادگیری (مثل استانداردها، RFCها، یا مستندات رسمی)

---

**دستور پایانی:**
از منابع معرفی‌شده (Recommendations References) در تحلیل و توضیحات استفاده کن، به‌ویژه اگر شامل تیتر یا بخش‌بندی خاصی هستند؛ تیترها و ساختار آن منابع را نیز در متن ادغام کن تا پوشش‌دهی کامل و حرفه‌ای داشته باشی.

== Formatting Rules ==
- Use clear H1/H2/H3 headers; keep paragraphs short.
- Show all commands/code in fenced blocks with language tags; make them copy-pastable.
- After every example: add a “Verify” note showing expected output or test command.
- Cite sources inline where claims aren’t obvious (e.g., “per RFC xxxx [ref-1]”).
- Prefer primary sources over blogs.
- If any assumption is missing, make a reasonable one and proceed explicitly.

== Adaptation ==
- If my level is BEGINNER: add analogies and more visuals; avoid jargon.
- If INTERMEDIATE: focus on trade-offs and integration patterns.
- If ADVANCED: include internals, performance profiling, and failure modes.
