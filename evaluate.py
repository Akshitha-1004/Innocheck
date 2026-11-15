# evaluate.py

import pandas as pd
from src.similarity import top_matches

df = pd.read_csv("data/patents.csv")

correct = 0
total = 100

for i in range(total):

    query = df.iloc[i]["abstract"]

    actual_title = df.iloc[i]["title"]

    results = top_matches(query)

    returned_titles = [
        r[0]
        for r in results
    ]

    if actual_title in returned_titles:
        correct += 1

accuracy = (
    correct / total
) * 100

print(
    "Top-5 Accuracy:",
    round(accuracy,2),
    "%"
)