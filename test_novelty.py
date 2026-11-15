from src.similarity import novelty_score

query = """
AI irrigation system using sensors
"""

print(
    "Novelty Score:",
    novelty_score(query),
    "%"
)