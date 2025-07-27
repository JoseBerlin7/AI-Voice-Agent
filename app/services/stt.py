import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def transcribe_audio(file_path):
    audio_file = open(file_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
