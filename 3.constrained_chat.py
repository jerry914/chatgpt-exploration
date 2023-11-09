import openai
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(message):
    system_message = "You are a helpful assistant that guides the student to the answer without giving it away."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message},
        ]
    )
    return response.choices[0].message['content']

print(get_response("What is 2 + 2?"))
