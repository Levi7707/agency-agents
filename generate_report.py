from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import datetime

# ─── Brand Colors ────────────────────────────────────────────────────────────
DARK_BLUE   = HexColor("#1a2f5e")
MID_BLUE    = HexColor("#2c4a8a")
ACCENT_BLUE = HexColor("#4a7cc7")
LIGHT_BLUE  = HexColor("#e8eef7")
RED_STATUS  = HexColor("#c0392b")
RED_BG      = HexColor("#fdf0ef")
GREEN_STATUS= HexColor("#27ae60")
GREEN_BG    = HexColor("#edfaf1")
YELLOW_STATUS = HexColor("#d68910")
YELLOW_BG   = HexColor("#fef9e7")
GOLD        = HexColor("#f39c12")
NORTH_STAR_BG = HexColor("#f0f4fa")
SECTION_BG  = HexColor("#f7f9fc")
DARK_TEXT   = HexColor("#1c2333")
BODY_TEXT   = HexColor("#2d3748")
SUBTLE_GREY = HexColor("#718096")
DIVIDER     = HexColor("#dce3ef")
WHITE       = colors.white

PAGE_W, PAGE_H = A4
MARGIN_L = 1.8 * cm
MARGIN_R = 1.8 * cm
MARGIN_T = 2.0 * cm
MARGIN_B = 2.2 * cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

OUTPUT_PATH = "/home/user/agency-agents/growth-hacker-report.pdf"
STORE_NAME  = "Ready For Take-Off Book"
REPORT_DATE = "June 7, 2026"
PREPARED_BY = "Growth Hacker Agent"

# ─── Page Number / Footer Canvas ─────────────────────────────────────────────
class PageTemplate:
    def __init__(self, total_pages=None):
        self.total_pages = total_pages

def on_page(canvas_obj, doc):
    canvas_obj.saveState()
    page_num = doc.page

    # Footer rule
    canvas_obj.setStrokeColor(DIVIDER)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(MARGIN_L, MARGIN_B - 4*mm, PAGE_W - MARGIN_R, MARGIN_B - 4*mm)

    # Footer left — store name
    canvas_obj.setFont("Helvetica", 7.5)
    canvas_obj.setFillColor(SUBTLE_GREY)
    canvas_obj.drawString(MARGIN_L, MARGIN_B - 9*mm, f"{STORE_NAME}  ·  Growth Analysis Report")

    # Footer right — page number
    canvas_obj.drawRightString(PAGE_W - MARGIN_R, MARGIN_B - 9*mm, f"Page {page_num}  ·  {REPORT_DATE}")

    canvas_obj.restoreState()


# ─── Custom Flowables ─────────────────────────────────────────────────────────
class RoundedBox(Flowable):
    """A filled rounded rectangle used as a section highlight box."""
    def __init__(self, width, height, fill_color, radius=6, border_color=None, border_width=0.5):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.radius = radius
        self.border_color = border_color or fill_color
        self.border_width = border_width

    def draw(self):
        self.canv.setFillColor(self.fill_color)
        self.canv.setStrokeColor(self.border_color)
        self.canv.setLineWidth(self.border_width)
        self.canv.roundRect(0, 0, self.width, self.height, self.radius, fill=1, stroke=1)


