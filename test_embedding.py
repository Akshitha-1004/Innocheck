from src.embedder import create_embedding

vector = create_embedding(
    "AI irrigation system"
)

print(vector)
print(len(vector))