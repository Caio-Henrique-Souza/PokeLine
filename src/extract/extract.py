import requests
import json
import os
from datetime import datetime


def extract_pokemon_raw(save_raw=True):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    
    response = requests.get(base_url)
    response.raise_for_status()
    data = response.json()

    all_details = []

    for pokemon in data["results"]:
        details_response = requests.get(pokemon["url"])
        details_response.raise_for_status()
        details = details_response.json()

        species_response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{details['name']}"
        )
        species_response.raise_for_status()
        species_data = species_response.json()

        # Guarda TUDO bruto, sem mexer
        all_details.append({
            "pokemon": details,
            "species": species_data
        })

    # salvar RAW
    if save_raw:
        os.makedirs("data/raw", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        with open(f"data/raw/pokemon_raw_{timestamp}.json", "w", encoding="utf-8") as f:
            json.dump(all_details, f, ensure_ascii=False)

    return all_details