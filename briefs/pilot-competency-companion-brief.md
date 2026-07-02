# Project Brief v3 — "OnCourse": The Pilot Competency-Continuity & Career Companion

> **Document type:** Master project brief (brand → business strategy → method → product → UI/UX)
> **Product name:** **OnCourse** *(selected; may change later, but any change is name-only — branding/colors/voice/story stay fixed. See §4.7.)*
> **Status:** Draft v4.4 — adds §8.0 **as-built addendum**: the design is realized in the OnCourse Aviation Figma file (Light + Teal / Inter, 35 core screens + 4 later-phase + design-system page + wired prototype), and founder-directed changes made during design review are **canonical** over the original inventory (code-style home header with first name, Quick Test/Custom Quiz home entries, code-matched quiz layouts + Custom Quiz hero, profile-setup-first onboarding, Welcome Back screen). Earlier: §17 Prior Work; content governance (§5.10, §6.7); data privacy (§14); restrained gamification (§6.4); name clearance (§4.7); free-first pricing (§4.10); pipeline & phased personalization (§5.9); phased roadmap (§13.1); tech stack (§14); exercise formats (§15); sample-content kit (§16). Name: OnCourse. Integrates four source documents (below).
> **Date:** 2026-06-29
> **Primary purpose:** The single source of truth and deep-context reference for AI design agents generating high-fidelity UI/UX screens in Figma. A downstream agent should be able to read *this brief alone* and understand the full picture — strategy, the underlying training method, the complete feature system, information architecture, screens, and visual language.

> **Canonical source documents this brief integrates (authoritative — defer to them on mechanics):**
> 1. **Product Functionality Specification** — the full feature system (onboarding, learning engine, home, retention psychology, privacy/trust, accessibility, content taxonomy).
> 2. **Competency Continuity Method (v3)** — the scientific/operational method: Operational Training Units (OTUs), EBT double-entry currentness, exposure model, recurrence pools, scoring, training-pattern generation, currentness engine.
> 3. **Question Architectures for Exercise-Type Generation** — the canonical exercise types, grammar structures per type, and formatting rules, with A320 example stems. Governs §15 and all question-screen content.
> 4. **Feature Prioritization Database (46 features)** — phasing (Concept/V0–V3), MoSCoW priority, effort, risk, value bundles (VB01–06), tech gates (T0–T3), dependencies, and suggested tools (Firebase + Capacitor). Governs §13.1 and §14.
> Where this brief and a source document differ on *product mechanics*, the source document wins. This brief adds the strategy, positioning, IA, and visual/design specification on top.

> **Key product decisions locked:**
> - **Scope:** MVP = the competency-continuity training engine. "Career companion" extras (documents, expiry, logbook, career prep) are **later phases**, not MVP.
> - **Aircraft:** **A320 short-haul content**, but the UI is designed as a **type-agnostic shell** that visibly generalizes to other types later.
> - **Personalization is phased (§5.9).** *Release 1* routes each pilot to **one of 3–4 hand-authored training paths** (via the intent quiz + light signup data) and pushes that path's **revision pools** — personalization by *routing*. The *full engine* (per-pilot computed patterns + dual-currentness radar/analytics) comes **later**. So early-release screens show **light status** (path, today's pool, streak, progress); the rich competency radar is a **later-phase** view.
> - **Engine content has a dedicated home.** A surface (working name **"Flight Plan"**) is where the engine **pushes** the due revision pools; **self-directed** single-question practice (quick test / search / build-your-own) lives separately in **Train**. See §8.
> - **Method visibility:** **Operational/simple UI.** Pilots see concrete *actions* ("fuel leak", "de-icing") and (later) the *9-competency* view. Internal machinery (OTU IDs, exposure categories EC1–EC6, recurrence-pool numbers, scoring) stays **backend** — never shown as jargon.
> - **Tech stack (§14):** hybrid mobile — **Capacitor** shell + **Firebase** (Auth, Firestore, Remote Config, Storage). Design within hybrid-rendering and native-feel constraints.
> - **First Figma batch:** the **core loop** (see §11).

