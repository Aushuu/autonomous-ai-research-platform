import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


class ReportAgent:

    def generate_pdf(
        self,
        topic,
        report_text,
        chart_paths,
        metrics,
        references
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        pdf_path = (
            f"reports/"
            f"{topic.replace(' ', '_')}_report.pdf"
        )

        doc = SimpleDocTemplate(pdf_path)

        styles = getSampleStyleSheet()

        content = []

        # -------------------------
        # TITLE PAGE
        # -------------------------

        title = Paragraph(
            "AUTONOMOUS AI RESEARCH REPORT",
            styles["Title"]
        )

        content.append(title)

        content.append(
            Spacer(1, 20)
        )

        topic_para = Paragraph(
            f"<b>Topic:</b> {topic}",
            styles["BodyText"]
        )

        content.append(topic_para)

        date_para = Paragraph(
            f"<b>Generated:</b> {datetime.now()}",
            styles["BodyText"]
        )

        content.append(date_para)

        content.append(
            Spacer(1, 30)
        )

        # -------------------------
        # EXECUTIVE SUMMARY
        # -------------------------

        summary_title = Paragraph(
            "EXECUTIVE SUMMARY",
            styles["Heading1"]
        )

        content.append(summary_title)

        content.append(
            Spacer(1, 10)
        )

        report_para = Paragraph(
            report_text.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )

        content.append(report_para)

        content.append(
            PageBreak()
        )

        # -------------------------
        # METRICS TABLE
        # -------------------------

        metrics_title = Paragraph(
            "AI METRICS",
            styles["Heading1"]
        )

        content.append(metrics_title)

        content.append(
            Spacer(1, 10)
        )

        table_data = [
            ["Metric", "Score"],
            ["Advantages", metrics.get("advantages", 0)],
            ["Challenges", metrics.get("challenges", 0)],
            ["Future Trends", metrics.get("future_trends", 0)],
            ["Market Growth", metrics.get("market_growth", 0)],
        ]

        table = Table(table_data)

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ])
        )

        content.append(table)

        content.append(
            Spacer(1, 20)
        )

        # -------------------------
        # CHARTS SECTION
        # -------------------------

        chart_title = Paragraph(
            "VISUAL ANALYSIS",
            styles["Heading1"]
        )

        content.append(chart_title)

        content.append(
            Spacer(1, 10)
        )

        for chart_path in chart_paths:

            if os.path.exists(chart_path):

                chart = Image(
                    chart_path,
                    width=400,
                    height=250
                )

                content.append(chart)

                content.append(
                    Spacer(1, 15)
                )

        # -------------------------
        # REFERENCES SECTION
        # -------------------------

        content.append(
            PageBreak()
        )

        content.append(
            Paragraph(
                "REFERENCES",
                styles["Heading1"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        for index, ref in enumerate(
            references,
            start=1
        ):

            reference_text = f"""
            {index}. <b>{ref['title']}</b><br/>
            {ref['url']}
            """

            content.append(
                Paragraph(
                    reference_text,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 8)
            )

        # -------------------------
        # BUILD PDF
        # -------------------------

        doc.build(content)

        return pdf_path