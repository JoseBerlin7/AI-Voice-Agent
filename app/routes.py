from fastapi import APIRouter, Form
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse
from datetime import datetime

from app.services import stt, intent
from app.utils.db import log_call

router = APIRouter()

@router.post("/inbound")
async def inbound_call(
    From: str = Form(None)
):
    try:
        response = VoiceResponse()
        response.say("Hello! Thanks for calling. Your number is " + str(From), voice="Polly.Amy")

        return Response(content=str(response), media_type="text/xml")
    except Exception as e:
        print("ERROR in /inbound:", e)
        return Response(content="Internal Server Error", status_code=500)

