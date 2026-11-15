from src.similarity import novelty_score
from src.classifier import predict_category
from src.keywords import extract_keywords

def generate_analysis(text):

    novelty = novelty_score(text)

    category = predict_category(text)

    keywords = extract_keywords(text)

    return f"""
Patent Analysis Report

Novelty Score: {novelty}%

Category: {category}

Key Technologies:
{', '.join(keywords)}

Interpretation:

This patent belongs to the {category}
domain.

The proposed idea achieved a novelty
score of {novelty}% based on semantic
comparison against the patent database.

The main concepts identified are:
{', '.join(keywords)}.

Further manual patent examination is
recommended before filing.
"""
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(text, report_text):

    pdf = SimpleDocTemplate(
        "Patent_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "Patent Novelty Report",
            styles["Title"]
        ),

        Paragraph(
            text,
            styles["BodyText"]
        ),

        Paragraph(
            report_text,
            styles["BodyText"]
        )

    ]

    pdf.build(content)

    print("PDF Generated")