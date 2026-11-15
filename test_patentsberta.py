from src.embedder import create_embedding

vec = create_embedding(
    "AI based irrigation system using sensors"
)

print("Vector Length:", len(vec))