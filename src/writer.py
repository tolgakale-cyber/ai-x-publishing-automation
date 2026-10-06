from openai import OpenAI

client = OpenAI()


def generate_post(topic):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "You are a professional social media content writer. "
            "Create one concise X/Twitter post based on the user's topic. "
            "Keep the post under 280 characters. "
            "Do not invent facts. "
            "Use hashtags only when they add value. "
            "Return only the post text."
        ),
        input=topic,
    )

    return response.output_text