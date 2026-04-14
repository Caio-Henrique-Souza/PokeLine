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

def extrair_especie(quantidade=151):
    url = f"https://pokeapi.co/api/v2/pokemon-species?limit={quantidade}"
    destino = "data/raw"
    resposta = requests.get(url)

    os.makedirs(destino, exist_ok=True)

    if resposta.status_code == 200: #se não der erro na API
        dados = resposta.json()

        caminho_arquivo = f"{destino}/pokemons_especies_raw.json"
        with open(caminho_arquivo, 'w') as f:
            json.dump(dados, f, indent= 4)

        print(f"Sucesso! {quantidade} espécies Salvos em {caminho_arquivo}")
    else:
        print(f"Erro ao acessar a API: {resposta.status_code}")