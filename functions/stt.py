'''Purpose: Converting the text to speech'''
import azure.cognitiveservices.speech as speechsdk
from config import API_KEY, STT_ENDPOINT

class stt:
    def __init__(self):
        pass

    def get_text(self):
        speech_config = speechsdk.SpeechConfig(subscription=API_KEY, endpoint=STT_ENDPOINT)
        speech_config.speech_recognition_language="en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            return "Unknown"
        else:
            return "Unknown"

# print(stt().get_text())