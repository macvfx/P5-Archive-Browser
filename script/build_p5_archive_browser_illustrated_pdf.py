#!/usr/bin/env python3
"""Build the illustrated P5 Archive Browser workflow guide as a polished PDF."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    Image,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


TITLE = "P5 Archive Browser - Illustrated Workflow Guide"
BLUE = colors.HexColor("#245A92")
LIGHT_BLUE = colors.HexColor("#E8F1FF")
GREEN = colors.HexColor("#247A46")
LIGHT_GREEN = colors.HexColor("#EAF8EF")
AMBER = colors.HexColor("#9A650F")
LIGHT_GRAY = colors.HexColor("#F4F6F8")
DARK = colors.HexColor("#17263A")
MID = colors.HexColor("#52657A")


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def normalize_text(value: str) -> str:
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u21e5": " | ",
        "\u25b8": " > ",
        "\u2318": "Cmd-",
    }
    for source, destination in replacements.items():
        value = value.replace(source, destination)
    return value


def inline_markup(value: str) -> str:
    value = normalize_text(value)
    tokens: list[str] = []

    def hold(code: str) -> str:
        tokens.append(f'<font name="Courier">{html.escape(code)}</font>')
        return f"@@TOKEN{len(tokens) - 1}@@"

    value = re.sub(r"`([^`]+)`", lambda match: hold(match.group(1)), value)
    value = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: match.group(1),
        value,
    )
    value = html.escape(value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", value)
    for index, token in enumerate(tokens):
        value = value.replace(f"@@TOKEN{index}@@", token)
    return value


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "GuideTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=27,
            textColor=DARK,
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "h2": ParagraphStyle(
            "GuideH2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=19,
            textColor=BLUE,
            spaceBefore=15,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "GuideH3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=GREEN,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "GuideBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.3,
            leading=13,
            textColor=DARK,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "GuideMeta",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=MID,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "list": ParagraphStyle(
            "GuideList",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.1,
            leading=12.5,
            textColor=DARK,
            leftIndent=18,
            firstLineIndent=-10,
            spaceAfter=3,
        ),
        "caption": ParagraphStyle(
            "GuideCaption",
            parent=base["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8.2,
            leading=10,
            textColor=MID,
            alignment=TA_CENTER,
            spaceBefore=3,
            spaceAfter=9,
        ),
        "code": ParagraphStyle(
            "GuideCode",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.8,
            leading=10,
            textColor=DARK,
            backColor=LIGHT_GRAY,
            borderColor=colors.HexColor("#D5DBE3"),
            borderWidth=0.5,
            borderPadding=7,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "table_header": ParagraphStyle(
            "GuideTableHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.3,
            leading=9,
            textColor=colors.white,
        ),
        "table": ParagraphStyle(
            "GuideTable",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.1,
            leading=9,
            textColor=DARK,
        ),
    }


def table_widths(column_count: int, available: float) -> list[float]:
    if column_count == 4:
        proportions = [0.18, 0.22, 0.30, 0.30]
    elif column_count == 3:
        proportions = [0.20, 0.38, 0.42]
    elif column_count == 2:
        proportions = [0.30, 0.70]
    else:
        proportions = [1 / column_count] * column_count
    return [available * value for value in proportions]


def build_table(rows: list[list[str]], available: float, style_map: dict[str, ParagraphStyle]) -> Table:
    column_count = max(len(row) for row in rows)
    padded = [row + [""] * (column_count - len(row)) for row in rows]
    content = []
    for row_index, row in enumerate(padded):
        style = style_map["table_header"] if row_index == 0 else style_map["table"]
        content.append([Paragraph(inline_markup(cell), style) for cell in row])
    table = Table(
        content,
        colWidths=table_widths(column_count, available),
        repeatRows=1,
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), BLUE),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
                ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#B9C4D0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def image_flowable(path: Path, available_width: float, max_height: float) -> Image:
    with PILImage.open(path) as source:
        width, height = source.size
    scale = min(available_width / width, max_height / height)
    return Image(str(path), width=width * scale, height=height * scale)


def parse_markdown(source: Path, available_width: float, style_map: dict[str, ParagraphStyle]) -> list:
    lines = source.read_text(encoding="utf-8").splitlines()
    story: list = []
    paragraph: list[str] = []
    index = 0

    def flush_paragraph() -> None:
        if not paragraph:
            return
        text = " ".join(item.strip() for item in paragraph).strip()
        if text:
            target_style = style_map["meta"] if text.startswith("**Status:**") else style_map["body"]
            story.append(Paragraph(inline_markup(text), target_style))
        paragraph.clear()

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip()
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(normalize_text(lines[index]))
                index += 1
            if language.lower() == "mermaid":
                code_lines.insert(0, "Mermaid source:")
            story.append(Preformatted("\n".join(code_lines), style_map["code"]))
            index += 1
            continue

        image_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if image_match:
            flush_paragraph()
            image_path = (source.parent / image_match.group(2)).resolve()
            if not image_path.is_file():
                raise FileNotFoundError(f"Missing illustration: {image_path}")
            story.append(Spacer(1, 4))
            story.append(image_flowable(image_path, available_width, 7.3 * inch))
            if image_match.group(1):
                story.append(Paragraph(inline_markup(image_match.group(1)), style_map["caption"]))
            index += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            raw_rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                raw_rows.append(cells)
                index += 1
            rows = [
                row
                for row in raw_rows
                if not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in row)
            ]
            story.append(build_table(rows, available_width, style_map))
            story.append(Spacer(1, 7))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            story.append(Paragraph(inline_markup(stripped[2:]), style_map["title"]))
            story.append(HRFlowable(width="54%", thickness=2, color=BLUE, spaceAfter=10))
            index += 1
            continue

        if stripped.startswith(("**Status:**", "**Canonical detail:**", "**Audience:**")):
            flush_paragraph()
            story.append(Paragraph(inline_markup(stripped), style_map["meta"]))
            index += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            if story and len(story) > 10 and stripped in {
                "## 1. Build a trusted local catalog",
                "## 2. Find the tape and inspect the evidence",
                "## 3. Restore one whole folder through P5",
            }:
                story.append(PageBreak())
            story.append(Paragraph(inline_markup(stripped[3:]), style_map["h2"]))
            index += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            story.append(Paragraph(inline_markup(stripped[4:]), style_map["h3"]))
            index += 1
            continue

        list_match = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if list_match:
            flush_paragraph()
            indent, marker, text = list_match.groups()
            level = max(0, len(indent) // 2)
            if marker in {"-", "*"}:
                marker_text = "&#8226;"
            else:
                marker_text = html.escape(marker)
            list_style = ParagraphStyle(
                f"ListLevel{level}",
                parent=style_map["list"],
                leftIndent=18 + level * 14,
            )
            story.append(Paragraph(f"{marker_text} {inline_markup(text)}", list_style))
            index += 1
            continue

        if stripped in {"---", "***"}:
            flush_paragraph()
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#C8D0DA")))
            story.append(Spacer(1, 5))
            index += 1
            continue

        if not stripped:
            flush_paragraph()
            index += 1
            continue

        paragraph.append(line)
        index += 1

    flush_paragraph()
    return story


class NumberedDocument(SimpleDocTemplate):
    def afterInit(self) -> None:
        self.title_text = TITLE


def draw_page(canvas, document) -> None:
    canvas.saveState()
    canvas.setTitle(TITLE)
    canvas.setAuthor("P5 Archive Browser documentation")
    canvas.setStrokeColor(colors.HexColor("#D5DBE3"))
    canvas.setLineWidth(0.5)
    canvas.line(document.leftMargin, 0.48 * inch, letter[0] - document.rightMargin, 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MID)
    canvas.drawString(document.leftMargin, 0.30 * inch, "P5 Archive Browser - Illustrated Workflow Guide")
    page = str(canvas.getPageNumber())
    canvas.drawRightString(letter[0] - document.rightMargin, 0.30 * inch, page)
    canvas.restoreState()


def main() -> int:
    args = arguments()
    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input guide does not exist: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)

    left = right = 0.62 * inch
    document = NumberedDocument(
        str(output),
        pagesize=letter,
        leftMargin=left,
        rightMargin=right,
        topMargin=0.55 * inch,
        bottomMargin=0.62 * inch,
        title=TITLE,
        author="P5 Archive Browser documentation",
        subject="Illustrated import, search, retrieval, restore, and recovery workflows",
    )
    available_width = letter[0] - left - right
    story = parse_markdown(source, available_width, styles())
    document.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
