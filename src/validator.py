import re


MAX_POST_LENGTH = 280
MAX_HASHTAGS = 3


def validate_post(post):
    errors = []
    warnings = []

    # Bos icerik kontrolu
    if not post.strip():
        errors.append("Post content is empty.")

    # Karakter limiti kontrolu
    if len(post) > MAX_POST_LENGTH:
        errors.append(
            f"Post exceeds {MAX_POST_LENGTH} characters. "
            f"Current length: {len(post)}."
        )

    # Hashtag kontrolu
    hashtags = re.findall(r"#\w+", post)

    if len(hashtags) > MAX_HASHTAGS:
        warnings.append(
            f"Too many hashtags detected: {len(hashtags)}. "
            f"Recommended maximum: {MAX_HASHTAGS}."
        )

    # Kiril alfabesi kontrolu
    if re.search(r"[\u0400-\u04FF]", post):
        errors.append(
            "Unexpected Cyrillic characters detected."
        )

    # Dogrulanmamis sayisal iddia kontrolu
    numeric_claim_patterns = [
        r"\b\d+(?:[.,]\d+)?\s?%",
        r"\b\d+(?:[.,]\d+)?\s?(?:kat|x)\b",
        r"\b\d+\s?(?:dakika|saat|gun|gün)\b",
    ]

    for pattern in numeric_claim_patterns:
        if re.search(pattern, post, re.IGNORECASE):
            warnings.append(
                "Potential unsupported numeric claim detected."
            )
            break

    is_valid = len(errors) == 0

    return {
        "valid": is_valid,
        "character_count": len(post),
        "hashtag_count": len(hashtags),
        "errors": errors,
        "warnings": warnings,
    }