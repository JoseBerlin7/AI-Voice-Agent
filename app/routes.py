'''Purpose: To initiate and manage work flow of the call'''
import requests
from fastapi import APIRouter, Form
from fastapi.responses import Response
import openai
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from app.services import stt, intent, tts
from app.utils.db import log_call
from datetime import datetime
from config import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_NUM

conversations = {}

router = APIRouter()

@router.post("/inbound")
async def inbound_call(
    From: str = Form(...)
):
    try:
        vr = VoiceResponse()
        vr.say("Hi! I will connect you to the Assistant. Please speak after the beep.", voice="Polly.Amy")
        vr.record(
            action="/conversation-callback",
            method="POST",
            max_length=20,
            play_beep=True,
            trim="trim-silence"
        )
        return Response(content=str(vr), media_type="text/xml")
    except Exception as e:
        print(f"Error in /inbound: {e}")
        return Response(content="Internal Server Error", status_code=500)

@router.post("/conversation-callback")
async def conversation_callback(
    RecordingUrl: str = Form(...),
    CallSid: str = Form(...),
    From: str = Form(...)
):
    try:
        audio_response = requests.get(RecordingUrl + ".mp3")
        audio_file = f"temp_{CallSid}.mp3"
        with open(audio_file, "wb") as f:
            f.write(audio_response.content)

        transcript = stt.transcribe_audio(audio_file)
        # print(transcript)

        if CallSid not in conversations:
            conversations[CallSid] = [
                {
                    "role": "system",
                    "content": (
                        "You are an AI voice assistant for a customer support line. "
                        "Greet the user briefly, then ask follow-up questions to understand the issue. "
                        "Keep responses short, friendly, and ask for one detail at a time. "
                        "Once the user finishes talking, say you will log the issue or forward to a human."
                    )
                }
            ]

        conversations[CallSid].append({"role": "user", "content": transcript})

        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=conversations[CallSid],
            max_tokens=150,
            temperature=0.7,
        )
        ai_reply = completion.choices[0].message.content.strip()
        # print(ai_reply)


        conversations[CallSid].append({"role": "assistant", "content": ai_reply})


        intent_result = intent.extract_intent(transcript)
        log_call(From, "inbound", datetime.now().isoformat(), transcript, intent_result)

        tts_url = tts.generate_tts(ai_reply)

        vr = VoiceResponse()
        if tts_url:
            vr.play(tts_url)
        else:
            vr.say(ai_reply, voice="Polly.Amy")

        # loop for user to respond
        vr.record(
            action="/conversation-callback",
            method="POST",
            max_length=10,
            play_beep=True,
            timeout=5
        )
        vr.say("Goodbye!")

        return Response(content=str(vr), media_type="text/xml")

    except Exception as e:
        print("Error in conversation callback:", e)
        vr = VoiceResponse()
        vr.say("Sorry, something went wrong. Goodbye!")
        return Response(content=str(vr), media_type="text/xml")
    
@router.get("/make_call")
async def outbound_call():
    account_sid = TWILIO_ACC_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="https://d9a366c2c342.ngrok-free.app/outbound",
        to="",
        from_=TWILIO_NUM,
    )
    print(call.sid)

@router.post("/outbound")
async def outbound_entrypoint(From: str = Form(None), CallSid: str = Form(None)):
    try:
        vr = VoiceResponse()
        vr.say("Hi! This is your AI assistant calling to check in with you. If you have any questions, feel free to ask", voice="Polly.Amy")
        vr.record(
            action="/conversation-callback",
            method="POST",
            max_length=10,
            play_beep=True
        )
        return Response(content=str(vr), media_type="text/xml")

    except Exception as e:
        print("Error in /outbound:", e)
        return Response(content="Internal Server Error", status_code=500)
