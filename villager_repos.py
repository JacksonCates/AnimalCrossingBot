import requests
import json
from domain import Villager
import numpy.random as random
import datetime

villager_dict_path = "data/villager_dict.json"

def get_villager_id(name: str) -> int:

    file = open(villager_dict_path, "r")
    villager_dict = json.load(file)
    file.close()

    lower = name.lower()
    return None if lower not in villager_dict else villager_dict[lower]

async def rand_villager() -> Villager:

    id = random.randint(391)
    return await get_villager_by_id(id)

async def get_villager_by_name(name: str) -> Villager:
    
    id = get_villager_id(name)

    if id is None:
        return None
    return await get_villager_by_id(id)

async def get_villager_by_id(id: int) -> Villager:

    response = requests.get(f"http://acnhapi.com/v1/villagers/{id}")
    if response.status_code != 200:
        raise Exception("API failed with a status code of", response.status_code)
    
    json = response.json()
    name = json["name"]["name-USen"]
    saying = json["saying"]
    color = int(json["bubble-color"][1:], 16)
    dob = json["birthday-string"]
    species = json["species"]
    hobby = json["hobby"]
    catch_phrase = json["catch-phrase"]
    gender = json["gender"]
    image_uri = json["image_uri"]
    icon_uri = json["icon_uri"]
    personality = json["personality"]

    return Villager(id, name, personality, dob, color, hobby, species, 
        gender, saying, catch_phrase, icon_uri, image_uri)

async def get_villagers_birthdays_today() -> list[Villager]:

    # Gets all of the villagers
    response = requests.get(f"http://acnhapi.com/v1/villagers")
    json = response.json()

    # Get today
    now = datetime.datetime.now()
    now_string = f"{now.day}/{now.month}"

    # Finds if it is any villager's birthday
    villagers = []
    for key in json:
        if json[key]["birthday"] == now_string:
            villager_id = json[key]["id"]
            villagers.append(await get_villager_by_id(villager_id))

    return villagers
