import os
import requests
from dotenv import load_dotenv

load_dotenv()

class manage_calls:
    def __init__(self):
        vapi_api_key = os.getenv("VAPI_API_KEY")
        assistant_id = os.getenv("VAPI_ASSISTANT_ID")
        webhook_url = os.getenv("VAPI_WEBHOOK_URL")

        base_url = "https:/"