import requests
import json

def ask_gpt3(prompt):
    url = 'https://api.openai.com/v1/engines/davinci/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 1000,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()

print(ask_gpt3("Write a Python code to mutiple each number from 1 to 100"))