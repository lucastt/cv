#!/usr/bin/env python3
"""
Usage: python generate_cv.py <input.html> <output_dir>

Parses Lucas Thiesen's CV HTML and renders it as a styled PDF.
Sections are fixed; styles are hardcoded. Only content is read from HTML.
"""

import sys
import os
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString, Tag

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
)

# ── Arguments ─────────────────────────────────────────────────────────────────
if len(sys.argv) != 3:
    print("Usage: python generate_cv.py <input.html> <output_dir>")
    sys.exit(1)

input_html = sys.argv[1]
output_dir = sys.argv[2]

if not os.path.isfile(input_html):
    print(f"Error: input file '{input_html}' not found.")
    sys.exit(1)

if not os.path.isdir(output_dir):
    print(f"Error: output directory '{output_dir}' does not exist.")
    sys.exit(1)

today = datetime.today()
filename = f"lucas-thiesen-cv-{today.day:02d}-{today.month:02d}-{today.year}.pdf"
output_path = os.path.join(output_dir, filename)

# ── Colours (from styles.css) ─────────────────────────────────────────────────
BODY_TEXT  = colors.HexColor("#595959")
HEADING    = colors.HexColor("#222222")
H2_COLOR   = colors.HexColor("#393939")
LINK_COLOR = colors.HexColor("#3399cc")
HR_COLOR   = colors.HexColor("#e5e5e5")
MID_GREY   = colors.HexColor("#777777")
TECH_GREY  = colors.HexColor("#999999")

# ── Page layout ───────────────────────────────────────────────────────────────
L_MARGIN = 13 * mm
R_MARGIN = 13 * mm
T_MARGIN = 11 * mm
B_MARGIN = 11 * mm

# ── Styles ────────────────────────────────────────────────────────────────────
base = ParagraphStyle(
    "base", fontName="Helvetica", fontSize=9,
    leading=13, textColor=BODY_TEXT,
    spaceAfter=0, spaceBefore=0,
)

def s(name, **kw):
    return ParagraphStyle(name, parent=base, **kw)

S = {
    "name":         s("name", fontName="Helvetica-Bold", fontSize=21, leading=24, textColor=HEADING, spaceAfter=1),
    "tagline":      s("tagline", fontSize=9, textColor=MID_GREY, spaceAfter=0),
    "section":      s("section", fontName="Helvetica-Bold", fontSize=8.5, leading=10, textColor=LINK_COLOR, spaceBefore=7, spaceAfter=1),
    "summary":      s("summary", fontSize=9, leading=13, textColor=BODY_TEXT, spaceAfter=2),
    "company":      s("company", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=H2_COLOR, spaceBefore=6, spaceAfter=0),
    "company_desc": s("company_desc", fontSize=8.5, textColor=MID_GREY, leading=11.5, spaceAfter=1),
    "role":         s("role", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=HEADING, spaceBefore=4, spaceAfter=0),
    "role_context": s("role_context", fontSize=8.5, textColor=MID_GREY, leading=12, spaceBefore=1, spaceAfter=2),
    "bullet":       s("bullet", fontSize=8.8, leading=12.5, leftIndent=8, textColor=BODY_TEXT, spaceAfter=1),
    "tech":         s("tech", fontSize=8, textColor=TECH_GREY, leading=11, leftIndent=8, spaceBefore=1, spaceAfter=0),
    "skill_label":  s("skill_label", fontSize=8.8, leading=12, textColor=BODY_TEXT, spaceAfter=1),
    "edu_title":    s("edu_title", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=HEADING, spaceAfter=0),
    "edu_sub":      s("edu_sub", fontSize=8.5, textColor=MID_GREY, leading=11, spaceAfter=0),
}

# ── ReportLab helpers ─────────────────────────────────────────────────────────
def rule():
    return HRFlowable(width="100%", thickness=1, color=HR_COLOR, spaceBefore=1, spaceAfter=3)

