from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "AI-Growth-Lab/PatentSBERTa"
)

def create_embedding(text):
    return model.encode(text)