class SectionHeader(Flowable):
    """Bold left-bordered section title with optional subtitle."""
    def __init__(self, number, title, subtitle="", width=None):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.width = width or CONTENT_W
        self.height = 36 if subtitle else 28

    def draw(self):
        c = self.canv
        # Left accent bar
        c.setFillColor(ACCENT_BLUE)
        c.rect(0, 0, 3.5, self.height, fill=1, stroke=0)

        # Background
        c.setFillColor(SECTION_BG)
        c.rect(4, 0, self.width - 4, self.height, fill=1, stroke=0)

        # Number badge
        badge_x = 10
        badge_y = self.height / 2 - 7
        c.setFillColor(DARK_BLUE)
        c.roundRect(badge_x, badge_y, 18, 14, 3, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(badge_x + 9, badge_y + 4, str(self.number))

        # Title
        c.setFillColor(DARK_BLUE)
        c.setFont("Helvetica-Bold", 12)
        title_y = self.height / 2 - 4 if not self.subtitle else self.height - 17
        c.drawString(34, title_y, self.title)

        # Subtitle
        if self.subtitle:
            c.setFillColor(SUBTLE_GREY)
            c.setFont("Helvetica", 8.5)
            c.drawString(34, 6, self.subtitle)


class CoverHeader(Flowable):
    """Full-width dark-blue cover header block."""
    def __init__(self, width, store_name, date, prepared_by):
        Flowable.__init__(self)
        self.width = width
        self.store_name = store_name
        self.date = date
        self.prepared_by = prepared_by
        self.height = 88

    def draw(self):
        c = self.canv
        # Main background
        c.setFillColor(DARK_BLUE)
        c.rect(0, 0, self.width, self.height, fill=1, stroke=0)

        # Accent stripe at bottom of header
        c.setFillColor(ACCENT_BLUE)
        c.rect(0, 0, self.width, 4, fill=1, stroke=0)

        # Decorative right-side geometry
        c.setFillColor(MID_BLUE)
        c.roundRect(self.width - 70, 8, 60, 72, 8, fill=1, stroke=0)
        c.setFillColor(ACCENT_BLUE)
        c.roundRect(self.width - 55, 20, 35, 48, 6, fill=1, stroke=0)

        # Top label
        c.setFillColor(ACCENT_BLUE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(14, self.height - 16, "GROWTH ANALYSIS REPORT")

        # Store name
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(14, self.height - 42, self.store_name)

        # Date pill
        pill_x, pill_y, pill_w, pill_h = 14, 12, 78, 16
        c.setFillColor(ACCENT_BLUE)
        c.roundRect(pill_x, pill_y, pill_w, pill_h, 4, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(pill_x + 6, pill_y + 4.5, f"Date:  {self.date}")

        # Prepared by
        c.setFillColor(HexColor("#a0b4d6"))
        c.setFont("Helvetica", 8)
        c.drawString(100, 17, f"Prepared by: {self.prepared_by}")


class NorthStarBox(Flowable):
    """Highlighted calculation box for the North Star section."""
    def __init__(self, width, rows):
        Flowable.__init__(self)
        self.width = width
        self.rows = rows  # list of (label, value, is_highlight)
        self.row_h = 24
        self.padding = 14
        self.height = self.padding * 2 + self.row_h * len(rows) + 8

    def draw(self):
        c = self.canv

        # Outer box
        c.setFillColor(NORTH_STAR_BG)
        c.setStrokeColor(ACCENT_BLUE)
        c.setLineWidth(1.2)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=1)

        # Top accent bar
        c.setFillColor(DARK_BLUE)
        c.roundRect(0, self.height - 28, self.width, 28, 8, fill=1, stroke=0)
        c.rect(0, self.height - 28, self.width, 14, fill=1, stroke=0)

        # Title in accent bar
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(self.padding, self.height - 18, "NORTH STAR TARGET — Conversion to 2.0%")

        # Rows
        for i, (label, value, highlight) in enumerate(self.rows):
            y = self.height - 28 - self.padding - (i + 1) * self.row_h + 4
            row_bg = LIGHT_BLUE if highlight else WHITE
            c.setFillColor(row_bg)
            c.roundRect(self.padding - 4, y - 2, self.width - self.padding * 2 + 8, self.row_h - 4, 4, fill=1, stroke=0)

            c.setFillColor(DARK_BLUE if highlight else BODY_TEXT)
            c.setFont("Helvetica-Bold" if highlight else "Helvetica", 9.5 if highlight else 9)
            c.drawString(self.padding + 2, y + 5, label)

            c.setFillColor(DARK_BLUE if highlight else ACCENT_BLUE)
            c.setFont("Helvetica-Bold", 10 if highlight else 9.5)
            c.drawRightString(self.width - self.padding + 4, y + 5, value)


# ─── Style Definitions ────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "body": ParagraphStyle(
            "Body", fontName="Helvetica", fontSize=9.5, leading=15,
            textColor=BODY_TEXT, spaceAfter=6, leftIndent=0, alignment=TA_JUSTIFY
        ),
        "body_left": ParagraphStyle(
            "BodyLeft", fontName="Helvetica", fontSize=9.5, leading=15,
            textColor=BODY_TEXT, spaceAfter=4, leftIndent=0, alignment=TA_LEFT
        ),
        "headline": ParagraphStyle(
            "Headline", fontName="Helvetica-Bold", fontSize=13, leading=18,
            textColor=DARK_BLUE, spaceBefore=6, spaceAfter=8
        ),
        "diagnosis": ParagraphStyle(
            "Diagnosis", fontName="Helvetica", fontSize=10.5, leading=17,
            textColor=BODY_TEXT, spaceAfter=6, alignment=TA_JUSTIFY,
            backColor=LIGHT_BLUE, borderPad=10, leftIndent=10, rightIndent=10,
            borderRadius=4
        ),
        "root_cause_title": ParagraphStyle(
            "RootCauseTitle", fontName="Helvetica-Bold", fontSize=10, leading=14,
            textColor=DARK_BLUE, spaceBefore=10, spaceAfter=3
        ),
        "root_cause_body": ParagraphStyle(
            "RootCauseBody", fontName="Helvetica", fontSize=9.5, leading=15,
            textColor=BODY_TEXT, spaceAfter=5, leftIndent=12, alignment=TA_JUSTIFY
        ),
        "experiment_week": ParagraphStyle(
            "ExpWeek", fontName="Helvetica-Bold", fontSize=10, leading=14,
            textColor=ACCENT_BLUE, spaceBefore=12, spaceAfter=4
        ),
        "exp_title": ParagraphStyle(
            "ExpTitle", fontName="Helvetica-Bold", fontSize=10, leading=14,
            textColor=DARK_BLUE, spaceBefore=6, spaceAfter=2
        ),
        "exp_body": ParagraphStyle(
            "ExpBody", fontName="Helvetica", fontSize=9, leading=14,
            textColor=BODY_TEXT, spaceAfter=4, leftIndent=16
        ),
        "start_here_item": ParagraphStyle(
            "StartHere", fontName="Helvetica", fontSize=9.5, leading=15,
            textColor=DARK_BLUE, spaceAfter=4, leftIndent=14
        ),
        "table_header": ParagraphStyle(
            "TblHdr", fontName="Helvetica-Bold", fontSize=9, leading=12,
            textColor=WHITE, alignment=TA_CENTER
        ),
        "table_cell": ParagraphStyle(
            "TblCell", fontName="Helvetica", fontSize=9, leading=12,
            textColor=DARK_TEXT, alignment=TA_LEFT
        ),
        "table_cell_center": ParagraphStyle(
            "TblCellC", fontName="Helvetica", fontSize=9, leading=12,
            textColor=DARK_TEXT, alignment=TA_CENTER
        ),
        "caption": ParagraphStyle(
            "Caption", fontName="Helvetica-Oblique", fontSize=8, leading=11,
            textColor=SUBTLE_GREY, spaceAfter=8, alignment=TA_CENTER
        ),
    }
    return styles