def section_header(title):
    return [Paragraph(title.upper(), S["section"]), rule()]

def sp(h=1):
    return Spacer(1, h * mm)

# ── HTML → ReportLab markup ───────────────────────────────────────────────────
def node_to_rl(node):
    """Recursively convert a BeautifulSoup node to ReportLab XML markup string."""
    if isinstance(node, NavigableString):
        text = str(node)
        # Escape ReportLab XML special chars, preserve HTML entities
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;").replace(">", "&gt;")
        return text

    if not isinstance(node, Tag):
        return ""

    inner = "".join(node_to_rl(c) for c in node.children)
    tag = node.name

    if tag in ("strong", "b"):
        return f"<b>{inner}</b>"
    elif tag in ("em", "i"):
        return f"<i>{inner}</i>"
    elif tag == "a":
        return f"<font color='#3399cc'>{inner}</font>"
    elif tag == "br":
        return " "
    else:
        return inner

def elem_text(el):
    """Get ReportLab-safe markup from a BeautifulSoup element."""
    return "".join(node_to_rl(c) for c in el.children).strip()

def is_tech_li(li):
    """Detect the Technologies line — li containing strong > em."""
    strong = li.find("strong")
    if strong and strong.find("em"):
        return True
    return False

def is_role_p(p):
    """Detect a role paragraph: contains strong and em side by side."""
    return bool(p.find("strong")) and bool(p.find("em"))

