from openai import OpenAI

client = OpenAI()


def revise_post(post, critique):
    suggestion = critique.get("suggestion", "")

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "You are a professional social media editor. "
            "Improve the provided X/Twitter post using the review suggestion. "
            "The COMPLETE final post MUST be 280 characters or fewer, "
            "including spaces, punctuation, and hashtags. "
            "Preserve the original meaning. "
            "Do not invent facts. "
            "Do not add statistics, percentages, performance metrics, "
            "time savings, or numerical claims unless they already "
            "exist in the original post. "
            "Use no more than 3 hashtags. "
            "Return only the revised post text."
        ),
        input=(
            f"Original post:\n{post}\n\n"
            f"Reviewer suggestion:\n{suggestion}"
        ),
    )

    return response.output_text


def fix_invalid_post(post, errors):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "You are a social media compliance editor. "
            "Fix the post so it passes all provided validation errors. "
            "The COMPLETE final post MUST be 280 characters or fewer. "
            "Preserve the main meaning. "
            "Do not invent facts. "
            "Do not add statistics, percentages, performance metrics, "
            "time savings, or numerical claims unless they already "
            "exist in the original post. "
            "Use no more than 3 hashtags. "
            "Return only the corrected post text."
        ),
        input=(
            f"Post:\n{post}\n\n"
            f"Validation errors:\n{errors}"
        ),
    )

    return response.output_text