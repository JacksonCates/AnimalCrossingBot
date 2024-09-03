import requests
from domain import Villager
import dotenv
import os

from domain import LoveResult

dotenv.load_dotenv()
TOKEN = os.getenv("RAPIDAPI_TOKEN")

async def get_love(villager1: Villager, villager2: Villager) -> LoveResult:

    response = requests.get(f"https://love-calculator.p.rapidapi.com/getPercentage", params={"fname": villager1.name, "sname": villager2.name}, 
        headers={"x-rapidapi-host": "love-calculator.p.rapidapi.com", "x-rapidapi-key": TOKEN})
    if response.status_code != 200:
        raise Exception("API failed with a status code of", response.status_code)

    json = response.json()
    return LoveResult(json["percentage"], json["result"])