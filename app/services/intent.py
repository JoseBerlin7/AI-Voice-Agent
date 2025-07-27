import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def extract_intent(transcript: str) -> str:
    prompt = f"Given the transcript: \"{transcript}\", extract the customer's intent (like \"schedule callback\", \"complaint\", \"resolve issue\")."
    resp = await openai.ChatCompletion.acreate(
        model="gpt‑4",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message["content"].strip()

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_intent(transcript):
    prompt = f"""
User said: "{transcript}"

Classify the user's intent as one of:
- Schedule callback
- Resolve issue
- Talk to human
- Complaint
- Other

Only return the intent.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()
