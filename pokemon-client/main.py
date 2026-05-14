
import requests

class PokemonClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name):
        response = requests.get(f"{self.BASE_URL}/{name}")
        response.raise_for_status()
        return response.json()

class Pokemon:
    def __init__(self, data):
        self.name = data["name"]
        self.height= data["height"]
        self.weight = data["weight"]
        self.types = [t["type"]["name"]for t in data["types"]]

    def display(self):
        print(f"Name: {self.name.title()}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"Types: {', '.join(self.types)}")

client = PokemonClient()

data = client.get_pokemon("pikachu")

pokemon = Pokemon(data)

pokemon.display()