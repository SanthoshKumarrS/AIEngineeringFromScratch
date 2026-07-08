import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

headers = {
    "Content-Type": "application/json",
}

body = json.dumps({
    "contents": [
        {
            "parts": [
                {
                    "text": "What is a neural network in one sentence?"
                }
            ]
        }
    ]
}).encode("utf-8")

req = urllib.request.Request(
    url,
    data=body,
    headers=headers,
    method="POST",
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())

print(result["candidates"][0]["content"]["parts"][0]["text"])
