import requests
import json
import dotenv
import os

url = "https://ai-chatbot.p.rapidapi.com/chat/free"

dotenv.load_dotenv()
RAPID_TOKEN = os.getenv("RAPIDAPI_TOKEN")

async def get_response(msg: str) -> str:

    querystring = {"message":msg,"uid":"user1"}
    headers = {
        'x-rapidapi-key': f"{RAPID_TOKEN}",
        'x-rapidapi-host': "ai-chatbot.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        raise Exception("API failed with a status code of", response.status_code)
    json = response.json()

    return json["chatbot"]["response"]