# ── Parse HTML ────────────────────────────────────────────────────────────────
with open(input_html, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

wrapper = soup.find("div", class_="wrapper")
elements = [el for el in wrapper.children if isinstance(el, Tag)]

# ── Known fixed section IDs ───────────────────────────────────────────────────
SECTION_IDS = {"summary", "skills", "engineering-experience", "education"}
COMPANY_IDS = {"delivery-hero", "zalando", "quinto-andar", "3778", "certi"}

# ── Build story ───────────────────────────────────────────────────────────────
story = []

# Name from h1
h1 = wrapper.find("h1")
name_text = h1.get_text(strip=True)
name_link = h1.find("a")
url = name_link["href"] if name_link else ""

story += [
    Paragraph(name_text, S["name"]),
    Paragraph(
        f"Senior Software Engineer  &nbsp;·&nbsp;  "
        f"<font color='#3399cc'>{url.replace('https://', '')}</font>",
        S["tagline"]
    ),
    sp(2.5),
]

# Walk remaining elements
i = 0
while i < len(elements):
    el = elements[i]

    # ── Section headers (h2 with hr following) ────────────────────────────────
    if el.name == "h2" and el.get("id") in SECTION_IDS:
        title = el.get_text(strip=True)
        story += section_header(title)
        i += 1
        # Skip the hr that follows
        if i < len(elements) and elements[i].name == "hr":
            i += 1
        continue

    # ── Company headers (h2 with link, no hr) ────────────────────────────────
    if el.name == "h2" and el.get("id") in COMPANY_IDS:
        company_name = el.get_text(strip=True)

        # Collect everything belonging to this company until the next h2
        company_els = []
        i += 1
        while i < len(elements) and elements[i].name != "h2":
            company_els.append(elements[i])
            i += 1

        # First p after company h2 = company description (no strong/em role pattern)
        ci = 0
        company_desc = ""
        if ci < len(company_els) and company_els[ci].name == "p" and not is_role_p(company_els[ci]):
            company_desc = elem_text(company_els[ci])
            ci += 1

        # Build company block: header + desc + first role grouped together
        # then each subsequent role as its own KeepTogether
        company_header = [
            Paragraph(company_name, S["company"]),
            Paragraph(company_desc, S["company_desc"]) if company_desc else None,
        ]
        company_header = [x for x in company_header if x]

        roles = []  # list of lists of flowables, each = one role block

        while ci < len(company_els):
            cel = company_els[ci]

            # Role paragraph (strong + em)
            if cel.name == "p" and is_role_p(cel):
                role_markup = elem_text(cel)
                # Split into title and dates: strong is title, em is dates
                strong = cel.find("strong")
                ems = cel.find_all("em")
                title_parts = []
                if strong:
                    title_parts.append(f"<b>{strong.get_text()}</b>")
                for em in ems:
                    title_parts.append(f"<font color='#999999'>{em.get_text()}</font>")
                role_line_markup = "  ".join(title_parts)

                role_block = [Paragraph(role_line_markup, S["role"])]
                ci += 1

                # Role context paragraph (plain p, no role pattern)
                if ci < len(company_els) and company_els[ci].name == "p" and not is_role_p(company_els[ci]):
                    ctx = elem_text(company_els[ci])
                    role_block.append(Paragraph(ctx, S["role_context"]))
                    ci += 1

                # ul of bullets
                if ci < len(company_els) and company_els[ci].name == "ul":
                    ul = company_els[ci]
                    for li in ul.find_all("li", recursive=False):
                        if is_tech_li(li):
                            # Full text of li, strip the "Technologies:" label prefix
                            full = li.get_text(strip=True)
                            tech_text = full.replace("Technologies:", "").strip().lstrip(":").strip()
                            role_block.append(
                                Paragraph(
                                    f"<font color='#999999'><i>Technologies:  {tech_text}</i></font>",
                                    S["tech"]
                                )
                            )
                        else:
                            li_markup = elem_text(li)
                            role_block.append(
                                Paragraph(f"<font color='#aaaaaa'>–</font>  {li_markup}", S["bullet"])
                            )
                    ci += 1

                roles.append(role_block)

            # Plain p with no role pattern (e.g. Quinto Andar inline role)
            elif cel.name == "p" and not is_role_p(cel):
                markup = elem_text(cel)
                roles.append([Paragraph(markup, S["company_desc"])])
                ci += 1

            # Bare ul (e.g. Quinto Andar bullets directly after company desc)
            elif cel.name == "ul":
                block = []
                for li in cel.find_all("li", recursive=False):
                    if is_tech_li(li):
                        full = li.get_text(strip=True)
                        tech_text = full.replace("Technologies:", "").strip().lstrip(":").strip()
                        block.append(
                            Paragraph(
                                f"<font color='#999999'><i>Technologies:  {tech_text}</i></font>",
                                S["tech"]
                            )
                        )
                    else:
                        li_markup = elem_text(li)
                        block.append(
                            Paragraph(f"<font color='#aaaaaa'>–</font>  {li_markup}", S["bullet"])
                        )
                roles.append(block)
                ci += 1

            else:
                ci += 1

        # First role keeps company header together with it (prevents orphan header)
        if roles:
            story.append(KeepTogether(company_header + roles[0]))
            for role_block in roles[1:]:
                story.append(KeepTogether(role_block))
        else:
            story.append(KeepTogether(company_header))

        continue

    # ── HR (standalone, between sections) ────────────────────────────────────
    if el.name == "hr":
        i += 1
        continue

    # ── Summary / Skills paragraphs ───────────────────────────────────────────
    if el.name == "p":
        markup = elem_text(el)
        # Skill lines have a leading strong tag
        if el.find("strong") and not el.find("em"):
            story.append(Paragraph(markup, S["skill_label"]))
        else:
            story.append(Paragraph(markup, S["summary"]))
        i += 1
        continue

    # ── Education ─────────────────────────────────────────────────────────────
    # Education p contains strong (degree) and em (dates) and a (institution)
    # Handled generically above as summary; override here isn't needed since
    # section_header for education is emitted before the p elements reach here.

    i += 1

# ── Build PDF ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=L_MARGIN,
    rightMargin=R_MARGIN,
    topMargin=T_MARGIN,
    bottomMargin=B_MARGIN,
    title=f"{name_text} — CV",
    author=name_text,
)
doc.build(story)
print(f"Done. Output: {output_path}")
