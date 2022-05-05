import requests
from pprint import pprint

SUPERHERO_TOKEN = 2619421814940190


class Hero:
    host = 'https://superheroapi.com/api'
    dict_hero = {}

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __id_hero(self):
        url = f'{self.host}/{self.token}/search/{self.name}'
        response = requests.get(url)
        return response.json()['results'][0]['id']

    def intelligence_hero(self):
        url = f'{self.host}/{self.token}/{self.__id_hero()}/powerstats'
        response = requests.get(url)
        self.dict_hero[self.name] = response.json()['intelligence']


hero_hulk = Hero('Hulk', SUPERHERO_TOKEN)
hero_captain_america = Hero('Captain America', SUPERHERO_TOKEN)
hero_thanos = Hero('Thanos', SUPERHERO_TOKEN)
hero_hulk.intelligence_hero()
hero_captain_america.intelligence_hero()
hero_thanos.intelligence_hero()
print(max(Hero.dict_hero))
