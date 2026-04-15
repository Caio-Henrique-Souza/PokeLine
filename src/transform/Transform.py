import pandas as pd
import json
import os

def criar_dpokemon():
    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/processed"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        lista.append({
            "pokemon_id": pokemon["id"],
            "name": pokemon["name"],
            "height": pokemon["height"],
            "weight": pokemon["weight"]
        })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokemon.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"✅ dPokemon criado com sucesso em {caminho_arquivo}")


def criar_dpokestats():
    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/processed"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        lista.append({
            "pokemon_id": pokemon["id"],
            "hp": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "hp"),
            "attack": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "attack"),
            "defense": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "defense"),
            "special-attack": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "special-attack"),
            "special-defense": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "special-defense"),
            "speed": next(stat["base_stat"] for stat in pokemon["stats"] if stat["stat"]["name"] == "speed")

        })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokeStats.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"✅ dPokemon criado com sucesso em {caminho_arquivo}")


criar_dpokestats()