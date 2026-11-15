from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text, top_n=5):

    keywords = kw_model.extract_keywords(
        text,
        top_n=top_n,
        stop_words="english"
    )

    return [k[0] for k in keywords]