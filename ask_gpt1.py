import openai
import os
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
        ]
)
print(response.choices[0].message.content)