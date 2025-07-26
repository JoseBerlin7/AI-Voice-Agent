from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from config import API_KEY,AZURE_REGION, TTS_VOICE_ID

class tts:
    def __init__(self):
        pass

    def speak_text(self, text):
        text = text.lower()
        speech_config = speechsdk.SpeechConfig(subscription=API_KEY, region=AZURE_REGION)
        speech_config.speech_synthesis_voice_name = TTS_VOICE_ID
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = speech_synthesizer.speak_text_async(text).get()

        if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Speech synthesis failed: {result.reason}")

# tts().speak_text("Hello")