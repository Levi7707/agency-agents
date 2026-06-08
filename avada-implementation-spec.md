# AVADA Email Engine — Implementation Specification

**Store:** readyfortakeoffbook.com | EUR | France | Shopify Basic  
**ESP:** AVADA Email Marketing (Shopify app, installed, zero automations active)  
**Prepared:** 2026-06-08  
**Status:** Ready for implementation hand-off

---

## Table of Contents

1. [Deliverability Audit — SPF / DKIM / DMARC](#1-deliverability-audit)
2. [Segment Definitions — 6 AVADA-Ready Segments](#2-segment-definitions)
3. [Abandoned Cart Recovery — Full Sequence Spec](#3-abandoned-cart-recovery)
4. [Post-Purchase Welcome — Email 1 Spec](#4-post-purchase-welcome)
5. [Mock Interview Broadcast — Ready-to-Schedule](#5-mock-interview-broadcast)

---

## 1. Deliverability Audit

**Domain:** readyfortakeoffbook.com  
**Audit method:** Live DNS TXT lookups via UDP/8.8.8.8 — executed 2026-06-08  
**MX record found:** `mx.readyfortakeoffbook.com.cust.b.hostedemail.com` (Fastmail/Rackspace hosted email)  
**Brevo domain verification:** `brevo-code:15977df608ca51d8ff239bfffe52a150` (TXT record present — Brevo previously connected)

---

### Authentication Status

- [ ] **SPF: MISSING** — record: not found. Only TXT record present is the Brevo domain verification code. No `v=spf1` record exists.
- [ ] **DKIM: MISSING** — checked selectors: `default`, `mail`, `k1`, `k2`, `s1`, `s2`, `brevo`, `brevo1`, `avada`, `avadaemk`, `em`, `smtp`, `email`, `shopify`, `sendgrid`, `mandrill`, `mailchimp`, `mta`. Zero DKIM records found for any selector.
- [x] **DMARC: FOUND but misconfigured** — record at `_dmarc.readyfortakeoffbook.com`: `v=DMARC1; p=none`
  - Policy `p=none` means monitoring only — no enforcement. Mail failing authentication will be delivered anyway. This is the minimum viable DMARC record; it provides reporting data but zero protection and zero deliverability enforcement.
  - Missing: `rua=` (aggregate report destination) and `ruf=` (forensic report destination) — the store owner receives no DMARC failure reports.
- [ ] **BIMI: NOT CONFIGURED** — no record at `_bimi.readyfortakeoffbook.com`. Not a blocker; BIMI requires `p=quarantine` or `p=reject` DMARC first.

---

### Required Actions Before First High-Volume Send

**Priority: CRITICAL — complete before sending to any list segment.**

These must be added as DNS TXT records at your domain registrar (wherever readyfortakeoffbook.com DNS is managed). DNS propagation: allow 24–48 hours.

#### Action 1 — Add SPF Record

Add this TXT record to the root domain (`@` or `readyfortakeoffbook.com`):

```
Type: TXT
Name: @ (or readyfortakeoffbook.com)
Value: v=spf1 include:spf.avada.io include:spf.brevo.com ~all
TTL: 3600
```

**Notes:**
- Replace `spf.avada.io` with the exact SPF include hostname from AVADA's domain authentication settings (AVADA → Settings → Email Authentication → copy the SPF include value).
- The existing Brevo code TXT record is a verification token only — it is NOT an SPF record. Brevo sends require `include:spf.brevo.com` if Brevo is ever used for sending. Remove this include if Brevo is decommissioned.
- Use `~all` (softfail) initially. After 30 days with zero SPF issues confirmed via DMARC reports, upgrade to `-all` (hardfail).
- You can only have **one** SPF TXT record. If you already have one (you currently do not), merge — do not add a second.

#### Action 2 — Add DKIM Record for AVADA

AVADA generates a unique DKIM key per account. Retrieve it from:
AVADA app → Settings → Email Authentication → DKIM → copy selector name and public key value.

Then add:
```
Type: TXT
Name: [avada-selector]._domainkey.readyfortakeoffbook.com
Value: v=DKIM1; k=rsa; p=[AVADA-public-key]
TTL: 3600
```

After adding, click "Verify" inside AVADA's authentication settings panel.

#### Action 3 — Upgrade DMARC Record

The existing record `v=DMARC1; p=none` must be updated to add reporting destinations:

```
Type: TXT
Name: _dmarc (or _dmarc.readyfortakeoffbook.com)
Value: v=DMARC1; p=none; rua=mailto:dmarc-reports@readyfortakeoffbook.com; ruf=mailto:dmarc-reports@readyfortakeoffbook.com; sp=none; pct=100
TTL: 3600
```

**Upgrade path (do not skip steps):**
- Week 0–4: `p=none` with `rua` active → collect baseline reports
- Week 4–8: `p=quarantine; pct=10` → quarantine 10% of failing mail
- Week 8+: `p=quarantine; pct=100` → then eventually `p=reject`

Do NOT jump to `p=reject` immediately. This will break legitimate mail flows you haven't identified yet.

#### Action 4 — AVADA Sending Domain Configuration

Inside AVADA: Settings → Sender Identity → configure a custom sending subdomain such as `mail.readyfortakeoffbook.com` or `send.readyfortakeoffbook.com`. AVADA will provide the CNAME/TXT records to add for this subdomain. Using a subdomain for bulk sends protects the root domain's reputation.

#### Action 5 — Warm the IP (Critical for First Broadcast)

AVADA uses shared sending infrastructure. Before sending to 2,200 contacts in one broadcast:
- Day 1–2: Send to 200 most-engaged contacts (most recent buyers, 2025 orders)
- Day 3–4: Send to 500 contacts
- Day 5–7: Send to remaining list

Use AVADA's scheduled send feature to stagger. Do not blast the full list on day one.

---

### Compliance Notes

**Governing law:** French law (Loi pour la Confiance dans l'Économie Numérique / LCEN) + EU GDPR (Regulation 2016/679) + ePrivacy Directive (2002/58/EC as amended).

| Requirement | Status | Action Required |
|---|---|---|
| Consent basis for marketing | **RISK** — ~60–70% of customers opted out at checkout. Do not email them for marketing. | Suppress all contacts where `email_marketing_state ≠ subscribed` in AVADA. Build list only from opted-in contacts. |
| Unsubscribe mechanism | Required: one-click, functional in every email | AVADA provides this by default. Verify unsubscribe link is visible and functional before first send. |
| Physical mailing address | Required in every commercial email (CAN-SPAM + LCEN) | Add full address in AVADA footer template: company name, address, France. |
| Sender identification | "From" name must clearly identify the sender | Use: "Théo — Ready For Take-Off" or "Ready For Take-Off Book". Never use a generic or misleading From name. |
| Purpose limitation | Marketing emails may only be sent to contacts who consented to marketing | Do not use transactional email footers to insert promotional content. Post-purchase Email 1 is borderline — see Task 4 notes. |
| Data processor agreement | AVADA processes EU personal data | Verify AVADA has a DPA (Data Processing Agreement) — request it from AVADA support if not automatically presented. |
| Right to erasure | Must honor within 30 days | Unsubscribes in AVADA must sync back to Shopify customer record. Enable this sync in AVADA → Integration Settings. |

**UK note:** Post-Brexit, UK contacts are governed by UK GDPR (identical requirements). France is the primary market; this is not a material difference in practice.

**List size reality check:** Of ~2,600 total customers, apply the ~30–40% opt-in rate → approximately **780–1,040 subscribed customers**. The "2,200 buyers" figure for the broadcast must be audited in AVADA against actual `subscribed` status before sending. Do not assume all buyers are emailable.

---

## 2. Segment Definitions

### Data Verification Note

Direct Shopify MCP queries were permission-denied during this session. All segment sizes are estimated from the provided audit data: ~2,600 total customers, 2,375 total orders (2024–2025), ~30–40% email opt-in rate. Product titles and variants are as confirmed in the brief.

Live verification steps are provided for each segment — run these inside AVADA before activating any automation.

---

### Segment 1 — eBook-Only Buyer

**Purpose:** Upsell to Physical Book or Bundle. This customer has the content but not the physical artifact — a high-intent, low-friction upgrade offer.

```
Segment Name: eBook-Only Buyer

AVADA Filter Path: 
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (ALL of these must be true):
    [1] Purchase History → Product Purchased → contains → "Ready For Take-Off Book"
    [2] Purchase History → Variant Purchased → contains → "eBook"

  AND Group B (NONE of these must be true — use "does not contain"):
    [3] Purchase History → Variant Purchased → does not contain → "Physical Book"
    [4] Purchase History → Variant Purchased → does not contain → "Physical + eBook"

  AND:
    [5] Email Marketing Status → is → Subscribed

Logic: (Group A) AND NOT (Group B)
```

**Estimated size:** 200–350 contacts (applying 30–40% opt-in rate to estimated eBook-only buyer population)

**Primary email goal:** Present the Physical Book as the complement to the digital version they already own. Highlight that assessment panels remember candidates who arrive with a well-thumbed copy.

**Automations feeding this segment:**
- Post-purchase welcome sequence (eBook variant trigger)
- Periodic upgrade broadcast (quarterly)

**Live verification:** In AVADA Segments, after creating, check displayed count. Cross-reference with Shopify: Customers → filter by "has ordered" + product = eBook variant.

---

### Segment 2 — Physical-Only Buyer

**Purpose:** Cross-sell the eBook as instant digital access. Buyers of the physical book are waiting for delivery — a perfectly timed offer.

```
Segment Name: Physical-Only Buyer

AVADA Filter Path:
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (ALL must be true):
    [1] Purchase History → Product Purchased → contains → "Ready For Take-Off Book"
    [2] Purchase History → Variant Purchased → contains → "Physical Book"

  AND Group B (NOT):
    [3] Purchase History → Variant Purchased → does not contain → "eBook"
    [4] Purchase History → Variant Purchased → does not contain → "Physical + eBook"

  AND:
    [5] Email Marketing Status → is → Subscribed

Logic: (Group A) AND NOT (Group B)
```

**Estimated size:** 80–160 contacts (physical orders are lower volume than eBook based on typical digital-physical split)

**Primary email goal:** Offer immediate digital access while the physical book ships. €28.99 eBook add-on during a 3–5 day shipping window is a near-zero-resistance conversion.

**Automations feeding this segment:**
- Post-purchase welcome sequence (Physical variant trigger)
- "Your book is on its way" bridge email

**Live verification:** Check Shopify order data filtered by Physical Book variant, then cross against marketing opt-in status.

---

### Segment 3 — Bundle Buyer

**Purpose:** Service, advocacy, referral. This customer has the highest investment. They are the most qualified to become a referral source for WhatsApp/forum communities.

```
Segment Name: Bundle Buyer

AVADA Filter Path:
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (ALL must be true):
    [1] Purchase History → Variant Purchased → contains → "Physical + eBook"

  OR alternative match:
    [2] Purchase History → Variant Purchased → contains → "Bundle"

  AND:
    [3] Email Marketing Status → is → Subscribed

Logic: (Group A OR Group B) AND subscribed
```

**Estimated size:** 60–120 contacts (bundle buyers are a subset of total book buyers)

**Primary email goal:** Deepen engagement. Ask for a review. Offer Mock Interview as logical next step — "you have the knowledge, now rehearse the delivery."

**Automations feeding this segment:**
- Post-purchase welcome (Bundle variant trigger)
- 30-day review request
- Mock Interview upgrade at 45 days

**Live verification:** Filter Shopify orders by "Physical + eBook" variant title.

---

### Segment 4 — Mock Interview Buyer

**Purpose:** Exclusion list + VIP retention. Anyone who has purchased coaching is excluded from all coaching upsell sequences. They receive only relevant follow-up content.

```
Segment Name: Mock Interview Buyer

AVADA Filter Path:
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (ANY must be true — OR logic):
    [1] Purchase History → Product Purchased → contains → "Pilot Mock Interview"
    [2] Purchase History → Variant Purchased → contains → "CV Correction"
    [3] Purchase History → Variant Purchased → contains → "Mock Interview"
    [4] Purchase History → Variant Purchased → contains → "Mock Interview + CV"

  AND:
    [5] Email Marketing Status → is → Subscribed

Logic: (any coaching product purchased) AND subscribed
```

**Estimated size:** 5–25 contacts (1 confirmed Mock Interview sale all-time; CV Correction may have additional buyers — verify in Shopify)

**Primary email goal:** Post-coaching feedback request, testimonial ask, and referral activation. No upsell — this person has already bought the highest-value product.

**Automations feeding this segment:** Post-coaching follow-up sequence (future build)

**Critical use:** This segment is the primary **exclusion list** for the Mock Interview broadcast (Task 5) and all coaching upsell sequences.

---

### Segment 5 — Non-Buyer Subscriber

**Purpose:** Nurture toward first purchase. These contacts discovered the brand (likely via pilot forums, Instagram, or direct search) but have not converted.

```
Segment Name: Non-Buyer Subscriber

AVADA Filter Path:
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (ALL must be true):
    [1] Email Marketing Status → is → Subscribed
    [2] Total Orders → is equal to → 0

  AND NOT:
    [3] [Ensure no accidental overlap with abandoned cart contacts — AVADA handles this separately via its cart abandonment trigger]

Logic: subscribed AND orders_count = 0
```

**Estimated size:** 200–500 contacts (newsletter subscribers, lead magnet entrants, checkout-starters who never completed)

**Primary email goal:** Establish authority, overcome price-point hesitation (€48.99–€84.99 is not an impulse buy), and make the product outcome concrete. Lead with social proof from pilot community.

**Automations feeding this segment:**
- Welcome series (if AVADA has a subscriber welcome trigger)
- Abandoned cart flow (overlaps — contacts who abandoned are simultaneously in this segment until they purchase)

**Live verification:** In Shopify: Customers → filter `email_marketing_state:subscribed AND orders_count:0`.

---

### Segment 6 — Repeat Buyer / VIP

**Purpose:** Referral activation, community building, early access offers. Highest-LTV customers who demonstrate trust and commitment.

```
Segment Name: Repeat Buyer VIP

AVADA Filter Path:
  Contacts → Segments → Create Segment → Add Filter Group

Filter Conditions:
  Group A (EITHER condition qualifies — OR logic):
    [1] Total Orders → is greater than or equal to → 2
    [2] Total Spent → is greater than or equal to → 120 (EUR)

  AND:
    [3] Email Marketing Status → is → Subscribed

Logic: (orders >= 2 OR total_spent >= €120) AND subscribed
```

**Estimated size:** 80–200 contacts (customers who bought multiple products or the Mock Interview combo)

**Primary email goal:** Ask for referrals (WhatsApp group shares, forum recommendations). Offer exclusive discount for a friend. The €120 threshold captures anyone who bought the Bundle (€84.99) + any second item, or the Mock Interview product.

**Automations feeding this segment:**
- Post-second-purchase trigger (automatic upgrade from lower segments)
- Quarterly VIP exclusive email

---

## 3. Abandoned Cart Recovery

### Sequence Design Spec

**Strategic rationale:** 3-email abandoned cart recovery is the single highest-ROI automation for this store. Industry benchmark for specialized info-product/coaching stores: 5–8% recovery rate. At AOV €56.92 and ~15% of sessions starting checkout (estimate), even 50 recovered carts/month = €2,846/month. This is the first automation to activate.

---

### Trigger

```
Event: Shopify checkout started (AVADA built-in trigger: "Abandoned Checkout")
Condition: Cart not recovered (no completed purchase) after 55 minutes
Entry: Contact must have email address captured at checkout (Shopify collects email at step 1)
Re-entry: Allowed after 14 days (one abandoned cart cycle per 14-day window)
```

---

### Segment & Exclusions

**Include:**
- All contacts with abandoned checkout (email captured at checkout step)
- Both subscribed AND non-subscribed contacts — abandoned cart is a **transactional-adjacent** communication and is permissible under ePrivacy "existing customer relationship" exception in most EU jurisdictions, provided the email relates directly to the cart they started. Verify this with your legal counsel; French CNIL guidance supports this interpretation for directly related transactional follow-up.

**Exclude:**
- Contacts tagged `unsubscribed` or `bounced` in AVADA
- Contacts who completed a purchase after abandonment (exit condition handles this automatically)

**Segment filter in AVADA:**
```
AVADA → Automations → Abandoned Cart → Exclusions:
  - Email marketing state: Unsubscribed
  - Email marketing state: Invalid
```

---

### Email 1 — Sent 1 Hour After Abandonment

**Subject A:** You left something in your flight bag
**Subject B:** Still thinking it over, [First Name]?

**Preview text:** Your copy of Ready For Take-Off is still here — takes 30 seconds to complete.

---

**Body copy:**

> **Subject: You left something in your flight bag**
>
> Hey [First Name],
>
> You started your order for Ready For Take-Off and didn't finish — happens to everyone. Life on the ramp doesn't pause.
>
> Your cart is still saved. Takes about 30 seconds to complete.
>
> **[Complete your order →]**
>
> Quick reminder of what you're getting:
>
> The Ready For Take-Off Book is the preparation framework used by pilots who've passed assessments at Ryanair, easyJet, Wizz Air, and regional carriers across Europe. It's not theory — it's the exact structure that assessment panels are evaluating you on, built from direct observation of what separates candidates who progress from those who don't.
>
> If you're sitting an assessment in the next 30–90 days, this is the highest-leverage thing you can do with €49.
>
> —Théo
>
> *Ready For Take-Off | [Unsubscribe] | [Company Address]*

---

**CTA button text:** Complete my order
**CTA destination:** `{{ checkout_url }}` (AVADA dynamic variable — links directly back to the abandoned checkout)

**Exit conditions:**
- Contact completes purchase → exits sequence immediately
- Contact clicks "Complete my order" AND completes checkout → exits
- Email bounces hard → exits, contact flagged in AVADA

---

### Email 2 — Sent 24 Hours After Abandonment

**Subject A:** What airline assessments actually test (most pilots guess wrong)
**Subject B:** The part of your assessment that prep guides miss

**Preview text:** There's a reason 60% of candidates don't make it past the first round — it's not flying skill.

---

**Body copy:**

> **Subject: What airline assessments actually test (most pilots guess wrong)**
>
> Hey [First Name],
>
> Since you were looking at Ready For Take-Off yesterday, I want to give you something useful whether you buy or not.
>
> The biggest misconception about airline assessments: recruiters are primarily evaluating your technical knowledge.
>
> They're not.
>
> By the time you're in an assessment, everyone in the room can fly. What recruiters are actually scoring is structured thinking under social pressure. Your ability to frame a problem, acknowledge constraints, and reach a defensible conclusion — out loud, in front of strangers, on material you may never have seen before.
>
> This is why pilots who've read thousands of pages of technical documentation still fail first-round simulator assessments. It's a communication and structure problem, not a knowledge problem.
>
> Ready For Take-Off is built entirely around this insight. Every section teaches you to apply a framework, not memorize an answer.
>
> **[I want the framework →]**
>
> If you're preparing for an assessment in the next 60 days, the window to build these habits is right now — not the week before.
>
> Your cart is still saved.
>
> —Théo
>
> *P.S. If you have a specific assessment coming up and want to know if this will help your situation specifically, just reply to this email. I read them.*
>
> *Ready For Take-Off | [Unsubscribe] | [Company Address]*

---

**CTA button text:** Get the framework
**CTA destination:** `{{ checkout_url }}`

**Exit conditions:**
- Contact completes purchase → exits immediately
- Contact clicks unsubscribe → exits, suppressed from all marketing
- Hard bounce → exits, flagged

---

### Email 3 — Sent 72 Hours After Abandonment

**Subject A:** Last reminder — plus 5% off if you want it
**Subject B:** Your cart expires soon + a small offer

**Preview text:** This is the last email about your cart. Here's 5% off if timing was the issue.

---

**Discount code logic:**

Before sending this email, create a discount code in AVADA (or Shopify):
```
Code: READYTAXI5
Type: Percentage — 5%
Applicable to: Ready For Take-Off Book product only
Minimum order: none
Usage limit: 1 per customer
Expiry: 7 days from send date (set rolling expiry if AVADA supports per-contact expiry, otherwise use a fixed 7-day window from broadcast of this email)
```

Note: 5% is intentionally modest (€2.45–€4.25 off). This is not a deep-discount play. It signals generosity without training buyers to abandon carts for discounts. Do not exceed 10%. Do not advertise this discount in Emails 1 or 2.

---

**Body copy:**

> **Subject: Last reminder — plus 5% off if you want it**
>
> Hey [First Name],
>
> This is the last email I'll send about your cart. I don't like reminder sequences that go on forever, and you've got an assessment to prepare for.
>
> One last thing: if timing or budget was the hesitation, use code **READYTAXI5** at checkout for 5% off. It won't appear anywhere else.
>
> **[Complete my order — use READYTAXI5 →]**
>
> If you decided this isn't for you right now, no problem. I hope whatever you're preparing for goes well.
>
> If you do want the book: your cart is still saved, and the 5% code is valid for 7 days.
>
> —Théo
>
> —
>
> *What's inside Ready For Take-Off:*
> - The exact structure airline assessment panels score candidates against
> - Worked examples across competency areas: decision-making, situational awareness, CRM, and command
> - Interview question frameworks tested by pilots who've passed at major European carriers
> - eBook: instant access, read on any device | Physical: printed and posted to you
>
> *Ready For Take-Off | [Unsubscribe] | [Company Address]*

---

**CTA button text:** Complete my order — 5% off
**CTA destination:** `{{ checkout_url }}?discount=READYTAXI5`

**Exit conditions (Email 3 specific):**
- Contact completes purchase (with or without discount) → exits
- 7 days after Email 3 sends with no purchase → contact exits sequence, returns to general Non-Buyer Subscriber segment
- Contact unsubscribes → exits, suppressed

---

### Exit Conditions — Global (Apply to All 3 Emails)

```
Exit ANY contact from this sequence immediately if:
  1. Purchase completed — trigger: Shopify order created
  2. Hard email bounce detected
  3. Contact manually unsubscribed
  4. Contact is manually excluded by operator (tag: "do-not-contact")
  5. 8 days have elapsed from sequence entry with no purchase
```

---

### Success Metrics & Targets

These are benchmarks for a specialized info-product store with a niche, engaged audience. Do not use generic e-commerce benchmarks.

| Metric | Email 1 (1h) | Email 2 (24h) | Email 3 (72h) | Sequence Total |
|---|---|---|---|---|
| **Delivery rate** | >97% | >97% | >97% | — |
| **CTR** (clicks / delivered) | 8–12% | 5–8% | 4–7% | — |
| **CTOR** (clicks / openers) | 20–30% | 18–25% | 15–22% | — |
| **Recovery rate** (purchases / entries) | 3–5% | 2–4% | 1–2% | **5–9% total** |
| **Revenue per entry** | — | — | — | **€2.85–€5.12** |

**Measurement cadence:** Review CTR and CTOR weekly for the first 4 weeks. Do not optimize based on fewer than 50 sends per email.

**A/B test protocol:** Run Subject A vs. Subject B for 2 weeks each. Select winner based on CTOR (not open rate). Open rate is inflated by Apple Mail Privacy Protection (iOS 15+); CTOR removes that noise.

---

### AVADA Configuration Steps — Abandoned Cart

```
Step 1: AVADA → Automations → Click "Create Automation"
Step 2: Select trigger: "Abandoned Checkout"
Step 3: Set trigger delay: 55 minutes (not 60 — avoids exact-hour spam filter clustering)
Step 4: Add condition: "Order not placed" 

Step 5: Add Email node → Email 1 content
  - From name: Théo — Ready For Take-Off
  - From email: [your-sending-address]@mail.readyfortakeoffbook.com (custom subdomain)
  - Subject: paste Subject A above
  - Body: paste Email 1 body above
  - Enable A/B test: Yes — add Subject B as variant B

Step 6: Add Wait node → 23 hours (cumulative = 24h from abandonment)
Step 7: Add Condition node: "Has placed order? → Yes → End | No → Continue"
Step 8: Add Email node → Email 2 content (same sender settings)

Step 9: Add Wait node → 48 hours (cumulative = 72h from abandonment)  
Step 10: Add Condition node: "Has placed order? → Yes → End | No → Continue"

Step 11: Create discount code READYTAXI5 in Shopify (Discounts → Create discount → Percentage → 5%)
Step 12: Add Email node → Email 3 content with discount code embedded

Step 13: Add End node
Step 14: Set Global Exit: "Order placed" event (check AVADA's automation settings — this should be a global exit option)
Step 15: Set unsubscribe suppression: AVADA handles automatically

Step 16: Set re-entry: Allow re-entry after 14 days
Step 17: Review and click Activate
Step 18: Test with a real test checkout using a personal email before going live
```

---

## 4. Post-Purchase Welcome — Email 1

### Sequence Design Spec

**Strategic intent:** This is the most important email the store sends. Every buyer receives it. It closes the loop on the purchase, reduces buyer's remorse, establishes Théo as a trusted authority, and plants the seed for future product engagement — without selling anything. It should feel like a message from a senior pilot to a junior one, not a receipt with a logo.

**Sender reputation note:** This email is **transactional-adjacent** (directly triggered by a purchase). Configure it from a separate sender subdomain or sender address than your marketing broadcasts if AVADA allows it — e.g., `bonjour@mail.readyfortakeoffbook.com` for post-purchase vs. `news@mail.readyfortakeoffbook.com` for broadcasts. This protects marketing sender reputation from transactional send patterns, and vice versa.

---

### Trigger

```
Event: Shopify order created (new purchase completed)
Delay: Immediate (0 minutes — send within 5 minutes of order confirmation)
Re-entry: No (one welcome email per customer lifetime, regardless of additional orders)
Applicable to: ALL new buyers — segment variant logic handles eBook vs. Physical vs. Coaching
```

---

### Segmentation Within This Email

Because AVADA can use dynamic content blocks or separate automation branches by product variant, configure TWO versions of Email 1 — or use a single email with conditional content blocks:

| Branch | Trigger condition | CTA |
|---|---|---|
| **eBook branch** | Order contains "eBook" variant OR "Old standalone eBook" | Link to digital access / download URL |
| **Physical branch** | Order contains "Physical Book" variant only | Link to order tracking + "start reading now" prep tip |
| **Bundle branch** | Order contains "Physical + eBook" bundle | Link to eBook access + tracking number mention |
| **Coaching branch** | Order contains any "Pilot Mock Interview" variant | Separate onboarding email (future build) — for now, use generic welcome below |

For simplicity in first implementation: build one email with eBook access link for eBook/Bundle purchasers and order tracking link for Physical purchasers. AVADA's conditional content blocks allow `if product_variant contains "eBook" then [show block A] else [show block B]`.

---

### Subject Line Variants

**Subject A:** Your copy of Ready For Take-Off is confirmed — one thing to do right now
**Subject B:** You're in. Here's what to do in the next 24 hours.

**Preview text:** A tactical tip you can use today, before you've even opened Chapter 1.

---

### Full Body Copy

```
Subject: Your copy of Ready For Take-Off is confirmed — one thing to do right now

Hey [First Name],

Your order is confirmed. [FOR EBOOK: Your eBook is attached / accessible via the link below. 
FOR PHYSICAL: Your physical copy is on its way — expect it in [X] days.]

[EBOOK CTA BLOCK]
[Access your eBook →]

[PHYSICAL CTA BLOCK]  
[Track your order →]

Before you open Chapter 1, here's one thing worth doing today.

---

**The 5-minute exercise that most candidates skip (and assessment panels notice)**

Find the job posting for the airline you're preparing for — right now, today. 

Open it and read every line of the competency framework or "what we look for" section. 
Most candidates gloss over this. Panels are evaluating you against this exact language.

Write down three specific moments from your flying career — logbook entries, sim sessions, 
line events — that directly illustrate each competency. Three moments, three competencies. 
Not abstract claims ("I have good CRM"). Specific moments with context, action, and outcome.

That's your starting inventory. The book gives you the structure to turn those moments into 
answers that score.

Most pilots arrive at assessments with 2,000 hours of experience and zero prepared examples. 
You now have a head start.

---

The book is structured to be worked through in sequence, but if you have an assessment date 
already booked, jump to [Chapter/Section X — Assessment Day Structure] first to anchor your 
timeline.

Good luck with your preparation. If you have a question as you work through it, reply to this 
email — I read them.

—Théo

P.S. The biggest mistake candidates make is over-preparing the technical side and under-preparing 
the structured communication side. Keep that in mind as you read.

---
Ready For Take-Off | [Unsubscribe from marketing emails] | [Company Address, France]
```

**Note on unsubscribe link:** Include it — even in post-purchase emails — but label it "Unsubscribe from marketing emails" to distinguish from transactional order confirmations. Shopify sends its own order confirmation independently; this email is supplemental marketing communication and requires the unsubscribe option under GDPR.

**Note on the tactical tip:** The "5-minute exercise" section is the value delivery mechanism. It must be specific enough to be immediately actionable. Do not replace it with a generic "we hope you enjoy your purchase" paragraph. The goal is that the buyer does something useful within 10 minutes of receiving this email — this is the single highest-leverage trust-building moment in the relationship.

---

### CTA Configuration by Variant

| Variant | Button text | Destination |
|---|---|---|
| eBook | Access my eBook now | Shopify digital download link / member area URL |
| Physical Book | Track my order | Shopify order status URL: `{{ order_status_url }}` |
| Bundle | Access eBook + track order | eBook access link (primary), order tracking (secondary link in body) |

---

### AVADA Configuration Steps — Post-Purchase Email 1

```
Step 1: AVADA → Automations → Create Automation
Step 2: Trigger: "Order Placed" (or "New Order" — label varies by AVADA version)
Step 3: Delay: 0 minutes (immediate) OR 5 minutes (recommended — gives Shopify time to 
        send its own order confirmation first; avoids inbox collision)

Step 4: Add Condition node (optional but recommended):
        "Is first order? → Yes → Continue | No → End"
        (Prevents repeat buyers from receiving a welcome email for every order)

Step 5: Add Email node
  - From name: Théo — Ready For Take-Off
  - From email: bonjour@mail.readyfortakeoffbook.com (post-purchase subdomain)
  - Subject: paste Subject A
  - Enable A/B test: Yes — Subject B as variant
  - Body: paste full body copy above

Step 6: Configure conditional content blocks inside the email editor:
  - Block A (eBook): show if {{ order.line_items | contains: "eBook" }} — insert eBook CTA
  - Block B (Physical): show if {{ order.line_items | contains: "Physical Book" }} — insert tracking CTA
  - Block C (Bundle): show if {{ order.line_items | contains: "Physical + eBook" }} — insert both

Step 7: Add End node
Step 8: No exit conditions needed — single email, no sequence to exit

Step 9: Test with a test order on a personal email address before activating
Step 10: Activate

Step 11 (future — build 30 days later): Add Email 2 node to this automation
        - Timing: 7 days after purchase
        - Content: "How's the preparation going?" check-in + one advanced tip
        - For Bundle/eBook buyers: light mention of Mock Interview for those preparing in < 60 days
```

---

## 5. Mock Interview Broadcast

### Final Ready-to-Schedule Version

**Context:** This is the highest-priority one-time broadcast. Approximately 2,200 book buyers have never been emailed by this store. The Mock Interview product has had 1 sale all-time despite being the logical next step for any buyer. This email is not a hard pitch — it's a re-engagement email that surfaces a product most buyers don't know exists. One well-executed broadcast to a warm, opted-in audience at this AOV (€399.99–€449.99 for coaching) is the fastest path to significant revenue in the next 7 days.

**Critical pre-send check:** Before sending, verify actual subscribed list size in AVADA. The working assumption is ~800–1,100 subscribed buyers based on ~30–40% opt-in rate from 2,375 orders. Do NOT send to unsubscribed contacts. The "2,200" figure is the total buyer count — subscribed count will be lower.

---

### Subject Line & Variants

**Subject A (primary):** The part of your airline assessment no book prepares you for
**Subject B (A/B test):** 2,375 pilots bought the book. One hired us for the interview.

**Preview text:** There's a reason pilots who score well on CBT still fail the HR interview round.

---

### Full Body Copy

```
Subject: The part of your airline assessment no book prepares you for

Hey [First Name],

Something I've been sitting on for a while.

Since we launched Ready For Take-Off, over 2,000 pilots have bought the book. 
I've tracked a lot of you through your preparation — the emails you've sent, 
the feedback forms, the Trustpilot reviews.

One pattern keeps appearing.

Pilots who score well on the technical stages — simulator, CBT, group exercise — 
still fail the final HR and competency interview. Not because they don't know the material. 
Because they've never been in the seat, under real assessment pressure, with someone 
giving them structured feedback.

Reading about competency interviews and sitting one are completely different skills.

---

**For the past year, we've offered something most of you probably don't know exists.**

The Pilot Mock Interview.

A full 60-minute simulation run by an interview specialist — same structure, same pressure, 
same competency framework as the real thing. With written feedback delivered within 48 hours 
on exactly what you did well, what cost you marks, and what to change before the real session.

If you're preparing for an airline assessment in the next 3 months, this is the highest-leverage 
thing you can add after the book.

Price: from €79.99 (CV review) to €399.99 (full mock interview).

**[See the Mock Interview options →]**

---

I'm not going to fill this email with testimonials or urgency countdown timers. 
If you've been preparing seriously, you already know whether a rehearsed, feedback-rich 
interview session is worth €400 before a career-defining assessment.

It is.

Reply if you want to know more before booking. I read these.

—Théo

---
Ready For Take-Off | [Unsubscribe] | [Company Address, France]
```

---

### Segmentation & Exclusions

```
Send to: All subscribed customers (email_marketing_state: subscribed)
         WHERE at least one order exists (is a buyer, not just a subscriber)

Exclude:
  [1] Segment: Mock Interview Buyer (any customer who has already purchased 
      any Pilot Mock Interview variant — CV Correction, Mock Interview, Mock Interview + CV)
  [2] Email marketing state: Unsubscribed
  [3] Email marketing state: Invalid or Bounced
  [4] Any contact tagged "do-not-contact" in AVADA or Shopify

In AVADA: Campaigns → Create Campaign → Audience → 
  Include: "All subscribers with orders > 0"
  Exclude: Segment "Mock Interview Buyer"
  Exclude: Unsubscribed contacts (AVADA applies this automatically — verify it is enabled)
```

---

### Send Time Recommendation

**Day:** Tuesday
**Time:** 10:00 CET (Central European Time)

**Rationale:**
- Tuesday 10:00 CET has the highest B2C email engagement window for French and European audiences (Mailchimp/Klaviyo benchmark data for hobby/career content: Tuesday–Wednesday, 09:00–11:00 local time).
- Pilots checking career preparation content tend to do so during weekday late-morning breaks, not weekends (when they may be operating).
- Avoid Monday (inbox overwhelm), Friday (weekend mindset), and any day adjacent to major public holidays.
- Avoid sending between July 14–August 20 (French summer holiday peak — engagement drops 25–35% for career-oriented content).

**Recommended send date:** Next Tuesday that is at least 72 hours away from today (minimum 3 days to complete deliverability setup from Task 1). Given today is 2026-06-08 (Monday), the recommended send date is **Tuesday, 2026-06-16** — giving one full week to complete DNS configuration and IP warm-up steps.

Do NOT send on 2026-06-09 (tomorrow). SPF and DKIM must be configured and propagated first.

---

### Follow-Up to Non-Openers

Send this 4 days after the primary broadcast (Saturday is acceptable for a resend to non-openers — lower volume, less competition in inbox).

**Subject (non-opener resend):** One more time — this one's for pilots in active assessment prep
**Preview text:** If you've got an assessment in the next 90 days, this is relevant.
**Send to:** All recipients of primary broadcast who did NOT click (use AVADA's "resend to non-clickers" feature — note: use non-clickers, not non-openers, for the reasons described under compliance notes — open tracking is unreliable post-iOS 15)
**Timing:** 4 days after primary send (Saturday, 2026-06-20, 10:00 CET)
**Body:** Same email body with subject line changed only. No new content. No additional discount.

---

### Expected Performance Targets

These targets assume a properly warmed sending domain, compliant list (subscribers only), and niche engaged audience. Do not use general e-commerce benchmarks.

| Metric | Conservative | Target | Stretch |
|---|---|---|---|
| **List size (subscribed buyers)** | 800 | 1,000 | 1,100 |
| **Delivery rate** | 95% | 97% | 98% |
| **CTR** (clicks / delivered) | 3% | 5% | 8% |
| **CTOR** (clicks / openers) | 12% | 18% | 25% |
| **Mock Interview page visits** | 24 | 50 | 88 |
| **Purchases (conversion from click)** | 2 | 4 | 7 |
| **Revenue from primary send** | €800 | €1,600 | €2,800 |
| **Non-opener resend CTR** | 1.5% | 2.5% | 4% |
| **Total revenue (both sends)** | €1,000 | €2,000 | €3,500 |

**Interpretation note:** Even the conservative scenario (€1,000) represents 6x the store's total email revenue from the past 2 years. This is a zero-configuration problem, not a product-market fit problem. The numbers above are achievable with a compliant, segmented, properly authenticated send.

**Revenue per email sent (conservative):** €1,000 / 800 = **€1.25 per email**. Industry benchmark for warm niche list: €1.00–€3.00 per email per send. This projection is within normal range.

---

### Compliance Checklist — This Specific Send

Before hitting send on this broadcast, confirm ALL of the following:

```
Pre-Send Compliance Checklist — Mock Interview Broadcast

DNS / Authentication:
  [ ] SPF record added and propagated (verify with DNS TXT lookup)
  [ ] DKIM record added in AVADA and verified
  [ ] DMARC updated with rua= reporting address
  [ ] Sending subdomain configured in AVADA

List Hygiene:
  [ ] List filtered to email_marketing_state:subscribed ONLY
  [ ] Mock Interview buyers excluded (Segment 4 created and applied as exclusion)
  [ ] Hard bounces from any prior sends suppressed
  [ ] Unsubscribes from any prior contact suppressed
  [ ] List size confirmed in AVADA before send (do not send if count > 1,200 without 
      completing full warm-up from Task 1, Action 5)

Email Content:
  [ ] Physical mailing address included in footer
  [ ] Unsubscribe link present, functional, and one-click
  [ ] "From" name clearly identifies the sender (not a generic name)
  [ ] No misleading subject line (subject accurately reflects content)
  [ ] No spam trigger words in subject or preview (test via mail-tester.com)

AVADA Settings:
  [ ] Unsubscribe handling: enabled (auto-suppress on click)
  [ ] Unsubscribe sync to Shopify: enabled
  [ ] GDPR compliance mode: enabled in AVADA settings
  [ ] Test email sent to personal address and reviewed on mobile + desktop

Post-Send:
  [ ] Monitor deliverability in AVADA dashboard for first 2 hours after send
  [ ] Check spam complaint rate in AVADA — if > 0.08%, pause and investigate immediately
  [ ] Check bounce rate — if > 2%, pause and investigate
  [ ] Log unsubscribe count for list quality tracking
```

---

## Implementation Priority Order

Execute in this sequence — do not skip ahead:

1. **Week 1, Day 1–2:** Complete DNS setup (Task 1 Actions 1–4). Add SPF + DKIM + upgrade DMARC.
2. **Week 1, Day 3:** Configure AVADA sender identity + custom sending subdomain.
3. **Week 1, Day 3–4:** Build Post-Purchase Welcome Email 1 (Task 4) and activate. This affects all future buyers immediately and has zero deliverability risk (it's to individual buyers, not bulk).
4. **Week 1, Day 4–5:** Build Abandoned Cart 3-email sequence (Task 3) and activate.
5. **Week 1, Day 5–7:** Create all 6 segments (Task 2) in AVADA.
6. **Week 2, Day 8–9:** Build and test Mock Interview broadcast. Send test to personal email. Check mail-tester.com score (target: >9/10).
7. **Week 2, Day 9 (Tuesday):** Execute Mock Interview broadcast in staged sends (warm-up protocol from Action 5).
8. **Week 2, Day 13 (Saturday):** Send non-opener follow-up.

**Total estimated setup time:** 8–12 hours across one week, spread across non-consecutive sessions.

---

*Document prepared by Email Marketing Strategist agent — 2026-06-08*  
*All DNS data verified live via UDP/8.8.8.8. Shopify product and customer data based on provided audit brief (live MCP queries permission-denied in this session — verify segment sizes against live Shopify data before activating).*
