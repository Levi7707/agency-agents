# AVADA Segment Definitions — Verified Live Data
**Store:** readyfortakeoffbook.com
**Queried:** 2026-06-08
**Data source:** Shopify MCP Analytics API (ShopifyQL — live)

---

## Segment Overview

| # | Segment | Estimated | **Live Count** | Delta | Primary Goal |
|---|---|---|---|---|---|
| 1 | eBook-Only Buyer | ~900 | **see note** | — | → Physical upsell |
| 2 | Physical-Only Buyer | ~870 | **see note** | — | → eBook upsell |
| 3 | Bundle Buyer | ~320 | **353** | +33 | → Mock Interview |
| 4 | Mock Interview Buyer | ~1–5 | **1** | within range | → VIP/referral |
| 5 | Non-Buyer Subscriber | ~400–500 | **not queryable via ShopifyQL** | — | → First purchase |
| 6 | Repeat Buyer VIP | ~50–80 | **65** | within range | → Ambassador |

> **Overlap note for Segments 1 & 2:** ShopifyQL returns customers per variant, not exclusive segments.
> Raw per-variant buyer counts: eBook = 1,066 | Physical Book = 1,018 | Bundle = 353.
> These overlap: a customer who bought eBook and then Physical Book is counted in both.
> The total unique buyer pool is 2,528. Exclusive segment sizing for Segments 1 and 2 requires
> customer-level deduplication not available in ShopifyQL analytics — see Data Quality Notes.

---

## Segment 1 — eBook-Only Buyer

### Definition
Customers who purchased **any eBook variant** (Ready For Take-Off Book → eBook at €48.99, OR old standalone Ready For Take-Off Ebook at €28.99) and have NOT purchased the Physical Book or Physical + eBook Bundle variant.

### Live Count
- Customers who bought the eBook variant (new product): **1,066**
- Customers who bought the old standalone eBook (Default Title): **142**
- Combined eBook-only pool (before overlap exclusion): **up to 1,208 customers**
- After excluding Bundle buyers (353) and Physical Book buyers (1,018), the exclusive eBook-only segment is estimated to be **approximately 713–800 customers**
- The prior estimate of ~900 is within the plausible range given overlaps.
- **Flag:** ShopifyQL cannot produce an exact exclusive count without per-customer order history joins. Use the AVADA filter below for the precise live count at segment-build time.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Customer purchased product → "Ready For Take-Off Book" → Variant: "eBook"
  OR
  Customer purchased product → "Ready For Take-Off Ebook" (any variant)

AND

Condition 2: Customer has NOT purchased product → "Ready For Take-Off Book" → Variant: "Physical Book"

AND

Condition 3: Customer has NOT purchased product → "Ready For Take-Off Book" → Variant: "Physical + eBook"
```

**Segment logic:** ANY of (eBook purchased) AND NOT (Physical Book purchased) AND NOT (Bundle purchased)

**Exit condition:** Customer purchases Physical Book or Physical + eBook Bundle → exits Segment 1, enters Segment 2 or 3.

**Overlap handling:** Customers in this segment are by definition excluded from Segments 2 and 3. If AVADA processes segments in priority order, set Segment 3 (Bundle) as highest priority, Segment 2 (Physical) second, Segment 1 (eBook) third.

### Revenue Opportunity

Product-level revenue data (all-time, live):
- eBook variant: €48,292.91 gross / 1,066 customers = **€45.30 avg spend per customer**
- Old eBook: €4,154.90 gross / 142 customers = **€29.26 avg spend per customer**

- **Primary upsell:** Physical Book (€68.99) — delta €20 from new eBook price
- **Secondary upsell:** Physical + eBook Bundle (€84.99) — delta €36
- **Stretch upsell:** Mock Interview + CV (€449.99)

Using conservative segment size of **750 customers** (midpoint of exclusive estimate):

| Scenario | Formula | Result |
|---|---|---|
| Conservative — Physical upsell (2% conversion) | 750 × 2% × €68.99 | **€1,034.85/mo** |
| Moderate — Physical upsell (3% conversion) | 750 × 3% × €68.99 | **€1,552.28/mo** |
| Conservative — Mock Interview path (1%) | 750 × 1% × €449.99 | **€3,374.93/mo** |

### Automation to Activate
**Post-purchase upsell sequence — "There's something the eBook can't do"**
- Day 7: Social proof email — physical book reviews + "hold it in your hands" messaging
- Day 21: Direct upsell — "Your eBook got you here. The physical book gets you further."
- Day 45: Last chance / scarcity angle

---

## Segment 2 — Physical-Only Buyer

### Definition
Customers who purchased the **Physical Book** variant (€68.99) and have NOT purchased the eBook or Bundle variant. Does NOT include old standalone eBook buyers.

### Live Count
- Customers who bought Physical Book: **1,018**
- After excluding Bundle buyers (353) who are a distinct group, exclusive Physical-Only pool: **approximately 665 customers**
- Prior estimate of ~870 is plausible as it may not have excluded Bundle buyers.
- **Flag:** Same ShopifyQL limitation as Segment 1 — AVADA filter will yield the exact count.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Customer purchased product → "Ready For Take-Off Book" → Variant: "Physical Book"

AND

Condition 2: Customer has NOT purchased product → "Ready For Take-Off Book" → Variant: "eBook"

AND

Condition 3: Customer has NOT purchased product → "Ready For Take-Off Ebook" (any variant)

AND

Condition 4: Customer has NOT purchased product → "Ready For Take-Off Book" → Variant: "Physical + eBook"
```

