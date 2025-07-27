'''Purpose: to convert the speach to text'''

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcript.text
