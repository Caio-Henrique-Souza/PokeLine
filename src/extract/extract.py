import requests
import pandas as pd

url = 'https://pokeapi.co/api/v2/pokemon/'
r = requests.get(url)
data = r.json()

pokemons = []

for pokemon in data["results"]:
    response = requests.get(pokemon["url"])
    details = response.json()

    pokemons.append({
        "id": details["id"],
        "name": details["name"],
        "base_xp": details["base_experience"],
        "Weight": details["weight"] 
    })

df = pd.DataFrame(pokemons)
print (df)