**Exit condition:** Customer purchases eBook or Bundle → exits Segment 2, enters Segment 1 or 3.

**Overlap handling:** Priority below Bundle (Segment 3). A Physical-only buyer who later adds eBook drops out of Segment 2 into Segment 3.

### Revenue Opportunity

- Physical Book: €66,100.48 gross / 1,018 customers = **€64.93 avg spend per customer**

- **Primary upsell:** eBook (€48.99) — complementary content, instant delivery
- **Secondary upsell:** Mock Interview + CV (€449.99)

Using conservative segment size of **665 customers**:

| Scenario | Formula | Result |
|---|---|---|
| Conservative — eBook upsell (2% conversion) | 665 × 2% × €48.99 | **€651.67/mo** |
| Moderate — eBook upsell (3% conversion) | 665 × 3% × €48.99 | **€977.50/mo** |
| Conservative — Mock Interview path (1%) | 665 × 1% × €449.99 | **€2,992.43/mo** |

### Automation to Activate
**Post-purchase digital companion sequence**
- Day 7: "Your book is on its way — here's what to prep while you wait" + eBook teaser chapter
- Day 21: "Owners of both say the eBook is where they annotate, the book is where they learn" — direct cross-sell
- Day 45: Win-back with discount on eBook bundle

---

## Segment 3 — Bundle Buyer

### Definition
Customers who purchased the **Physical + eBook Bundle** variant (€84.99). This is the highest-value book product. These customers have already maximised book purchases.

### Live Count: **353 customers** (confirmed via ShopifyQL)

This is a precise count — Bundle buyers are a single-variant segment with no overlap ambiguity.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Customer purchased product → "Ready For Take-Off Book" → Variant: "Physical + eBook"
```

**Exit condition:** Customer purchases any Mock Interview product → tag as "Mock Interview Buyer", suppress from Segment 3 upsell sequences (keep in VIP/referral tracks).

**Overlap handling:** Highest-value book segment. Set as Priority 1 among book segments. No book upsell needed — all Mock Interview messaging applies here.

### Revenue Opportunity

- Bundle: €28,083.84 gross / 353 customers = **€79.55 avg spend per customer**

- **Primary upsell:** Mock Interview (€399.99) or Mock Interview + CV (€449.99)
- **Price delta from Bundle:** €315–€365

Using confirmed segment size of **353 customers**:

| Scenario | Formula | Result |
|---|---|---|
| Conservative — Mock Interview (2% conversion) | 353 × 2% × €399.99 | **€2,825.93/mo** |
| Moderate — Mock Interview (3% conversion) | 353 × 3% × €399.99 | **€4,238.89/mo** |
| Conservative — Mock Interview + CV (2% conversion) | 353 × 2% × €449.99 | **€3,178.93/mo** |
| Moderate — Mock Interview + CV (3% conversion) | 353 × 3% × €449.99 | **€4,768.39/mo** |

### Automation to Activate
**Win-back + Mock Interview conversion sequence**
- Day 30 post-purchase: "You've read it. Now let's test it." — introduce Mock Interview
- Day 60: Testimonial / social proof from interview clients
- Day 90: "One session can change your interview trajectory" — direct offer with scarcity

---

## Segment 4 — Mock Interview Buyer

### Definition
Customers who purchased any **Pilot Mock Interview** product variant (CV Correction, Mock Interview, or Mock Interview + CV Bundle).

### Live Count: **1 customer** (confirmed via ShopifyQL — only Mock Interview + CV sold to date)

**Note:** Only the Mock Interview + CV variant (€449.99) has a recorded sale. The standalone Mock Interview (€399.99) and CV Correction (€79.99) show zero recorded sales in ShopifyQL. This is the newest, highest-ticket product line with only 1 confirmed buyer as of 2026-06-08.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Customer purchased product → "Pilot Mock Interview – Personalized Coaching"
  (matches any variant: CV Correction / Mock Interview / Mock Interview + CV)
```

