import pandas as pd
import json
import os

def transformar_pokemon():
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