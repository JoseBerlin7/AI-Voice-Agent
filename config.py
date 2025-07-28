import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT")


AZURE_SPEECH_KEY = os.getenv("API_KEY")
AZURE_REGION = os.getenv("AZURE_REGION")

TTS_VOICE_ID = os.getenv("TTS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")
STT_ENDPOINT = os.getenv("STT_ENDPOINT")

VAPI_API_KEY = os.getenv("VAPI_API_KEY")

DATABASE_URL = "sqlite:///./data/calls.db"

TWILIO_ACC_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUM = os.getenv("TWILIO_NUMBER")

OPENAI_API_KEY = os.getenv("API_KEY")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
