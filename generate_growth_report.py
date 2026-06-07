from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ── colour constants ──────────────────────────────────────────────────────────
DARK_BLUE    = RGBColor(0x1a, 0x2f, 0x5e)
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT    = RGBColor(0x22, 0x22, 0x22)
MID_TEXT     = RGBColor(0x33, 0x33, 0x33)
GREY_TEXT    = RGBColor(0x88, 0x88, 0x88)
LIGHT_BLUE_TEXT = RGBColor(0xA8, 0xC8, 0xF0)

HEX_DARK_BLUE    = "1a2f5e"
HEX_RED          = "C62828"   # CRITICAL fill
HEX_GREEN        = "2E7D32"   # Good fill
HEX_YELLOW       = "E65100"   # Fixable fill
HEX_ROW_EVEN     = "F5F5F5"
HEX_ROW_ODD      = "FFFFFF"
HEX_NS_LIGHT     = "EAF0FB"
HEX_NS_GREEN     = "E8F5E9"
HEX_PHASE_BG     = "F8FAFD"
HEX_BORDER_GREY  = "CCCCCC"
HEX_BORDER_BLUE  = "D0DDF0"
HEX_DIAG_BG      = "EBF5FB"

# ── helpers ───────────────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_color: str):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    # remove existing shd if any
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    tcPr.append(shd)

def set_cell_borders(cell, color="CCCCCC", sz="4"):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:tcBorders")):
        tcPr.remove(old)
    tcBorders = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"),   "single")
        el.set(qn("w:sz"),    sz)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        tcBorders.append(el)
    tcPr.append(tcBorders)

def fmt_para(para, space_before=0, space_after=6, left_indent=None,
             right_indent=None, align=WD_ALIGN_PARAGRAPH.LEFT):
    para.alignment = align
    para.paragraph_format.space_before = Pt(space_before)
    para.paragraph_format.space_after  = Pt(space_after)
    if left_indent  is not None:
        para.paragraph_format.left_indent  = left_indent
    if right_indent is not None:
        para.paragraph_format.right_indent = right_indent

def add_run(para, text, bold=False, italic=False, color=None,
            size=11, name="Calibri"):
    run = para.add_run(text)
    run.bold       = bold
    run.italic     = italic
    run.font.name  = name
    run.font.size  = Pt(size)
    if color:
        run.font.color.rgb = color
    return run

def cell_write(cell, text, bold=False, color=DARK_TEXT, size=10.5,
               align=WD_ALIGN_PARAGRAPH.LEFT, sb=4, sa=4):
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    para = cell.paragraphs[0]
    fmt_para(para, space_before=sb, space_after=sa, align=align)
    add_run(para, text, bold=bold, color=color, size=size)

def add_heading(doc, text, level=1, color=DARK_BLUE, sb=16, sa=6):
    p = doc.add_heading(text, level=level)
    fmt_para(p, space_before=sb, space_after=sa)
    for run in p.runs:
        run.font.color.rgb = color
        run.font.name      = "Calibri"
    return p

def para_underline_border(p, color_hex="1a2f5e"):
    pPr  = p._p.get_or_add_pPr()
    pb   = OxmlElement("w:pBdr")
    bot  = OxmlElement("w:bottom")
    bot.set(qn("w:val"),   "single")
    bot.set(qn("w:sz"),    "4")
    bot.set(qn("w:space"), "2")
    bot.set(qn("w:color"), color_hex)
    pb.append(bot)
    pPr.append(pb)

def add_footer(doc, date_str="June 7, 2026"):
    section = doc.sections[0]
    footer  = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    fmt_para(p, space_before=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_run(p,
            f"Growth Hacker Analysis  |  Ready For Take-Off Book  |  {date_str}  |  Page ",
            color=GREY_TEXT, size=9)
    # PAGE field
    r   = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rf  = OxmlElement("w:rFonts")
    rf.set(qn("w:ascii"), "Calibri")
    rPr.append(rf)
    sz  = OxmlElement("w:sz")
    sz.set(qn("w:val"), "18")
    rPr.append(sz)
    r.append(rPr)
    for ftype in ("begin", "separate", "end"):
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), ftype)
        r.append(fc)
        if ftype == "begin":
            it = OxmlElement("w:instrText")
            it.text = "PAGE"
            r.append(it)
    p._p.append(r)

# ── build document ────────────────────────────────────────────────────────────
doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 0 — COVER HEADER
# ══════════════════════════════════════════════════════════════════════════════
ct = doc.add_table(rows=1, cols=1)
ct.alignment = WD_TABLE_ALIGNMENT.CENTER
cc = ct.cell(0, 0)
set_cell_bg(cc, HEX_DARK_BLUE)
set_cell_borders(cc, HEX_DARK_BLUE, "0")

