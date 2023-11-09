from dotenv import load_dotenv
import os
import openai

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I want to know more about you."},
  ]
)

print(completion.choices[0].message)