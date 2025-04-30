import requests
import config

def generate_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {config.AI_API_KEY}"
    }
    payload = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 100
    }
    try:
        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        return f"⚠️ Error fetching response: {e}"