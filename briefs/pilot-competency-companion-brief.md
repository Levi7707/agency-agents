# Project Brief v2 — "Crosscheck": The Pilot Competency-Continuity & Career Companion

> **Document type:** Master project brief (business strategy → method → product → UI/UX)
> **Working product name:** **Crosscheck** *(placeholder — see §3.4)*
> **Status:** Draft v2.0 — integrates the two authoritative source documents (see below)
> **Date:** 2026-06-29
> **Primary purpose:** The single source of truth and deep-context reference for AI design agents generating high-fidelity UI/UX screens in Figma. A downstream agent should be able to read *this brief alone* and understand the full picture — strategy, the underlying training method, the complete feature system, information architecture, screens, and visual language.

> **Canonical source documents this brief integrates (authoritative — defer to them on mechanics):**
> 1. **Product Functionality Specification** — the full feature system (onboarding, learning engine, home, retention psychology, privacy/trust, accessibility, content taxonomy).
> 2. **Competency Continuity Method (v3)** — the scientific/operational method: Operational Training Units (OTUs), EBT double-entry currentness, exposure model, recurrence pools, scoring, training-pattern generation, currentness engine.
> Where this brief and a source document differ on *product mechanics*, the source document wins. This brief adds the strategy, positioning, IA, and visual/design specification on top.

> **Key product decisions locked for v2:**
> - **Scope:** MVP = the competency-continuity training engine. "Career companion" extras (documents, expiry, logbook, career prep) are **later phases**, not MVP.
> - **Aircraft:** **A320 short-haul content**, but the UI is designed as a **type-agnostic shell** that visibly generalizes to other types later.
> - **Method visibility:** **Operational/simple UI.** Pilots see concrete *actions* ("fuel leak", "de-icing") and the *9-competency* view. The method's internal machinery (OTUs, exposure categories, recurrence pools, scoring) stays **backend** — never shown as jargon.
> - **First Figma batch:** the **core loop** (see §11).

