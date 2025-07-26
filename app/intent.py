
import os
import base64
from openai import AzureOpenAI
from config import OPENAI_ENDPOINT,OPENAI_DEPLOYMENT, API_KEY


class classify:
    def __init__(self):
        endpoint = OPENAI_ENDPOINT
        subscription_key = API_KEY
        self.deployment = OPENAI_DEPLOYMENT
        self.client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=subscription_key,
            api_version="2025-01-01-preview",
)

    def get_prompt(self, message):
        # Prepare the chat prompt
        chat_prompt = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant for a company that provides eSIM mobile services. Your task is to classify customer queries into one of the following intent categories:\n\nSchedule Callback: The customer requests a call or asks to arrange a call at a specific time.\n\nResolve Issue: The customer is reporting a problem or requesting help to solve a technical or account-related issue.\n\nPurchase/Upgrade Plan: The customer is interested in buying, changing, or upgrading a plan.\n\nGeneral Inquiry: The customer is asking for information but does not request a callback or raise a resolvable issue.\n\nAccount/Billing: The customer asks about account details, billing, or payments.\n\nOther: The intent does not fit any of the above categories.\n\nGiven the following customer message, identify and return only the intent label from the above list. If uncertain, choose \"Other\".\n\n"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I want to upgrade to your premium plan"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Purchase/Upgrade Plan"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "what offers do you have"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "General Inquiry"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{message}"
                    }
                ]
            },
        ]
        return chat_prompt
    
    def get_intent(self, message):
        messages = self.get_prompt(message)

        # Generate the completion
        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=messages,
            max_tokens=100,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )

        answer = response.choices[0].message.content.strip()
        return answer
    
    def generate_response(intent):
        return "Yes"

        
    
# print(classify().get_intent("I want to recharge my sim card"))