class Villager():
    def __init__(self, id: int, name: str, personality: str, birthday: str, color: str, hobby: str, 
        species: str, gender: str, saying: str, catch_phrase: str, icon_uri: str, image_uri: str):
        self.id = id
        self.name = name
        self.personality = personality
        self.birthday = birthday
        self.species = species
        self.gender = gender
        self.catch_phrase = catch_phrase
        self.saying = saying
        self.hobby = hobby
        self.icon_uri = icon_uri
        self.image_uri = image_uri
        self.color = color

class LoveResult():
    def __init__(self, perc:int, msg:str):
        self.perc = perc
        self.msg = msg

class JokeResult():
    def __init__(self, msgs:list[str]):
        self.msgs = msgs