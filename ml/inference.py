# inference.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def query_model(model_str, system_prompt, prompt, temp, openai_api_key=None, base_url=None):
    client = OpenAI(
        api_key=openai_api_key if openai_api_key else os.getenv("OPENAI_API_KEY"),
        base_url=base_url if base_url else "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    # print("OpenAI API Key:", openai_api_key)
    # print("Base URL:", base_url)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    try:
        completion = client.chat.completions.create(
            model=model_str,
            messages=messages,
            temperature=temp
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"API Error: {str(e)}")
        return ""