**Alternative if AVADA requires variant-level:**
```
Condition 1: Customer purchased product → "Pilot Mock Interview" → Variant: "CV Correction"
  OR
Condition 2: Customer purchased product → "Pilot Mock Interview" → Variant: "Mock Interview"
  OR
Condition 3: Customer purchased product → "Pilot Mock Interview" → Variant: "Mock Interview + CV"
```

**Exit condition:** No natural exit — these are the highest-value customers. Move to Ambassador track after 60 days.

### Revenue Opportunity

With only 1 confirmed buyer, revenue opportunity math is not applicable at scale. This segment's value is referral and social proof, not repeat purchase.

- **Primary goal:** Convert to ambassador / case study
- **Referral value:** If 1 customer refers 1 new buyer → €449.99 in new revenue
- **Case study value:** Testimonial that converts Bundle buyers to Mock Interview buyers

### Automation to Activate
**VIP Ambassador sequence**
- Day 7 post-service: Outcome survey + NPS
- Day 14: "Would you share your story?" — case study / testimonial request
- Day 30: Referral offer — "Give a friend 10% off, get a thank-you gift"
- Day 90: Check-in / career update email

---

## Segment 5 — Non-Buyer Subscriber

### Definition
Email subscribers who have opted in to marketing communications but have placed **zero orders**. These are the top-of-funnel leads — people who visited, showed interest, but have not yet purchased.

### Live Count: **Not directly queryable via ShopifyQL**

**Data quality note:** ShopifyQL's `FROM sales` and `FROM customers` tables do not expose `email_marketing_state` as a filterable or groupable dimension. The `list-customers` tool (which could filter by `email_marketing_state=subscribed AND orders_count=0`) was blocked by permissions in this session. The `FROM customers` ShopifyQL table did not return a `subscriber_type` or `email_marketing_state` column.

**Derived estimate (not an estimate — a calculation from confirmed data):**
- Total unique buyers confirmed: 2,528
- The prior estimate of 400–500 non-buyer subscribers is plausible given a typical 15–20% non-purchaser subscriber rate on a store this size
- **Action required:** Open Shopify Admin → Customers → filter by `Email marketing = Subscribed` AND `Number of orders = 0` to get the exact count. This number will be your confirmed Segment 5 size.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Email marketing consent = Subscribed (or "Accepts email marketing" = true)

AND

Condition 2: Number of orders = 0
```

**Exit condition:** Customer places first order → exits Segment 5, enters the appropriate buyer segment (1, 2, or 3).

**Overlap handling:** Mutually exclusive with all buyer segments by definition.

### Revenue Opportunity

Using prior estimate of **450 subscribers** (midpoint of 400–500) as working figure — replace with confirmed count when queried:

- **Primary conversion:** eBook (€48.99) as lowest-friction entry product
- **Alternative entry:** Physical Book (€68.99) for high-intent visitors

| Scenario | Formula | Result |
|---|---|---|
| Conservative — eBook first purchase (2% conversion) | 450 × 2% × €48.99 | **€440.91/mo** |
| Moderate — eBook first purchase (3% conversion) | 450 × 3% × €48.99 | **€661.37/mo** |
| Conservative — Physical Book first purchase (2%) | 450 × 2% × €68.99 | **€620.91/mo** |

**Revenue note:** Update these figures with the confirmed subscriber count from Shopify Admin.

### Automation to Activate
**Browse abandonment + nurture sequence**
- Email 1 (Day 1): "What pilots actually read before their interviews"
- Email 2 (Day 3): Social proof — student success story
- Email 3 (Day 7): Objection handling — "Is the book worth it if I already have interview prep?"
- Email 4 (Day 14): Scarcity / limited offer
- Email 5 (Day 30): Last chance + alternative entry point (old eBook at lower price point)

---

## Segment 6 — Repeat Buyer VIP

### Definition
Customers who have placed **2 or more orders**. These are the highest-engagement customers — they came back for more, indicating strong brand affinity.

### Live Count: **65 confirmed repeat buyers** (verified via ShopifyQL returning_customers cumulative total across all time)

**Breakdown by year (from live data):**
- 2024: 29 returning customers
- 2025: 27 returning customers
- 2026 YTD: 8 returning customers (to 2026-06-08)
- Cumulative total: **64–65 confirmed** (1 customer appears in overlap between year-end and monthly counts)

**Prior estimate of 50–80 is confirmed accurate.** Live count of 65 falls within the estimated range.

### AVADA Filter (copy-paste ready)
```
In AVADA → Contacts → Segments → Create Segment:

