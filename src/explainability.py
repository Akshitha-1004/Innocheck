from src.keywords import extract_keywords

def explain_similarity(
    user_text,
    matched_title
):

    user_keywords = extract_keywords(user_text)

    return {
        "matched_patent": matched_title,
        "common_concepts": user_keywords[:5],
        "reason":
        f"Patent appears related due to concepts such as {', '.join(user_keywords[:3])}"
    }