p1 = cc.paragraphs[0]
fmt_para(p1, space_before=18, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
add_run(p1, "GROWTH HACKER ANALYSIS", bold=True, color=WHITE, size=24)

p2 = cc.add_paragraph()
fmt_para(p2, space_before=0, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
add_run(p2, "Ready For Take-Off Book", bold=True, color=LIGHT_BLUE_TEXT, size=17)

p3 = cc.add_paragraph()
fmt_para(p3, space_before=0, space_after=18, align=WD_ALIGN_PARAGRAPH.CENTER)
add_run(p3, "June 7, 2026  |  Prepared by: Growth Hacker Agent",
        color=RGBColor(0xCC, 0xDD, 0xEE), size=11)

sp = doc.add_paragraph()
fmt_para(sp, space_before=4, space_after=4)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — HEADLINE DIAGNOSIS
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "1. Headline Diagnosis", level=1)

dt = doc.add_table(rows=1, cols=1)
dt.alignment = WD_TABLE_ALIGNMENT.CENTER
dc = dt.cell(0, 0)
set_cell_bg(dc, HEX_DIAG_BG)
set_cell_borders(dc, HEX_DARK_BLUE, "6")

dp = dc.paragraphs[0]
fmt_para(dp, space_before=10, space_after=10,
         left_indent=Inches(0.15), right_indent=Inches(0.15))
add_run(dp, "Traffic Success / Conversion Failure\n",
        bold=True, color=DARK_BLUE, size=13)
add_run(dp,
        "Your SEO brought in 307K sessions — that's excellent. But you're converting at 0.73%, "
        "roughly 3× below the e-commerce average of 2–3%. You're essentially leaving ~€300K/year "
        "on the table with your current traffic volume.",
        color=DARK_TEXT, size=11)

sp2 = doc.add_paragraph()
fmt_para(sp2, space_before=4, space_after=4)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — KEY METRICS TABLE
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "2. Key Metrics", level=1)

METRICS = [
    ("Sessions",             "306,959 (+104%)", "—",     "Growing fast",        HEX_GREEN,  WHITE),
    ("Conversion Rate",      "0.73%",           "2–3%",  "CRITICAL",            HEX_RED,    WHITE),
    ("Average Order Value",  "€56.09",          "—",     "Healthy",             HEX_GREEN,  WHITE),
    ("Orders",               "2,590",           "—",     "Too low for traffic", HEX_YELLOW, WHITE),
    ("Returning Customers",  "2.53%",           "20–30%","CRITICAL",            HEX_RED,    WHITE),
    ("Add-to-Cart Rate",     "1.63%",           "8–12%", "CRITICAL",            HEX_RED,    WHITE),
    ("Cart → Purchase",      "53%",             "~65%",  "Fixable",             HEX_YELLOW, WHITE),
]

COL_W = [Inches(2.1), Inches(1.4), Inches(1.2), Inches(1.4)]

mt = doc.add_table(rows=len(METRICS)+1, cols=4)
mt.alignment = WD_TABLE_ALIGNMENT.LEFT

# header row
for ci, hdr in enumerate(["Metric", "Your Number", "Benchmark", "Status"]):
    hc = mt.cell(0, ci)
    hc.width = COL_W[ci]
    set_cell_bg(hc, HEX_DARK_BLUE)
    set_cell_borders(hc, HEX_DARK_BLUE, "4")
    cell_write(hc, hdr, bold=True, color=WHITE, size=11,
               align=WD_ALIGN_PARAGRAPH.CENTER, sb=6, sa=6)

# data rows
for ri, (metric, value, bench, status, status_fill, status_txt_color) in enumerate(METRICS):
    row_bg = HEX_ROW_EVEN if ri % 2 == 0 else HEX_ROW_ODD
    for ci, (text, fill, tc, bold, align) in enumerate([
        (metric, row_bg,     DARK_TEXT,         True,  WD_ALIGN_PARAGRAPH.LEFT),
        (value,  row_bg,     DARK_TEXT,         False, WD_ALIGN_PARAGRAPH.CENTER),
        (bench,  row_bg,     DARK_TEXT,         False, WD_ALIGN_PARAGRAPH.CENTER),
        (status, status_fill,status_txt_color,  True,  WD_ALIGN_PARAGRAPH.CENTER),
    ]):
        cell = mt.cell(ri+1, ci)
        cell.width = COL_W[ci]
        set_cell_bg(cell, fill)
        set_cell_borders(cell, HEX_BORDER_GREY, "4")
        cell_write(cell, text, bold=bold, color=tc, size=10.5,
                   align=align, sb=5, sa=5)

sp3 = doc.add_paragraph()
fmt_para(sp3, space_before=4, space_after=4)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — ROOT CAUSES
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "3. The 3 Root Causes", level=1)

