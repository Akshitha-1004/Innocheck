# src/faiss_search.py

import faiss
import pandas as pd
import numpy as np

from src.embedder import create_embedding

df = pd.read_csv("data/patents.csv")

index = faiss.read_index("models/faiss.index")

def search_patents(text, k=5):

    vec = create_embedding(text)

    vec = np.array([vec]).astype("float32")

    D, I = index.search(vec, k)

    results = []

    for idx in I[0]:
        results.append(
            (
                df.iloc[idx]["title"],
                df.iloc[idx]["publication_number"]
            )
        )

    return results