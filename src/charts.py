import plotly.graph_objects as go
import plotly.express as px


def novelty_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Novelty Score"}
        )
    )

    return fig.to_html(full_html=False)


def similarity_chart(matches):

    titles = [
        m[0][:30]
        for m in matches
    ]

    scores = [
        m[2]
        for m in matches
    ]

    fig = px.bar(
        x=titles,
        y=scores,
        labels={
            "x": "Patent",
            "y": "Similarity"
        }
    )

    return fig.to_html(full_html=False)