CAUSES = [
    ("3.1  SEO Traffic is Informational, Not Transactional",
     "Your #1 landing page — /products/ready-for-take-off-book — got 113,700 sessions but almost "
     "none converted. Your blog articles (pilot recruitment, A320 type rating) are pulling in "
     "aspiring pilots who are researching, not ready to buy. Top-of-funnel traffic landed directly "
     "on the buy page with no warm-up. That kills conversion."),
    ("3.2  Cart Abandonment is a Leak Nobody is Plugging",
     "5,017 added to cart → 2,267 completed = 2,750 abandoned carts. At €56 AOV, that's "
     "€154,000 of near-purchases you're not recovering."),
    ("3.3  Zero Retention — No Second Product to Buy",
     "The cohort analysis shows 0% repeat purchase after month 1 across every cohort. One product, "
     "customers buy it once, and they're gone. The email list is being massively underutilised."),
]

for title, body in CAUSES:
    h = add_heading(doc, title, level=2, color=DARK_BLUE, sb=10, sa=4)
    p = doc.add_paragraph()
    fmt_para(p, space_before=2, space_after=8)
    add_run(p, body, color=MID_TEXT, size=11)

sp4 = doc.add_paragraph()
fmt_para(sp4, space_before=2, space_after=2)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — EXPERIMENT ROADMAP
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "4. Prioritised Experiment Roadmap", level=1)

PHASES = [
    {
        "label":  "This Week — Highest Leverage, Zero Cost",
        "color":  "2E7D32",
        "items": [
            ("1.", "Abandoned Cart Email Sequence",
             "Set up a 3-email flow in Shopify (1hr / 24hr / 72hr). Recovering 20% of your "
             "2,750 abandoned carts = +550 orders = +€30K. This is the single biggest win available right now."),
            ("2.", "Add Apple Pay / Google Pay to Checkout",
             "Traffic is predominantly mobile. One-tap payment removes the biggest mobile checkout "
             "friction. Expected CVR lift: +0.2–0.4%."),
            ("3.", "Sticky 'Buy Now' Button on Mobile Product Page",
             "113K sessions hit that page. A persistent CTA costs nothing to test and directly "
             "addresses the 1.63% add-to-cart rate."),
        ]
    },
    {
        "label":  "Next 2–4 Weeks — Conversion Funnel Fixes",
        "color":  "1565C0",
        "items": [
            ("4.", "Email Capture on Blog Articles",
             'The pilot recruitment blog gets 14K sessions from perfect prospects. Add a lead magnet '
             'mid-article: "Free: The 7 Questions Airlines Always Ask (and How to Answer Them)." '
             "Even 5% capture = 700 emails/month. Nurture with a 7-day sequence ending in a purchase "
             "offer. Estimated: +150–300 orders/month."),
            ("5.", "Post-Purchase Upsell",
             'Add an instant upsell after checkout: "Complete your preparation — add the ebook for €X." '
             "The ebook and mock interview products barely register in orders despite existing. Bundle "
             "them. This lifts AOV from €56 toward €80+."),
            ("6.", "Product Page Social Proof Overhaul",
             "Add: number of pilots who passed using the book, specific airline logos, a money-back "
             "guarantee badge, and 3–5 video or named testimonials. The page is getting 113K sessions "
             "— even a 0.5% CVR lift = +565 orders."),
        ]
    },
    {
        "label":  "Month 2+ — Scale What's Working",
        "color":  "6A1B9A",
        "items": [
            ("7.", "Facebook / Instagram Retargeting",
             "Already getting €21.4K from Facebook organically. Set up retargeting audiences: "
             "product page visitors who didn't buy, blog readers, email list. At current traffic "
             "volume, retargeting should generate €5–10K/month at low CAC."),
            ("8.", "TikTok — Fix or Kill",
             "4.2K sessions, ~€96 in sales. Either invest in it properly (organic content strategy) "
             "or kill it. Don't leave it as a half-measure."),
            ("9.", "Create a Second Product",
             "A subscription, course, or community (€99–199) targeting the same audience. Even 5% "
             "of your 2,590 existing customers buying a second product = €13–26K incremental revenue "
             "with zero new traffic needed."),
        ]
    },
]

