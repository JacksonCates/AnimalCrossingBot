import requests
import os
import dotenv

from domain import JokeResult

url = "https://jokeapi-v2.p.rapidapi.com/joke/Pun?safe-mode"

dotenv.load_dotenv()
TOKEN = os.getenv("RAPIDAPI_TOKEN")

async def get_joke() -> JokeResult:

    querystring = {"lang":"en"}
    headers = {
        'x-rapidapi-key': f"{TOKEN}",
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        raise Exception("API failed with a status code of", response.status_code)
    json = response.json()

    joke_type = json["type"]
    msgs = []
    if joke_type == "twopart":
        msgs.append(json["setup"])
        msgs.append(json["delivery"])
    elif joke_type == "single":
        msgs.append(json["joke"])
    else:
        raise Exception("Invalid Joke Type Given:", joke_type)

    return JokeResult(msgs)
    