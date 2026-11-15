from src.similarity import top_matches
from src.keywords import extract_keywords

def keyword_similarity(user_keywords, patent_keywords):

    common = set(user_keywords) & set(patent_keywords)

    union = set(user_keywords) | set(patent_keywords)

    if len(union) == 0:
        return 0

    return len(common) / len(union)

def hybrid_novelty(text):

    matches = top_matches(text, 1)

    distance = matches[0][2]

    semantic_score = max(0, 100 - distance)

    user_keywords = extract_keywords(text)

    patent_keywords = extract_keywords(matches[0][0]) if matches else []

    keyword_score = keyword_similarity(user_keywords, patent_keywords)

    final_score = (
        0.8 * semantic_score +
        0.2 * keyword_score
    )

    return round(final_score, 2)