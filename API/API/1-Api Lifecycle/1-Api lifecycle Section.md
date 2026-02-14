<style>
.rtl-align {
  direction: rtl;
  text-align: right;
}

/* لیست‌ها هم راست‌چین */
.rtl-align ul,
.rtl-align ol {
  list-style-position: inside;
  padding-right: 0;
  margin-right: 1em;
}

/* فقط باکس‌های کد (مثل ```...```) چپ‌چین و مونو */
.rtl-align pre code {
  direction: ltr;           /* جهت چپ به راست */
  text-align: left;         /* تراز چپ */
  display: block;           /* حالت باکس */
  background: #f5f5f5;      /* پس‌زمینه روشن مثل حالت کد */
  padding: 10px;            /* فاصله داخلی */
  border-radius: 5px;       /* گوشه‌های گرد */
  font-family: monospace;   /* فونت مونو برای کد */
  white-space: pre;         /* حفظ فاصله‌ها */
}

</style>

<div class="rtl-align">

## فصل ۱ — Overview of API Lifecycle

(مستندات: Postman API Lifecycle — Introducing the API lifecycle)

1. تعریف API Lifecycle
2. مراحل اصلی (Design → Mock → Develop → Test → Document → Deploy → Observe → Version → Retire)
3. ارتباط با API Platform و Governance
4. چرایی اهمیت Lifecycle در تیم‌های نرم‌افزار، داده و اکوسیستم‌های مقیاس بزرگ

---

## فصل ۲ — API Design

(مستندات: Postman API Design, OpenAPI Specification 3.1, RFC9110 Concepts)

1. اصول طراحی API
2. Semantic Design
3. OpenAPI 3.1 Specification
4. API Governance + Design Rules
5. Version Strategy در مرحله طراحی

---

## فصل ۳ — API Documentation

(مستندات: Postman Documentation, Best Practices for Collections)

1. Writing for Humans vs Machines
2. OpenAPI → Docs
3. Postman Collection Documentation
4. نمونه‌های استاندارد تولید مستندات
5. Anti-Patterns در مستندسازی

---

## فصل ۴ — API Test Automation

(مستندات: Postman Test Automation, Newman, CI/CD Integration)

1. Test Pyramid برای API
2. Contract Testing
3. Integration Testing
4. Load/Stress Testing
5. Test Automation Pipeline در CI/CD

---

## فصل ۵ — API Deployment & Versioning

(مستندات: RFCs, API Gateway Patterns, Kong/Kubernetes Ingress)

1. Deployment Models
2. Versioning Strategies (URI-based, Header-based, Media Type Versioning)
3. Backward Compatibility
4. Release Strategy (Blue/Green, Canary)
5. API Gateways & Ingress

---

## فصل ۶ — API Monitoring

(مستندات: Postman Monitoring, Postman Reliability Guidelines)

1. Health Checks
2. Monitoring KPIs
3. Synthetic Monitoring
4. Alerting
5. SLA/SLI/SLO در API

---

## فصل ۷ — API Observability

(مستندات: Postman Observability, OpenTelemetry)

1. Telemetry: Logs, Metrics, Traces
2. Distributed Tracing
3. Correlation IDs
4. Error Taxonomy
5. Observability Patterns

---

## فصل ۸ — Governance & API Platform

(مستندات: Postman API Platform, Internal API Catalogs)

1. Definition of API Platform
2. Governance Models (Centralized / Decentralized / Hybrid)
3. Standards, Style Guides, Linting
4. API Discoverability & Catalogs
5. Security Governance & Zero Trust

---

## فصل ۹ — API Retirement & Deprecation

(مستندات: Postman Lifecycle, API Sunsetting Guides)

1. Deprecation Notice
2. Sunset HTTP Header (per RFC)
3. Migration Paths
4. Monitoring API Consumers
5. Shutdown Strategy

---

## فصل ۱۰ — Deep Architecture & Trade-Offs

(مستندات: RFC9110, API Gateways, distributed system patterns)

1. API در سیستم‌های توزیع‌شده
2. Latency Budgeting
3. Consistency Trade-offs
4. Scalability Models
5. API as a Product (APIOps)

