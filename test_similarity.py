from src.similarity import top_matches

query = """
AI irrigation system using sensors
"""

matches = top_matches(query)

for title, score in matches:
    print(title, "-", score, "%")