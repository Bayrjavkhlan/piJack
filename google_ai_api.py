import os
from dotenv import load_dotenv
import requests

# Load .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def ask_google_ai(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        candidates = result.get("candidates", [])
        if not candidates:
            return f"No candidates in response: {result}"

        # New API: content is a dict with 'parts' list
        content_dict = candidates[0].get("content", {})
        parts = content_dict.get("parts", [])
        if not parts:
            return f"No parts in content: {content_dict}"

        # Join all text parts
        answer = "".join([p.get("text", "") for p in parts])
        return answer

    except requests.exceptions.RequestException as e:
        return f"HTTP error: {e}"
    except ValueError:
        return f"Failed to parse JSON: {response.text}"
    except Exception as e:
        return f"Unexpected error: {e}"
