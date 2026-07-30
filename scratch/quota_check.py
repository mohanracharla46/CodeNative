import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('GEMINI_API_KEY', '')
if not key:
    print("ERROR: GEMINI_API_KEY not found in .env")
    exit(1)

models = ['gemini-2.0-flash', 'gemini-1.5-flash']

for model in models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    resp = requests.post(url, json={"contents": [{"parts": [{"text": "hi"}]}]})
    print(f"\n{model}: HTTP {resp.status_code}")
    if resp.status_code == 200:
        print("  STATUS: OK - quota available, API working fine")
    elif resp.status_code == 429:
        err = resp.json().get("error", {})
        print(f"  STATUS: QUOTA EXHAUSTED - {err.get('message', 'daily limit hit')}")
    elif resp.status_code == 404:
        err = resp.json().get("error", {})
        print(f"  STATUS: Model not found - {err.get('message', '')}")
    else:
        err = resp.json().get("error", {})
        print(f"  STATUS: Error - {err.get('message', 'unknown error')}")
