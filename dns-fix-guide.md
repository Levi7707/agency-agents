# DNS Email Authentication Fix Guide
## Domain: readyfortakeoffbook.com
## Goal: Fix SPF, DKIM, and DMARC so broadcast emails reach the inbox

**Prepared for:** Store owner of readyfortakeoffbook.com  
**Date:** June 2026  
**Urgency:** Complete before sending any broadcast to your 2,200 subscribers

---

## Why This Matters

Right now, every email you send from AVADA Email Marketing is arriving at Gmail and Yahoo with no proof that it actually came from you. This means:

- Gmail's spam filters are already suspicious of your emails
- Yahoo may be silently rejecting some of them
- As your list grows, deliverability will get worse — not better

Three records fix this: **SPF** (proves which servers can send on your behalf), **DKIM** (digitally signs each email so it can't be forged), and **DMARC** (tells receiving servers what to do if SPF or DKIM fail). All three are DNS records — think of them as public signposts that tell email servers "these emails are legitimate."

This guide walks you through adding all three, step by step.

---

## Section 1 — Understanding Shopify DNS Management

### Where the DNS panel lives

Because your domain `readyfortakeoffbook.com` was purchased through and is managed by Shopify, all DNS changes are made inside your Shopify admin — not at a separate domain registrar.

**Exact navigation path:**

```
Shopify Admin → Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage
```

Step by step:

1. Log in to your Shopify Admin (your-store.myshopify.com/admin)
2. In the left sidebar, click **Settings** (bottom left)
3. Click **Domains**
4. Click on **readyfortakeoffbook.com** (your primary domain)
5. Scroll down to the **DNS settings** section
6. Click **Manage**
7. You will see all your current DNS records listed here
8. To add a new record, click **Add custom record**

[Shopify Admin screenshot: Settings → Domains → readyfortakeoffbook.com → DNS Settings]

### What record types Shopify supports

In the "Add custom record" dropdown, Shopify allows you to add:
- **A** — points your domain to an IP address
- **AAAA** — same as A but for IPv6
- **CNAME** — points one domain name to another
- **MX** — controls where email is delivered
- **TXT** — free-form text records used for SPF, DKIM, DMARC, and domain verification
- **SRV** — service records (rarely needed)

All three records you need (SPF, DKIM, and DMARC) are **TXT records**.

### How to edit or delete an existing record

Shopify does allow editing and deleting DNS records you've created:

- To **edit** a record: In the DNS settings list, find the record, click the **Actions** menu (three dots or ellipsis) next to it, and select **Edit**
- To **delete** a record: Click **Actions** → **Remove**, then confirm

**This is important for Section 4** (DMARC), where you have a broken existing record that needs to be replaced.

### Shopify DNS limitations to know

- **You cannot change the nameserver (NS) or SOA records** — these are locked by Shopify. This is expected and not a problem for what we're doing.
- **DNS changes take 1–48 hours to propagate** — usually faster (30 minutes to a few hours), but plan for up to 48 hours before testing.
- **Shopify DNS only works if your domain uses Shopify's nameservers.** Since you purchased the domain through Shopify, this is already the case.
- **Subdomain depth:** Shopify supports standard subdomains (like `_dmarc.readyfortakeoffbook.com` or `selector1._domainkey.readyfortakeoffbook.com`). You do not need to enter the root domain name in the Host/Name field — Shopify appends it automatically.
- **One SPF record per domain** — DNS allows only one `v=spf1` TXT record on your root domain (`@`). If you add a second one, both will fail. We will combine everything into a single record.
- **One DMARC record per domain** — Only one `v=DMARC1` record is allowed on `_dmarc`. You must delete the existing broken one and replace it. (Instructions are in Section 4.)

---

## Section 2 — SPF Record (Add This First)

### What SPF does

SPF is a list of servers that are allowed to send email from your domain. When Gmail receives an email claiming to be from `you@readyfortakeoffbook.com`, it checks this list. If the sending server is on the list, it passes. If not, it fails — and the email goes to spam or gets rejected.

### Your sending setup

Your domain sends email from two places:

1. **AVADA Email Marketing** — your Shopify app, used for broadcasts and automations
2. **Fastmail** — your domain's email hosting (the MX records point to Fastmail's `mx.readyfortakeoffbook.com.cust.b.hostedemail.com` server), meaning any email you send directly from your `@readyfortakeoffbook.com` inbox also needs to be covered

