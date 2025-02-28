from openai import OpenAI
from docs import gpt_api_key
client = OpenAI(api_key=gpt_api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Как зовут Пушкина?"
        }
    ]
)
print(completion.choices[0].message.content)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "О чем я спрашивал в прошлом запросе?"
        }
    ]
)

print(completion.choices[0].message.content)