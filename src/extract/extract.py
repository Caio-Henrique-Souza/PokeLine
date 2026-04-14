import requests
import json
import os

def extrair_pokemons(quantidade=151):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={quantidade}"
    destino = "data/raw"
    resposta = requests.get(url)

    os.makedirs(destino, exist_ok=True) #garantindo que a pasta exista

    if resposta.status_code == 200: #se não der erro na API
        dados = resposta.json()

        caminho_arquivo = f"{destino}/pokemons_base_raw.json"
        with open(caminho_arquivo, 'w') as f:
            json.dump(dados, f, indent= 4)

        print(f"Sucesso! {quantidade} Pokémons Salvos em {caminho_arquivo}")
    else:
        print(f"Erro ao acessar a API: {resposta.status_code}")

def extrair_detalhes_pokemons():
    origem = "data/raw/pokemons_base_raw.json"
    destino = "data/raw"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    detalhes = []

    for pokemon in dados["results"]:
        url = pokemon["url"]
        
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            detalhes.append(resposta.json())
        else:
            print(f"Erro ao acessar {url}: {resposta.status_code}")

    caminho_arquivo = f"{destino}/pokemons_detalhes_raw.json"
    
    with open(caminho_arquivo, 'w') as f:
        json.dump(detalhes, f, indent=4)

    print(f"Sucesso! Detalhes salvos em {caminho_arquivo}")