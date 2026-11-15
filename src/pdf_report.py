from reportlab.platypus import *

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(

    novelty,

    category,

    keywords,

    analysis

):

    doc = SimpleDocTemplate(
        "Patent_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "Patent Novelty Report",
            styles["Title"]
        ),

        Paragraph(
            f"Novelty Score: {novelty}%",
            styles["BodyText"]
        ),

        Paragraph(
            f"Category: {category}",
            styles["BodyText"]
        ),

        Paragraph(
            f"Keywords: {', '.join(keywords)}",
            styles["BodyText"]
        ),

        Paragraph(
            analysis,
            styles["BodyText"]
        )
    ]

    doc.build(content)