### The SPF record to add

**Important note about AVADA's SPF:** AVADA Email Marketing is a Shopify-native app that sends email through its own sending infrastructure (operating under `avada.io` / `send.avada.io`). When you verify your domain in AVADA (Section 3), AVADA generates DKIM keys and — depending on your plan — may use either a shared sending pool or dedicated IPs.

AVADA's domain verification process generates a custom SPF record value specific to your account. When you complete Step 3 (the AVADA domain setup), AVADA will show you the exact SPF value to use. That value will look like one of these formats:

- `v=spf1 include:spf.avada.io ~all`
- `v=spf1 include:em.avada.io ~all`
- Or it may use an underlying provider like SendGrid: `v=spf1 include:sendgrid.net ~all`

**Because AVADA shows you your specific SPF value during domain setup, complete Section 3 first, then return here to finalize the combined SPF record.**

### The combined SPF record to enter

Once you have the AVADA-provided SPF include value, combine it with Fastmail into a single TXT record:

```
Host:  @
Type:  TXT
Value: v=spf1 include:[AVADA-provided-include] include:spf.messagingengine.com ~all
TTL:   3600
```

**Example** (if AVADA provides `include:spf.avada.io`):
```
v=spf1 include:spf.avada.io include:spf.messagingengine.com ~all
```

**What each part means:**

| Part | What it does |
|------|--------------|
| `v=spf1` | Declares this is an SPF record (required, always first) |
| `include:spf.avada.io` | Authorizes AVADA's sending servers (replace with the actual value AVADA shows you) |
| `include:spf.messagingengine.com` | Authorizes Fastmail's servers (Fastmail's parent company is Messaging Engine — this is their official SPF domain) |
| `~all` | "Soft fail" — emails from unauthorized servers are marked suspicious but not outright rejected. This is the safe default while getting everything set up. Once DMARC is at `p=reject` (Stage 3), you can optionally change this to `-all` (hard fail). |

### About the Brevo token

There is currently a TXT record with `brevo-code:15977df608ca51d8ff239bfffe52a150` on your domain. **This is a domain ownership token from Brevo, not an SPF record** — it does not affect email delivery by itself. See Section 7 for advice on whether to keep or remove it.

Importantly, Brevo does NOT need to be included in your SPF record unless you are actively sending email through Brevo. Since the DNS audit shows no active Brevo sending setup, **do not add `include:spf.brevo.com` to your SPF record.**

### How to add the SPF record in Shopify

1. Go to **Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage**
2. Click **Add custom record**
3. Select record type: **TXT**
4. In the **Name / Host** field, enter: `@`  
   (This represents the root domain — `readyfortakeoffbook.com` itself)
5. In the **Value** field, paste your combined SPF record:  
   `v=spf1 include:[AVADA-include] include:spf.messagingengine.com ~all`
