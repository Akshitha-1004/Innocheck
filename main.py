from src.similarity import top_matches
from src.similarity import novelty_score

text = input(
    "Enter Patent Description:\n"
)

print(
    "\nNovelty Score:",
    novelty_score(text),
    "%"
)

print("\nTop Similar Patents:\n")

for title, patent_id, score in top_matches(text):

    print(
        patent_id,
        "|",
        title,
        "| Distance:",
        score
    )