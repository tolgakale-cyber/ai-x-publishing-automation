import json

from openai import OpenAI

client = OpenAI()


def critique_post(post):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "You are a social media quality reviewer. "
            "Evaluate the provided X/Twitter post. "
            "Score clarity, relevance, professionalism, and engagement "
            "from 1 to 10. "
            "Also provide one short improvement suggestion. "
            "Return only valid JSON with these keys: "
            "clarity, relevance, professionalism, engagement, suggestion."
        ),
        input=post,
    )

    return json.loads(response.output_text)