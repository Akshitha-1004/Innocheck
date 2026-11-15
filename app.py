from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from src.similarity import (
    top_matches,
    novelty_score
)

from src.classifier import (
    predict_category
)

from src.keywords import (
    extract_keywords
)

from src.report import (
    generate_analysis
)

from src.pdf_report import (
    generate_pdf
)

from src.charts import (
    novelty_gauge,
    similarity_chart
)

app = Flask(__name__)

# Store latest result for PDF generation
latest_result = {}


@app.route("/", methods=["GET", "POST"])
def home():

    novelty = None
    matches = []
    category = ""
    keywords = []
    analysis = ""
    gauge = ""
    chart = ""

    if request.method == "POST":

        text = request.form["patent"]

        # Novelty Score
        novelty = novelty_score(text)

        # Similar Patents
        matches = top_matches(text)

        # Category
        category = predict_category(text)

        # Keywords
        keywords = extract_keywords(text)

        # Analysis
        analysis = generate_analysis(text)

        # Charts
        gauge = novelty_gauge(novelty)

        chart = similarity_chart(matches)

        # Save for PDF
        latest_result["novelty"] = novelty
        latest_result["category"] = category
        latest_result["keywords"] = keywords
        latest_result["analysis"] = analysis

    return render_template(
        "index.html",
        novelty=novelty,
        matches=matches,
        category=category,
        keywords=keywords,
        analysis=analysis,
        gauge=gauge,
        chart=chart
    )


@app.route("/download")
def download():

    if not latest_result:

        return "Analyze a patent first."

    generate_pdf(
        novelty=latest_result["novelty"],
        category=latest_result["category"],
        keywords=latest_result["keywords"],
        analysis=latest_result["analysis"]
    )

    return send_file(
        "Patent_Report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )