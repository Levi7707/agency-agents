# DNS Audit — readyfortakeoffbook.com
**Audit date:** 2026-06-08
**DNS host:** Google Domains (ns-cloud-a1/a2/a3/a4.googledomains.com) — NOT Shopify DNS
**Method:** Live DNS resolution via Python dnspython (system DNS + Google Public DNS) + Shopify MCP attempted

---

## Note on Shopify MCP Access

All Shopify MCP tools (`get-shop-info`, `graphql_schema`, `graphql_query`) returned **permission denied** during this audit. The Shopify Admin API data (emailDomain, domain configuration, SSL status) could not be retrieved via MCP. All findings below are based exclusively on **live DNS lookups** performed directly against authoritative nameservers.

---

## 1. Store Domain Configuration (from Shopify API)

**Shopify MCP tools:** PERMISSION DENIED — could not query `shop.primaryDomain`, `emailDomain`, or domain settings.

**Inferred from DNS (confirmed):**
- `readyfortakeoffbook.com` A record resolves to `23.227.38.72` → reverse DNS: `myshopify.com` (confirmed Shopify infrastructure)
- `www.readyfortakeoffbook.com` CNAME → `shops.myshopify.com.` (Shopify standard www redirect)
- The domain is actively serving a Shopify store
- **IMPORTANT: DNS is managed via Google Domains (Google Cloud DNS), NOT Shopify's own nameservers.** This means DNS records must be added in Google Domains admin panel, not Shopify Admin.

---

## 2. Live DNS Records Found

### NS Records (Nameservers)

| Nameserver |
|---|
| ns-cloud-a1.googledomains.com. |
| ns-cloud-a2.googledomains.com. |
| ns-cloud-a3.googledomains.com. |
| ns-cloud-a4.googledomains.com. |

