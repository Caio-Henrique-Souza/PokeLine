import requests
import pandas as pd

url = 'https://pokeapi.co/api/v2/pokemon/'
r = requests.get(url)
data = r.json()

pokemons = []

for pokemon in data["results"]:
    response = requests.get(pokemon["url"])
    details = response.json()

    r_egg = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{details['name']}")
    egg_data = r_egg.json()
    egg_groups = [e["name"] for e in egg_data["egg_groups"]]

    stat_map = {s["stat"]["name"]: s["base_stat"] for s in details["stats"]}



    pokemons.append({
        "id": details["id"],
        "name": details["name"],
        "base_xp": details["base_experience"],
        "weight": details["weight"],
        "type": [t["type"]["name"] for t in details["types"]],
        "specie": egg_groups,
        **stat_map,
        "sprite_default": details["sprites"]["front_default"],
        "sprite_shiny": details["sprites"]["front_shiny"]
    })

df = pd.DataFrame(pokemons)
df.to_csv("pokemons.csv", index=False, encoding="utf-8")
print (df.head())