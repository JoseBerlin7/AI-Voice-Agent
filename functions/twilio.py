'''Purpose: Handling the calls'''
from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from config import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_NUM
import app.main as main  

app = Flask(__name__)

class TwilioAgent:
    def __init__(self):
        self.client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

    def make_call(self, recipient_number, message_url):
        call = self.client.calls.create(
            from_=TWILIO_NUM,
            to=recipient_number,
            url=message_url
        )
        print(call.sid)

# Flask endpoint: first response when call starts
@app.route("/voice", methods=['POST'])
def voice():
    call_sid = request.form.get("CallSid")
    response = VoiceResponse()
    
    message = main.get_message(call_sid)

    gather = Gather(num_digits=1, action="/gather", method="POST")
    gather.say(message, voice="alice")
    response.append(gather)

    response.say("We didn't get input. Goodbye!", voice="alice")
    response.hangup()
    return Response(str(response), mimetype='text/xml')

# Flask endpoint: handle DTMF input
@app.route("/gather", methods=['POST'])
def gather():
    call_sid = request.form.get("CallSid")
    digits = request.form.get("Digits")

    response = VoiceResponse()
    message = main.get_message(call_sid, digits)
    response.say(message, voice="alice")
    response.hangup()
    return Response(str(response), mimetype='text/xml')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
