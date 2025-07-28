# AI-Voice-Agent
This repo containing AI Voice Agent System developed using Vapi, Azure OpenAI, FastAPI

## How to run the project
1. Navigate to AI-VOICE-AGENT
    git clone https://github.com/JoseBerlin7/AI-Voice-Agent.git

    cd AI-Voice-Agent

2. Install requirements

    pip install -r requirements.txt

3. create your .env file with the following API's

    API_KEY = ""
    
    TWILIO_SID=""
    TWILIO_AUTH_TOKEN=""
    TWILIO_NUMBER = ""

    ELEVENLABS_API_KEY = ""
    ELEVENLABS_VOICE_ID = ""

4. Open another terminal for ngrok

    ngrok http http://localhost:8000

This will give you the target url looking like

    Forwarding                    https://{domain} -> http://localhost:8000

This will give you a temp domain where we can launch the app

5. add this target url to your Twilio webhook url while on HTTP POST to receive incoming calls

    eg: https://{domain}/inbound

Then hit save configuration 

6. Add the url to the routes.py on line 115

    https://{domain}/outbound

6. run the program

    python -m uvicorn app.main:app --reload --port 8000

this will let your program to interact with ngrok, twilio

7. Now you can either call the Twilio number 
or make the Twilio call you by entering the following

http://localhost:8000/make_call/{Phone_Number}

Note: 
Step 5, 6 myst be repeated every time you restart ngrok
