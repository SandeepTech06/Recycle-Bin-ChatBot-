# test_openai_key.py
from openai import OpenAI

client = OpenAI(api_key="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")  # Replace with your new key

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello!"}
        ],
        max_tokens=1000
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")