import faiss
import pandas as pd
import numpy as np

from src.embedder import create_embedding
from src.preprocessing import clean_text

# Load patent dataset
df = pd.read_csv("data/patents.csv")

# Load FAISS index
index = faiss.read_index("models/faiss.index")


def top_matches(text, k=5):

    text = clean_text(text)

    query_vector = create_embedding(text)

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        k
    )

    results = []

    for i in range(k):

        idx = indices[0][i]

        results.append(
            (
                df.iloc[idx]["title"],
                df.iloc[idx]["publication_number"],
                round(float(distances[0][i]), 2)
            )
        )

    return results


def novelty_score(text):

    text = clean_text(text)

    query_vector = create_embedding(text)

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        1
    )

    distance = float(distances[0][0])

    novelty = max(
        0,
        100 - distance
    )

    return round(novelty, 2)