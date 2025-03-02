from docs import gpt_api
api = gpt_api
from openai import OpenAI
client = OpenAI(api_key=api)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Привет"
        }
    ]
)

print(completion.choices[0].message.content)