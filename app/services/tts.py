import requests
from config import ELEVENLABS_API_KEY

def generate_tts(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, headers=headers, json=payload)
    with open("response.mp3", "wb") as f:
        f.write(response.content)
    return "response.mp3"