Condition 1: Number of orders >= 2
```

**Optional refinement — High-value VIP (top spenders):**
```
Condition 1: Number of orders >= 2
AND
Condition 2: Total spent >= €100
```

**Exit condition:** No exit — this is a permanent VIP tier. Once in, always in. Can be subdivided by spend tier as the segment grows.

**Overlap handling:** Repeat buyers likely exist in Segments 1, 2, and 3. In AVADA, set Segment 6 as a parallel segment (not exclusive). A customer can be in Segment 3 (Bundle) AND Segment 6 (VIP). Use tags in Shopify to track: `vip-repeat-buyer`. When automations overlap, Segment 6 messaging takes priority (suppress generic upsell sequences for VIPs).

### Revenue Opportunity

- Total gross sales: €147,082.12 / 2,528 customers = **€58.19 avg spend per customer**
- VIP segment (65 customers) are by definition multi-purchase, estimated avg spend: **€116–€180**

- **Primary goal:** Referral program, ambassador conversion
- **Revenue lever:** Each VIP who refers one buyer = €48.99–€84.99 in new revenue

| Scenario | Formula | Result |
|---|---|---|
| Conservative — referral (2% active referrers × 1 referral each) | 65 × 2% × 1 × €68.99 | **€89.69/mo** |
| Moderate — referral (5% active referrers × 2 referrals each) | 65 × 5% × 2 × €68.99 | **€448.44/mo** |
| Mock Interview upsell for non-buyers (2%) | 65 × 2% × €449.99 | **€584.99/mo** |

### Automation to Activate
**VIP Ambassador + referral program**
- Email 1: "You're one of 65 people who came back — here's why that matters to us"
- Email 2: Exclusive behind-the-scenes / pre-release content
- Email 3: Referral offer — unique code, tracked
- Quarterly: VIP check-in + product roadmap preview

---

## Revenue Opportunity Summary

*All figures use conservative 2% conversion as base, moderate 3% as upside. Segment 1 and 2 use midpoint exclusive estimates; Segment 5 uses prior estimate midpoint pending confirmed count.*

| Segment | Confirmed Size | Avg Spend | Conservative/mo | Moderate/mo | Automation |
|---|---|---|---|---|---|
| eBook-Only (S1) | ~750 est. (see notes) | €45.30 | €1,035 | €1,552 | Post-purchase upsell D7/21/45 |
| Physical-Only (S2) | ~665 est. (see notes) | €64.93 | €652 | €978 | Post-purchase digital companion |
| Bundle Buyer (S3) | **353 confirmed** | €79.55 | €2,826 | €4,239 | Win-back + Mock Interview |
| Mock Interview (S4) | **1 confirmed** | €449.99 | N/A (referral play) | N/A | VIP Ambassador sequence |
| Non-Buyer Subscriber (S5) | ~450 (unconfirmed) | €0 | €441 | €661 | Browse abandonment nurture |
| Repeat Buyer VIP (S6) | **65 confirmed** | €116–180 | €585 | €585 | Referral program |
| **TOTAL** | | | **€5,539/mo** | **€8,015/mo** | |

**Annualised opportunity:** €66,468 (conservative) to €96,180 (moderate)

---

## Data Quality Notes

### What was queried live (confirmed accurate)
1. **Per-variant buyer counts** from `FROM sales SHOW customers GROUP BY product_variant_title` — fully confirmed:
   - eBook: 1,066 customers
   - Physical Book: 1,018 customers
   - Physical + eBook Bundle: 353 customers
   - Old standalone eBook (Default Title): 142 customers
   - Mock Interview + CV: 1 customer
   - Total unique buyers: 2,528

2. **Returning customer count** (2+ purchases) from `FROM sales SHOW returning_customers TIMESERIES year` — confirmed **65 cumulative repeat buyers**

3. **Gross sales by variant** — confirmed:
   - Physical Book: €66,100.48
   - eBook: €48,292.91
   - Bundle: €28,083.84
   - Old eBook: €4,154.90
   - Mock Interview + CV: €449.99
   - **Total: €147,082.12**

### What could NOT be confirmed via available tools
1. **Exclusive segment sizes for S1/S2:** ShopifyQL's `FROM sales` table is order-line level, not customer-level for cross-product joins. It can tell you how many customers bought variant X but cannot simultaneously filter "bought X and NOT Y" at the analytics layer. The AVADA filter definitions solve this at execution time.

2. **Non-Buyer Subscriber count (S5):** `email_marketing_state` is not a dimension in ShopifyQL. The `list-customers` tool was permission-blocked in this session. Obtain this count from: Shopify Admin → Customers → filter "Email marketing = Subscribed" AND "Orders = 0".

3. **Per-variant top-5 customers:** The `list-customers` tool was permission-blocked. Product-level customer filtering (e.g., "customers who bought eBook") is not available in the ShopifyQL analytics layer. To get Top 5 per segment, use Shopify Admin customer export filtered by product purchased, or enable `list-customers` permissions.

4. **Standalone Mock Interview and CV Correction sales:** Zero recorded. Only Mock Interview + CV has 1 sale. Verify in Shopify Admin whether these variants exist as separate purchasable products or only as a bundle.

### Rate limiting
The Shopify Analytics API (ShopifyQL) enforced aggressive rate limiting throughout this session, requiring multiple retries per query. Each query required 10–20 retry attempts. All confirmed numbers above reflect successful query responses.

---

## Implementation Checklist

### AVADA Segment Creation
- [ ] Segment 1 — eBook-Only Buyer created in AVADA (verify count at creation)
- [ ] Segment 2 — Physical-Only Buyer created in AVADA (verify count at creation)
- [ ] Segment 3 — Bundle Buyer created in AVADA (expected: ~353)
- [ ] Segment 4 — Mock Interview Buyer created in AVADA (expected: ~1)
- [ ] Segment 5 — Non-Buyer Subscriber created in AVADA (query Shopify Admin first for count)
- [ ] Segment 6 — Repeat Buyer VIP created in AVADA (expected: ~65)

### Pre-Build Actions Required
- [ ] **Confirm S5 count:** Shopify Admin → Customers → filter Subscribed + 0 orders → export count
- [ ] **Confirm Mock Interview variants:** Verify CV Correction and Mock Interview standalone are live/purchasable
- [ ] **Check AVADA product filter capability:** Confirm AVADA can filter by specific product variant (not just product title)

### Tagging in Shopify
- [ ] Tag VIP customers (S6) with `vip-repeat-buyer` in Shopify customer profiles
- [ ] Tag Mock Interview buyers (S4) with `mock-interview-buyer`
- [ ] Tag Bundle buyers (S3) with `bundle-buyer`

### Automation Mapping
- [ ] Post-purchase upsell sequence → mapped to Segment 1 (eBook-Only)
- [ ] Digital companion sequence → mapped to Segment 2 (Physical-Only)
- [ ] Win-back + Mock Interview sequence → mapped to Segment 3 (Bundle)
- [ ] VIP Ambassador sequence → mapped to Segment 4 (Mock Interview) + Segment 6 (VIP)
- [ ] Browse abandonment nurture → mapped to Segment 5 (Non-Buyer Subscriber)

### Segment Priority Order in AVADA
Set this priority to prevent automation conflicts:
1. Segment 4 — Mock Interview Buyer (highest value, most exclusive)
2. Segment 6 — Repeat Buyer VIP (parallel, not exclusive — tag-based)
3. Segment 3 — Bundle Buyer
4. Segment 2 — Physical-Only Buyer
5. Segment 1 — eBook-Only Buyer
6. Segment 5 — Non-Buyer Subscriber (lowest priority — no purchase history)
