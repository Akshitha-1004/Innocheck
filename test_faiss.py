from src.similarity import top_matches
from src.similarity import novelty_score

query = """
AI based irrigation system using sensors
"""

print("Novelty Score:",
      novelty_score(query),
      "%")

print("\nTop Similar Patents:\n")

for title, patent_id, score in top_matches(query):

    print(
        patent_id,
        "|",
        title,
        "| Distance:",
        score
    )