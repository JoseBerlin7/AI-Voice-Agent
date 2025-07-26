''' Plan : Able to Make & Recieve calls -> Speak using TTS -> Listen and use STT -> Extract customer intent using openai -> log everything '''


from fastapi import FastAPI, Request
from app import vapi, db

app = FastAPI()

@app.on_event("startup")
async def startup():
    db.init_db()

@app.post("/webhook/call-events")
async def call_events(request: Request):
    payload = await request.json()
    return await vapi.handle_webhook(payload)

@app.get("/logs")
def get_logs():
    logs = db.get_all_logs()
    return {"logs": logs}


@app.get("/")
def root():
    return {"message":"Voice Assistant Running"}
