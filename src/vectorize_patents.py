import pandas as pd
import pickle

from src.embedder import create_embedding
from src.preprocessing import clean_text

df = pd.read_csv("data/patents.csv")
df["abstract"]

vectors = []

for patent in df["abstract"]:

    cleaned = clean_text(str(patent))

    vec = create_embedding(cleaned)

    vectors.append(vec)

pickle.dump(
    vectors,
    open("models/patent_vectors.pkl", "wb")
)

print("Vectors Saved")
print("Total Patents:", len(vectors))