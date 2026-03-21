import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_key_points(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Extract key points from text as a list."},
            {"role": "user", "content": f"Extract key points:\n{text}"}
        ],
        temperature=0.5
    )

    points = response.choices[0].message.content.strip().split("\n")
    return [p.strip("- ") for p in points if p]