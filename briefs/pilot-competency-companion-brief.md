# Project Brief — "Crosscheck": The Pilot Competency & Career Companion

> **Document type:** Master project brief (business strategy → product → UI/UX)
> **Working product name:** **Crosscheck** *(placeholder — see §1.5 for alternatives)*
> **Status:** Draft v1.0 for design generation
> **Date:** 2026-06-29
> **Primary purpose of this document:** Serve as the single source of truth and deep-context reference for AI design agents generating high-fidelity UI/UX screens in Figma. Every downstream agent (UX Researcher, UI Designer, UX Architect, Figma generation) should be able to read this brief and understand the *full* picture — strategy, users, scope, information architecture, screens, and visual language — without needing additional context.
>
> **How to read this brief:**
> - **§1–§4** = the *why* and *what* (strategy, market, users, product). Read for context.
> - **§5–§9** = the *how it looks and feels* (IA, screens, design system, interaction). This is the actionable design specification — Figma agents should treat §6 (Screen Inventory) and §7 (Design System) as build instructions.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Market & Competitive Landscape](#2-market--competitive-landscape)
3. [Strategic Positioning & Business Model](#3-strategic-positioning--business-model)
4. [Product Definition & The Competency Model](#4-product-definition--the-competency-model)
5. [Users, Personas & Journeys (UX Research Layer)](#5-users-personas--journeys-ux-research-layer)
6. [Information Architecture & Screen Inventory](#6-information-architecture--screen-inventory)
7. [Design System & Visual Language](#7-design-system--visual-language)
8. [Interaction Patterns, States & Accessibility](#8-interaction-patterns-states--accessibility)
9. [Figma Generation Handoff Notes](#9-figma-generation-handoff-notes)
10. [Roadmap, Metrics & Risks](#10-roadmap-metrics--risks)

---

## 1. Executive Summary

### 1.1 The one-paragraph pitch

**Crosscheck** is a mobile-first companion that helps professional pilots stay *competent*, not just *current*. Where every existing pilot app logs the past — hours flown, landings made, certificates earned — Crosscheck looks forward: it keeps a pilot's aviation knowledge sharp, tracks readiness for the next recurrent check, and surfaces personal weak areas before they become a problem in the simulator or on the line. It is the pilot's private "personal training department in their pocket," built around the same competency framework (EBT/CBTA, the 9 ICAO/EASA competencies) that airlines and regulators are adopting worldwide. Over time it grows into a complete career companion — adding document and expiry management, a digital logbook, an AI study assistant, and career-progression tools.

### 1.2 The core insight (read this first — it drives every design decision)

The entire competitive market is built around **logging what already happened**. LogTen Pro, ForeFlight Logbook, and CrewLounge are excellent *logbooks* — they record hours, calculate night time, track currency expiry, and produce regulator-compliant reports. They answer the question *"What have I done?"*

No consumer app owns the forward-looking question every professional pilot actually loses sleep over: **"Am I ready, and where am I weak?"**

Meanwhile, the training world has moved decisively from *hour-counting* to *competency*. ICAO Doc 9995, EASA's ORO.FC.231 (Evidence-Based Training), and the 9-competency model (KNO, PRO, COM, FPA, FPM, LTW, PSD, SAW, WLM) are now the language of recurrent training at every major airline. Crosscheck brings that professional competency framework to the *individual* pilot, for the first time, in a beautiful consumer-grade mobile app.

> **Design implication:** Crosscheck is **not** a logbook with a fresh coat of paint. The UI must feel like a *readiness and coaching* product (think: a fitness/health app or a language-learning app like Duolingo, but for aviation competence) — proactive, motivating, forward-looking — *not* a data-entry spreadsheet. This distinction should be visible on every screen.

### 1.3 What we are building (MVP) vs. where it goes (vision)

| | **MVP — "Stay Sharp"** | **Full Vision — "Career Companion"** |
|---|---|---|
| **Core job** | Knowledge maintenance + recurrent readiness + weak-area tracking | Everything in MVP, plus the full professional life of a pilot |
| **Pillars** | 1. Knowledge Maintenance<br>2. Recurrent Readiness<br>3. Weak-Area Tracking | + Documents & Expiry Vault<br>+ Digital Logbook<br>+ AI Assistant<br>+ Career Preparation |
| **Feeling** | "My personal training department" | "My entire flying career, organized" |

### 1.4 Target users (phased)

- **Phase 1 (B2C, launch focus):** Individual professional and aspiring-professional pilots — airline first officers/captains, cadets in type-rating or line training, business-jet and regional pilots, and instructors. They buy it themselves, for themselves.
- **Phase 2+ (B2B / ATO expansion):** Airlines, training departments, and Approved Training Organizations (ATOs) who want fleet-wide competency visibility, with the individual app as the trojan horse already in pilots' pockets.

### 1.5 Naming

Lead candidate: **Crosscheck** — a real, universally understood cockpit term ("crosscheck complete"), implying verification, scanning for what's off, and readiness. Memorable, ownable, app-store-friendly.

Alternatives if "Crosscheck" is unavailable or not preferred: **Ready Room**, **Brief**, **Sharp**, **Proficient**, **Crosswind**, **The Loop**. *(This brief uses "Crosscheck" throughout; substitute freely.)*

---

## 2. Market & Competitive Landscape

### 2.1 The category today

The "pilot software" market splits into roughly four buckets:

| Bucket | Examples | What they do | The gap they leave |
|--------|----------|--------------|--------------------|
| **Electronic logbooks** | LogTen Pro, ForeFlight Logbook, CrewLounge (PILOTLOG), ZuluLog, Capzlog, Safelog | Record flights, auto-calc night/IFR time, track currency expiry, export regulator-compliant reports | Backward-looking. Tracks *what you did*, not *whether you're ready or where you're weak* |
| **EFB / flight-bag** | ForeFlight, Jeppesen FliteDeck, Garmin Pilot | Charts, weather, flight planning, performance | Operational, in-cockpit; not about personal development or competency |
| **Airline/ATO training systems** | Boeing/Airbus EBT platforms, CAE Rise, internal LMS | Competency-based recurrent training & assessment (CBTA/EBT), grading against 9 competencies | B2B only, locked inside the airline, pilot has no personal copy, not consumer-grade UX |
| **Study/ground-school** | Sporty's, ATPL question banks, app-based test prep | Exam prep for a *specific* license milestone | One-and-done; nothing for *maintaining* knowledge across a career |

**Crosscheck sits in the white space between them:** it brings the *competency framework* of the airline training systems and the *knowledge maintenance* of the study apps into a *consumer-grade, career-long, personally-owned* product — a category that does not currently exist for the individual pilot.

### 2.2 Competitive snapshot

| Competitor | Strength | Price (approx, 2025) | Why Crosscheck wins |
|------------|----------|----------------------|---------------------|
| **LogTen Pro** | Gold-standard logging accuracy, 120k+ pilots, airline-trusted | $80–130/yr | We don't compete on logging; we own *readiness & competency*, which LogTen ignores |
| **ForeFlight Logbook** | Bundled with the dominant EFB, digital endorsements | Bundled $130–390/yr | Locked to ForeFlight's EFB ecosystem & price; ours is standalone, affordable, dev-focused |
| **CrewLounge / PILOTLOG** | Cheap, roster sync, EASA/CAA-compliant reports | ~$34/yr | Feature-rich but a classic logbook with dated UX; we win on *forward-looking value* + modern design |

> **Design implication:** The bar for *visual quality* in this category is **low** — most competitors look like utilitarian database front-ends. A genuinely beautiful, modern, motivating mobile experience is itself a competitive moat. The Figma output should look like it belongs next to the best fintech/health apps of 2026, not next to legacy aviation software.

### 2.3 Market tailwinds

- **Regulatory momentum toward competency:** EASA codified EBT in ORO.FC.231; ICAO Doc 9995 and IATA are driving CBTA expansion globally. The *language of competency* is becoming universal — Crosscheck speaks it natively.
- **Pilot shortage & rapid progression:** Faster upgrades and high churn mean more pilots in training pipelines who need to stay sharp and prove readiness.
- **Consumerization expectation:** A generation of pilots raised on Duolingo, Strava, and Notion expects their professional tools to be just as good.

**Sources:** [Aviatize — Best Pilot Logbook Apps](https://www.aviatize.com/blog/best-pilot-logbook-apps-2026) · [Axis Intelligence — 23 apps tested](https://axis-intelligence.com/best-pilot-logbook-apps-2025-tested/) · [Aviatize — EBT glossary](https://www.aviatize.com/glossary/ebt) · [MCC-APS — The 9 EASA competencies](https://mcc-aps.com/en/9-easa-pilot-competencies/) · [Airbus — Is CBTA the future of pilot training?](https://www.aircraft.airbus.com/en/newsroom/stories/2024-12-is-cbta-the-future-of-pilot-training-airbus-head-of-pedagogy-standards) · [Flight Safety Foundation — Moving beyond traditional training](https://flightsafety.org/asw-article/moving-beyond-traditional-training/)

---

## 3. Strategic Positioning & Business Model

### 3.1 Positioning statement

> **For** professional and aspiring-professional pilots **who** worry about staying sharp and being ready for their next check, **Crosscheck is** a personal competency and readiness companion **that** keeps their knowledge fresh, tracks their readiness against the same competency framework airlines use, and pinpoints their weak areas before they matter — **unlike** logbook apps that only record the past, **Crosscheck** is forward-looking, coaching, and built around how pilots are actually trained today.

### 3.2 Brand personality

| Trait | What it means for design |
|-------|--------------------------|
| **Professional & credible** | This is a serious tool for serious aviators. No gimmicks, no clip-art planes. Precision and trust. |
| **Calm under pressure** | Aviation rewards composure. The UI is uncluttered, confident, never alarmist — even when surfacing a problem. |
| **Coaching, not nagging** | Motivating like a great instructor: direct about weak areas, but always paired with a path forward. |
| **Precise** | Numbers, dates, and statuses are exact and trustworthy. Pilots live and die by precision. |

**Voice & tone:** Concise, confident, plain-language (pilots hate fluff). Uses correct aviation terminology naturally. Encouraging without being saccharine. Example microcopy: *"You're recurrent-ready. One soft spot: nail down your engine-failure-after-V1 callouts before next month's sim."*

### 3.3 Business model (recommendation)

**Recommended: Freemium with a single paid "Pro" subscription tier.** Rationale:

- **Freemium** maximizes top-of-funnel adoption in a niche, trust-sensitive market — pilots try before they trust. The free tier seeds the B2B trojan horse (pilots already using it when we sell to their airline).
- **A single Pro tier** (avoid confusing multi-tier pricing at launch) converts the pilots who get daily value.
- **One-time purchase rejected:** the product's value is *ongoing* (knowledge stays fresh, readiness updates) — recurring revenue matches recurring value, and funds the content/AI that makes it good.

| Tier | Price (proposed) | Includes |
|------|------------------|----------|
| **Free** | $0 | Core knowledge maintenance (limited daily questions), basic readiness countdown to next check, view-only competency radar |
| **Pro** | ~$6–9/mo or ~$59–79/yr | Unlimited knowledge practice, full weak-area analytics, recurrent-readiness planner, document vault, logbook, AI assistant, multi-aircraft |
| **(Future) Teams/ATO** | Per-seat B2B | Fleet competency dashboards, instructor assignment, compliance export |

> Priced deliberately *below* LogTen/ForeFlight to signal "complement, not replacement" and lower the trial barrier. **Design implication:** the paywall/upsell screens must feel premium and worth it — show the *value* (analytics, AI) being unlocked, never just a feature checklist.

### 3.4 Go-to-market (summary)

- **Beachhead:** cadets and first-year line pilots in type-rating/line-training — highest anxiety about knowledge retention and checks, most digitally native, strong word-of-mouth in tight training cohorts.
- **Channels:** aviation communities (Reddit r/flying, pilot Discords, forums), flight-school partnerships, aviation influencers/YouTubers, ATO referrals.
- **Hook:** "Walk into your next sim *knowing* you're ready." Free knowledge-maintenance loop drives daily habit; readiness + weak-area analytics drive conversion.

---

## 4. Product Definition & The Competency Model

### 4.1 The competency framework (the spine of the whole product)

Crosscheck is organized around the **9 ICAO/EASA core competencies** — the same model airlines grade pilots against in EBT/CBTA. This is the product's structural backbone and a key piece of credibility. Every weak-area insight, knowledge topic, and readiness score maps back to one or more of these.

| # | Code | Competency | Plain-language meaning (for UI tooltips) |
|---|------|------------|------------------------------------------|
| 1 | **KNO** | Application of Knowledge | What you know: systems, procedures, regs, performance |
| 2 | **PRO** | Application of Procedures & Compliance | Doing the right procedure, correctly, by the book |
| 3 | **COM** | Communication | Clear, timely, correct communication (crew, ATC) |
| 4 | **FPA** | Flight Path Management — Automation | Managing the aircraft via automation/FMS |
| 5 | **FPM** | Flight Path Management — Manual | Hand-flying, manual control |
| 6 | **LTW** | Leadership & Teamwork | CRM, leadership, working as a crew |
| 7 | **PSD** | Problem Solving & Decision Making | Diagnosing and deciding under pressure |
| 8 | **SAW** | Situation Awareness | Knowing what's happening and what's next |
| 9 | **WLM** | Workload Management | Prioritizing, managing capacity & time |

> **Design implication:** The **9-competency radar/wheel** is the product's signature visual — its "Apple Watch rings." It appears on the dashboard, drives the weak-area view, and is the most important single component to get right in Figma. See §6.3 and §7.5.

### 4.2 The three MVP pillars

**Pillar 1 — Knowledge Maintenance ("Stay Sharp")**
A spaced-repetition / adaptive knowledge engine across aviation topics (aircraft systems, performance, regulations, procedures, weather, human factors, etc.). Daily bite-sized practice ("Daily Crosscheck") keeps knowledge fresh across a whole career — not crammed for one exam and forgotten. Adapts to the pilot's aircraft type and weak areas. *Think: Duolingo's daily habit loop, applied to aviation knowledge.*

**Pillar 2 — Recurrent Readiness ("Be Ready")**
Tracks the countdown to the pilot's next recurrent training/check (sim, proficiency check, line check, OPC/LPC), and builds a personalized **readiness plan** — what to review, which competencies to shore up, which scenarios to rehearse mentally — so the pilot walks in confident. Surfaces a single **Readiness Score** and a clear "days until next check."

**Pillar 3 — Weak-Area Tracking ("Know Your Gaps")**
Continuously builds a personal competency profile from knowledge-practice performance and self-assessment, mapped to the 9 competencies. Highlights soft spots ("your QRH non-normals are slipping," "engine-failure callouts need work") and routes the pilot to targeted practice. This is the *coaching* heart of the product.

### 4.3 Full feature map (MVP → vision)

| Phase | Feature | Pillar / Theme |
|-------|---------|----------------|
| **MVP** | Daily Crosscheck (adaptive knowledge practice) | Knowledge Maintenance |
| **MVP** | Topic library & practice by subject/aircraft | Knowledge Maintenance |
| **MVP** | Competency radar (9-competency profile) | Weak-Area Tracking |
| **MVP** | Weak-area insights & targeted drills | Weak-Area Tracking |
| **MVP** | Recurrent readiness countdown + readiness score | Recurrent Readiness |
| **MVP** | Readiness plan (personalized review checklist) | Recurrent Readiness |
| **MVP** | Streaks, progress, motivation loop | Engagement |
| **v1.1** | Documents & Expiry Vault (medical, licenses, ratings, type, language proficiency) with smart expiry alerts | Documents |
| **v1.2** | Currency tracking (FAA §61.57, EASA recency) | Currency/Expiry |
| **v1.3** | Digital logbook (hours, flights, import from competitors) | Logbook |
| **v2.0** | AI Assistant (ask-anything aviation tutor, scenario coach, debrief helper) | AI |
| **v2.1** | Career preparation (interview prep, upgrade readiness, command prep, type-rating prep) | Career |
| **v3.0** | B2B / ATO dashboards, instructor assignment, fleet competency analytics | B2B |

> **Design implication for Figma:** Design the **MVP screens fully**, but design the navigation and dashboard so the later pillars (Documents, Logbook, AI, Career) have an obvious, pre-planned home — e.g., a "+" / "Coming soon" affordance or reserved nav slots — so the app visibly has room to grow into the full companion. Don't paint the IA into a corner.

### 4.4 Regulatory approach (multi-jurisdiction)

Crosscheck is **ICAO-first / jurisdiction-aware**. The competency model (ICAO/EASA 9 competencies) is universal. Jurisdiction-specific logic (FAA Part 61/121/135 recency vs. EASA Part-FCL recency & OPC/LPC cycles) is a *configuration layer* the pilot sets in onboarding (home authority + aircraft + operation type), which tailors currency rules, terminology, and expiry logic.

> **Design implication:** Onboarding must capture **authority (FAA/EASA/Other-ICAO), license type, aircraft/type, and operation type**. Currency/recency UI must be able to render different rule sets without redesign. Avoid hard-coding US-only or Europe-only terminology in shared components.

---

## 5. Users, Personas & Journeys (UX Research Layer)

### 5.1 Primary personas

**Persona A — "Maya, the Cadet/New First Officer"** *(launch beachhead)*
- 24, just finished type rating, 6 months on the line in an A320. Anxious about her first recurrent sim. Terrified of "looking stupid" in the box.
- **Jobs:** keep freshly-learned systems knowledge from fading; know she's ready for the sim; find her weak spots privately before an instructor does.
- **Pains:** knowledge decays fast after the type-rating cram; no structured way to stay sharp; recurrent dates feel like ambushes.
- **Quote:** *"I passed the type rating, but six months later I can't remember half the hydraulics. I want to walk into the sim knowing I've got this."*

**Persona B — "David, the Experienced Captain"**
- 48, 12,000 hrs, wide-body captain. Confident but aware complacency is the enemy. Values precision and his time; hates fluff.
- **Jobs:** maintain a professional edge; keep non-normals/QRH sharp; stay current on reg changes; quietly self-check competencies.
- **Pains:** existing apps are beneath him; nothing respects his expertise while still adding value.
- **Quote:** *"I don't need a logbook. I need ninety seconds a day that keeps me a step ahead."*

**Persona C — "Sam, the Career-Climber"** *(activates in later phases)*
- 31, regional FO eyeing a major-airline job and command upgrade.
- **Jobs:** prep for airline interviews & sim assessments; demonstrate competency; manage documents/currency as they job-hunt.
- **Pains:** scattered prep; no single place that ties knowledge, readiness, and career milestones together.

### 5.2 Jobs-to-be-done (ranked for MVP)

1. *When my recurrent check is approaching, I want to know exactly how ready I am and what to review, so I walk in confident.*
2. *When I have a few spare minutes, I want a quick, relevant way to keep my knowledge sharp, so it doesn't decay.*
3. *When I'm honest with myself, I want to know my real weak areas privately, so I can fix them before they're exposed.*
4. *Over my career, I want one trusted place that grows with me — knowledge, documents, logbook, career — so my professional life is organized.*

### 5.3 Core user journey (MVP — the daily & readiness loop)

```
                                  ┌─────────────────────────────────────────┐
   First launch                   │              DAILY LOOP                  │
   ───────────                    │                                          │
   Onboarding ──▶ Set authority,  │   Open app ──▶ Dashboard (Readiness +    │
   type, next     aircraft, next  │   ▲            Competency radar +        │
   check date     check, goals    │   │            "Daily Crosscheck" CTA)   │
        │                         │   │                  │                   │
        ▼                         │   │                  ▼                   │
   First "Daily Crosscheck"       │   │         Do Daily Crosscheck          │
   (instant value, no setup wall) │   │         (adaptive Qs, ~2–5 min)      │
        │                         │   │                  │                   │
        ▼                         │   │                  ▼                   │
   See first competency snapshot ─┼───┘         Get instant feedback +       │
   + readiness score              │             weak-area update             │
                                  │                  │                       │
                                  │                  ▼                       │
   PERIODIC (pre-check) LOOP      │         Streak ++ , radar updates         │
   ───────────────────────       │                                          │
   Check approaching ──▶ Readiness└──────────────────────────────────────────┘
   plan surfaces ──▶ Review weak competencies ──▶ Rehearse scenarios ──▶ Walk in ready
```

**Design principles drawn from this journey:**
- **Instant value:** the first Daily Crosscheck must be reachable in <60 seconds, before any heavy setup. No long form wall.
- **The dashboard is home base:** it must answer three questions at a glance — *Am I ready? Where am I weak? What do I do right now?*
- **The daily loop must be habit-forming but respectful** of a busy/expert pilot's time (David needs a 90-second path; Maya wants to go deeper).

---

## 6. Information Architecture & Screen Inventory

> This section is the **primary build spec for Figma generation.** Each screen below should become one or more hi-fi frames. Screens are grouped by MVP priority. Design **mobile-first (iOS primary, 390×844 / iPhone reference; Android parity via Material adaptation)**, dark-mode-first (see §7).

### 6.1 Navigation model

**Bottom tab bar (primary nav), 4 tabs + center action:**

| Tab | Icon idea | Purpose |
|-----|-----------|---------|
| **Home / Dashboard** | gauge / radar | Readiness, competency radar, today's action |
| **Practice** | brain / cards | Daily Crosscheck, topic library, drills |
| **Readiness** | checklist / target | Next-check countdown, readiness plan, scenarios |
| **Profile** | pilot / wings | Stats, settings, subscription, (future: documents, logbook, career) |
| **Center CTA (FAB)** | "+" → *Start Daily Crosscheck* | One-tap into the daily loop from anywhere |

> Reserve space in Profile/More for the future pillars (Documents, Logbook, AI, Career) as clearly-labeled "Coming soon" rows so the growth path is visible but not cluttering MVP.

### 6.2 Full MVP screen list (design all of these)

**Onboarding & auth**
1. **Splash / brand** — logo, tagline ("Stay sharp. Be ready.")
2. **Welcome carousel** — 3 slides: Stay Sharp / Be Ready / Know Your Gaps (sell the forward-looking value)
3. **Sign up / log in** — email + Apple/Google SSO
4. **Onboarding Q1 — Authority & license** (FAA / EASA / Other ICAO; license type: CPL/ATPL/etc.)
5. **Onboarding Q2 — Aircraft & operation** (type/fleet e.g. A320, B737, regional, bizjet; operation: airline/charter/instruction)
6. **Onboarding Q3 — Next recurrent check date** (date picker; "skip / not sure" allowed)
7. **Onboarding Q4 — Goals** (stay sharp / pass next check / upgrade prep — sets tone)
8. **First Daily Crosscheck** (instant-value moment — a short practice set, no paywall)
9. **First competency snapshot reveal** ("Here's your starting picture" — animates the radar in)

**Home / Dashboard**
10. **Dashboard (home)** — see §6.3 detailed spec
11. **Readiness detail** (drill-in from dashboard readiness card)
12. **Competency radar detail** (tap a competency spoke → competency detail)
13. **Single competency detail** (e.g. "Knowledge (KNO)": trend, sub-topics, recommended drills)

**Practice (Knowledge Maintenance)**
14. **Daily Crosscheck — question screen** (one question, clean, focused; supports MCQ, true/false, scenario)
15. **Daily Crosscheck — feedback screen** (correct/incorrect + explanation + competency tag)
16. **Daily Crosscheck — session summary** (score, streak, what improved, weak areas touched)
17. **Topic library** (browse by subject: systems, performance, regs, weather, human factors…; filtered to aircraft type)
18. **Topic detail / practice set launcher**
19. **Targeted drill** (auto-generated from weak areas — "Fix your soft spots")

**Readiness**
20. **Readiness home** (big readiness score, days-to-check, status by competency)
21. **Readiness plan** (personalized checklist: review topics, drills, scenarios to rehearse, sorted by impact)
22. **Scenario rehearsal** (mental-model prompts: "Walk through an engine failure after V1…" with self-rating)
23. **Edit/Set next check** (date, type of check: OPC/LPC/Recurrent/Line check/PC)

**Profile & system**
24. **Profile home** (pilot identity, aircraft, stats overview, streak, achievements)
25. **Stats / progress** (knowledge trend over time, competency history, consistency)
26. **Settings** (authority, aircraft, notifications, theme, account)
27. **Subscription / paywall** (Free vs Pro — value-led, see §3.3)
28. **Notifications / reminders config** (daily practice reminder, check-approaching alerts)
29. **"Coming soon" / roadmap teaser** (Documents, Logbook, AI, Career — sets expectations, captures interest)

**Global states (design as variants, not separate flows)**
30. Empty states, loading/skeleton, error, offline, success/celebration (streak milestone, "Ready!" state)

### 6.3 Dashboard — detailed specification (the most important screen)

The dashboard must answer, top to bottom, in one glance:

1. **Greeting + identity strip** — "Good morning, Maya" · aircraft chip (A320) · streak flame (🔥 12).
2. **Readiness card (hero)** — large, the emotional core:
   - Big **Readiness Score** (e.g. a 0–100 or a status: *On Track / Needs Work / Ready*) with a circular/arc gauge.
   - **Days until next check** ("Recurrent sim in 23 days").
   - One-line coaching summary ("On track — 2 competencies need attention").
   - Tappable → Readiness detail (#11).
3. **Competency radar card** — the signature 9-spoke radar/wheel:
   - Visual at-a-glance of strong vs. weak competencies (filled = strong, hollow/amber = weak).
   - 1–2 weak competencies called out below ("Soft spots: Procedures (PRO), Knowledge (KNO)").
   - Tappable spokes → competency detail (#13).
4. **Primary CTA — "Daily Crosscheck"** — prominent button/card: "Today's Crosscheck · ~3 min" with progress (e.g. "0/8"). This is the daily habit anchor.
5. **Weak-area quick action** — "Fix your soft spots" → targeted drill (#19).
6. **Secondary row** — small cards: streak/stats, recent activity, (reserved) "Coming soon" teaser.

> This single screen embodies the positioning: *readiness first, competency second, daily action third.* If a viewer of the Figma file can't tell within 3 seconds that this is a **readiness/coaching** app and not a logbook, the design has missed the brief.

---

## 7. Design System & Visual Language

### 7.1 Recommended visual direction: **"Modern Glass-Cockpit"** (dark-first, precision-instrument inspired)

**Recommendation & rationale:** Go with a **premium, dark-first, glass-cockpit-inspired** aesthetic — but *modern and restrained*, closer to a high-end fintech/health app than to literal avionics skeuomorphism. Why:

- **Credibility & differentiation:** competitors look like utilitarian databases. A precise, confident, instrument-inspired dark UI instantly signals "serious professional tool" and stands apart.
- **Emotional fit:** dark, calm, high-contrast data displays mirror the cockpit environment pilots trust; gauges/arcs/radars are native visual metaphors (readiness gauge, competency radar).
- **Practical:** pilots often use devices in low-light (early shows, night ops, dimmed crew rooms); dark-first is comfortable and battery-friendly on OLED.

> Provide a **light theme** as well (system-toggle), but design dark as the primary/hero theme in Figma.

### 7.2 Color tokens

Design the Figma file with these as named variables/styles (semantic naming so the build inherits cleanly).

**Dark theme (primary):**
| Token | Hex | Use |
|-------|-----|-----|
| `--bg-base` | `#0B0F14` | App background (near-black, blue-cool) |
| `--bg-surface` | `#141A22` | Cards / surfaces |
| `--bg-surface-elevated` | `#1C2530` | Modals, elevated cards |
| `--border-subtle` | `#26303C` | Hairline borders, dividers |
| `--text-primary` | `#F2F6FA` | Primary text |
| `--text-secondary` | `#9AAABB` | Secondary/muted text |
| `--brand-primary` | `#3FA9F5` | Primary brand (instrument cyan-blue) — CTAs, key accents |
| `--brand-primary-deep` | `#1E6FB8` | Pressed/gradient end |
| `--accent-amber` | `#F5A623` | Caution / "needs attention" (cockpit amber) |
| `--accent-red` | `#FF4D4F` | Warning / expired / critical |
| `--accent-green` | `#34D399` | Ready / strong / success (avoid pure green; use mint) |
| `--radar-fill` | `#3FA9F5` @ 30–60% | Competency radar fill |

**Status semantics (critical — reused everywhere):**
- **Green/mint = Ready / Strong / Current.**
- **Amber = Needs attention / Approaching / Soft spot.**
- **Red = Critical / Expired / Weak.**
- These three map directly to readiness, competency strength, and (later) document expiry. Keep them consistent across every screen.

**Light theme:** invert to `#F7F9FB` base, `#FFFFFF` surfaces, `#0B0F14` text; keep brand/accent hues, darken slightly for contrast (WCAG AA).

### 7.3 Typography

- **Primary typeface:** a clean, precise grotesque/geometric sans — **Inter** (recommended, free, excellent for data/UI) or **SF Pro** on iOS. Optional: a slightly technical display face for big numbers (e.g. tabular figures for scores/dates).
- **Always use tabular/monospaced figures for numbers** (scores, dates, countdowns, hours) — precision is a brand value and prevents jitter in counters.

| Style | Size / weight | Use |
|-------|---------------|-----|
| Display | 34–40 / Bold | Readiness score, big numbers |
| H1 | 28 / Bold | Screen titles |
| H2 | 22 / Semibold | Section headers |
| H3 | 17 / Semibold | Card titles |
| Body | 16 / Regular | Default text |
| Body-sm | 14 / Regular | Secondary |
| Caption | 12 / Medium | Labels, competency codes |

### 7.4 Spacing, radius, elevation

- **Spacing scale (4px base):** 4, 8, 12, 16, 24, 32, 48.
- **Corner radius:** cards 16px, buttons 12px, chips/pills full-round, modals 24px. Generous, soft, modern — not sharp/industrial.
- **Elevation:** subtle. On dark, use lighter surface + thin border rather than heavy shadows; reserve soft glows for the brand accent on key elements (e.g. a faint cyan glow on the readiness gauge when "Ready").

### 7.5 Signature components (build as Figma components with variants)

1. **Competency Radar / Wheel** — 9-spoke radar chart. Variants: full-detail (tappable spokes), compact (dashboard card), single-competency focus. Filled area = competency strength; amber spokes flag weak areas. *This is the hero component — invest the most polish here.*
2. **Readiness Gauge** — circular/arc gauge (0–100 or status arc). Variants: On Track (cyan), Needs Work (amber), Ready (mint glow). Center shows score; sub-label shows days-to-check.
3. **Daily Crosscheck Card** — the daily CTA. Variants: not-started, in-progress (n/total), completed (✓ + streak).
4. **Question Card** — focused single-question component. Variants: MCQ, true/false, scenario; default / selected / correct / incorrect states.
5. **Competency Chip** — small pill showing competency code + color status (e.g. `PRO ●`). Reused across feedback, weak-areas, radar legend.
6. **Status Pill** — Ready / Attention / Critical (green/amber/red). Reused for readiness, competencies, and later documents/currency.
7. **Stat Card** — streak, hours-practiced, consistency. Tabular figures.
8. **Insight/Coaching Banner** — the "coaching voice" surface: a calm, accent-bordered callout with a weak-area insight + action button.
9. **Bottom Tab Bar + Center FAB** — per §6.1.
10. **Aircraft/Authority Chips** — small contextual chips (e.g. `A320`, `EASA`).

### 7.6 Iconography & imagery

- **Icons:** thin-to-medium line icons, consistent stroke (1.5–2px), rounded joins. Aviation-literate but universal (gauge, radar, target, checklist, brain, wings).
- **Imagery:** avoid stock clip-art planes. If imagery is used (onboarding, empty states), prefer abstract instrument/horizon/HUD-inspired graphics, subtle gradients, and data-viz motifs over literal aircraft photos. Keep it premium and restrained.
- **Motion (note for prototypes):** gauge/radar should animate in (count-up, draw-on); celebrate streaks and "Ready!" with tasteful, brief motion — never childish.

---

## 8. Interaction Patterns, States & Accessibility

### 8.1 Key interaction patterns

- **One-tap to value:** the center FAB / dashboard CTA always launches the Daily Crosscheck. Minimize taps to the core loop.
- **Drill-down, not menus:** dashboard cards are tappable into detail; competency radar spokes are tappable; everything important on the dashboard has a deeper view.
- **Progressive disclosure:** David (expert) gets the 90-second path; Maya (cadet) can expand into explanations, topic libraries, and scenarios. Default to concise; allow depth on demand.
- **Honest, calm feedback:** wrong answers are coaching moments — show the correct answer + a crisp explanation + the competency it maps to, never a harsh "WRONG."

### 8.2 Required states for each screen (design as variants)

- **Empty:** e.g. no check date set ("Add your next check to unlock your readiness plan"), no practice yet ("Take your first Crosscheck").
- **Loading:** skeleton screens (no spinners on content surfaces); gauge/radar shimmer-in.
- **Error / offline:** the app must work offline for practice (knowledge content cached); show a calm offline chip, queue sync. Never block the daily loop on connectivity.
- **Success / celebration:** streak milestones, "You're Ready" readiness state, competency improvement — tasteful positive reinforcement.

### 8.3 Accessibility (non-negotiable baseline)

- **WCAG 2.1 AA contrast** on both themes — verify amber/red/green against dark surfaces (amber especially).
- **Do not rely on color alone** for status — pair every green/amber/red with an icon, label, or shape (color-blindness is relevant in the pilot population given medical color-vision standards).
- **Dynamic Type / scalable text**; 44×44pt minimum tap targets; full VoiceOver/TalkBack labels (especially for the radar/gauge — provide text equivalents like "Procedures: needs attention").
- **Reduce-motion** variants for the animated gauge/radar.

---

## 9. Figma Generation Handoff Notes

> Direct instructions for the AI design agent(s) producing the hi-fi Figma file from this brief.

1. **Build the design system first** (§7): create color variables (dark + light modes), text styles, spacing tokens, and the signature components (§7.5) with variants — *then* assemble screens from them. This makes the file coherent and dev-ready.
2. **Frame size & platform:** iPhone reference (390×844 pt), iOS-primary patterns; design dark theme as the hero, provide light-theme variants of at least the dashboard, a practice screen, and the radar.
3. **Prioritize these "hero" frames** if scope must be limited: (a) Dashboard §6.3, (b) Competency Radar detail, (c) Daily Crosscheck question + feedback, (d) Readiness home + plan, (e) Onboarding authority/aircraft/check-date, (f) Paywall. These tell the whole story.
4. **Use realistic, credible content** — real competency names/codes (§4.1), plausible aviation knowledge questions (systems, performance, regs), realistic dates and aircraft (A320/B737). Avoid lorem ipsum; avoid inventing fake regulations — keep question *topics* realistic but generic enough to be safe placeholders.
5. **Honor the positioning in every frame:** forward-looking, coaching, calm, precise. Readiness and competency lead; logging is absent from MVP. If a frame looks like a logbook, revise it.
6. **Show the growth path** subtly: reserved "Coming soon" rows for Documents / Logbook / AI / Career — present but not competing for attention.
7. **Status color semantics are global** (§7.2): green=ready/strong, amber=attention/soft-spot, red=critical. Never reassign these.
8. **Accessibility variants:** include at least one reduce-motion / high-contrast consideration and ensure status is never color-only.

---

## 10. Roadmap, Metrics & Risks

### 10.1 Phased roadmap

| Phase | Theme | Scope | Goal |
|-------|-------|-------|------|
| **0 — Now** | This brief | Strategy + full UX/UI spec → Figma hi-fi | Validate the vision visually; align design |
| **1 — MVP** | "Stay Sharp" | 3 pillars (knowledge, readiness, weak-areas), onboarding, dashboard, freemium | Daily habit + first paying pilots |
| **1.x** | "Organize" | Documents & expiry vault, currency tracking, logbook (+import) | Become the daily home base |
| **2.x** | "Coach" | AI assistant, scenario coaching, career prep | Deepen value & retention |
| **3.x** | "Scale" | B2B/ATO dashboards, instructor tools, fleet analytics | Expand to airlines via the installed base |

### 10.2 Success metrics (MVP)

| Metric | Why it matters | Target (directional) |
|--------|----------------|----------------------|
| D7 / D30 retention | Daily-habit product lives or dies here | D30 ≥ 25% (strong for niche) |
| Daily Crosscheck completion rate | Core loop engagement | ≥ 40% of MAU practice ≥3×/week |
| Free→Pro conversion | Business viability | 4–8% |
| Readiness feature usage before a check | Validates core differentiator | ≥ 60% of users with a check date open the readiness plan |
| Weak-area drill follow-through | Validates the coaching value | ≥ 30% act on a surfaced weak area |

### 10.3 Key risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Content credibility** — pilots are unforgiving of wrong/dated knowledge | High | High | Source content from credible material; jurisdiction-tag; expert review; let users flag; never present unverified regs as authoritative |
| **"Just another logbook" perception** | Medium | High | Relentlessly forward-looking UX; lead with readiness/competency; defer logbook to v1.3 |
| **Niche market size (B2C)** | Medium | Medium | Low price for trial; freemium funnel; B2B/ATO as the scale path via installed base |
| **Regulatory complexity across jurisdictions** | High | Medium | ICAO-first universal core + jurisdiction config layer; don't hard-code one authority |
| **Engagement decay** (knowledge apps fade) | Medium | High | Tie practice to *real upcoming checks* (stakes) + streaks + adaptive relevance to the pilot's type |
| **Trust/data sensitivity** (medical, licenses later) | Medium | High | Privacy-first, encryption, clear data ownership; document vault designed for security from day one |

---

*End of brief v1.0. This document is intended to be handed directly to UX Research, UI Design, and Figma-generation agents. Update the working name, pricing specifics, and content sourcing as decisions are finalized.*