> **How to read this brief:**
> - **§1–§4** = the *why* (problem, market, strategy). Context.
> - **§5** = the *method* (the core mechanic every screen ultimately serves). Essential.
> - **§6** = the *full feature system* (what exists in the product).
> - **§7–§11** = the *how it looks and works* — the actionable design specification. Treat §8 (Screens) and §9 (Design System) as build instructions.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Problem & Why This Exists](#2-the-problem--why-this-exists)
3. [Market & Competitive Landscape](#3-market--competitive-landscape)
4. [Strategic Positioning & Business Model](#4-strategic-positioning--business-model)
5. [The Core Mechanic — Competency Continuity Method](#5-the-core-mechanic--competency-continuity-method)
6. [The Full Feature System](#6-the-full-feature-system)
7. [Users, Personas & Journeys](#7-users-personas--journeys)
8. [Information Architecture & Screen Inventory](#8-information-architecture--screen-inventory)
9. [Design System & Visual Language](#9-design-system--visual-language)
10. [Interaction, Adaptive UI, States & Accessibility](#10-interaction-adaptive-ui-states--accessibility)
11. [Figma Generation Handoff Notes](#11-figma-generation-handoff-notes)
12. [Content Taxonomy (A320)](#12-content-taxonomy-a320)
13. [Roadmap, Metrics & Risks](#13-roadmap-metrics--risks)

---

## 1. Executive Summary

### 1.1 The one-paragraph pitch

**Crosscheck** keeps professional pilots *competent between checks*, not just *current on paper*. Line flying naturally rehearses some actions every sector (cockpit prep, briefings, approaches) while leaving rare-critical ones dormant for months (engine failure after V1, fuel leak, windshear escape, evacuation). Crosscheck closes that **exposure gap** with short, spaced, scenario-based micro-training — scheduled by a method built on Evidence-Based Training (EBT) competencies and memory science. It learns each pilot's weak spots, schedules the right retrieval at the right time, and shows two honest readiness pictures: *which actions you're rusty on* and *which underlying competencies are slipping*. It is a pilot's private "personal training department in their pocket." Over time it grows into a full career companion (documents, logbook, career prep), but the MVP is the training engine.

### 1.2 The core insight (drives every design decision)

The whole competitor market *logs the past* (LogTen, ForeFlight, CrewLounge — hours, currency, endorsements). Crosscheck answers the forward-looking question pilots actually lose sleep over: **"Am I still sharp on the things I almost never do — and where am I weak?"**

It does this with a real method (the **Competency Continuity Method**, §5): not a generic question bank, but training generated from **mapped operational actions/events**, scheduled by **how often line flying, the sim, and recurrent training already refresh each one**, and graded against the **9 EBT competencies**.

> **Design implication:** Crosscheck is a **readiness & coaching** product — closer to a beautifully-made adaptive learning app (Duolingo-class daily habit) crossed with a flight-training mindset — **not** a logbook or a spreadsheet. If a Figma frame looks like data entry, it's wrong.

### 1.3 The critical disclaimer (must be respected in UI copy)

Per the source method: Crosscheck is a **competency-continuity and cognitive-reinforcement layer between approved recurrent training events.** It does **not** replace an operator's approved training programme, manuals, SOPs, regulatory training, simulator checking, or instructor-led assessment. The UI must never imply formal qualification, certification, or regulatory currentness. *(See §13 risk table — content credibility is the #1 risk.)*

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

**Crosscheck occupies the empty intersection:** the *competency framework* of airline EBT systems + the *spaced retrieval* of study apps, delivered as a *consumer-grade, career-long, personally-owned* app — which does not exist today for the individual pilot.

### 3.2 Competitive snapshot

| Competitor | Strength | Price (~2025) | Why Crosscheck wins |
|------------|----------|---------------|---------------------|
| **LogTen Pro** | Logging accuracy, 120k+ pilots, airline-trusted | $80–130/yr | We don't compete on logging; we own *continuity & competency* |
| **ForeFlight Logbook** | Bundled with dominant EFB | Bundled $130–390/yr | Locked to ForeFlight; ours is standalone, focused, affordable |
| **CrewLounge / PILOTLOG** | Cheap, roster sync, compliant reports | ~$34/yr | Classic logbook, dated UX; we win on forward-looking value + design |

> **Design implication:** The visual bar in this category is **low** — competitors look like database front-ends. A genuinely beautiful, modern mobile experience is itself a moat. Output should belong next to the best fintech/health apps of 2026.

**Sources:** [Aviatize — Best Pilot Logbook Apps](https://www.aviatize.com/blog/best-pilot-logbook-apps-2026) · [Axis Intelligence — 23 apps tested](https://axis-intelligence.com/best-pilot-logbook-apps-2025-tested/) · [Aviatize — EBT glossary](https://www.aviatize.com/glossary/ebt) · [MCC-APS — The 9 EASA competencies](https://mcc-aps.com/en/9-easa-pilot-competencies/) · [Airbus — Is CBTA the future?](https://www.aircraft.airbus.com/en/newsroom/stories/2024-12-is-cbta-the-future-of-pilot-training-airbus-head-of-pedagogy-standards) · [Flight Safety Foundation — Moving beyond traditional training](https://flightsafety.org/asw-article/moving-beyond-traditional-training/)

---

## 4. Strategic Positioning & Business Model

### 4.1 Positioning statement

> **For** professional pilots **who** worry about staying sharp on rare-critical actions and being ready for their next check, **Crosscheck is** a personal competency-continuity companion **that** schedules short, science-based retrieval of exactly the actions line flying leaves dormant, graded against the EBT competencies airlines use — **unlike** logbook apps that only record the past, **Crosscheck** is forward-looking, method-driven, and operationally real.

### 4.2 Brand personality

| Trait | Design meaning |
|-------|----------------|
| **Professional & credible** | Serious tool for aviators. No clip-art planes. Precision, trust, correct terminology. |
| **Calm under pressure** | Uncluttered, confident, never alarmist — even when flagging a weak area. |
| **Coaching, not nagging** | "Your KNO profile is slipping — today we'll run a fuel-leak scenario." Never "Train KNO." Always a path forward. |
| **Precise** | Exact numbers, dates, statuses. Tabular figures. Pilots live by precision. |

**Voice:** concise, confident, plain-language, aviation-literate, encouraging without being saccharine.

### 4.3 Business model (proposal — not in source docs; confirm)

**Freemium + single paid "Pro" tier.** Freemium maximizes top-of-funnel in a trust-sensitive niche and seeds the future B2B trojan horse (pilots already using it when we sell to their airline). One Pro tier avoids confusing pricing. One-time purchase rejected — value is ongoing (continuous retrieval), so recurring revenue matches recurring value and funds content/QA (the credibility moat).

| Tier | Price (proposed) | Includes |
|------|------------------|----------|
| **Free** | $0 | Limited daily retrieval, basic action-currentness view, view-only competency snapshot |
| **Pro** | ~$6–9/mo · ~$59–79/yr | Unlimited retrieval, full dual-currentness analytics, AI curator programs, micro-quiz everywhere, offline vault, advanced gamification |
| **(Future) Teams/ATO** | Per-seat B2B | Fleet currentness dashboards, instructor assignment, validation/governance, compliance-aware export |

> Priced below LogTen/ForeFlight to signal "complement, not replacement" and lower trial friction. **Design implication:** paywall screens must sell *value* (the analytics, the AI curator, the offline vault) — never a bare feature checklist.

### 4.4 Naming

Lead: **Crosscheck** (real cockpit term — verification, scanning for what's off, readiness). Alternatives: **Ready Room, Brief, Sharp, Proficient, Currentness, The Loop.** Brief uses "Crosscheck" throughout.

### 4.5 Go-to-market (summary)

Beachhead: **A320 first officers & cadets in/after type rating** — highest anxiety about knowledge decay and the next sim, most digitally native, tight word-of-mouth cohorts. Channels: pilot communities (r/flying, Discords, forums), flight-school/type-rating partnerships, aviation influencers, ATO referrals. Hook: *"Walk into your next sim knowing you're ready — even on the things you never see on the line."*

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

> **Design implication:** Crosscheck needs **two complementary readiness views** — an **Action Currentness** view (operational, the one pilots live in: a list/map of actions with due status) and a **Competency Currentness** view (the 9-competency radar/analytics). My v1 "competency radar" was only the second; the first is equally important and arguably more prominent for pilots.

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
- *Exception:* an optional power-user/advanced reveal is **out of scope for v2** (we chose operational/simple).

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
- **Contextual Smart Notifications:** opt-in, low-frequency, only in allowed windows; deep-link to a one-tap session (same engine as the Hero Tile) with a "why" + easy mute/snooze.
- **Training Streak:** two modes — **Daily** (1 qualifying action/day) and **Cadence** (pilot-optimized: e.g. 4 sessions/week → counts consecutive weeks hitting target). Pilot schedules vary, so cadence matters.
- **Streak Guard (Freezes)** + **Streak Guard Marketplace:** spend earned points or pre-schedule a vacation to protect a streak (points-sink for the gamification currency).
- **Relative Leaderboards:** compare to ~10 peers, not millions (winnable).
- **Collaborative Quests:** features requiring a partner (social accountability).
- **Value Realization Screens:** weekly "time/knowledge gained" reports (reason to pay).
- **Verifiable Milestones:** shareable, verification-backed mastery badges (e.g. "A320 Bleed Air") — granted only on **sustained retention (SRS) + performance (accuracy + coverage)**, not on content completion. Links to a public verification page (scope/criteria/date) trustable by peers or training orgs.

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

> **Primary build spec for Figma.** Mobile-first, **iOS primary** (390×844 / iPhone reference; Android parity via Material adaptation). **Dark-first** (§9). Operational/simple language (§5.8). A320 content, type-agnostic shell. **Batch-1 (core loop) screens are marked ⭐.**

### 8.1 Navigation model — bottom tabs + center action

| Tab | Icon idea | Purpose |
|-----|-----------|---------|
| **Home** ⭐ | gauge / target | Predictive Hero Tile, today's best action, currentness + streak summary |
| **Review** ⭐ | refresh / cards | SRS due-items queue (the spaced-repetition engine) |
| **Train** ⭐ | brain / sliders | Quick Test, Custom Quiz, Natural-Language Search, Low-Load toggle, topic library |
| **Readiness** ⭐ | radar / list | Dual currentness: Action list + 9-competency view; next-check context |
| **Profile** | pilot / wings | Stats, streak, milestones, skill tree, settings, AI & Trust, subscription |
| **Center FAB** ⭐ | "+" → *Start best session* | One-tap into the Hero Tile's recommended session from anywhere |

> Reserve clearly-labeled "Coming soon" rows in Profile for the future career-companion pillars (Documents, Logbook, Career) so the growth path is visible without cluttering MVP.

### 8.2 Screen inventory

**Onboarding & identity** ⭐
1. ⭐ Splash / brand (logo, tagline: "Stay sharp between checks.")
2. ⭐ Zero-login welcome (start instantly; passkey/email offered later)
3. ⭐ Predictive Intent Quiz — 3 visual cards (limitations / memory items / systems / performance…)
4. ⭐ Play-First Tutorial — one sample per exercise type (flashcard, cloze, scenario), each a different subject
5. ⭐ Dynamic Goal Setting — commitment level (e.g. 1 min/day · 4×/week · intensive)
6. ⭐ First-Session Choice — Explore / Quick Start / Build My Own Path
7. ⭐ Passkey / account creation (offered *after* first value)

**Home** ⭐
8. ⭐ **Home / Predictive Hero Tile** — see §8.3 (the most important screen)
9. ⭐ Hero Tile "Why?" sheet — plain-language reason + **Change** (override to pick another session)
10. Social Activity Ticker (compact, on Home)

**The session (learning engine)** ⭐
11. ⭐ Question — **Flashcard** (recall, flip)
12. ⭐ Question — **Cloze / fill-in-the-blank**
13. ⭐ Question — **MCQ**
14. ⭐ Question — **Scenario / decision** (e.g. "WINDSHEAR after rotation — immediate priority?")
15. ⭐ Question — **Ordering / sequencing** (e.g. memory-item steps)
16. ⭐ Question — **Time-limited drill** (Pool 5 immediate-action; visible countdown)
17. ⭐ Feedback screen — correct/incorrect + crisp explanation + competency tag + source-reference link
18. ⭐ **SRS rating** control — Again / Hard / Good / Easy (on review items)
19. ⭐ Session summary — score, streak ++, what improved, which actions/competencies were refreshed

**Review (SRS)** ⭐
20. ⭐ **Review tab home** — due-items queue, count + est. time ("8 due ≈ 2 min"), start
21. ⭐ Review in-progress (same question components, SRS framing)

**Train** ⭐
22. ⭐ Train home — Quick Test · Custom Quiz · search entry · Low-Load (Cognitive Load Ceiling) toggle
23. ⭐ **Natural-Language Search** — free-text → auto-built quiz preview ("PTU logic → 8 Q")
24. ⭐ Quick Test setup (adaptive on; or manual difficulty fallback)
25. Custom Quiz / Build My Own Path (subject, system, count)
26. Topic library — browse taxonomy (§12), filtered to A320
27. Micro-quiz interrupt — in-app overlay variant + notification/Dynamic Island/widget mockups (3 question intents §6.2)

**Readiness — dual currentness** ⭐ *(the differentiator)*
28. ⭐ **Action Currentness** — operational list/map of actions/events with status (current/due/overdue), sorted by urgency; tap → detail
29. ⭐ Action detail — one action (e.g. "Fuel leak in cruise"): status, last reviewed, next due, **Why?**, "Drill now"
30. ⭐ **Competency Currentness** — 9-competency radar; weak competencies called out
31. ⭐ Single competency detail (e.g. KNO) — trend, linked actions that are weak, recommended drills
32. Next-check context — optional date of next recurrent/sim; surfaces a pre-check focus list

**Retention / gamification**
33. Streak screen — daily vs cadence mode, calendar, freezes
34. Streak Guard Marketplace — spend points / schedule vacation
35. Relative Leaderboard (~10 peers)
36. Collaborative Quest (partner)
37. Milestones / verifiable badges — earned + verification page mock
38. Progressive Investment Tracker — skill tree / knowledge map
39. Value Realization — weekly report

**Profile, trust & system**
40. Profile home — identity, aircraft chip (A320), stats, streak, milestones, skill-tree entry
41. Stats / progress — currentness over time, competency history, consistency
42. **AI & Trust Hub** — AI on/off, signals used, privacy boundaries, reset; reachable from every Why?
43. Settings — auth/passkey, aircraft, notifications + windows, theme (incl. Pure Black / High Contrast), haptics, Eco-Mode, Focus Mode, Incognito Pause, Privacy Zones, State-Persistence/devices
44. Training Preferences — Learning Style Profile (formats + explanation depth)
45. Subscription / paywall — Free vs Pro, value-led (§4.3)
46. Offline Vault — downloaded content manager
47. "Coming soon" / roadmap teaser — Documents · Logbook · Career

**Global states** (design as variants, not separate flows) ⭐
48. ⭐ Empty (no due items: "You're current — nice."; no goal set), Loading (skeletons; radar/gauge shimmer-in), Error, **Offline** (calm chip; daily loop still works from vault), Success/celebration (streak milestone, "all current" state, badge earned), **Low-Load mode** active variant.

### 8.3 Home / Predictive Hero Tile — detailed spec (most important screen) ⭐

Top → bottom, answer in one glance: *what do I do right now, am I ready, where am I weak.*

1. **Greeting + identity strip** — "Good morning, Maya" · aircraft chip (A320) · streak (🔥 12).
2. **Predictive Hero Tile (hero):** the single best next session, large and tappable:
   - Title: the concrete action/session ("Drill: Windshear escape" / "Review 8 due items").
   - Time budget ("≈ 2 min") and progress if resuming.
   - Plain **Why** label ("due items" / "weak topic: PSD" / "your priority") + **Change** (override).
   - Primary CTA button: **Start**.
3. **Dual-currentness summary band** — two compact, tappable cards side by side:
   - **Action readiness** — e.g. "3 actions due" with a mini status bar (green/amber/red) → Action Currentness (#28).
   - **Competency snapshot** — the 9-spoke radar in compact form, 1–2 weak spokes flagged → Competency Currentness (#30).
4. **Micro-quiz nudge** (optional) — "Got 15 seconds? Quick check." → micro-quiz overlay.
5. **Secondary row** — streak/stats chip, skill-tree progress, social ticker, (reserved) "Coming soon".

> If a viewer can't tell within 3 seconds this is a **forward-looking readiness/training** app — and can't see *both* "what to do now" and "how ready am I" — the design missed the brief.

---

## 9. Design System & Visual Language

### 9.1 Direction: **"Modern Glass-Cockpit"** (dark-first) — recommended & spec-aligned

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
- **Primary:** clean precise grotesque — **Inter** (recommended) or **SF Pro** on iOS. Optional technical display face for big numbers.
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
2. **Frame:** iPhone 390×844, iOS-primary; **dark is the hero**. Provide light + Pure-Black variants of at least Home, a question screen, and the competency radar.
3. **Batch 1 = the core loop (⭐ screens).** Prioritize, in order:
   1. Onboarding (zero-login → intent quiz → play-first tutorial → goal → first-session choice)
   2. **Home / Predictive Hero Tile** (§8.3) + Why? sheet
   3. Session: at least flashcard, MCQ, scenario, time-limited drill + feedback + SRS rating + summary
   4. **Review tab** (SRS due queue)
   5. **Dual currentness:** Action Currentness list + Action detail, and Competency radar + single-competency detail
   6. Train home + Natural-Language Search → auto-quiz
   *(Gamification, trust/privacy, and adaptive screens are later batches.)*
4. **Operational/simple language (§5.8):** show concrete actions ("Fuel leak in cruise", "De-icing") + the 9 competencies. **Never** surface OTU IDs, exposure categories (EC1–6), or pool numbers as user-facing text.
5. **A320 + type-agnostic shell:** use realistic A320 content from §12; design the structure so type selection/other aircraft obviously slot in later (e.g. the aircraft chip, taxonomy filters).
6. **Honor the positioning everywhere:** forward-looking, coaching, calm, precise. Two readiness truths (action + competency) must be reachable. No logbook/data-entry aesthetics.
7. **Status colors are global (§9.2):** green=current/strong, amber=due/attention, red=overdue/weak/critical.
8. **Respect the disclaimer (§1.3):** no copy implying formal qualification/certification/regulatory currentness. Use plausible-but-generic content; never invent regulations or present unverified procedures as authoritative.
9. **Accessibility variants:** include a Pure-Black/high-contrast pass and ensure status is never color-only.

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

### 13.1 Roadmap (product method × business)

| Phase | Theme | Scope |
|-------|-------|-------|
| **0 — Now** | This brief → Figma hi-fi (core loop) | Strategy + method + full UX/UI spec → batch-1 screens |
| **1 — MVP** | The training engine | Onboarding · learning engine (SRS/adaptive/micro-quiz/NL search/AI curator) · dual currentness · Home/Hero Tile · core gamification · privacy/trust · adaptive accessibility · **A320 content** |
| **1.x** | Method completion | Exposure/pool scoring assistant (method Automation 3), exercise templates per pool, scheduler/currentness engine at scale, pilot-validation/governance |
| **2.x** | Career companion | Documents & expiry vault · currency tracking · digital logbook · expanded AI assistant · career prep |
| **3.x** | Scale | B2B/ATO currentness dashboards · instructor assignment · fleet analytics · compliance-aware export |

*(The source method's own phases — mapping, competency tagging (Automations 1–2 built), exposure scoring (to build), exercise design, scheduler, validation — live inside Phases 1–1.x.)*

### 13.2 Success metrics (MVP, directional)

| Metric | Why | Target |
|--------|-----|--------|
| D7 / D30 retention | Daily-habit product lives or dies here | D30 ≥ 25% |
| Daily session completion | Core loop engagement | ≥ 40% MAU practice ≥3×/wk |
| Rare-critical action currentness improvement | Validates the *core promise* (closing the exposure gap) | Measurable lift on EC4–EC6 items |
| Pre-check engagement | Validates the differentiator | ≥ 60% of users with a check date open currentness before it |
| Weak-area drill follow-through | Validates the coaching value | ≥ 30% act on a surfaced weak action/competency |
| Free→Pro conversion | Viability | 4–8% |

### 13.3 Key risks & mitigations

| Risk | L | I | Mitigation |
|------|---|---|------------|
| **Content credibility** — pilots are unforgiving of wrong/dated content | High | High | Source from validated bank only (no AI invention); keep source references per OTU; **mandatory pilot/expert validation**; store confidence + separate inferred vs pilot-scored; user flagging; clear disclaimers (§1.3) |
| **"Just another logbook" perception** | Med | High | Relentlessly forward-looking UX; lead with currentness; logbook deferred to Phase 2 |
| **Method credibility / over-claiming** | Med | High | Position as a *continuity layer between approved events*; never imply certification/regulatory currentness; auditable "why" |
| **Scheduling accuracy** (intervals are approximations, not validated law) | Med | Med | Make pools/intervals auditable & adjustable; pilot validation; periodic review vs feedback/fleet data |
| **Engagement decay** (knowledge apps fade) | Med | High | Tie retrieval to *real rare-critical risk* + cadence streaks + adaptive relevance to the pilot's exposure profile |
| **Cross-jurisdiction / multi-type complexity** | High | Med | A320-first + type-agnostic shell; ICAO/EASA 9-competency universal core; jurisdiction as config later |
| **Data sensitivity / trust** | Med | High | Privacy-first (Privacy Zones, Incognito Pause, Offline Vault), AI Trust Hub, clear data ownership; vault secure by design |

---

*End of brief v2.0. Integrates the Product Functionality Specification and the Competency Continuity Method (v3). Open proposals to confirm: product name, exact pricing, and content-sourcing/validation plan (the #1 risk). Ready to hand to UX Research, UI Design, and Figma-generation agents — starting with the Batch-1 core-loop screens (§11).*