> **How to read this brief:**
> - **§1–§4** = the *why* (problem, market, brand & strategy). §4 is the brand foundation — name, story, values, voice — that all visual/copy decisions inherit from.
> - **§5** = the *method* (the core mechanic every screen ultimately serves). Essential.
> - **§6** = the *full feature system* (what exists in the product).
> - **§7–§11** = the *how it looks and works* — the actionable design specification. Treat §8 (Screens) and §9 (Design System) as build instructions.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Problem & Why This Exists](#2-the-problem--why-this-exists)
3. [Market & Competitive Landscape](#3-market--competitive-landscape)
4. [Brand Foundations & Identity](#4-brand-foundations--identity)
5. [The Core Mechanic — Competency Continuity Method](#5-the-core-mechanic--competency-continuity-method)
6. [The Full Feature System](#6-the-full-feature-system)
7. [Users, Personas & Journeys](#7-users-personas--journeys)
8. [Information Architecture & Screen Inventory](#8-information-architecture--screen-inventory)
9. [Design System & Visual Language](#9-design-system--visual-language)
10. [Interaction, Adaptive UI, States & Accessibility](#10-interaction-adaptive-ui-states--accessibility)
11. [Figma Generation Handoff Notes](#11-figma-generation-handoff-notes)
12. [Content Taxonomy (A320)](#12-content-taxonomy-a320)
13. [Roadmap, Metrics & Risks](#13-roadmap-metrics--risks)
14. [Tech Stack & Design Constraints](#14-tech-stack--design-constraints)
15. [Exercise Formats & Question Architecture](#15-exercise-formats--question-architecture)
16. [Design-Ready Sample Content Kit](#16-design-ready-sample-content-kit)
17. [Prior Work / Reference (context only)](#17-prior-work--reference-context-only)

---

## 1. Executive Summary

### 1.1 The one-paragraph pitch

**OnCourse** keeps professional pilots *competent between checks*, not just *current on paper*. Line flying naturally rehearses some actions every sector (cockpit prep, briefings, approaches) while leaving rare-critical ones dormant for months (engine failure after V1, fuel leak, windshear escape, evacuation). OnCourse closes that **exposure gap** with short, spaced, scenario-based micro-training — scheduled by a method built on Evidence-Based Training (EBT) competencies and memory science. It learns each pilot's weak spots, schedules the right retrieval at the right time, and shows two honest readiness pictures: *which actions you're rusty on* and *which underlying competencies are slipping*. It is a pilot's private "personal training department in their pocket." Over time it grows into a full career companion (documents, logbook, career prep), but the MVP is the training engine.

### 1.2 The core insight (drives every design decision)

The whole competitor market *logs the past* (LogTen, ForeFlight, CrewLounge — hours, currency, endorsements). OnCourse answers the forward-looking question pilots actually lose sleep over: **"Am I still sharp on the things I almost never do — and where am I weak?"**

It does this with a real method (the **Competency Continuity Method**, §5): not a generic question bank, but training generated from **mapped operational actions/events**, scheduled by **how often line flying, the sim, and recurrent training already refresh each one**, and graded against the **9 EBT competencies**.

> **Design implication:** OnCourse is a **readiness & coaching** product — closer to a beautifully-made adaptive learning app (Duolingo-class daily habit) crossed with a flight-training mindset — **not** a logbook or a spreadsheet. If a Figma frame looks like data entry, it's wrong.

### 1.3 The critical disclaimer (must be respected in UI copy)

Per the source method: OnCourse is a **competency-continuity and cognitive-reinforcement layer between approved recurrent training events.** It does **not** replace an operator's approved training programme, manuals, SOPs, regulatory training, simulator checking, or instructor-led assessment. The UI must never imply formal qualification, certification, or regulatory currentness.

> **Hard UI requirement (founder-directed):** the "never replaces official documentation or airline training" message must be **clearly and visibly stated in the app** — not buried. Surface it at **onboarding** (a brief, dismissible acknowledgement), keep it permanently accessible in **About/Settings**, and reference it near content where appropriate. It is a trust cornerstone, not fine print. *(See §5.10 for content governance and §13 risk table — content credibility is the #1 risk.)*

### 1.4 MVP vs. full vision

| | **MVP — the training engine** | **Full vision — career companion** |
|---|---|---|
| **Core job** | Maintain competency between checks via spaced, scenario-based micro-training | The whole professional life of a pilot |
| **What's in it** | Onboarding · learning engine (SRS + adaptive + micro-quiz + NL search + AI curator) · dual currentness (action + competency) · home/Predictive Hero Tile · retention/gamification · privacy/trust · adaptive accessibility | + Documents & expiry vault · digital logbook · currency tracking · expanded AI assistant · career preparation · B2B/ATO dashboards |
| **Aircraft** | A320 content, type-agnostic shell | Multi-type |
| **Feeling** | "My personal training department" | "My entire flying career, organized" |

---

## 2. The Problem & Why This Exists

*(From the Competency Continuity Method, §1–§4.)*

Formal airline training is **episodic**; operations are **continuous**. Between formal events, some skills are refreshed by line flying and some decay almost entirely. The problem is **unequal exposure**, not simple ignorance:

| Problem | Plain explanation | How the method responds |
|---------|-------------------|--------------------------|
| **Uneven line exposure** | Some actions happen every sector; others almost never | Classify each action by exposure source + remaining gap |
| **Memory decay** | Knowledge & decision patterns weaken without retrieval | Spaced, *active retrieval* tasks — not passive reading |
| **Rare-critical events** | Low probability, high consequence, seconds to react | Higher-frequency micro-drills for immediate-action items |
| **EBT cognitive-substrate gap** | EBT grades competencies, but they rest on knowledge/procedures/mental models | Maintain that underlying base between formal events |
| **Generic question banks** | Topic revision ≠ real mission demands | Generate training from mapped operational actions/events |

**Scientific grounding** (used to justify the schedule, not as exact law): memory/procedural decay without retrieval; spaced practice > massed practice; retrieval practice (recall, decide, spot the trap, sequence) > passive revision. Practical implication: *rare-critical actions must be periodically retrieved through short scenario-based exercises.*

> **Design implication:** Every training interaction must be **active retrieval** (recall / decide / sequence / spot-the-trap / time-limited first-action) — never a passive "read this." Exercise *type* changes by how critical/time-pressured the action is (§5.6).

---

## 3. Market & Competitive Landscape

### 3.1 The white space

| Bucket | Examples | What they do | Gap |
|--------|----------|--------------|-----|
| **Electronic logbooks** | LogTen Pro, ForeFlight Logbook, CrewLounge, ZuluLog, Capzlog, Safelog | Log flights, auto-calc night/IFR, track currency expiry, compliant reports | Backward-looking; *what you did*, not *whether you're ready or where you're weak* |
| **EFB / flight-bag** | ForeFlight, Jeppesen FliteDeck, Garmin Pilot | Charts, weather, planning | In-cockpit ops; not personal development |
| **Airline/ATO training (EBT/CBTA)** | Boeing/Airbus EBT, CAE Rise, internal LMS | Competency-based recurrent training & assessment | B2B only, locked in the airline, not consumer-grade, pilot keeps no personal copy |
| **Study / ground-school** | Sporty's, ATPL banks | Exam prep for one milestone | One-and-done; nothing for *career-long maintenance* |

**OnCourse occupies the empty intersection:** the *competency framework* of airline EBT systems + the *spaced retrieval* of study apps, delivered as a *consumer-grade, career-long, personally-owned* app — which does not exist today for the individual pilot.

### 3.2 Competitive snapshot

| Competitor | Strength | Price (~2025) | Why OnCourse wins |
|------------|----------|---------------|---------------------|
| **LogTen Pro** | Logging accuracy, 120k+ pilots, airline-trusted | $80–130/yr | We don't compete on logging; we own *continuity & competency* |
| **ForeFlight Logbook** | Bundled with dominant EFB | Bundled $130–390/yr | Locked to ForeFlight; ours is standalone, focused, affordable |
| **CrewLounge / PILOTLOG** | Cheap, roster sync, compliant reports | ~$34/yr | Classic logbook, dated UX; we win on forward-looking value + design |

> **Design implication:** The visual bar in this category is **low** — competitors look like database front-ends. A genuinely beautiful, modern mobile experience is itself a moat. Output should belong next to the best fintech/health apps of 2026.

**Sources:** [Aviatize — Best Pilot Logbook Apps](https://www.aviatize.com/blog/best-pilot-logbook-apps-2026) · [Axis Intelligence — 23 apps tested](https://axis-intelligence.com/best-pilot-logbook-apps-2025-tested/) · [Aviatize — EBT glossary](https://www.aviatize.com/glossary/ebt) · [MCC-APS — The 9 EASA competencies](https://mcc-aps.com/en/9-easa-pilot-competencies/) · [Airbus — Is CBTA the future?](https://www.aircraft.airbus.com/en/newsroom/stories/2024-12-is-cbta-the-future-of-pilot-training-airbus-head-of-pedagogy-standards) · [Flight Safety Foundation — Moving beyond traditional training](https://flightsafety.org/asw-article/moving-beyond-traditional-training/)

---

## 4. Brand Foundations & Identity

> Built from the founder's inputs: **origin** = lived experience as a pilot *and* watching peers quietly struggle *and* a recognized industry gap; **brand role** = **"the quiet edge"** (the private advantage against complacency); **naming tone** = **credible aviation term**. These foundations are upstream of all UI/UX — name, voice, values and color all flow from here, so the design stays coherent with the vision.

### 4.1 Mission

Keep every professional pilot **quietly, continuously ready** — sharp on the rare-critical actions that line flying lets fade — between every check.

### 4.2 Vision

A world where no pilot is ever caught rusty on the things that matter most: where maintaining your own competency between checks is as normal and unremarkable as a preflight scan — and where "competency continuity" becomes a standard layer of professional airmanship, owned by the pilot.

### 4.3 Brand values

| Value | What it means | How it shows up |
|-------|---------------|-----------------|
| **Competence over completion** | Readiness is proven by *retention + performance*, never by "finishing" content | Milestones earned on sustained recall, not lessons completed; honest currentness, not vanity progress |
| **Quiet confidence** | Understated, precise; the work speaks for itself — no hype, no fear-mongering | Calm UI, restrained copy, no exclamation marks or alarm-bells; an edge you don't have to announce |
| **Truth you can trust** | Validated content only, sourced and auditable; honest about what we are and aren't | No AI-invented content; source references kept; the "between approved events" disclaimer respected |
| **Respect for the pilot** | Their time, expertise, privacy and autonomy are sacred | 90-second paths; override everything; incognito/privacy controls; never patronizing |
| **Forward-looking** | We build readiness; we don't just record the past | Currentness & retrieval lead; logging is deferred and secondary |
| **Calm, never alarmist** | Safety-serious like the cockpit — composed under pressure | Weak areas surfaced as coaching, not warnings; amber/red used precisely, never theatrically |

### 4.4 Brand archetype & personality — "The Quiet Edge"

**Archetype:** a **Sage** (mastery, knowledge, truth) expressed with deliberate **restraint** — closer to a trusted, unshowy guardian of your standards than a loud coach or a chirpy buddy. The brand is the *private advantage* a serious professional keeps: it makes you better without making a show of it.

| We ARE | We are NOT |
|--------|------------|
| Precise, composed, quietly confident | Loud, gamified-for-its-own-sake, hype-y |
| A peer-level professional who respects your expertise | A lecturing instructor or a cartoon mascot |
| Understated — the edge you don't talk about | Boastful, badge-spammy, motivational-poster |
| Honest, even when the news is "you're rusty" | Flattering or falsely reassuring |
| Calm under pressure, like a good flight deck | Alarmist, anxious, cluttered |

> **Design implication:** "Quiet edge" is a *visual discipline*, not just copy. Restraint everywhere — generous space, muted dark surfaces, one confident accent, precise numerals, motion that's brief and earned. If a screen feels loud, it's off-brand.

### 4.5 Positioning statement

> **For** professional pilots **who** worry about staying sharp on rare-critical actions and being ready for their next check, **OnCourse is** a personal competency-continuity companion **that** schedules short, science-based retrieval of exactly the actions line flying leaves dormant, graded against the EBT competencies airlines use — **unlike** logbook apps that only record the past, **it** is forward-looking, method-driven, and operationally real.

### 4.6 Brand story

**Long form:**

> There's a truth most pilots don't say out loud: months can pass without ever touching the things that could one day save the aircraft — and you. Line flying rehearses the routine every sector. The rare-critical — engine failure after V1, a fuel leak in the cruise, windshear on rotation — sits dormant, waiting for a simulator detail or, worse, the real day.
>
> The founder felt it first-hand. After the type rating, the systems knowledge that had been razor-sharp started to quietly fade — and there was a private unease before every recurrent sim that no logbook could fix. Talking to other pilots, it turned out everyone carried the same quiet worry, and nobody had a real way to deal with it.
>
> Meanwhile the whole industry had moved on — to Evidence-Based and Competency-Based Training, built around the competencies that actually keep flights safe. But that progress lived *inside the airline*. There was nothing the individual pilot could own to maintain their own edge between the formal events.
>
> So we built it. Not another logbook. A continuity layer between checks — short, spaced, science-based retrieval of exactly the actions that are fading, measured against the competencies that matter. It doesn't replace your training, your manuals, or your operator's programme. It keeps the quiet edge between them.
>
> Because the best pilots aren't the loudest in the room. They're the ones who are simply, quietly, always ready.

**Short form (for store listings / landing hero):**

> Line flying keeps you sharp on the routine — and lets the rare-critical fade. [The app] is a personal competency-continuity companion that quietly keeps you ready on the things you almost never see, between every check. Not a logbook. Your edge.

### 4.7 Name — decision: **OnCourse** ✅

The name is **OnCourse**. Working/final for now; it may change later — but **any future change is name-only: branding, colors, voice, archetype and story do not change.**

Why it fits:
- **Credible aviation phraseology** — "on course" means tracking the correct route/path; the on-course indication is a core navigation reference. Insider-credible without being obscure.
- **"Quiet edge" meaning** — being *on course* is calm, in control, on the right path — exactly the brand's understated confidence (§4.4).
- **Double meaning** — a training *course*; quietly reinforces the learning/continuity purpose.
- **Brandable & tagline-ready** — one word, easy to say and spell, and it fits the brand lines directly: **"Stay on course."**

> **Conceptual anchor regardless of name:** **airmanship** — the holistic competence the product builds; useful for story/tagline.

**Name-clearance findings (research completed — act before public/commercial launch):**
- **Collision found:** **"OnCourse Systems for Education"** is an established K-12 education/school-management brand with live App Store apps ("OnCourse Systems", "OnCourse Walkthrough", "OnCourse Connect"). Because OnCourse-the-pilot-app is a *learning/training* product, this is an **adjacent trademark class (education/training software) — a real conflict risk**, and a bare "OnCourse" App Store name is likely already crowded.
- **Aviation space is clear:** no pilot/aviation app named "OnCourse" was found — within aviation the name reads as ownable.
- **Recommendation:** keep **OnCourse** as the brand, but (a) have a **trademark attorney** assess the education-class overlap in target jurisdictions; (b) plan a **distinguishing App Store name** (e.g. *"OnCourse — Pilot Training"* / *"OnCourse Aviation"*) since the plain name is contested; (c) secure a distinct **domain/handles** (e.g. `getoncourse.app` / `flyoncourse.com` — `oncourse.com` is almost certainly taken) ; (d) keep a **fallback name** ready given the collision. *(You've noted the name can change later with **zero branding/color impact** — §header — so this is low-risk to carry forward.)*
- **Sources:** [OnCourse Systems (App Store)](https://apps.apple.com/us/app/oncourse-systems/id6575387171) · [OnCourse Systems for Education](https://app.oncoursesystems.com/) · [OnCourse Walkthrough (App Store)](https://apps.apple.com/us/app/oncourse-walkthrough/id1136709462)

> Earlier shortlisted candidates (Scan, Maintain, Vigil, Trim, and the original working name) are preserved in this document's version history.

### 4.8 Taglines (options)

- **Brand line:** *"The quiet edge."*
- **Functional:** *"Stay sharp between checks."*
- Alternatives: *"Always a step ahead."* · *"Ready, quietly."* · *"Sharp on what you never see."* · *"Competence, maintained."* · *"Your edge between checks."*

### 4.9 Voice & tone

Concise · confident · calm · peer-level · aviation-literate · coaching not nagging · never hype. We talk to a professional like a respected colleague — direct about weak areas, always with a path forward, never alarmist or saccharine.

| Do | Don't |
|----|-------|
| "Your engine-failure-after-V1 recall is fading. 3-minute drill?" | "⚠️ WARNING! You're not current!! Train NOW!!!" |
| "You're current on the essentials. One soft spot: de-icing decision." | "Amazing job, champion! 🎉 You're crushing it!!" |
| "Your KNO profile is slipping — today: a fuel-leak scenario." | "Time to train KNO." *(abstract, not operational)* |
| "Done. De-icing back to current; PSD trending up." | "Lesson 4 of 12 complete." *(completion, not competence)* |

### 4.10 Business model — **free-first, then subscription + B2B licensing** *(decided)*

Monetization is **phased**, prioritizing adoption and trust before revenue:

| Stage | Model | Rationale |
|-------|-------|-----------|
| **Stage 1 — Launch** | **100% free, fully unlocked** (no paywall, no locked features) | Land-grab in a trust-sensitive niche; remove every barrier to habit formation and word-of-mouth; build the user base and the validated content library first |
| **Stage 2 — Growth** | **Introduce a paid subscription** as advanced features mature (dual-currentness analytics, AI curator, deeper personalization, expanded content) | Convert engaged users once ongoing value is proven; the free tier persists as the funnel |
| **Stage 3 — Scale (major revenue)** | **Strong push of B2B licenses to ATOs + airlines worldwide** | Fleet-wide competency-continuity; the individual app is the trojan horse already in pilots' pockets |

> **Design implications (important for the first Figma batch):**
> - **No paywall / no locked-feature UI at launch.** Do **not** design subscription/paywall screens for the early batch — everything is unlocked. (Screen #46 is a **later-phase** artifact.)
> - Design so a subscription layer can be **added later without rework** — e.g., leave conceptual room for "Pro" affordances, but show nothing locked now.
> - The **B2B/ATO** surface (fleet dashboards, instructor assignment, licensing) is a separate later product track (§13.1 Scale), not part of the consumer app's early design.

### 4.11 Go-to-market (summary)

Beachhead: **A320 first officers & cadets in/after type rating** — highest anxiety about knowledge decay and the next sim, most digitally native, tight word-of-mouth cohorts. Channels: pilot communities (r/flying, Discords, forums), flight-school/type-rating partnerships, aviation influencers, ATO referrals. Hook: *"Walk into your next sim knowing you're ready — even on the things you never see on the line."* **Free at launch (§4.10)** removes all trial friction and maximizes this word-of-mouth loop; the resulting installed base becomes the wedge for the later **ATO/airline licensing** push.

---

## 5. The Core Mechanic — Competency Continuity Method

*(This is the heart of the product. From the Competency Continuity Method v3. Everything in the UI ultimately serves this. **Note the visibility rule: the machinery below is mostly backend; §5.8 defines exactly what surfaces to pilots.**)*

### 5.1 The architecture in one line

```
Map the mission → create OTUs → tag competencies → assess exposure sources
→ determine review interval → assign recurrence pool → generate training pattern
→ deliver retrieval task → update action currentness AND competency currentness
```

### 5.2 The OTU (Operational Training Unit) — the central object

An **OTU is one operational action or event** in one phase/context that can be scheduled, trained, and tracked — e.g. *cockpit preparation*, *de-icing decision*, *RTO decision*, *fuel leak in cruise*, *TCAS RA*. Recurrence is assigned to **the OTU (the action)**, not to each competency.

| OTU field | Example |
|-----------|---------|
| OTU ID | NOR-CP-002 |
| Phase | Cockpit preparation |
| Action/event | FMGS preparation |
| Source reference | FCOM / OM-A reference *(kept for auditability)* |
| Primary competency | FPA |
| Secondary competencies | KNO, PRO, SAW, WLM, COM |
| Exposure category | EC1/EC2 (see §5.5) |
| Review interval / Pool | e.g. 1–3 months / Pool 2 |
| Training pattern | Trap detection / missing-item / consistency check |

### 5.3 The 9 EBT competencies (the analytical tags)

| Code | Competency | Plain meaning (UI tooltip) |
|------|------------|----------------------------|
| **KNO** | Application of Knowledge | Systems, procedures, regs, performance |
| **PRO** | Procedures & Compliance | Right procedure, correctly, by the book |
| **COM** | Communication | Clear, timely, correct (crew, ATC) |
| **FPA** | Flight Path — Automation | Managing the aircraft via automation/FMS |
| **FPM** | Flight Path — Manual | Hand-flying, manual control |
| **LTW** | Leadership & Teamwork | CRM, leadership, crew |
| **PSD** | Problem Solving & Decision | Diagnose & decide under pressure |
| **SAW** | Situation Awareness | Know what's happening & what's next |
| **WLM** | Workload Management | Prioritize, manage capacity & time |

### 5.4 The double-entry currentness model (the signature concept)

Every completed task updates **two** ledgers:

| Entry | Question it answers | Pilot-facing example |
|-------|--------------------|-----------------------|
| **Action currentness** | Which concrete action/event am I rusty on? | "Not current on de-icing, fuel leak, RTO, runway change" |
| **Competency currentness** | Which underlying competencies are weakening across all my actions? | "KNO weakening, PSD weak, SAW due soon" |

Example: a *de-icing scenario* (tagged PSD primary; KNO/PRO/SAW/COM/WLM secondary) — completing it lifts de-icing **action** currentness *and* sends positive signals to those **competencies**; failing/hesitating sends weaker signals, weighted by result.

> **Design implication:** OnCourse needs **two complementary readiness views** — an **Action Currentness** view (operational, the one pilots live in: a list/map of actions with due status) and a **Competency Currentness** view (the 9-competency radar/analytics). My v1 "competency radar" was only the second; the first is equally important and arguably more prominent for pilots.

### 5.5 Exposure model & categories (backend — drives scheduling)

Exposure is assessed across **5 sources**: line flying, simulator, recurrent/CBT/formal, seasonal/network context, personal profile. The remaining **exposure gap** (after all sources) drives recurrence. Each OTU lands in one **Exposure Category**:

| EC | Profile | Typical OTUs | Review logic |
|----|---------|--------------|--------------|
| **EC1** Routine line-reinforced | Done most sectors | Cockpit prep, normal checklist, routine briefing | Low frequency; focus on *traps/quality* |
| **EC2** Frequent but variable / error-sensitive | High exposure, context changes | Approach briefing, energy/mode awareness, runway/departure change | Moderate; scenario variation + traps |
| **EC3** Contextual / seasonal | Depends on season/airport/weather | De-icing, contaminated runway, LVO, winter ops | Intense in season; low outside |
| **EC4** Rare but formally trained | Low line, regular sim/recurrent | RTO, engine failure after V1, TCAS, windshear | Micro-retrieval between formal events |
| **EC5** Rare & weakly trained / complex abnormal | Low line, occasional formal | Fuel leak, smoke/fumes, emergency descent, hydraulic failure | Frequent rare-critical scenarios |
| **EC6** Immediate-action critical | Almost never on line; seconds; high consequence | Windshear escape, GPWS, TCAS RA, RTO stop/go, evacuation | Highest frequency; time-limited drills |

### 5.6 Recurrence pools & training patterns (backend — drives *what* and *how often*)

Recommended review interval → recurrence **pool** (a label for a family of intervals) → **exercise type**:

| Pool | Interval | Best exercise types | Example |
|------|----------|---------------------|---------|
| **1** | 3–6 mo | Short checks, missing-item detection, briefing critique, system-logic refresh | FMGS/OFP inconsistency in cockpit prep |
| **2** | 1–3 mo | Scenario variation, clearance/runway change, mode-awareness trap | ATC changes runway + SID on taxi — what to recheck? |
| **3** | Monthly in season / 3–6 mo out | Seasonal threat scenario, weather interpretation, contaminated-runway case | Snow before departure — is de-icing required? |
| **4** | 2–6 wk | Abnormal scenario, ECAM/QRH reasoning, diversion planning | Fuel trend inconsistent — what info is needed? |
| **5** | Weekly–monthly | Time-limited recognition drill, first-action selection, immediate-priority question | WINDSHEAR after rotation — immediate priority? |

**Override rules** (examples): time-pressure 5 + criticality ≥4 → min Pool 5; rare line + criticality ≥4 → min Pool 4; high line but error-sensitive ≥4 → min Pool 2; seasonal items get a seasonal pattern; low recent flying / return-from-leave temporarily shortens intervals.

> **Scoring is semi-automated + pilot-validated and must be auditable** — the system shows *why* an item is due (exposure gap / criticality / time pressure / decay). This "why" is the basis of the AI Trust Hub (§6.5). Pilot-scored data is kept separate from AI-inferred data; confidence levels are stored.

### 5.7 The currentness engine & the two decay signals (drives *what's next*)

Training is triggered by **two evidence streams**, but the task surfaced to the pilot is **always a concrete operational task** (never "train a competency"):

- **Signal A — OTU/action decay:** a specific action is overdue → assign *that* action's scenario (de-icing overdue → de-icing scenario).
- **Signal B — competency decay:** a competency is weakening across many linked OTUs → pick a high-value OTU that strongly exercises it (KNO weakening → fuel-leak analysis scenario, framed as *"your KNO is slipping, so today: fuel-leak analysis"*).
- **Mixed:** an item satisfying both (overdue *and* exercises a weak competency) is highest priority.

**Action currentness metrics (per OTU):** `last_reviewed`, `next_due`, `performance_status` (passed/weak/failed/hesitated/reviewed-only/not-attempted), `action_currentness_score`, `due_status` (current / due-soon / overdue / weak / critical-overdue).

> **Design implication:** `due_status` maps directly to the **status color system** (§9.2): current = green, due-soon = amber, overdue/weak/critical = red. Reuse everywhere.

### 5.8 What surfaces to the pilot (the visibility rule — **critical for design**)

**Show (operational/simple):**
- Concrete **actions/events** by name ("Fuel leak in cruise", "De-icing decision", "TCAS RA") with a clear status (current / due / overdue).
- The **9-competency** picture (radar + per-competency trend) as the higher-level "how am I doing" view.
- The **"why"** behind any recommendation, in plain language ("due soon", "weak topic", "your selected priority") via a one-tap *Why?* (ⓘ).
- The **next best action** (Predictive Hero Tile) and the session itself.

**Hide (backend machinery — never as jargon):**
- OTU IDs, exposure-category codes (EC1–EC6), recurrence pool numbers, scoring formulas, the double-entry implementation detail.
- *Exception:* an optional power-user/advanced reveal is **out of scope** (we chose operational/simple).

### 5.9 Content pipeline & phased personalization (how the engine reaches the pilot)

The method above is the *scheduling brain*. Here is how it actually produces and delivers content — and how that is **phased** so Release 1 ships without the full engine.

**The content pipeline:**

```
Validated A320 source (FCOM / OM-A …)
      │   RAG generation — many questions/exercises,
      ▼   in the fixed question-architecture formats (§15)
Question bank  ──(human/pilot validation — no unvalidated content ships, §13.3)──►
      │
      ▼   the engine maps each item to OTUs + competencies + exposure/recurrence,
          then SELECTS & GROUPS items into REVISION POOLS
Parallel "Revision Pools" database  ──►  pushed into the app's dedicated surface ("Flight Plan")
      │
      └► individual items can also be PULLED ad hoc (Train: quick test / search / build-your-own)
```

**Terminology (kept distinct to avoid confusion):**
- **Recurrence pool** *(method term, backend)* — an *interval family* (Pool 1–5) describing how often an OTU should recur.
- **Revision pool / set** *(the deliverable)* — a concrete, ordered **list of questions/exercises** the engine assembled for one revision, stored in the parallel database and pushed to the pilot.

**Two delivery modes in the app:**
| Mode | What it is | Where it lives |
|------|-----------|----------------|
| **Engine-pushed** *(the differentiator)* | Revision pools the engine assigns/schedules for you — "your personal training department" | **Flight Plan** surface (+ the Predictive Hero Tile surfaces the top due pool) |
| **Self-directed** | You pull single questions / build a quick test / search a topic | **Train** tab |

**Phased personalization — this is the key delivery decision:**

| | **Release 1 — personalization by *routing*** | **Later — personalization by *engine*** |
|---|---|---|
| How a pilot gets their content | Intent quiz + light signup data **routes** them to **one of 3–4 hand-authored training paths**; the app pushes that path's revision pools | The full competency-continuity engine **computes a unique pattern per pilot** from signup + exposure + performance, and generates/schedules pools dynamically |
| Feels like | Personalized (curated path chosen for you) | Truly individual (1:1) |
| Status shown | **Light:** your path, today's pool, streak, path progress | **Rich:** dual-currentness (action list + 9-competency radar), "why due" analytics |
| Content | Pre-assembled, fully validated pools | Engine-assembled from the validated bank |

> **Design implications (critical for the first Figma batch):**
> - Design the **Flight Plan** surface around **"your path → today's revision pool → do it."** A **path** is a named, recurring program (e.g. *"Sharp FO — Systems & Abnormals"*); a pilot has **one active path** at a time.
> - Onboarding needs a **path-assignment moment** ("Based on your answers, your OnCourse path is …") — honest, not over-claiming AI.
> - Early-release **status is light** (path progress, pool completion, streak, due count). **Do not** design the full competency radar as an early-release screen — mark it a **later-phase** view.
> - Keep the **self-directed Train** mode visibly separate from the engine-pushed Flight Plan, so "what OnCourse tells me to do" ≠ "what I chose to poke at."

### 5.10 Content sourcing, review & the trust promise *(founder-directed — the credibility moat)*

Content credibility is the #1 risk (§13.3). The governance model:

- **Source of truth:** all content derives from **official aircraft-manufacturer documentation** — **Airbus first (A320)**, with **Boeing and other types later**. As the product scales toward becoming an industry standard, the plan is to **acquire licensed access to official sources**. *(Design/legal note: never present manufacturer text verbatim as the app's own; keep source references per item; secure appropriate content rights — see §13.3 IP row.)*
- **Generation:** questions/exercises are **RAG-generated** from that source, in the fixed formats (§15).
- **Human review is mandatory — every single item.** Even though generation is automated, **professional pilots manually review every question before it can reach a user.** No unreviewed item ships.
- **Admin Review console (internal tool):** admins use a review mode that shows *unverified* generated questions with a **Correct / False / To rewrite** control; "to rewrite" and "false" route back to admins (us) for correction/removal. Only **Correct-marked** items enter the revision-pool database. *(This is a separate internal surface — see §6.7 and screen #50; not part of the consumer app, lower design priority than the core loop.)*
- **Item lifecycle:** `generated → in review → (correct | rewrite | rejected) → approved → in pool`. Store reviewer + timestamp for auditability.
- **In-app trust signal:** because every question is pilot-reviewed, surface a quiet **"Reviewed by professional pilots"** signal (e.g., on feedback screens / content info), and keep the **source reference** visible. This is a genuine differentiator vs. generic AI question banks — show it, don't shout it (per the "quiet edge" brand).
- **Safety-net (later):** an optional user **"flag this question"** control feeds items back to the review queue.

> **Design implications:** (1) the consumer app must show the **"reviewed by pilots"** trust cue and honor the **"never replaces official docs/training"** disclaimer (§1.3); (2) the **Admin Review console** is its own internal product surface to design later (§6.7).

---

## 6. The Full Feature System

*(From the Product Functionality Specification. Grouped as the spec is. Each feature notes its design relevance. Items the spec marked "Not applicable / not planned for V1" are flagged.)*

### 6.1 Onboarding & Identity
- **One-Tap Auth (Passkeys):** biometric-first login; minimize drop-off.
- **Zero-Login:** let users experience value *before* asking for email.
- **Predictive Intent Quiz:** 3-question visual survey tagging goals (limitations / memory items / systems / performance). Powers personalization **and** pre-fills the Home "What do you want to train today?" section from first visit.
- **Play-First Tutorial:** one sample question for *each* exercise type (flashcard, fill-in-the-blank/cloze, scenario), each in a different subject — instantly shows scope + formats.
- **Dynamic Goal Setting:** user picks commitment level (mental contract).
- **Progressive Enabling / First-Session Choice:** end onboarding with a choice — **Explore** (land on Home) · **Quick Start** (predefined Quick Test, zero settings) · **Build My Own Path** (Custom Quiz setup). Preserves autonomy for experts, structure for the unsure.

### 6.2 Core Learning Engine
- **SRS (Spaced Repetition):** a dedicated **Review tab** continuously queues due items using an FSRS/DSR forgetting-curve model (tracks Stability & Difficulty, schedules at target retention ~90%). Ratings: **Again / Hard / Good / Easy**.
- **Adaptive Difficulty (ELO/IRT):** quick-test difficulty adjusts after each answer, within and across tests; falls back to manual difficulty pick if incremental fetch isn't available.
- **Micro-Quiz Interrupts:** 10–15s assessments via push notifications, Live Activities / Dynamic Island, home-screen widgets, lock-screen complications, haptic nudges, in-app overlays. Three question intents: **Concept Probe** (categorize/refine interest), **State Check** (calibrate difficulty — "how much effort, 1–3?"), **Discriminative Quiz** (resolve a specific confusion point).
- **Natural-Language Search:** free-text bar on Home & Quick Test ("PTU logic", "green hydraulic pump", "VNAV constraints") → instantly auto-builds a short, relevant quiz by mapping text to the taxonomy.
- **Personal Content Curator (the AI agent):** an *orchestrator over deterministic building blocks* — selects a **team-curated program template** (e.g. "Command Upgrade Prep", "Interview Technical Bootcamp"), splits/schedules it into micro-sessions fitting the user's constraints (e.g. 1 min/day, 4×/week). **AI maps inputs→template and proposes scheduling only; all content comes from the validated question bank — no content invention.** Plan adapts to performance (SRS due, weak areas, misses) while staying stable/predictable.

### 6.3 Home Page & Context
- **Predictive Hero Tile:** the Home "Start" card surfacing the single best next session (SRS review / micro-quiz / quick test / resume), chosen from intent + due reviews + recent activity + time budget. Includes a plain **"Why"** label and a manual **override**. *This is the real home anchor — choice-architecture default.*
- **Progressive Investment Tracker:** a skill tree / knowledge map that visually fills as you learn (endowment effect).
- **Social Activity Ticker:** small feed of friends' wins (passive accountability).
- **Choice Architecture Defaults:** always compute one best next action; expose as the Hero Tile; allow override.

### 6.4 Retention & Behavioral Psychology

> **Founder-directed guardrail: keep gamification restrained.** OnCourse must **not feel like a game** (it's a serious professional tool) — but it must not be **boring** either. The core motivator is **daily lesson/session completion → streak** ("you need to train every day"). Celebration is tasteful and quiet (per the "quiet edge" brand), never confetti-heavy or childish. **De-scope the points *currency*/marketplace** (see below).

- **Contextual Smart Notifications:** opt-in, low-frequency, only in allowed windows; deep-link to a one-tap session (same engine as the Hero Tile) with a "why" + easy mute/snooze.
- **Training Streak (primary loop):** earned by **completing a lesson/session** — two modes: **Daily** (1 qualifying session/day) and **Cadence** (pilot-optimized: e.g. 4 sessions/week → consecutive weeks hitting target). Pilot schedules vary, so cadence matters.
- **Streak Guard (Freezes):** protect a streak via freezes **earned through consistency** or a pre-scheduled vacation. **No points currency / no marketplace** — this keeps it non-gamey. *(The former "Streak Guard Marketplace" + points economy is **de-scoped**.)*
- **Verifiable Milestones:** quiet, verification-backed mastery badges (e.g. "A320 Bleed Air") — granted only on **sustained retention + performance**, not content completion. Optional public verification page. *(Later phase.)*
- **Value Realization Screens:** occasional "knowledge maintained / progress" summary — informative, not boastful. *(Later phase.)*
- **Social (Leaderboards, Collaborative Quests, Activity Ticker):** **later-phase and to be validated** — competing publicly on competency may feel unprofessional to some pilots; if built, keep it optional and low-key.

### 6.5 Control, Privacy & Trust
- **Privacy Zones:** geofence to mute notifications at home/work.
- **AI Trust Hub:** a dedicated **AI & Trust** settings page + a lightweight **Why? (ⓘ)** next to *every* AI-driven suggestion. Centralizes AI on/off, which signals are used (SRS due, weak areas, priorities, recent searches), privacy boundaries, reset. The Why? icon shows the "because…" + instant controls (**Change / Not relevant / Wrong**). *(This is the surfacing of §5.6's auditable "why".)*
- **AI Persona Selector:** **not planned for V1** — single professional voice; later maybe simple Exam-vs-Training mode + explanation depth.
- **Offline Vault:** auto-download upcoming lessons; guarantees access anywhere (essential for crews/airports/aircraft).
- **Focus Mode:** silence all non-essential notifications except the user's daily window (flow state).
- **Incognito Pause Mode:** toggle to stop all data logging for a period (ghost sessions that don't pollute AI recommendations — e.g. a friend tries the app).

### 6.6 Accessibility, Adaptation & Device Experience
- **Cognitive Load Ceiling ("Low Power Brain Mode"):** a Low-Load toggle on the Quick Test start page restricts to single-step, minimal-reading, no-multi-step-scenario items (a dedicated Load tag) — fatigue-friendly training on low-energy days; user can expand.
- **Learning Style Profile:** lightweight format preferences (flashcard, cloze, MCQ, scenario, step-ordering) + explanation depth; used as *weights* when assembling sessions (never blocks essential formats — e.g. memory items stay recall/ordering). Captured once after the Play-First Tutorial; editable in Settings → Training Preferences.
- **Dynamic UI Layouts:** optional adaptive interface moving most-used features into the thumb-zone based on real usage.
- **Haptic Feedback Levels:** adjustable vibration for correct/incorrect (multisensory; helps in noisy environments / visual impairment).
- **Dynamic Contrast & Font Scaling:** system-wide accessibility support incl. **High Contrast** and **OLED-friendly Pure Black**. *(Validates the dark-first direction, §9.)*
- **Mood-Aware Adaptive UI:** if on-device signals suggest high stress (e.g. erratic scrolling), can auto-trigger the Cognitive Load Ceiling and soften UI tone.
- **Sustainable / Energy-Aware (Eco-Mode):** reduce background activity & network to save battery.
- **AI Refinement Toggle:** quick feedback to correct/dismiss AI suggestions (retrain to preference).
- **State Persistence Hand-off:** real-time task sync across phone / desktop / wearable — start a micro-quiz on phone, finish on laptop.
- *Marked Not Applicable in spec:* Multimodal Input "how", Interest-Based Content Skinning, Narrative Roles, Commute-Detection Sync, Venue-Aware Content. **Do not design these for v2.**

### 6.7 Admin Review Console *(internal tool — separate from the consumer app)*

The engine that guarantees content credibility (§5.10). A **web/admin surface** (not shipped to pilots) where reviewers see RAG-generated, *unverified* questions and clear each one:
- **Queue view:** unverified items with source reference, exercise type (§15), competency tag, and the generated content.
- **Per-item action:** **Correct** (approve → enters pool DB) · **False** (reject) · **To rewrite** (route back to admins for editing).
- **Editing:** admins modify stems/answers/explanations; edited items re-enter the queue.
- **Audit:** reviewer identity + timestamp stored; approved items carry the "reviewed by pilots" flag surfaced in-app.
- **Access:** admin-only account/role (distinct from pilot accounts).

> **Design priority:** *lower than the consumer core loop* — design after the V1/V2 pilot-facing batch. But it's a real product surface (likely desktop-first) and belongs in the roadmap.

---

## 7. Users, Personas & Journeys

### 7.1 Personas (A320, short-haul focus for MVP)

**A — "Maya," Cadet / new A320 First Officer** *(beachhead)*
- 24, fresh off type rating, ~6 months on the line. Terrified the rare-critical stuff (engine failure after V1, fuel leak) has gone stale before her first recurrent sim.
- **Jobs:** keep freshly-learned systems from fading; know she's ready; find weak spots privately first.
- **Quote:** *"I passed the type rating, but six months later I'm rusty on half the abnormals. I want to walk into the sim knowing I've got this."*

**B — "David," Experienced A320 Captain**
- 48, 12,000 hrs. Confident; knows complacency is the enemy; values precision and his time; hates fluff.
- **Jobs:** keep QRH/non-normals sharp; stay current on rare items; quietly self-check.
- **Quote:** *"I don't need a logbook. I need ninety seconds a day that keeps me a step ahead."*

**C — "Sam," Career-Climber** *(later phases)*
- 31, regional → major + command upgrade. Wants interview/sim-assessment prep and a single organized professional home.

### 7.2 Jobs-to-be-done (ranked, MVP)
1. *When a check approaches, know exactly how ready I am — including the rare stuff — and what to drill.*
2. *In spare minutes, get a quick, relevant retrieval that actually maintains memory.*
3. *Privately know my real weak actions/competencies so I can fix them before they're exposed.*
4. *(Later) one trusted place that grows with my whole career.*

### 7.3 Core user journey — the daily & continuity loop

```
FIRST RUN
Zero-login welcome → Predictive Intent Quiz (3 visual Qs) → Play-First Tutorial
(1 sample per exercise type) → Dynamic Goal Setting → First-Session Choice
(Explore / Quick Start / Build My Own Path)
        │  (instant value — a real retrieval task within ~60s, no paywall, no long form)
        ▼
DAILY LOOP  ┌─────────────────────────────────────────────────────────────┐
            │ Open app → HOME: Predictive Hero Tile = "the one best thing"  │
            │   ("Review 8 due items ≈2 min" / "Drill: Windshear escape")  │
            │        │  (Why? ⓘ + Change override always available)        │
            │        ▼                                                       │
            │ Do session (SRS review / micro-quiz / quick test / scenario)  │
            │        ▼                                                       │
            │ Active-retrieval feedback (correct + crisp explanation +      │
            │   competency tag) → rate Again/Hard/Good/Easy                 │
            │        ▼                                                       │
            │ BOTH ledgers update: Action currentness ↑ + Competency ↑      │
            │ Streak ++ ; skill tree fills ; next due recalculated          │
            └─────────────────────────────────────────────────────────────┘
MICRO-MOMENTS: micro-quiz interrupts (notification / widget / Dynamic Island)
PRE-CHECK: currentness surfaces overdue rare-critical items → drill before the sim
```

**Principles from this journey:**
- **Instant value < 60s**, before any heavy setup or paywall.
- **Home = one decision, not a menu.** The Hero Tile removes choice fatigue; everything else is one tap away.
- **Respect the expert** (David's 90-second path) *and* **support the anxious** (Maya's deeper drills + explanations) via progressive disclosure.
- **Two readiness truths** always reachable: *which actions am I rusty on* + *which competencies are slipping*.

---

## 8. Information Architecture & Screen Inventory

> **Primary build spec for Figma.** Mobile-first, **iOS primary** (390×844 / iPhone reference; Android parity via Material adaptation). **Light + teal** (§9 as-built note). Operational/simple language (§5.8). A320 content, type-agnostic shell. **Batch-1 (core loop) screens are marked ⭐.**

### 8.0 As-built addendum — founder-directed changes (CANONICAL, supersede the inventory below)

The design was built in the **OnCourse Aviation** Figma file (`VfD60619fgSHWnd3EtFDUg`) and reviewed live by the founder. The following founder-directed decisions are **canonical** wherever they differ from the original inventory:

1. **Home ("Flight Plan") header matches the shipped app's code**: gradient **avatar tile with initial** + uppercase greeting label + **first name only** ("Maya"), with **A320 chip · streak chip (drawn flame icon) · settings** icon-buttons on the right. (Replaces the plain one-line greeting.)
2. **Home surfaces self-directed entry points**: a **"Practice on your own"** row with **Quick Test** and **Custom Quiz** cards sits under the Today hero (replacing the "also due" list in the early release).
3. **Custom Quiz** reproduces the shipped app's configuration layout — Number-of-questions slider (1–100), Filter (All / Weak areas / Flagged), Reference manual (FCOM/FCTM/OMA), Domain, Category, Exercise type, sticky Start bar — **plus a new "Suggested for you" hero tile** above the manual configuration.
4. **Quick Test** reproduces the shipped app's mode picker: featured "All categories · 40 random" card + category grid with **Coming Soon** locked cells.
5. **Onboarding starts with a quick profile setup** ("Which aircraft do you train on?" — A320 / 737 / Other-coming-soon + role chips) inserted **between Welcome and the Intent Quiz** (canvas label "02 · Profile setup").
6. **Welcome Back (sign-in)** screen matches the shipped app: email + password, Sign In, OR divider, Continue with Google/Apple, "Create account" footer. Second prototype entry point for returning users.
7. **Visual language is Light + Teal / Inter** per the founder's "vector — V0" reference (see §9 note); the dark direction is historical.
8. **File organization (as-built):** pages = 📐 Design System (variable-bound tokens, type ramp, component sets) · 📱 App · Core Screens (35 screens: session + answered states, onboarding, home/engine, tabs, system, notification surfaces, streak/cold-start/offline states) · 🧭 Later Phase (Action & Competency Currentness, competency detail, Admin Review Console) · 📖 Cover & Handoff. Clickable prototype: play-first flow + returning-user flow, tab-bar navigation wired.
9. **Welcome-screen trust-proof block (from the persona-walkthrough audit):** the Welcome (Zero-Login) screen carries a three-row credibility/reassurance block above the CTA — ✓ *Sourced from official A320 documentation* · ✓ *Written & reviewed by professional pilots* · ✓ *Private by default — never shared with your airline*. Rationale: surface the authority + privacy proof at the first anxious moment (fold 2) rather than only at the play-first tutorial (fold 5); ties to §5.10 (pilot review) and the privacy promise (§2/§4). Keep this proof at first contact in any redesign.

### 8.1 Navigation model — 4 tabs + center action *(resolved for early release)*

Early release uses **4 tabs + a center FAB** (not 5) — cleaner, and it matches the "one best action" philosophy. The engine-pushed content and the home are the *same* surface (**Flight Plan**); SRS "due" items surface *within* Flight Plan early and can graduate to their own tab later.

| Tab | Icon idea | Purpose |
|-----|-----------|---------|
| **Flight Plan** ⭐ *(home)* | route / target | The engine-pushed path: Predictive Hero Tile (today's top pool), your active path, due revision pools, streak + light progress. **The dedicated engine-content surface.** |
| **Train** ⭐ | brain / sliders | Self-directed *pull*: Quick Test, Custom Quiz, Natural-Language Search, Low-Load toggle, topic library |
| **Progress** ⭐ | chart / rings | Streak, path progress, pool history, milestones. *(Later phase: the dual-currentness action list + 9-competency radar land here.)* |
| **Profile** | pilot / wings | Identity, settings, AI & Trust, subscription, Offline Vault |
| **Center FAB** ⭐ | "+" → *Start today's pool* | One-tap into the Hero Tile's recommended revision pool from anywhere |

> Reserve clearly-labeled "Coming soon" rows in Profile for the future career-companion pillars (Documents, Logbook, Career) so the growth path is visible without cluttering MVP. The **later-phase competency radar / dual-currentness** views (screens 30–33 below) also live under Progress when they arrive.

### 8.2 Screen inventory

**Onboarding & identity** ⭐
1. ⭐ Splash / brand (logo, tagline: "Stay on course.")
2. ⭐ Zero-login welcome (start instantly; passkey/email offered later)
3. ⭐ Predictive Intent Quiz — 3 visual cards (limitations / memory items / systems / performance…) — *drives path routing*
4. ⭐ Play-First Tutorial — one sample per exercise type (flashcard, cloze, MCQ, true/false, drag-drop), each a different subject
5. ⭐ Dynamic Goal Setting — commitment level (e.g. 1 min/day · 4×/week · intensive)
6. ⭐ **Path Assignment** — "Based on your answers, your OnCourse path is **[e.g. 'Sharp FO — Systems & Abnormals']**" — the routed path (1 of 3–4); honest, no AI over-claim; option to view/switch path
7. ⭐ First-Session Choice — Explore / Quick Start / Build My Own Path
8. ⭐ Passkey / account creation (offered *after* first value)

**Flight Plan (home + engine-pushed pools)** ⭐
9. ⭐ **Flight Plan / Predictive Hero Tile** — see §8.3 (the most important screen): active path, today's top revision pool, streak, light progress
10. ⭐ **Revision Pool overview** — the pushed pool: name, what it covers (actions/topics), item count + est. time, **Start**; the engine's "why this pool" in plain language
11. ⭐ Hero Tile / pool "Why?" sheet — plain-language reason + **Change** (override to another due pool)
12. ⭐ **Path detail** — the active path: its pools, cadence, progress; switch-path entry
13. Social Activity Ticker (compact, on Flight Plan) *(later phase)*

**The session (learning engine)** ⭐ — *canonical exercise types per Source Doc 3 (§15)*
14. ⭐ Question — **Flashcard** (retrieval cue → flip/reveal)
15. ⭐ Question — **Multiple Choice (MCQ)**
16. ⭐ Question — **Fill-in-the-blank (cloze)**
17. ⭐ Question — **True / False**
18. ⭐ Question — **Drag-drop** (variants: order / match / sort)
19. ⭐ Session summary — score, streak ++, pool completed, what improved
20. ⭐ Feedback screen — correct/incorrect + crisp explanation + competency tag + source-reference link
21. ⭐ **SRS rating** control — Again / Hard / Good / Easy (on review items)

> **Not separate question types:** a **scenario** is a *content style* rendered via MCQ/flashcard (e.g. "WINDSHEAR after rotation — immediate priority?"); a **time-limited drill** is a *mode/wrapper* (a visible countdown overlay) applied to any type for Pool-5 immediate-action items. Design both as **variants/overlays**, not new screens.

**Train (self-directed pull)** ⭐
22. ⭐ Train home — Quick Test · Custom Quiz · search entry · Low-Load (Cognitive Load Ceiling) toggle
23. ⭐ **Natural-Language Search** — free-text → auto-built quiz preview ("PTU logic → 8 Q")
24. ⭐ Quick Test setup (adaptive on; or manual difficulty fallback)
25. Custom Quiz / Build My Own Path (subject, system, count)
26. Topic library — browse taxonomy (§12), filtered to A320
27. Micro-quiz interrupt — in-app overlay variant + notification/Dynamic Island/widget mockups (3 question intents §6.2) *(V3)*

**Progress (early = light status)** ⭐
28. ⭐ Progress home — streak, path progress, pool history, consistency; milestones entry
29. ⭐ Empty/early state — "Your picture builds as you train" (cold-start; see §16)

**Dual currentness — the differentiator** 🔒 *(LATER PHASE — design after the engine ships; lives under Progress)*
30. 🔒 **Action Currentness** — operational list of actions with status (current/due/overdue), sorted by urgency
31. 🔒 Action detail — one action (e.g. "Fuel leak in cruise"): status, last reviewed, next due, **Why?**, "Drill now"
32. 🔒 **Competency Currentness** — 9-competency radar; weak competencies called out
33. 🔒 Single competency detail (e.g. KNO) — trend, linked weak actions, recommended drills
34. 🔒 Next-check context — optional date of next recurrent/sim; pre-check focus list

**Retention / gamification** *(restrained — §6.4)*
35. ⭐ Streak screen — daily vs cadence mode, calendar, freezes (earned via consistency; **no points/marketplace**) *(V1)*
36. Milestones / verifiable badges — earned on sustained retention + performance *(V2)*
37. Value Realization — occasional progress summary (informative, not boastful) *(V2)*
38. 🔒 Social (Leaderboard / Quests / Activity Ticker) — *later phase; validate fit with pro audience; optional & low-key if built*

**Profile, trust & system**
39. Profile home — identity, aircraft chip (A320), streak, milestones, active path
40. **AI & Trust Hub** — AI on/off, signals used, privacy boundaries, reset; **"reviewed by pilots" + data-privacy promise** surfaced here; reachable from every Why? *(V2)*
41. Settings — auth/passkey, aircraft, notifications + windows, theme (incl. Pure Black / High Contrast), haptics, Eco-Mode, Focus Mode, Incognito Pause, Privacy Zones, **data export/delete**, State-Persistence/devices
42. Training Preferences — Learning Style Profile (formats + explanation depth)
43. ⭐ **Disclaimer acknowledgement** — brief onboarding notice: "OnCourse never replaces official documentation or airline training" (also permanent in About) *(§1.3)*
44. 🔒 Subscription / paywall — *later phase; **not** in early release (launch is 100% free, §4.10)*
45. Offline Vault — downloaded content manager *(V2)*
46. "Coming soon" / roadmap teaser — Documents · Logbook · Career

**Internal (not the consumer app)** 🔧
47. 🔧 **Admin Review Console** — queue of unverified generated questions; per-item **Correct / False / To rewrite** + edit; audit trail (§6.7). Desktop-first; design after the consumer core loop.

**Global states** (design as variants, not separate flows) ⭐
48. ⭐ Empty ("Your path starts here" / no pool due yet), Loading (skeletons; shimmer-in), Error, **Offline** (calm chip; daily loop still works from vault), Success/celebration (streak milestone, pool complete, badge earned), **Low-Load mode** active variant, **cold-start** (§16).

### 8.3 Flight Plan / Predictive Hero Tile — detailed spec (most important screen) ⭐

The home surface. Answer in one glance, top → bottom: *what do I do right now, and how's my path going.*

1. **Greeting + identity strip** — "Good morning, Maya" · aircraft chip (A320) · streak (🔥 12).
2. **Active-path strip** — the routed path name ("Sharp FO — Systems & Abnormals") + progress (e.g. "Week 3 · 62%"). Tap → Path detail (#12).
3. **Predictive Hero Tile (hero):** today's top revision pool, large and tappable:
   - Title: the pool ("Today: Hydraulics & abnormal config — 8 items").
   - Time budget ("≈ 4 min") and progress if resuming.
   - Plain **Why** label (early release: "next in your path" / "due for review") + **Change** (pick another due pool).
   - Primary CTA button: **Start**.
4. **Due pools list** (if more than one) — other revision pools ready, with item count + est. time.
5. **Light status row** — streak chip · path progress · pools-completed. *(No competency radar in early release.)*
6. **Micro-quiz nudge** (optional, V3) — "Got 15 seconds? Quick check." → micro-quiz overlay.

> **Later-phase enhancement:** once the engine ships, add a **dual-currentness summary band** here (compact action-readiness bar + compact 9-spoke competency radar → screens #30/#32). Do **not** design this band for the early-release batch.
>
> If a viewer can't tell within 3 seconds this is a **forward-looking, path-driven training** app (not a logbook) — and can't see *what to do right now* + *how my path is going* — the design missed the brief.

---

## 9. Design System & Visual Language

> **⚠️ DIRECTION UPDATED (supersedes the dark proposal below).** The realized OnCourse design language is **Light + Teal, Inter** — matching the founder's existing "vector — V0" reference and built in the **OnCourse Aviation** Figma file (21 screens). Use **this** system for all design work. The "Modern Glass-Cockpit / dark-first" text in §9.1–9.3 is the earlier *proposal* and is retained only as history.
>
> **Live design file:** OnCourse Aviation — `https://www.figma.com/design/VfD60619fgSHWnd3EtFDUg`
>
> **Palette (light + teal):** bg `#f4f6f7` · surface/cards `#ffffff` · border `#e2e7e9` · text `#0c1a24` · text-secondary `#5b6b76` · muted `#9aa7ae` · chip `#ecf1f2` · **brand teal `#0e9594`** (+ tint `#eaf5f4`) · **correct/positive `#1fa971`** (bg `#e4f4ec`) · attention `#e8952b` · critical `#dc2626`.
> **Type:** **Inter** (Regular/Medium/Semi Bold/Bold). *(DM Sans — the prior app's font — is an acceptable swap, but the reference and built screens use Inter.)*
> **Components:** iOS status bar · segmented progress dots · category chips (uppercase, tracked) · white bordered cards (radius 12–20) · option cards with green correct-state · explanation card with source reference (e.g. `FCOM 1.29.10`) · teal primary button (h 54, radius 14) · 4-tab bar (Flight Plan · Train · Progress · Profile) + center FAB · toggles/radios · streak week-dots.
> **Status semantics** are unchanged from §9.2 in meaning (green = current/correct · amber = attention/due · red = critical); only the hues shifted to the teal-family palette above.

### 9.1 Direction *(HISTORICAL PROPOSAL — superseded by the note above)*: "Modern Glass-Cockpit" (dark-first)

Premium, dark-first, precision-instrument-inspired, but **modern and restrained** (high-end fintech/health app, not literal avionics skeuomorphism). Rationale: credibility + differentiation in a category of database-like UIs; calm high-contrast data displays mirror the cockpit; gauges/radars are native metaphors (currentness gauge, competency radar); and the source spec **explicitly** asks for OLED Pure-Black + Dynamic Contrast (§6.6). Provide a **light theme** too (system toggle), but design dark as the hero.

### 9.2 Color tokens (name as Figma variables/styles)

**Dark theme (primary):**
| Token | Hex | Use |
|-------|-----|-----|
| `--bg-base` | `#0B0F14` | App background (near-black, cool) |
| `--bg-pure-black` | `#000000` | OLED Pure-Black mode background |
| `--bg-surface` | `#141A22` | Cards / surfaces |
| `--bg-surface-elevated` | `#1C2530` | Modals, elevated cards |
| `--border-subtle` | `#26303C` | Hairlines, dividers |
| `--text-primary` | `#F2F6FA` | Primary text |
| `--text-secondary` | `#9AAABB` | Secondary/muted |
| `--brand-primary` | `#3FA9F5` | Instrument cyan-blue — CTAs, key accents |
| `--brand-primary-deep` | `#1E6FB8` | Pressed / gradient end |
| `--accent-amber` | `#F5A623` | Caution / due-soon / "needs attention" |
| `--accent-red` | `#FF4D4F` | Overdue / critical / weak |
| `--accent-green` | `#34D399` | Current / strong / success (mint, not pure green) |
| `--radar-fill` | `#3FA9F5` @ 30–60% | Competency radar fill |

**Status semantics (global — map to `due_status` §5.7):** **green = current / strong**, **amber = due-soon / needs attention**, **red = overdue / weak / critical**. Identical across action currentness, competency strength, streak risk, and (later) document expiry. Never reassign.

**Light theme:** `#F7F9FB` base, `#FFFFFF` surfaces, `#0B0F14` text; keep brand/accent hues, darken for WCAG AA.

### 9.3 Typography
- **Primary:** **DM Sans** — *adopted from the prior prototype (§17): already owned/loaded, a clean geometric sans that suits the precision brand.* Fallbacks: SF Pro (iOS) / Inter. **Drop the prototype's "Poppins/playful" face** — it conflicts with the restrained "quiet edge" (§4.4). Optional technical display face for big numbers only.
- **Always tabular figures** for scores, dates, counts, countdowns (precision; no jitter).

| Style | Size / weight | Use |
|-------|---------------|-----|
| Display | 34–40 / Bold | Big numbers, countdowns |
| H1 | 28 / Bold | Screen titles |
| H2 | 22 / Semibold | Section headers |
| H3 | 17 / Semibold | Card titles |
| Body | 16 / Regular | Default |
| Body-sm | 14 / Regular | Secondary |
| Caption | 12 / Medium | Labels, competency codes |

### 9.4 Spacing, radius, elevation
- **Spacing (4px base):** 4 · 8 · 12 · 16 · 24 · 32 · 48.
- **Radius:** cards 16 · buttons 12 · chips/pills full · modals 24. Generous, modern, not industrial.
- **Elevation:** subtle — on dark prefer lighter surface + thin border over heavy shadow; reserve a faint cyan glow for key "current/ready" states.

### 9.5 Signature components (build as Figma components with variants)
1. **Predictive Hero Tile** ⭐ — variants: review / micro-quiz / quick-test / scenario-drill / resume; with Why-label + Change.
2. **Competency Radar / Wheel** ⭐ — 9 spokes; variants: detail (tappable spokes), compact (Home band), single-competency focus. Fill = strength; amber spoke = weak.
3. **Action Currentness Row/Card** ⭐ — an action with status pill + due text + "Drill now"; variants: current / due-soon / overdue / weak.
4. **Currentness Gauge** — circular/arc for an overall readiness read; variants on-track (cyan) / attention (amber) / current (mint glow).
5. **Question Cards** ⭐ — one per exercise type (flashcard, cloze, MCQ, scenario, ordering, time-limited); states default / selected / correct / incorrect.
6. **SRS Rating Bar** ⭐ — Again / Hard / Good / Easy.
7. **Competency Chip** — code + status dot (`PRO ●`).
8. **Status Pill** ⭐ — Current / Due / Overdue (green/amber/red) — reused everywhere.
9. **Why? (ⓘ) sheet** — plain reason + Change / Not relevant / Wrong (AI Trust surface).
10. **Streak / Skill-Tree / Milestone-Badge** components.
11. **Bottom Tab Bar + Center FAB.**
12. **Aircraft / context chips** (`A320`).

### 9.6 Iconography & imagery
- **Icons:** thin-to-medium line, 1.5–2px stroke, rounded joins; aviation-literate but universal (gauge, radar, target, checklist, brain, wings).
- **Imagery:** no stock clip-art planes. Prefer abstract instrument/horizon/HUD motifs, subtle gradients, data-viz. Premium, restrained.
- **Motion (prototype notes):** gauges/radar animate in (count-up, draw-on); celebrate streaks / "all current" / badge-earned briefly and tastefully — never childish. Provide reduce-motion variants.

### 9.7 Logo & brand-mark direction (expresses "the quiet edge")

The identity should feel like a precision instrument, not a consumer toy — restraint is the brand (§4.4).
- **Wordmark:** clean technical sans (Inter/SF-adjacent), tight tracking, lowercase or small-caps; quietly confident, no italics, no "swoosh".
- **Mark concept directions** (explore 2–3 in Figma): (a) an abstracted **instrument-scan / crosscheck path** — a minimal cross or scanning reticle; (b) a **single precise reference point / datum** on a subtle horizon line; (c) a **9-point motif** echoing the competency radar. All geometric, single-weight, monochrome-capable.
- **Color:** mark works in `--brand-primary` cyan on dark and in mono (white/black); a faint cyan glow is the only "shine" permitted.
- **Avoid:** literal aircraft silhouettes, wings/roundels, gradients-as-decoration, anything that reads as a budget aviation clip-art brand.
- **App icon:** the mark on `--bg-base`/Pure-Black; legible at 1× and instantly recognizable in a crew-room glance.

---

## 10. Interaction, Adaptive UI, States & Accessibility

### 10.1 Interaction patterns
- **One decision on Home:** the Hero Tile is the default action; FAB launches it from anywhere. Everything important is one tap deep.
- **Active retrieval always:** every item asks the pilot to recall/decide/sequence/spot-a-trap — never passive reading.
- **Honest, calm feedback:** wrong = coaching (correct answer + crisp explanation + competency tag + source link), never a harsh buzzer.
- **Why everywhere:** every AI-driven suggestion carries a one-tap **Why?** with override (Change / Not relevant / Wrong).
- **Progressive disclosure:** expert 90-second path vs. cadet deep-dive; advanced features unlock progressively (Progressive Enabling).

### 10.2 Adaptive UI (design at least the toggles + the active states)
- **Cognitive Load Ceiling (Low-Load):** restricts to single-step, minimal-reading items; design the toggle + a visibly calmer "Low-Load" session state.
- **Learning Style Profile:** format weighting; design the preference capture + Settings editor.
- **Dynamic UI / thumb-zone, Mood-Aware tone-shift, Eco-Mode, Haptic levels, State-persistence handoff:** represent as settings + (where visible) their effect; don't over-engineer mockups for the invisible ones.

### 10.3 Required states (variants per screen)
- **Empty:** "You're current — nice." (no due items); "Set a goal to get your first plan."
- **Loading:** skeletons; gauge/radar shimmer-in (no spinners on content).
- **Error / Offline:** the **daily loop must work offline** from the Offline Vault; calm offline chip; queue sync. Never block retrieval on connectivity.
- **Success / celebration:** streak milestones, "all actions current", badge earned.

### 10.4 Accessibility (non-negotiable baseline)
- **WCAG 2.1 AA** contrast on both themes (verify amber especially); support **Dynamic Contrast / Pure-Black / font scaling**.
- **Never color-only status** — pair every green/amber/red with icon/label/shape. *(Color-vision standards make this doubly important in the pilot population.)*
- **44×44pt** min targets; full VoiceOver/TalkBack labels — give the radar/gauge text equivalents ("Procedures: needs attention; due in 3 days").
- **Haptic feedback levels** and **reduce-motion** variants.

---

## 11. Figma Generation Handoff Notes

> Direct instructions for the AI design agent(s).

1. **Build the design system first** (§9): color variables (dark + light + Pure-Black), text styles (tabular figures), spacing tokens, then the signature components (§9.5) with variants — *then* assemble screens. Coherent + dev-ready.
2. **Frame:** iPhone 390×844, iOS-primary; **dark is the hero**. Provide light + Pure-Black variants of at least Flight Plan, a question screen, and a revision-pool screen.
3. **Batch 1 = the V1/V2 core loop (⭐ screens).** Prioritize, in order:
   1. Onboarding (zero-login → intent quiz → play-first tutorial → goal → **path assignment** → first-session choice)
   2. **Flight Plan / Predictive Hero Tile** (§8.3) + **Revision Pool overview** + Why? sheet + Path detail
   3. Session: all 5 exercise types (flashcard, MCQ, cloze, true/false, drag-drop) + feedback + SRS rating + session summary — use the §16 sample items
   4. **Train** home + Natural-Language Search → auto-quiz
   5. **Progress** (light: streak, path progress, pool history) + cold-start/empty states (§16)
   *(Later batches: the dual-currentness radar #30–34, gamification, trust/privacy, adaptive screens.)*
4. **Use the §16 sample-content kit and §15 formats** — real A320 items, a real path and pool, real light-status numbers. **No lorem ipsum.**
5. **Operational/simple language (§5.8):** show concrete actions/topics and pool/path names. **Never** surface OTU IDs, exposure categories (EC1–6), or recurrence-pool numbers as user-facing text.
6. **A320 + type-agnostic shell:** design the structure so other aircraft slot in later (aircraft chip, taxonomy filters).
7. **Honor the positioning everywhere:** forward-looking, path-driven, coaching, calm, precise. No logbook/data-entry aesthetics.
8. **Status colors are global (§9.2):** green=current/strong, amber=due/attention, red=overdue/weak/critical.
9. **Respect the disclaimer (§1.3):** no copy implying formal qualification/certification/regulatory currentness. Use plausible-but-generic content; never invent regulations or present unverified procedures as authoritative.
10. **Accessibility variants:** include a Pure-Black/high-contrast pass and ensure status is never color-only.

---

## 12. Content Taxonomy (A320)

*(From the Functionality Spec. Use for realistic content and the topic library/filters. Type-agnostic shell: these are the A320 instance of a generalizable taxonomy.)*

- **Aircraft System:** Electrical · Hydraulics · Flight Controls
- **Limitations:** Aircraft General · Auto Flight System · Flight Controls · Ice & Rain Protection
- **Performances:** Takeoff · In-Flight · Landing
- **Normal Procedures:** Standard Callouts · Departure change · Descent preparation · Climb
- **Abnormal Procedures:** ALL MEM items · HYD B+Y SYS LO · HYD B+G · HYD G+Y · EMER ELEC · Landing with Slats/Flaps Jammed
- **Airbus Operational Philosophy:** Procedures design · Use of Summaries · How to conduct briefing · Handling of ECAM
- **Operative Manual A (OM-A):** 8.1.6 Interpretation of MET info · 8.1.7 Determination of Fuel & Oil · 8.8 Oxygen requirements · 8.3.5 GPWS · 8.1.3 Aerodrome determination methods · 8.3.9 Wake turbulence

> Mapped to the mission layers (normal phases · non-normal event families · operational wrapper) and to OTUs in the backend. Example non-normal OTUs for scenario content: RTO decision, engine failure after V1, smoke/fumes, fuel leak in cruise, emergency descent, TCAS RA, windshear escape, GPWS, evacuation decision.

---

## 13. Roadmap, Metrics & Risks

### 13.1 Roadmap — phased release plan *(from the Feature Prioritization Database, Source Doc 4)*

Phases run **Concept → V0 → V1 → V2 → V3**, grouped by **value bundle** (VB01 Guided Start · VB02 Retention Loop · VB03 Discovery · VB04 Instructor · VB05 Trust · VB06 Accessibility). The **P0 "Must" core is only four features:** Zero-Login (F002), Play-First Tutorial (F004), Predictive Intent Quiz (F003), SRS Engine (F010).

| Phase | Ships (feature IDs) | Result |
|-------|---------------------|--------|
| **V0** | Zero-Login (F002), Play-First Tutorial (F004); data foundations (Guest DB, A320 DB, Compete admin) | Instant-value trial; content foundation |
| **V1** | Predictive Hero Tile — *simple next-in-list* (F015), Training Streak (F022), Haptics (F043, *done*), Offline mode | The **Flight Plan loop, lean**: path → today's pool → do it → streak |
| **V2** | SRS Engine (F010), Intent Quiz (F003), Goal Setting (F005), First-Session Choice (F006), Choice-Architecture Defaults (F016), Adaptive Difficulty (F011), NL Search (F013), Smart Notifications (F021), Offline Vault (F035), Focus Mode (F036), AI Trust Hub (F032), Value Realization (F025), Milestones (F026), Dynamic Contrast (F044) | The **real learning engine** + trust + retention |
| **V3** | Micro-Quiz Interrupts (F012), Personal Content Curator / Instructor Agent (F014), Progressive Investment Tracker (F017), Social (F018–F020), Streak Guard (F023), AI Refinement (F033), Dynamic UI (F042), Mood-Aware UI (F045), State Hand-off (F050) | Advanced AI, social, adaptive |
| **Concept** *(unscheduled)* | Passkeys (F001), Privacy Zones (F030), Incognito (F031), Cognitive-Load Ceiling (F040), Learning-Style Profile (F041), Sustainable Design (F046), Collaborative Quests (F020) | Backlog / to be scheduled |

**Personalization phasing (§5.9):** Release 1 = **routing to 3–4 hand-authored paths**; the **full computed engine + dual-currentness radar** is a later phase (lands under Progress, screens #30–34).

**Career-companion phase (post-engine):** Documents & expiry vault · currency tracking · digital logbook · expanded AI assistant · career prep → then **B2B/ATO** (fleet currentness dashboards, instructor assignment, fleet analytics, compliance-aware export).

> **Note on "MVP" wording elsewhere in this brief:** where earlier sections say "MVP = the training engine," read it as **V1 (lean Flight Plan loop) → V2 (engine)**. The full engine is V2; V0/V1 are deliberately thinner.

### 13.2 Success metrics (MVP, directional)

| Metric | Why | Target |
|--------|-----|--------|
| D7 / D30 retention | Daily-habit product lives or dies here | D30 ≥ 25% |
| Daily session completion | Core loop engagement | ≥ 40% MAU practice ≥3×/wk |
| Rare-critical action currentness improvement | Validates the *core promise* (closing the exposure gap) | Measurable lift on EC4–EC6 items |
| Pre-check engagement | Validates the differentiator | ≥ 60% of users with a check date open currentness before it |
| Weak-area drill follow-through | Validates the coaching value | ≥ 30% act on a surfaced weak action/competency |
| Active user growth / word-of-mouth (referral rate) | Free-first land-grab is the Stage-1 goal (§4.10) | Strong MoM growth; viral coefficient tracked |
| *(Later, Stage 2)* Free→paid conversion | Viability once subscription launches | 4–8% |

### 13.3 Key risks & mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| **Content credibility** — pilots are unforgiving of wrong/dated content | High | High | Official manufacturer source only, no AI invention; **every question human-reviewed by professional pilots** via the Admin Review console before it ships (§5.10, §6.7); source reference per item; "reviewed by pilots" trust cue; user flag-to-review safety net; clear disclaimers (§1.3) |
| **Source licensing / IP** — manufacturer manuals are copyrighted | Med | High | Never reproduce manufacturer text verbatim as our own; generate original questions; **acquire licensed access to official sources as the product scales** (§5.10); keep counsel involved before public/commercial launch |
| **"Just another logbook" perception** | Med | High | Relentlessly forward-looking UX; lead with the path/pools; logbook deferred to later phase |
| **Method credibility / over-claiming** | Med | High | Position as a *continuity layer between approved events*; **prominent in-app "never replaces official docs/airline training" notice** (§1.3); never imply certification/regulatory currentness |
| **Scheduling accuracy** (intervals are approximations, not validated law) | Med | Med | Make intervals auditable & adjustable; pilot validation; periodic review vs feedback |
| **Engagement decay** (knowledge apps fade) | Med | High | Tie retrieval to *real rare-critical risk* + daily-completion streaks + relevance to the pilot's path |
| **Over-gamification** (feels unprofessional) | Med | Med | Restrained gamification (§6.4); no points marketplace; quiet celebration; social features later & optional |
| **Cross-jurisdiction / multi-type complexity** | High | Med | A320-first + type-agnostic shell; ICAO/EASA 9-competency universal core; jurisdiction as config later |
| **Data sensitivity / trust** | Med | High | **Weakness/performance data private to the pilot's account; employers/airlines never see individual data** (B2B = anonymized/aggregated only); privacy-by-default, encryption in transit + at rest, data export/delete, Incognito Pause; promise surfaced in onboarding + AI & Trust Hub (§14) |

---

## 14. Tech Stack & Design Constraints

*(From the Feature Prioritization Database, Source Doc 4 — suggested tools.)*

- **Hybrid mobile:** **Capacitor** (web tech in a native shell) — *not* pure native Swift/Kotlin. Design must render well via web engine and still feel native (respect iOS conventions, safe areas, momentum scroll, haptics F043).
- **Backend / platform:** **Firebase** — Auth, **Cloud Firestore** (data lives in the cloud), Remote Config (feature flags / phased rollout, e.g. First-Session Choice, Choice-Architecture Defaults), Storage (Offline Vault content).
- **Secure storage:** **Capacitor secure storage** for sensitive local data.
- **Data-trust posture (decided — founder-directed):**
  - **A pilot's weakness/performance data is private to their own account.** Full stop.
  - **Employers/airlines never see individual data.** When the B2B/ATO product arrives, operators receive **only anonymized/aggregated** fleet-level insight — never a named pilot's weak areas. This is a non-negotiable trust cornerstone (many pilots won't touch a tool their airline could monitor them with).
  - **Recommended handling (my answer to your open 2b):** keep cloud sync (Firestore) for cross-device continuity, **but** pair it with — encryption in transit **and** at rest; **privacy-by-default** (minimal collection, no third-party ad tracking); **pilot owns their data** with in-app **export + delete**; Incognito Pause for un-logged sessions. Surface the promise plainly at **onboarding** and in the **AI & Trust Hub**.
- **Other design implications:**
  - **Offline-first for the daily loop:** Offline Vault (F035) preloads due pools; the session + streak must work with no connectivity, syncing on reconnect.
  - **Remote Config** means screens may be flag-gated — design graceful on/off states for flagged features.

## 15. Exercise Formats & Question Architecture

*(Canonical, from Source Doc 3. These are the **only** exercise types; design one question component per type with the states in §9.5. Content in §16 follows these rules.)*

| Exercise type | Allowed structures (IDs) | Formatting rules |
|---------------|--------------------------|------------------|
| **Flashcard** | `CUE_NP`, `CUE_LIMIT`, `CUE_DEF`, `CUE_SCENARIO`, `EMBEDDED_PROMPT` | Retrieval cue, usually ends with `:`. Not a long interrogative. |
| **Multiple Choice** | `WH_OBJ`, `WH_SUBJ`, `WH_ADJUNCT`, `WH_MEASURE`, `YN_*` (rare), `ALT_CHOICE` | Stem ends with `?`; **no** blank token. |
| **Fill-in-the-blank** | `CLOZE_1`, `CLOZE_COND` | Contains exactly one `____`; no `?`. |
| **True / False** | `DECL_FACT`, `DECL_RULE` | Declarative proposition; no `?`, no `____`, no imperative. |
| **Drag-drop** | `INST_ORDER`, `INST_MATCH`, `INST_SORT` | Begins with imperative (Put/Arrange/Order/Match/Sort); ends with `:`. Variants: **order · match · sort**. |

**Design notes:**
- **Scenario** = a *content style* delivered via MCQ or flashcard-cue (`CUE_SCENARIO`), **not** a separate type.
- **Time-limited drill** (Pool-5 immediate-action) = a *countdown wrapper/overlay* on any type — design as a mode, not a new screen.
- Each item carries a **competency tag** (shown on feedback) and a **source reference** (for auditability/trust).

## 16. Design-Ready Sample Content Kit *(starter — expand with validated bank)*

> Realistic, A320-appropriate examples so hi-fi screens look like a real product — **not** lorem ipsum. *(Content is illustrative for design; production content must pass pilot/expert validation, §13.3.)*

**Sample training paths (Release 1 — pick one to feature in mockups):**
- **"Sharp FO — Systems & Abnormals"** — hydraulics, electrical, abnormal config; balances routine traps + rare-critical drills.
- **"Command Prep — Decision & Non-Normals"** — decision-heavy scenarios (fuel leak, diversion, RTO).
- **"Winter Ops Ready"** — seasonal: de-icing, contaminated runway, LVO.

**Sample revision pool (pushed to Flight Plan):**
> **"Hydraulics & abnormal config" · 8 items · ≈ 4 min · Why: next in your path**

**Sample items (one per exercise type — use verbatim in mockups):**

1. **Flashcard** (`CUE_LIMIT`) — Front: *"Maximum operating Mach (MMO):"* · Back: *"M0.82"* · Tag: `KNO` · Src: FCOM LIM.
2. **MCQ** (`WH_MEASURE`) — *"At what differential pressure does the PTU run automatically (green to yellow)?"* · Options: **A** 200 psi · **B** 350 psi · **C** 500 psi · **D** 600 psi · Correct: **C** · Tag: `KNO/PRO` · Feedback: *"The PTU activates on a Δp ≈ 500 psi between green and yellow systems."*
3. **Fill-in-the-blank** (`CLOZE_COND`) — *"In a rejected takeoff, if ground speed exceeds `____` kt, the spoilers extend automatically."* · Answer: *72* · Tag: `PRO` · Src: FCOM.
4. **True / False** (`DECL_RULE`) — *"External power has priority over the APU generator when the EXT PWR pushbutton is ON."* · Answer: **True** · Tag: `KNO`.
5. **Drag-drop / order** (`INST_ORDER`) — *"Put the emergency electrical power supply sequence (loss of main generators) in the correct order:"* · Items to sequence: RAT deploys → EMER GEN online → AC/DC ESS restored → shed non-essential loads · Tag: `PRO/SAW`.

**Sample light-status data (early release — for Flight Plan / Progress mockups):**
- Streak: **🔥 12 days** · Path: **"Sharp FO — Systems & Abnormals" · Week 3 · 62%** · Pools completed this week: **4 / 6** · Due now: **1 pool (8 items)**.

**Cold-start states (day 0 → day 7):**
- **Day 0 (post-onboarding):** no history — Flight Plan shows the assigned path + first pool; status row reads *"Your picture builds as you train."* No radar, no streak yet.
- **Day 1:** streak = 1; path progress ticks; first pool complete shown.
- **Day 7:** streak building; several pools done; path progress bar meaningful. *(Full competency radar still not shown — later phase.)*

**Display data model (early release — the exact values screens show):**
- **Streak:** integer days (or weeks in cadence mode).
- **Path progress:** % complete + week N.
- **Pool:** item count, est. minutes, completion state (not-started / in-progress n·of·N / done).
- **Status semantics** stay per §9.2 (green current · amber due · red overdue) applied to *pools/items*. *(The 0–100 currentness scores + radar thresholds are defined when the engine/dual-currentness ships — deferred with screens #30–34.)*

---

## 17. Prior Work / Reference (context only)

> **Purpose:** a prior working prototype exists. This section mines it for context so the design agents are *better informed* — it is **not** a spec to copy. Agents should design **fresh** toward the best outcome and the current brief's direction; where the prototype conflicts with the brand (§4), the **brief wins**. *(The prototype's operator branding is intentionally omitted here.)*

### 17.1 What exists
A functional prototype — internally *"FL Change / Pilot Academy"* — a **Duolingo-style A320 (and 737) quiz app**. In OnCourse terms, it is essentially the **self-directed "Train" substrate + streaks already built**: Quick Test and Custom Quiz, four working exercise types, streaks, stats, question flagging/reporting. It does **not** yet have the engine-pushed **Flight Plan** (paths + revision pools), the competency-continuity/currentness layer, the RAG pipeline, or the admin review console — those are the net-new OnCourse work.

### 17.2 What it confirms / de-risks (carry forward)
- **Tech stack — validates §14 exactly:** Next.js 14 (App Router, static export) + TypeScript + Tailwind + **Framer Motion** + **Lucide** icons + **Firebase** (Firestore + Auth: Email/Google/Apple) + **Capacitor 6** (iOS), Capacitor Secure Storage/Preferences. The stack is proven, not theoretical.
- **Exercise types — validates §15:** the type union is already `multiple-choice | flashcard | true-false | fill-blank | drag-drop` (all five; drag-drop typed). And `QuizType` already includes `'daily'` and `'course'` — the codebase *anticipated* the daily/path concepts OnCourse formalizes.
- **Question schema — reusable for the revision-pool DB:** `{ id, question, answer, type, options?, explanationsText, explanationsReference, category, domain, topic }`. Note **`explanationsReference`** (e.g. an FCOM/OM-A citation) is exactly the **source-reference/trust signal** §5.10 calls for — already in the model.
- **User/data model — seeds currentness:** `users` carries `streak, lastPracticeDate, totalQuestionsAnswered, correctQuestions[], failedQuestions[], flaggedQuestions[]`. **`failedQuestions[]` is the embryonic weak-area signal.**
- **Existing modes map cleanly:** Quick Test + Custom Quiz (filters incl. **Weak Areas**, reference manual, domain Normal/Abnormal/Systems, exercise-type, count slider, est. time) → OnCourse's **Train** tab. Streak (gauge, auto-reset) → retention loop.
- **Status palette already matches the brief (§9.2):** sky-blue primary, emerald success, amber warning, red error — the brief's status semantics are effectively pre-validated.
- **Font:** DM Sans is already in use → **adopted as primary** (§9.3).

### 17.3 What is SUPERSEDED (do **not** carry forward)
- **Visual theme:** the prototype is **light / cream / sky-blue / gradient / "playful."** OnCourse's locked direction is **dark-first "Modern Glass-Cockpit," restrained "quiet edge"** (§4.4, §9.1). Design to the **brief**, not the prototype's look.
- **Poppins "playful" font** and **XP/lesson-reward gamification** conflict with the restrained-gamification decision (§6.4) — drop/de-emphasize.
- **Name:** the prototype's name is retired → **OnCourse** (§4.7).

### 17.4 Net-new for OnCourse (the real design/build ahead)
Flight Plan (paths + engine-pushed revision pools) · path routing/assignment · competency-continuity + (later) dual-currentness · RAG content pipeline + Admin Review console (§6.7) · the dark quiet-edge redesign of the whole experience · the phased personalization (§5.9).

> **Bottom line for the agents:** reuse the *stack, data model, exercise mechanics, and status palette*; **redesign the look and feel** to the brief; **build** the engine/Flight Plan/paths that the prototype never had.

---

*End of brief v4.3. Name: **OnCourse** (§4.7). Adds §17 Prior Work / Reference (a working prototype on the exact stack — reuse its stack/data-model/exercise mechanics/palette; supersede its light-playful look with the dark quiet-edge direction; DM Sans adopted as primary font). The four previously-open items are now resolved from founder input: **content sourcing & pilot-review model** (§5.10, §6.7 — official manufacturer source, RAG-generated, every question human-reviewed by pilots via an Admin console; licensed sources as it scales); **data privacy** (§14 — weakness data private to the pilot; airlines never see individual data; B2B aggregated-only); **gamification** (§6.4 — restrained; daily-completion streaks, no points marketplace); **name clearance** (§4.7 — researched: usable but an education-class collision exists; attorney check + distinguishing store name recommended). Pricing free-first (§4.10). Integrates all four source documents. Residual to-dos (execution, not design blockers): trademark-attorney review + final content-license path as the product scales. The brief is ready to hand to Brand, UX Research, UI Design, and Figma-generation agents — first Figma batch = the **V1/V2 core loop** (onboarding → path assignment → Flight Plan/Hero Tile → revision pool → session + feedback → light Progress), all **unlocked/free**, per §11.*