**Assessment:** Google Domains / Google Cloud DNS is the authoritative DNS provider. DNS changes must be made at [domains.google.com](https://domains.google.com) or Google Cloud DNS console — **not** in Shopify Admin.

---

### A Records

| Host | IP Address | Reverse DNS |
|---|---|---|
| readyfortakeoffbook.com | 23.227.38.72 | myshopify.com |
| www.readyfortakeoffbook.com | 23.227.38.74 | shops.myshopify.com |

**Assessment:** Both root and www correctly point to Shopify infrastructure. PASS.

---

### AAAA Records (IPv6)

| Host | Address |
|---|---|
| readyfortakeoffbook.com | 2620:127:f00f:c:: |

**Assessment:** IPv6 address present and resolves to Shopify IPv6 range. PASS.

---

### CNAME Records

| Subdomain | Points To |
|---|---|
| www | shops.myshopify.com. |

---

### MX Records (Email Routing)

| Priority | Mail Server | Resolved IP | Reverse DNS |
|---|---|---|---|
| 1 | mx.readyfortakeoffbook.com.cust.b.hostedemail.com. | 64.98.38.4 | mx.b.hostedemail.com |

**Assessment:** Email is routed through **Rackspace Hosted Email** (hostedemail.com / cust.b.hostedemail.com). This is the inbound mail handler. Only one MX record with priority 1 — no backup MX configured.

---

### TXT Records (all)

| Record | Value |
|---|---|
| readyfortakeoffbook.com | `"brevo-code:15977df608ca51d8ff239bfffe52a150"` |

**Only one TXT record exists.** This is a **Brevo (formerly Sendinblue) domain verification token** — confirming that Brevo has been connected to this domain as an email sending platform. However, the Brevo integration is **incomplete** — no SPF or DKIM records for Brevo are present.

---

### SPF Record

**Status:** MISSING — CRITICAL

**Value:** No `v=spf1` TXT record exists for `readyfortakeoffbook.com`

**Assessment:** FAIL

**Issues:**
1. No SPF record whatsoever. Any email sent from this domain (via Brevo, Shopify Email, Rackspace, or any other service) has no authorized sender list.
2. Receiving mail servers cannot validate which services are permitted to send on behalf of `readyfortakeoffbook.com`.
3. Emails are highly likely to land in spam or be rejected outright by strict receivers.
4. Brevo domain verification token (`brevo-code:`) is present, confirming Brevo is intended for sending, but SPF has not been configured to authorize Brevo's sending IPs.
5. Rackspace Hosted Email (inbound MX) may also send outbound mail — no SPF authorization for Rackspace exists.

---

### DKIM Records

**Status:** MISSING — CRITICAL

**Selectors checked (all returned NXDOMAIN — record does not exist):**

| Selector | Result |
|---|---|
| default._domainkey | NOT FOUND |
| mail._domainkey | NOT FOUND |
| k1._domainkey | NOT FOUND |
| avada._domainkey | NOT FOUND |
| shopify._domainkey | NOT FOUND |
| s1._domainkey | NOT FOUND |
| s2._domainkey | NOT FOUND |
| google._domainkey | NOT FOUND |
| sendgrid._domainkey | NOT FOUND |
| mailchimp._domainkey | NOT FOUND |
| klaviyo._domainkey | NOT FOUND |
| brevo._domainkey | NOT FOUND |
| smtp._domainkey | NOT FOUND |
| brevo1._domainkey | NOT FOUND |
| brevo2._domainkey | NOT FOUND |
| sendinblue._domainkey | NOT FOUND |
| mail1._domainkey | NOT FOUND |
| mail2._domainkey | NOT FOUND |
| dkim._domainkey | NOT FOUND |
| rackspace._domainkey | NOT FOUND |
| rs._domainkey | NOT FOUND |
| mxv1._domainkey | NOT FOUND |
| mxv2._domainkey | NOT FOUND |

**Assessment:** FAIL

**Issues:**
1. Zero DKIM records exist for any sending service.
2. Brevo is verified (domain ownership token present) but DKIM signing is not configured — Brevo emails will not be DKIM-signed with this domain's key.
3. Shopify Email DKIM selectors (s1/s2) are absent — Shopify transactional emails (order confirmations, shipping notifications) are not DKIM-authenticated.
4. No Rackspace DKIM selector — inbound/outbound mail via Rackspace is not DKIM-signed.
5. Without DKIM, emails cannot be verified as genuinely originating from authorized infrastructure, severely impacting deliverability and spam classification.

---

### DMARC Record

**Status:** MISCONFIGURED — Present but non-enforcing and incomplete

**Value:** `"v=DMARC1; p=none"`

**Policy:** `none` (monitor only — no action taken on failures)

**Reporting:** MISSING — No `rua=` (aggregate report URI) and no `ruf=` (forensic report URI) are configured

**Assessment:** WARNING

**Issues:**
1. `p=none` means DMARC is in monitoring mode only — failing messages are **not quarantined or rejected**. This provides zero protection against spoofing.
2. No `rua=` tag means DMARC aggregate reports are never sent — the domain owner receives no visibility into who is sending mail as `readyfortakeoffbook.com` or what is passing/failing.
3. No `ruf=` tag means no forensic/failure reports are generated.
4. With SPF and DKIM both missing, DMARC alignment checks will **always fail** — but because `p=none`, there is no enforcement consequence.
5. The DMARC record itself is syntactically valid but functionally useless without SPF and DKIM alignment to back it up.
6. Without `rua=` reports, it is impossible to safely escalate to `p=quarantine` or `p=reject` because there is no data on what legitimate senders would be affected.

---

### BIMI Record

**Status:** NOT CONFIGURED

`default._bimi.readyfortakeoffbook.com` → NXDOMAIN

BIMI requires DMARC at `p=quarantine` or `p=reject` as a prerequisite — not applicable until DMARC is enforced.

---

## 3. Shopify Email Authentication (from API)

**Status:** COULD NOT QUERY — Shopify MCP tools returned permission denied for all calls including `graphql_query`, `get-shop-info`, and `graphql_schema`.

**Inferred from DNS:**
- No Shopify Email DKIM records (s1/s2 selectors) are present → Shopify transactional emails are not sending with custom domain DKIM authentication
- This means Shopify sends order confirmations and shipping notifications via Shopify's shared domain rather than authenticated as `readyfortakeoffbook.com`
- The domain owner should configure Shopify Email authentication in: **Shopify Admin → Settings → Notifications → Sender email** and follow the DKIM setup prompts

**Brevo (email marketing platform — confirmed by TXT token):**
- Domain ownership verified via `brevo-code:15977df608ca51d8ff239bfffe52a150`
- SPF authorization for Brevo: NOT CONFIGURED
- DKIM for Brevo: NOT CONFIGURED
- Brevo campaigns sent from `@readyfortakeoffbook.com` are currently unauthenticated

---

## 4. Audit Verdict

| Record | Status | Priority | Risk |
|---|---|---|---|
| SPF | MISSING | P0 — Critical | Emails rejected/spam-flagged by strict receivers; no authorized sender list |
| DKIM | MISSING (all selectors) | P0 — Critical | Emails cannot be cryptographically verified; high spam score |
| DMARC | Present but non-enforcing (`p=none`); no `rua=` reporting | P1 — High | Domain spoofable; no visibility into authentication failures |
| MX | Present (Rackspace Hosted Email) | PASS | Inbound mail routing functional; no backup MX |
| A / CNAME | Present (Shopify IPs) | PASS | Website routing correct |
| SSL | Not queryable via MCP | Unknown — assumed OK given Shopify hosting |
| Brevo DKIM | MISSING despite domain verification | P0 — Critical | Marketing emails are unauthenticated |
| Shopify Email DKIM | MISSING | P0 — Critical | Transactional emails unauthenticated |

**Overall email deliverability risk:** HIGH

**Summary:** This domain has a Brevo domain ownership token and a non-enforcing DMARC record, but is missing the two foundational email authentication records — SPF and DKIM. Every email sent from this domain (transactional, marketing, manual) is currently unauthenticated. Gmail, Yahoo, and other major providers apply aggressive spam filtering to unauthenticated senders. Since February 2024, Google and Yahoo require SPF/DKIM for bulk senders; failure to comply results in deferrals or outright rejection.

---

## 5. Remediation Plan (prioritized)

### P0 — Do Before Next Email Send

These must be in place before sending any marketing campaigns or expecting transactional emails to reach inboxes.

1. **Add SPF TXT record** — authorize all email sending services (Brevo + Rackspace + Shopify)
2. **Configure Brevo DKIM** — complete the DKIM setup in Brevo dashboard to get the selector/value, then add the DNS record
3. **Configure Shopify Email DKIM** — go to Shopify Admin → Settings → Notifications → configure sender domain authentication
4. **Add `rua=` to DMARC** — add a reporting email address so you can monitor authentication results before escalating policy

### P1 — Do This Week

5. **Add backup MX record** — Rackspace typically provides a secondary MX; configure it to prevent mail loss during primary MX outages
6. **Escalate DMARC to `p=quarantine`** — after 1–2 weeks of monitoring aggregate reports confirming all legitimate mail passes SPF+DKIM alignment
7. **Verify Rackspace DKIM** — log into Rackspace Email admin panel and complete DKIM setup for the hosted email domain

### P2 — Do This Month

8. **Escalate DMARC to `p=reject`** — after confirming no legitimate mail is failing; this is the gold standard for spoofing protection
9. **Add DMARC forensic reporting (`ruf=`)** — enables per-message failure reports
10. **Consider BIMI** — once DMARC `p=reject` is in place, add a BIMI record with a verified logo for brand display in Gmail/Yahoo
11. **DNS host migration assessment** — evaluate whether consolidating DNS to Shopify nameservers simplifies management (currently split: Google Domains manages DNS, Shopify hosts the store)

---

## 6. Exact DNS Records to Add

### IMPORTANT: Where to Add These Records

DNS is managed by **Google Domains / Google Cloud DNS**, NOT Shopify Admin.
Go to: **Google Domains → [readyfortakeoffbook.com] → DNS → Manage custom records**
Or: **Google Cloud Console → Cloud DNS → readyfortakeoffbook.com zone → Add record set**

---

### Record 1 — SPF (Authorize all sending services)

**Record type:** TXT
**Host/Name:** `@` (or leave blank for root domain)
**Value:** `v=spf1 include:spf.brevo.com include:_spf.hostedemail.com include:shops.myshopify.com ~all`
**TTL:** 3600
**Notes:** This SPF record authorizes:
- `spf.brevo.com` — Brevo email marketing sends
- `_spf.hostedemail.com` — Rackspace Hosted Email (inbound/outbound)
- `shops.myshopify.com` — Shopify transactional emails
- `~all` = softfail for unauthorized senders (use `-all` once verified to work)

**VERIFY BEFORE ADDING:** Confirm the exact Brevo SPF include by checking Brevo's current documentation at app.brevo.com → Settings → Senders & IP → Domains. Confirm Rackspace SPF include in your Rackspace Email admin panel under domain authentication settings.

---

### Record 2 — DKIM for Brevo

You must first retrieve the DKIM selector and public key from Brevo:
1. Log into [app.brevo.com](https://app.brevo.com)
2. Go to **Settings → Senders & IP → Domains**
3. Click on `readyfortakeoffbook.com`
4. Find the **DKIM** section — it will show a selector name (typically `mail`) and a TXT value

Then add:

**Record type:** TXT
**Host/Name:** `[selector]._domainkey` (e.g., `mail._domainkey`)
**Value:** `v=DKIM1; k=rsa; p=[public_key_from_brevo]`
**TTL:** 3600

---

### Record 3 — DKIM for Shopify Email

1. Go to **Shopify Admin → Settings → Notifications**
2. Find the sender email / domain authentication section
3. Shopify will provide two CNAME records (s1 and s2 selectors) to add

Typical format:
**Record type:** CNAME
**Host/Name:** `s1._domainkey`
**Value:** `s1.domainkey.shopify.com.` (confirm exact value from Shopify Admin)
**TTL:** 3600

**Record type:** CNAME
**Host/Name:** `s2._domainkey`
**Value:** `s2.domainkey.shopify.com.` (confirm exact value from Shopify Admin)
**TTL:** 3600

---

### Record 4 — DMARC with Reporting (Upgrade)

Replace the existing bare `v=DMARC1; p=none` record with:

**Record type:** TXT
**Host/Name:** `_dmarc`
**Value:** `v=DMARC1; p=none; rua=mailto:dmarc-reports@readyfortakeoffbook.com; ruf=mailto:dmarc-reports@readyfortakeoffbook.com; sp=none; adkim=r; aspf=r; pct=100; fo=1`
**TTL:** 3600

**Notes:**
- Replace `dmarc-reports@readyfortakeoffbook.com` with a real email address you monitor (or use a DMARC reporting service like Postmark, Valimail, or Dmarcian)
- After 1–2 weeks of reviewing aggregate reports and confirming all legitimate mail passes, change `p=none` to `p=quarantine`
- After another 2–4 weeks, escalate to `p=reject`

---

### Record 5 — Backup MX (Recommended)

Check your Rackspace Hosted Email admin panel for a secondary MX host. A typical Rackspace configuration:

**Record type:** MX
**Host/Name:** `@`
**Value:** `mx2.readyfortakeoffbook.com.cust.b.hostedemail.com.` (confirm with Rackspace)
**Priority:** 5
**TTL:** 3600

---

## 7. Discrepancy Summary

| Finding | Expected | Actual |
|---|---|---|
| DNS Provider | Shopify DNS (per task brief) | Google Domains / Google Cloud DNS (ns-cloud-a*.googledomains.com) |
| SPF | Present | MISSING |
| DKIM | Present | MISSING for all 23 selectors tested |
| DMARC | Enforcing (`p=quarantine` or `reject`) | `p=none` — non-enforcing, no reporting |
| Email platform | Unknown | Brevo (domain verified) + Rackspace Hosted Email (MX) + Shopify (assumed) |
| Backup MX | Recommended | MISSING — single point of failure for inbound mail |

**Critical correction on DNS host:** The task brief assumed DNS is managed through Shopify's nameservers. Live NS record lookup confirms DNS is managed through **Google Domains (Google Cloud DNS)**. All remediation steps must be executed in Google Domains or Google Cloud DNS console, not Shopify Admin DNS Settings.