# ─── Metrics Table ────────────────────────────────────────────────────────────
def build_metrics_table(styles):
    STATUS_COLORS = {
        "CRITICAL":     (RED_STATUS,    RED_BG),
        "Growing fast": (GREEN_STATUS,  GREEN_BG),
        "Healthy":      (GREEN_STATUS,  GREEN_BG),
        "Too low for traffic": (YELLOW_STATUS, YELLOW_BG),
        "Fixable":      (YELLOW_STATUS, YELLOW_BG),
    }

    headers = ["Metric", "Your Number", "Benchmark", "Status"]
    rows_data = [
        ("Sessions",           "306,959  (+104%)", "—",       "Growing fast"),
        ("Conversion rate",    "0.73%",            "2–3%",    "CRITICAL"),
        ("AOV",                "€56.09",           "—",       "Healthy"),
        ("Orders",             "2,590",            "—",       "Too low for traffic"),
        ("Returning customers","2.53%",            "20–30%",  "CRITICAL"),
        ("Add-to-cart rate",   "1.63%",            "8–12%",   "CRITICAL"),
        ("Cart → Purchase",    "53%",              "~65%",    "Fixable"),
    ]

    col_widths = [CONTENT_W * 0.30, CONTENT_W * 0.22, CONTENT_W * 0.18, CONTENT_W * 0.30]

    # Build header row
    header_row = [
        Paragraph(h, styles["table_header"]) for h in headers
    ]

    table_rows = [header_row]
    style_cmds = [
        # Header
        ("BACKGROUND",  (0, 0), (-1, 0), DARK_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, SECTION_BG]),
        ("FONTNAME",    (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, -1), 9),
        ("ALIGN",       (1, 1), (2, -1), "CENTER"),
        ("ALIGN",       (3, 1), (3, -1), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",  (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",(0, 0), (-1, -1), 8),
        ("GRID",        (0, 0), (-1, -1), 0.4, DIVIDER),
        ("LINEBELOW",   (0, 0), (-1, 0), 1.5, ACCENT_BLUE),
    ]

    for i, (metric, number, bench, status) in enumerate(rows_data):
        row_i = i + 1
        txt_color, bg_color = STATUS_COLORS.get(status, (SUBTLE_GREY, WHITE))

        status_para = Paragraph(
            f'<font color="#{txt_color.hexval()[2:]}"><b>{status}</b></font>',
            styles["table_cell_center"]
        )
        metric_para  = Paragraph(f"<b>{metric}</b>", styles["table_cell"])
        number_para  = Paragraph(number, styles["table_cell_center"])
        bench_para   = Paragraph(bench,  styles["table_cell_center"])

        table_rows.append([metric_para, number_para, bench_para, status_para])
        style_cmds.append(("BACKGROUND", (3, row_i), (3, row_i), bg_color))

    tbl = Table(table_rows, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(TableStyle(style_cmds))
    return tbl


# ─── Experiment Roadmap Entries ───────────────────────────────────────────────
def build_experiment_item(num, title, body_text, styles):
    """Returns a list of flowables for one numbered experiment."""
    col_widths = [22, CONTENT_W - 22]

    num_para  = Paragraph(
        f'<font color="#ffffff"><b>{num}</b></font>',
        ParagraphStyle("NumBadge", fontName="Helvetica-Bold", fontSize=9,
                       alignment=TA_CENTER, leading=12)
    )
    title_para = Paragraph(title, styles["exp_title"])
    body_para  = Paragraph(body_text, styles["exp_body"])

    num_cell_style = [
        ("BACKGROUND", (0, 0), (0, 0), DARK_BLUE),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING",(0, 0), (0, 0), 3),
        ("LEFTPADDING", (1, 0), (1, 0), 8),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
    ]

    tbl = Table(
        [[num_para, [title_para, body_para]]],
        colWidths=col_widths,
    )
    tbl.setStyle(TableStyle(num_cell_style))
    return tbl


# ─── Main Build Function ──────────────────────────────────────────────────────
def build_report():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T,
        bottomMargin=MARGIN_B,
        title=f"Growth Analysis Report — {STORE_NAME}",
        author=PREPARED_BY,
        subject="E-commerce Growth Analysis",
    )

    styles = build_styles()
    story  = []

    # ── Cover Header ──────────────────────────────────────────────────────────
    story.append(CoverHeader(CONTENT_W, STORE_NAME, REPORT_DATE, PREPARED_BY))
    story.append(Spacer(1, 14))

    # ── Section 1: Headline Diagnosis ─────────────────────────────────────────
    story.append(SectionHeader(1, "HEADLINE DIAGNOSIS", "Top-level performance snapshot"))
    story.append(Spacer(1, 8))

    diag_text = (
        "You have a <b>traffic success / conversion failure</b> problem. Your SEO brought in "
        "<b>307K sessions</b> — that's excellent. But you're converting at <b>0.73%</b>, roughly "
        "3× below the e-commerce average of 2–3%. You're essentially leaving "
        "<b>~€300K/year on the table</b> with your current traffic volume."
    )

    # Diagnosis box via Table (reliable background rendering)
    diag_para = Paragraph(diag_text, ParagraphStyle(
        "DiagInner", fontName="Helvetica", fontSize=10.5, leading=17,
        textColor=DARK_BLUE, alignment=TA_JUSTIFY
    ))
    diag_tbl = Table([[diag_para]], colWidths=[CONTENT_W])
    diag_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LIGHT_BLUE),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("TOPPADDING",    (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LINEAFTER",     (0, 0), (0, -1), 4, ACCENT_BLUE),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    story.append(diag_tbl)
    story.append(Spacer(1, 16))

    # ── Section 2: Key Metrics Table ──────────────────────────────────────────
    story.append(SectionHeader(2, "KEY METRICS", "Performance vs. industry benchmarks"))
    story.append(Spacer(1, 8))
    story.append(build_metrics_table(styles))
    story.append(Paragraph(
        "Status: <font color='#c0392b'><b>CRITICAL</b></font> = immediate action required  |  "
        "<font color='#27ae60'><b>Healthy / Growing</b></font> = maintain  |  "
        "<font color='#d68910'><b>Fixable</b></font> = near-term opportunity",
        ParagraphStyle("Legend", fontName="Helvetica-Oblique", fontSize=7.5,
                       textColor=SUBTLE_GREY, alignment=TA_CENTER, spaceBefore=5, spaceAfter=14)
    ))

    # ── Section 3: Root Causes ────────────────────────────────────────────────
    story.append(SectionHeader(3, "THE 3 ROOT CAUSES", "Why conversions are failing"))
    story.append(Spacer(1, 10))

    root_causes = [
        (
            "1.  SEO Traffic Is Informational, Not Transactional",
            "Your #1 landing page — <i>/products/ready-for-take-off-book</i> — got 113,700 sessions "
            "but almost none converted. Your blog articles (pilot recruitment, A320 type rating) are "
            "pulling in aspiring pilots who are <b>researching, not ready to buy</b>. Top-of-funnel "
            "traffic landed directly on the buy page with no warm-up. That kills conversion."
        ),
        (
            "2.  Cart Abandonment Is a Leak Nobody Is Plugging",
            "5,017 added to cart → 2,267 completed = <b>2,750 abandoned carts</b>. "
            "At €56 AOV, that's <b>€154,000 of near-purchases you're not recovering</b>."
        ),
        (
            "3.  Zero Retention — No Second Product to Buy",
            "The cohort analysis shows <b>0% repeat purchase after month 1</b> across every cohort. "
            "One product, customers buy it once, and they're gone. "
            "The email list is being massively underutilised."
        ),
    ]

    for title, body in root_causes:
        story.append(Paragraph(title, styles["root_cause_title"]))
        story.append(Paragraph(body,  styles["root_cause_body"]))
    story.append(Spacer(1, 8))

    # ── Section 4: Experiment Roadmap ─────────────────────────────────────────
    story.append(SectionHeader(4, "PRIORITIZED EXPERIMENT ROADMAP", "Ordered by impact and speed to implement"))
    story.append(Spacer(1, 10))

    # Phase label
    def phase_label(text, color=ACCENT_BLUE):
        label_tbl = Table(
            [[Paragraph(f"<b>{text}</b>", ParagraphStyle(
                "PhaseLabel", fontName="Helvetica-Bold", fontSize=8.5,
                textColor=WHITE, alignment=TA_LEFT, leading=12
            ))]],
            colWidths=[CONTENT_W]
        )
        label_tbl.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), color),
            ("LEFTPADDING",   (0, 0), (-1, -1), 10),
            ("TOPPADDING",    (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("ROUNDEDCORNERS", [4, 4, 0, 0]),
        ]))
        return label_tbl

    # Phase 1
    story.append(phase_label("THIS WEEK — Highest Leverage, Zero Cost", DARK_BLUE))

    experiments_w1 = [
        (1, "Abandoned Cart Email Sequence",
         "Set up a 3-email flow in Shopify (1 hr / 24 hr / 72 hr). Recovering 20% of your 2,750 "
         "abandoned carts = +550 orders = <b>+€30K</b>. This is the single biggest win available right now."),
        (2, "Add Apple Pay / Google Pay to Checkout",
         "Traffic is predominantly mobile. One-tap payment removes the biggest mobile checkout friction. "
         "Expected CVR lift: <b>+0.2–0.4%</b>."),
        (3, "Sticky 'Buy Now' Button on Mobile Product Page",
         "113K sessions hit that page. A persistent CTA costs nothing to test and directly addresses "
         "the 1.63% add-to-cart rate."),
    ]
    for num, title, body in experiments_w1:
        story.append(Spacer(1, 6))
        story.append(build_experiment_item(num, title, body, styles))

    story.append(Spacer(1, 12))
    story.append(phase_label("NEXT 2–4 WEEKS — Conversion Funnel Fixes", MID_BLUE))

    experiments_w2 = [
        (4, "Email Capture on Blog Articles",
         "The pilot recruitment blog gets 14K sessions from perfect prospects. Add a lead magnet "
         "mid-article: <i>'Free: The 7 Questions Airlines Always Ask (and How to Answer Them).'</i> "
         "Even 5% capture = 700 emails/month. Nurture with a 7-day sequence ending in a purchase offer. "
         "Estimated: <b>+150–300 orders/month</b>."),
        (5, "Post-Purchase Upsell",
         "Add an instant upsell after checkout: <i>'Complete your preparation — add the ebook for €X.'</i> "
         "The ebook and mock interview products barely register in orders despite existing. Bundle them. "
         "This lifts AOV from <b>€56 toward €80+</b>."),
        (6, "Product Page Social Proof Overhaul",
         "Add: number of pilots who passed using the book, specific airline logos, a money-back guarantee "
         "badge, and 3–5 video or named testimonials. The page is getting 113K sessions — even a 0.5% CVR "
         "lift = <b>+565 orders</b>."),
    ]
    for num, title, body in experiments_w2:
        story.append(Spacer(1, 6))
        story.append(build_experiment_item(num, title, body, styles))

    story.append(Spacer(1, 12))
    story.append(phase_label("MONTH 2+ — Scale What's Working", ACCENT_BLUE))

    experiments_m2 = [
        (7, "Facebook / Instagram Retargeting",
         "Already getting €21.4K from Facebook organically. Set up retargeting audiences: product page "
         "visitors who didn't buy, blog readers, email list. At current traffic volume, retargeting should "
         "generate <b>€5–10K/month</b> at low CAC."),
        (8, "TikTok — Fix or Kill",
         "4.2K sessions, ~€96 in sales. Either invest in it properly (organic content strategy) or kill it. "
         "Don't leave it as a half-measure."),
        (9, "Create a Second Product",
         "A subscription, course, or community (€99–199) targeting the same audience. Even 5% of your 2,590 "
         "existing customers buying a second product = <b>€13–26K incremental revenue</b> with zero new "
         "traffic needed."),
    ]
    for num, title, body in experiments_m2:
        story.append(Spacer(1, 6))
        story.append(build_experiment_item(num, title, body, styles))

    story.append(Spacer(1, 18))

    # ── Section 5: North Star ─────────────────────────────────────────────────
    story.append(SectionHeader(5, "NORTH STAR TARGET", "The financial upside of fixing the funnel"))
    story.append(Spacer(1, 10))

    ns_rows = [
        ("Current state:  306,000 sessions × 0.73% CVR × €56 AOV", "~€125,000 / year", False),
        ("Target state:   306,000 sessions × 2.00% CVR × €68 AOV", "~€416,000 / year", False),
        ("Potential upside — same traffic, fixed funnel",           "+€291,000 / year",  True),
    ]
    story.append(NorthStarBox(CONTENT_W, ns_rows))
    story.append(Spacer(1, 18))

    # ── Section 6: Start Here ─────────────────────────────────────────────────
    story.append(SectionHeader(6, "START HERE — IN ORDER", "Immediate actions for this week"))
    story.append(Spacer(1, 10))

    start_items = [
        ("TODAY",      "Activate abandoned cart emails in Shopify  (built-in, free)"),
        ("THIS WEEK",  "Enable Apple Pay / Google Pay in checkout settings"),
        ("THIS WEEK",  "Add email capture + lead magnet to blog articles"),
        ("NEXT WEEK",  "Run a mobile UX audit of your product page — have someone film themselves trying to buy on iPhone"),
    ]

    for i, (timing, action) in enumerate(start_items, 1):
        row_bg = LIGHT_BLUE if i % 2 == 0 else WHITE
        timing_para = Paragraph(
            f'<font color="#1a2f5e"><b>{timing}</b></font>',
            ParagraphStyle("Timing", fontName="Helvetica-Bold", fontSize=8.5,
                           alignment=TA_CENTER, leading=12, textColor=DARK_BLUE)
        )
        action_para = Paragraph(action, ParagraphStyle(
            "Action", fontName="Helvetica", fontSize=9.5, leading=14, textColor=BODY_TEXT
        ))
        row_tbl = Table(
            [[Paragraph(f"<b>{i}</b>", ParagraphStyle(
                "StepNum", fontName="Helvetica-Bold", fontSize=10,
                textColor=WHITE, alignment=TA_CENTER, leading=13
            )), timing_para, action_para]],
            colWidths=[20, CONTENT_W * 0.18, CONTENT_W - 20 - CONTENT_W * 0.18]
        )
        row_tbl.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), DARK_BLUE),
            ("BACKGROUND",    (1, 0), (1, 0), ACCENT_BLUE),
            ("BACKGROUND",    (2, 0), (2, 0), row_bg),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LEFTPADDING",   (0, 0), (0, 0), 4),
            ("LEFTPADDING",   (2, 0), (2, 0), 10),
            ("GRID",          (0, 0), (-1, -1), 0.3, DIVIDER),
        ]))
        story.append(row_tbl)
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 14))

    # Closing statement
    closing_tbl = Table(
        [[Paragraph(
            "<b>The traffic is there. The audience is right. The funnel just has holes in it.</b>",
            ParagraphStyle("Closing", fontName="Helvetica-Bold", fontSize=11, leading=16,
                           textColor=DARK_BLUE, alignment=TA_CENTER)
        )]],
        colWidths=[CONTENT_W]
    )
    closing_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LIGHT_BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
        ("LINEABOVE",     (0, 0), (-1, 0), 3, ACCENT_BLUE),
        ("LINEBELOW",     (0, -1), (-1, -1), 3, ACCENT_BLUE),
    ]))
    story.append(closing_tbl)

    # ── Build ─────────────────────────────────────────────────────────────────
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"Report saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_report()
