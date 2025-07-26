import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT")


AZURE_SPEECH_KEY = os.getenv("API_KEY")
AZURE_REGION = os.getenv("AZURE_REGION")

TTS_VOICE_ID = os.getenv("TTS_VOICE_ID")
STT_ENDPOINT = os.getenv("STT_ENDPOINT")

VAPI_API_KEY = os.getenv("VAPI_API_KEY")

DATABASE_URL = "sqlite:///./data/calls.db"
