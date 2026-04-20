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
            "name": pokemon["name"]
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

    print(f"✅ dPokeStats criado com sucesso em {caminho_arquivo}")

def criar_dpokecharac():
    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/processed"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        lista.append({
            "pokemon_id": pokemon["id"],
            "base_xp": pokemon["base_experience"],
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "abilities": [abilitie["ability"]["name"] for abilitie in pokemon["abilities"]]
            
        })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokeCharac.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"✅ dPokeCharac criado com sucesso em {caminho_arquivo}")


def criar_dpoketype():
    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/processed"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        lista.append({
            "pokemon_id": pokemon["id"],
            "type": [type["type"]["name"] for type in pokemon["types"]]

            
        })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokeType.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"✅ dPokeType criado com sucesso em {caminho_arquivo}")

def criar_dpokeegg():
    origem = "data/raw/pokemons_species_raw.json"
    destino = "data/processed"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        lista.append({
            "pokemon_id": pokemon["id"],
            "is_legendary": pokemon["is_legendary"],
            "is_mythical": pokemon["is_mythical"],
            "hatch_counter": pokemon["hatch_counter"],
            "generation": pokemon["generation"]["name"],
            "growth_rate": pokemon["growth_rate"]["name"],
            "habitat": pokemon["habitat"]["name"]if pokemon["habitat"] else None,
            "evolves_from": pokemon["evolves_from_species"]["name"] if pokemon["evolves_from_species"] else None,
            "egg": [egg["name"] for egg in pokemon["egg_groups"]]

        })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokeEgg.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"✅ dPokeEgg criado com sucesso em {caminho_arquivo}")


def criar_dpokemoves():
    import json
    import os
    import pandas as pd

    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/processed"

    os.makedirs(destino, exist_ok=True)

    with open(origem, "r", encoding="utf-8") as f:
        dados = json.load(f)

    lista = []

    for pokemon in dados:
        pokemon_id = pokemon["id"]

        for move in pokemon["moves"]:
            move_name = move["move"]["name"]

            for detail in move["version_group_details"]:
                lista.append({
                    "pokemon_id": pokemon_id,
                    "move": move_name,
                    "level_requirement": detail["level_learned_at"],
                    "learn_method": detail["move_learn_method"]["name"],
                    "game_version": detail["version_group"]["name"]
                })

    df = pd.DataFrame(lista)

    caminho_arquivo = f"{destino}/dPokeMoves.csv"
    df.to_csv(caminho_arquivo, index=False)

    print(f"🔥 dPokeMoves correto criado: {len(df)} linhas")