for phase in PHASES:
    ph = add_heading(doc, phase["label"], level=2, color=DARK_BLUE, sb=14, sa=4)
    para_underline_border(ph, phase["color"])

    for num, title, body in phase["items"]:
        # two-column table: number badge | content
        et = doc.add_table(rows=1, cols=2)
        et.alignment = WD_TABLE_ALIGNMENT.LEFT
        nc = et.cell(0, 0)
        dc = et.cell(0, 1)
        nc.width = Inches(0.42)
        dc.width = Inches(5.68)

        set_cell_bg(nc, HEX_DARK_BLUE)
        set_cell_borders(nc, HEX_DARK_BLUE, "4")
        nc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        np_ = nc.paragraphs[0]
        fmt_para(np_, space_before=8, space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
        add_run(np_, num, bold=True, color=WHITE, size=12)

        set_cell_bg(dc, HEX_PHASE_BG)
        set_cell_borders(dc, HEX_BORDER_BLUE, "4")
        dc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        dp_ = dc.paragraphs[0]
        fmt_para(dp_, space_before=7, space_after=7,
                 left_indent=Inches(0.12), right_indent=Inches(0.08))
        add_run(dp_, title + "\n", bold=True, color=DARK_BLUE, size=11)
        add_run(dp_, body, color=MID_TEXT, size=10.5)

        sp_ = doc.add_paragraph()
        fmt_para(sp_, space_before=0, space_after=4)

sp5 = doc.add_paragraph()
fmt_para(sp5, space_before=2, space_after=2)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — NORTH STAR TARGET
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "5. North Star Target", level=1)

ns = doc.add_table(rows=4, cols=1)
ns.alignment = WD_TABLE_ALIGNMENT.CENTER

NS_ROWS = [
    # (fill, border, text_parts)
    # text_parts: list of (text, bold, color, size)
    (HEX_DARK_BLUE, HEX_DARK_BLUE,
     [("Get Conversion Rate from 0.73% to 2.0% with the Same Traffic", True, WHITE, 14)]),
    (HEX_NS_LIGHT, HEX_BORDER_BLUE,
     [("Current state:  ", True, DARK_BLUE, 11),
      ("306,000 sessions × 0.73% CVR × €56 AOV = ~€125,000/year", False, MID_TEXT, 11)]),
    (HEX_NS_GREEN, "4CAF50",
     [("Target state:  ", True, RGBColor(0x1B,0x5E,0x20), 11),
      ("306,000 sessions × 2.00% CVR × €68 AOV = ~€416,000/year", True, RGBColor(0x1B,0x5E,0x20), 11)]),
    (HEX_DARK_BLUE, HEX_DARK_BLUE,
     [("Potential upside: +€291,000/year", True, WHITE, 14),
      ("\nSame traffic. Fixed funnel.", True, LIGHT_BLUE_TEXT, 11)]),
]

for ri, (fill, border, parts) in enumerate(NS_ROWS):
    cell = ns.cell(ri, 0)
    set_cell_bg(cell, fill)
    set_cell_borders(cell, border, "6")
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p = cell.paragraphs[0]
    fmt_para(p, space_before=12, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    for text, bold, color, size in parts:
        add_run(p, text, bold=bold, color=color, size=size)

sp6 = doc.add_paragraph()
fmt_para(sp6, space_before=4, space_after=4)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — START HERE
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, "6. Start Here — In Order", level=1)

ACTION_ITEMS = [
    ("TODAY",      "Activate abandoned cart emails in Shopify (built-in, free)"),
    ("THIS WEEK",  "Enable Apple Pay / Google Pay in checkout settings"),
    ("THIS WEEK",  "Add email capture + lead magnet to blog articles"),
    ("NEXT WEEK",  "Run a mobile UX audit of your product page"),
]

for timing, action in ACTION_ITEMS:
    at = doc.add_table(rows=1, cols=2)
    at.alignment = WD_TABLE_ALIGNMENT.LEFT
    lc = at.cell(0, 0)
    rc = at.cell(0, 1)
    lc.width = Inches(0.95)
    rc.width = Inches(5.15)

    set_cell_bg(lc, HEX_DARK_BLUE)
    set_cell_borders(lc, HEX_DARK_BLUE, "4")
    lc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    lp = lc.paragraphs[0]
    fmt_para(lp, space_before=6, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_run(lp, timing, bold=True, color=WHITE, size=10)

    set_cell_bg(rc, HEX_ROW_EVEN)
    set_cell_borders(rc, HEX_BORDER_GREY, "4")
    rc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    rp = rc.paragraphs[0]
    fmt_para(rp, space_before=6, space_after=6, left_indent=Inches(0.12))
    add_run(rp, action, color=DARK_TEXT, size=11)

    sp_ = doc.add_paragraph()
    fmt_para(sp_, space_before=0, space_after=4)

# Closing line
cl = doc.add_paragraph()
fmt_para(cl, space_before=14, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
add_run(cl,
        "The traffic is there. The audience is right. The funnel just has holes in it.",
        bold=True, italic=True, color=DARK_BLUE, size=13)

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
add_footer(doc, "June 7, 2026")

# ══════════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════════
output = "/home/user/agency-agents/growth-hacker-report.docx"
doc.save(output)
print(f"Saved: {output}")
