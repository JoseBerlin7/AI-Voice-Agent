'''Purpose: To find the intent of the query'''

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
