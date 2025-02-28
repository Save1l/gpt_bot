from openai import OpenAI
client = OpenAI(api_key='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')

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