6. Set TTL to **3600** (or leave as default if Shopify doesn't show this field)
7. Click **Confirm**

[Shopify Admin screenshot: Add custom record → TXT → Host: @ → Value: v=spf1...]

---

## Section 3 — DKIM Record (Generate in AVADA, Add to Shopify DNS)

### What DKIM does

DKIM is a digital signature on every email you send. AVADA generates a private key (kept secret on their servers) and a public key (you publish in DNS). When Gmail receives your email, it checks the public key in DNS to verify the signature. If it matches, the email is authenticated. Without DKIM, Gmail has no way to confirm the email wasn't tampered with in transit.

### Step 1: Generate DKIM in AVADA

**Navigation path inside AVADA:**

1. Log into your AVADA Email Marketing app from your Shopify admin:  
   **Shopify Admin → Apps → AVADA Email Marketing**
2. In the AVADA dashboard, go to **Settings** (gear icon, usually in the left sidebar)
3. Look for **Email Settings** or **Sender Settings**
4. Find the section labeled **Sending Domain**, **Custom Domain**, or **Domain Authentication**
5. Click **Add Domain** or **Verify Domain**
6. Enter your domain: `readyfortakeoffbook.com`
7. AVADA will show you a popup or page with three records to copy:
   - **Step 1: SPF Record** (TXT record — use this for Section 2 above)
   - **Step 2: DKIM Record** (TXT record — this is what you need now)
   - **Step 3: Tracking Record** (usually a CNAME — for link tracking in emails)

[AVADA screenshot: Settings → Email Settings → Sending Domain → Add Domain]

**Important:** Do not close this window or navigate away from AVADA until you have added all three records to Shopify DNS.

### Step 2: What the DKIM record will look like

AVADA will give you a DKIM TXT record in this format:

```
Host:  [selector]._domainkey
Type:  TXT
Value: v=DKIM1; k=rsa; p=[long-string-of-characters]
TTL:   3600
```

Where:
- `[selector]` is a unique identifier AVADA assigns (examples: `avada1`, `s1`, `k1`, `em`, or a long alphanumeric string)
- `._domainkey` is the standard suffix for all DKIM records
- The full host name, when Shopify appends your domain, becomes: `avada1._domainkey.readyfortakeoffbook.com`
- `p=[...]` is your public key — a long string of letters and numbers. Copy it exactly, including all characters.

**Example of what it looks like:**
```
Host:  avada1._domainkey
Type:  TXT
Value: v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC...
TTL:   3600
```

### Step 3: Add the DKIM record in Shopify DNS

1. Go back to **Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage**
2. Click **Add custom record**
3. Select record type: **TXT**
4. In the **Name / Host** field, enter what AVADA shows you for the host — for example: `avada1._domainkey`  
   (Do NOT include `.readyfortakeoffbook.com` — Shopify adds this automatically)
5. In the **Value** field, paste the full DKIM value from AVADA:  
   `v=DKIM1; k=rsa; p=[your-public-key]`
6. Click **Confirm**

### Step 4: Add the Tracking CNAME (optional but recommended)

AVADA may also provide a CNAME record for click/open tracking. Adding this means email links will be tracked under your domain instead of AVADA's domain — which looks more professional and trustworthy to spam filters.

If AVADA shows a Step 3 tracking record:
1. Click **Add custom record**
2. Select record type: **CNAME**
3. Enter the Host and Value exactly as AVADA shows
4. Click **Confirm**

### Step 5: Tell AVADA you've added the records

After adding the records in Shopify:
1. Return to AVADA
2. Click the **Verify** or **Check DNS** button in AVADA's domain setup screen
3. If it says "Pending" or "Not yet verified," wait 30–60 minutes and try again — DNS propagation takes time
4. Once AVADA shows a green checkmark or "Verified," DKIM is working

### How to verify DKIM is working after DNS propagation

Use this free tool after 24–48 hours:

1. Go to: [https://mxtoolbox.com/dkim.aspx](https://mxtoolbox.com/dkim.aspx)
2. In the "Domain" field enter: `readyfortakeoffbook.com`
3. In the "Selector" field enter: the selector AVADA gave you (e.g., `avada1`)
4. Click **DKIM Lookup**
5. A passing result shows: "DKIM Record Found" and your public key in green

---

## Section 4 — DMARC Record (Staged Upgrade Path)

### The current situation

Your domain already has a DMARC record: `v=DMARC1; p=none`

This record is technically present but useless because:
- **No `rua=` address** — you receive zero failure reports, so you can't tell who is spoofing your domain or whether your SPF/DKIM are working
- **`p=none`** — this means "do nothing" — even if SPF and DKIM fail, the email is still delivered as normal

The fix has two parts:
1. Delete the existing broken record
2. Add a proper DMARC record with a reporting address

### Important: Handle the existing DMARC record first

**Shopify does allow editing and deleting DNS records.** Before adding a new DMARC record, you MUST remove the existing one. DMARC is a strict standard — only one `v=DMARC1` TXT record is allowed on `_dmarc.readyfortakeoffbook.com`. Having two will cause both to fail, and your DMARC check will show "multiple records found — invalid."

**How to delete the existing DMARC record:**
1. Go to **Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage**
2. Find the TXT record with host `_dmarc` and value `v=DMARC1; p=none`
3. Click the **Actions** menu (three dots) next to it
4. Select **Remove**
5. Confirm the deletion

Then immediately add the Stage 1 record below.

### What email address to use for DMARC reports

DMARC reports are sent by Gmail, Yahoo, and other email providers to tell you which emails from your domain passed or failed authentication. These reports are XML files — not human-readable — but free tools parse them for you.

**Options for your `rua=` reporting address:**

**Option A (Easiest):** Use your existing Fastmail inbox:
```
rua=mailto:you@readyfortakeoffbook.com
```
Then use a free service to parse the reports: [https://dmarc.postmarkapp.com](https://dmarc.postmarkapp.com) (Postmark's free DMARC report digest — sends you a weekly human-readable summary by email)

**Option B (Cleanest):** Create a dedicated mailbox on Fastmail:
- Log into your Fastmail account
- Create a new alias or mailbox: `dmarc-reports@readyfortakeoffbook.com`
- Register it at [https://dmarc.postmarkapp.com](https://dmarc.postmarkapp.com) for weekly digests

**Option C (Third-party parsing service):** Use a free DMARC monitoring service that provides its own reporting address:
- [https://dmarcdigests.com](https://dmarcdigests.com) — free plan includes weekly reports
- [https://app.dmarcanalyzer.com](https://app.dmarcanalyzer.com) — free tier available

For simplicity, Option A is recommended: use your primary email and sign up at dmarc.postmarkapp.com to receive weekly human-readable summaries.

---

### Stage 1 — Add reporting immediately (do this today)

This stage says "don't block anything, but start sending me reports."

**Delete the existing `_dmarc` record first (see instructions above), then add:**

```
Host:  _dmarc
Type:  TXT
Value: v=DMARC1; p=none; rua=mailto:your@readyfortakeoffbook.com; pct=100
TTL:   3600
```

Replace `your@readyfortakeoffbook.com` with whichever email address you chose above.

**How to add in Shopify:**
1. Go to **Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage**
2. Click **Add custom record**
3. Select: **TXT**
4. Host/Name: `_dmarc`
5. Value: `v=DMARC1; p=none; rua=mailto:your@readyfortakeoffbook.com; pct=100`
6. Click **Confirm**

**What to do:** Wait 2–4 weeks and collect reports. You should start receiving DMARC report emails (or weekly summaries if using Postmark). Look for:
- "SPF: pass" — your SPF record is working
- "DKIM: pass" — your DKIM record is working
- Any "fail" entries — these could indicate someone spoofing your domain, or a sending source you forgot to authorize in SPF

**Move to Stage 2 when:** You've received at least 2 weeks of reports and nearly all legitimate emails show SPF=pass and DKIM=pass.

---

### Stage 2 — After 2–4 weeks of clean reports (quarantine at 10%)

This stage says "put 10% of unauthenticated emails in spam, continue sending reports."

**Edit the existing `_dmarc` record** (Actions → Edit):

```
Host:  _dmarc
Type:  TXT
Value: v=DMARC1; p=quarantine; rua=mailto:your@readyfortakeoffbook.com; pct=10
TTL:   3600
```

**What changed:**
- `p=quarantine` — unauthenticated emails are sent to spam (not delivered normally)
- `pct=10` — only applies to 10% of failing emails (a gradual rollout so you catch any surprises)

**What to watch:** Continue monitoring reports for 2–4 more weeks. Check that your SPF and DKIM are still showing as "pass" for your legitimate email. If you see any unexpected failures, investigate before proceeding.

**Move to Stage 3 when:** Reports show consistent SPF=pass and DKIM=pass for all your legitimate sending, with no unexplained failures, for 4+ weeks.

---

### Stage 3 — After 4–8 weeks of clean reports (full enforcement)

This is the gold standard. It tells the world: "Any email claiming to be from readyfortakeoffbook.com that fails authentication is not from us — reject it."

**Edit the existing `_dmarc` record** (Actions → Edit):

```
Host:  _dmarc
Type:  TXT
Value: v=DMARC1; p=reject; rua=mailto:your@readyfortakeoffbook.com; pct=100
TTL:   3600
```

**What this means for your deliverability:**
- Gmail, Yahoo, and all major providers will reject emails that fail SPF and DKIM
- Spammers cannot impersonate your domain in phishing attacks
- Your domain reputation improves significantly over time
- Some email clients display a green "verified sender" badge

**Timeline summary:**
- Today: Stage 1 (with `rua=` address)
- Weeks 2–4: Advance to Stage 2 if reports are clean
- Weeks 4–8: Advance to Stage 3 if still clean

---

## Section 5 — Verification Checklist

After making all DNS changes, wait at least 24–48 hours before testing. DNS propagation is worldwide and takes time.

### SPF Verification

**Tool:** [https://mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx)

1. Enter `readyfortakeoffbook.com` and click **SPF Lookup**
2. **Passing result:** Green banner saying "SPF Record Found," showing your `v=spf1` record with all your includes
3. **If it fails:** Check that the value was entered exactly (no typos, no extra spaces). Make sure you used `@` as the host, not `readyfortakeoffbook.com`

**Alternative tool:** [https://toolbox.googleapps.com/apps/checkmx/](https://toolbox.googleapps.com/apps/checkmx/)  
Enter `readyfortakeoffbook.com` — this Google tool checks SPF, DKIM, and DMARC all at once.

### DKIM Verification

**Tool:** [https://mxtoolbox.com/dkim.aspx](https://mxtoolbox.com/dkim.aspx)

1. Enter domain: `readyfortakeoffbook.com`
2. Enter selector: whatever AVADA showed you (e.g., `avada1`, `s1`, etc.)
3. **Passing result:** "DKIM Record Found" in green, with your public key displayed
4. **If it fails:** Double-check that the host value in Shopify DNS matches exactly what AVADA provided. Make sure you didn't accidentally include `.readyfortakeoffbook.com` in the host field.

### DMARC Verification

**Tool:** [https://mxtoolbox.com/dmarc.aspx](https://mxtoolbox.com/dmarc.aspx)

1. Enter `readyfortakeoffbook.com` and click **DMARC Lookup**
2. **Passing result:** "DMARC Record Found" showing your `v=DMARC1; p=none; rua=...` record
3. **If it shows "multiple records":** You have two DMARC records. Delete both using Shopify's DNS panel and add one clean record
4. **If it shows "not found":** The record hasn't propagated yet — wait another hour and try again

### Full email authentication header check

The most reliable verification is to send a real test email and read its headers:

1. Send a test email from AVADA to a Gmail address
2. In Gmail, open the email, click the three-dot menu (⋮), and select **Show original**
3. Look for these lines near the top:
   - `dkim=pass` — DKIM is working
   - `spf=pass` — SPF is working
   - `dmarc=pass` — DMARC is passing
4. Also look for `Authentication-Results:` — it should show all three as "pass"

**If DKIM or SPF shows "fail" in headers:**
- SPF fail: The sending IP is not in your SPF record. Check with AVADA support whether they use a different include
- DKIM fail: The DKIM record in DNS doesn't match what AVADA is signing with. Re-verify the domain inside AVADA and re-copy the DKIM value

---

## Section 6 — Pre-Send Broadcast Checklist

Before sending your broadcast to 2,200 subscribers, confirm every item below. Do not send until all boxes are checked.

```
[ ] SPF record added in Shopify DNS (host: @, type: TXT, value: v=spf1 include:...)
[ ] SPF verified as passing at mxtoolbox.com/spf.aspx
[ ] DKIM record added in Shopify DNS (host: [selector]._domainkey, type: TXT)
[ ] DKIM verified as passing at mxtoolbox.com/dkim.aspx with correct selector
[ ] DMARC record updated: old "v=DMARC1; p=none" deleted, new record with rua= added
[ ] DMARC verified as passing at mxtoolbox.com/dmarc.aspx (only ONE record showing)
[ ] At least 24 hours have passed since adding DNS records
[ ] AVADA sending domain shows as "Verified" / green checkmark in AVADA Settings
[ ] Test email sent from AVADA to a Gmail address you control
[ ] Test email landed in Gmail INBOX (not spam)
[ ] Gmail "Show original" headers show: dkim=pass, spf=pass, dmarc=pass
[ ] AVADA sending domain confirmation email (if any) was received and clicked
```

**If even one item shows a failure:** Do not send the broadcast. Identify and fix the failing item first. Sending to 2,200 people with broken authentication will generate spam complaints, damage your domain reputation, and may get your sending account flagged by AVADA.

### Recommended send timing

Once all checks pass:
- Send the broadcast to a **small segment first** (100–200 subscribers) and wait 24 hours
- Check your AVADA analytics for opens, bounces, and spam rates
- If the open rate is normal (20%+ is healthy) and spam complaints are under 0.1%, send to the full list

---

## Section 7 — The Brevo Token (Keep or Delete?)

There is a TXT record on your domain with this value:
```
brevo-code:15977df608ca51d8ff239bfffe52a150
```

This is a **domain verification token from Brevo** (formerly Sendinblue), a different email marketing platform. It was added when someone — presumably you or a previous service provider — verified your domain in Brevo.

### What this token does

This token by itself does not send emails and does not affect SPF, DKIM, or DMARC. It is simply proof-of-domain-ownership in the Brevo system.

**However, it does carry a risk:**

Anyone with access to the Brevo account that verified your domain using this token can still use Brevo to send emails claiming to come from `readyfortakeoffbook.com`. If that Brevo account credentials are ever compromised (or if you no longer control that Brevo account), an attacker could use it to send spam or phishing emails from your domain.

### Recommendation

| Scenario | Action |
|----------|--------|
| You no longer use Brevo and have no plans to return | **Delete it.** There is no benefit to keeping it. |
| You might use Brevo again in the future | **Delete it anyway.** You can re-verify your domain in Brevo at any time — it takes 5 minutes to generate a new token. Keeping an old unmonitored token is an unnecessary risk. |
| You actively use Brevo right now | **Keep it, but also add Brevo's SPF include** (`include:spf.brevo.com`) to your SPF record. |

**How to delete it:**
1. Go to **Settings → Domains → readyfortakeoffbook.com → DNS Settings → Manage**
2. Find the TXT record with value starting `brevo-code:`
3. Click **Actions → Remove**
4. Confirm

This will not affect your Brevo account itself — it just removes the domain association. If you want to formally disconnect the domain from Brevo, also log into your Brevo account and remove the domain there.

---

## Quick Reference: All Records to Add

Here is a summary of every DNS change needed:

| Action | Host | Type | Value |
|--------|------|------|-------|
| **ADD** | `@` | TXT | `v=spf1 include:[AVADA-include] include:spf.messagingengine.com ~all` |
| **ADD** | `[selector]._domainkey` | TXT | `v=DKIM1; k=rsa; p=[public-key]` (from AVADA) |
| **ADD** | `[avada-tracking]` | CNAME | `[value from AVADA]` (tracking subdomain) |
| **DELETE** | `_dmarc` | TXT | `v=DMARC1; p=none` (the existing broken record) |
| **ADD** | `_dmarc` | TXT | `v=DMARC1; p=none; rua=mailto:your@readyfortakeoffbook.com; pct=100` |
| **DELETE** (recommended) | `@` | TXT | `brevo-code:15977df608ca51d8ff239bfffe52a150` |

**Do this in order:**
1. Complete AVADA domain setup to get the exact SPF and DKIM values
2. Add SPF record
3. Add DKIM record
4. Add AVADA tracking CNAME (if provided)
5. Delete old DMARC record
6. Add new DMARC record with `rua=`
7. Delete Brevo token (recommended)
8. Wait 24–48 hours
9. Run all verification checks
10. Send a test email before broadcasting

---

## Need Help?

- **AVADA Support:** Live chat inside the AVADA app, or email support@avada.io
- **Shopify Support:** help.shopify.com → Contact Support (24/7 chat available)
- **DMARC reports explained:** [https://dmarc.postmarkapp.com](https://dmarc.postmarkapp.com) — free weekly digest service
- **All-in-one check:** [https://toolbox.googleapps.com/apps/checkmx/](https://toolbox.googleapps.com/apps/checkmx/)
- **MXToolbox SPF:** [https://mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx)
- **MXToolbox DKIM:** [https://mxtoolbox.com/dkim.aspx](https://mxtoolbox.com/dkim.aspx)
- **MXToolbox DMARC:** [https://mxtoolbox.com/dmarc.aspx](https://mxtoolbox.com/dmarc.aspx)
