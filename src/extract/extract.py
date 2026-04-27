import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed



def get_json(url):
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            print(f"Erro ao acessar {url}: {resposta.status_code}")
            return None
    except Exception as e:
        print(f"Erro na request {url}: {e}")
        return None

def extrair_pokemons(quantidade=151):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={quantidade}"
    destino = "data/raw"

    os.makedirs(destino, exist_ok=True)

    dados = get_json(url)

    if not dados:
        print("Erro ao acessar a API")
        return

    caminho_arquivo = f"{destino}/pokemons_base_raw.json"
    with open(caminho_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

    print(f"✅ Sucesso! {quantidade} Pokémons salvos em {caminho_arquivo}")

def extrair_detalhes_pokemons():
    origem = "data/raw/pokemons_base_raw.json"
    destino = "data/raw"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    urls = [pokemon["url"] for pokemon in dados["results"]]

    detalhes = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(get_json, url) for url in urls]

        for future in as_completed(futures):
            resultado = future.result()
            if resultado:
                detalhes.append(resultado)

    # opcional: ordenar por id (evita bagunça por paralelismo)
    detalhes.sort(key=lambda x: x["id"])

    caminho_arquivo = f"{destino}/pokemons_detalhes_raw.json"
    
    with open(caminho_arquivo, 'w') as f:
        json.dump(detalhes, f, indent=4)

    print(f"🔥 Sucesso! Detalhes salvos em {caminho_arquivo}")

def extrair_species_pokemons():
    origem = "data/raw/pokemons_detalhes_raw.json"
    destino = "data/raw"
    
    os.makedirs(destino, exist_ok=True)

    with open(origem, 'r') as f:
        dados = json.load(f)

    urls = [pokemon["species"]["url"] for pokemon in dados]

    species_detalhes = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(get_json, url) for url in urls]

        for future in as_completed(futures):
            resultado = future.result()
            if resultado:
                species_detalhes.append(resultado)

    # ordenar por id também
    species_detalhes.sort(key=lambda x: x["id"])

    caminho_arquivo = f"{destino}/pokemons_species_raw.json"
    
    with open(caminho_arquivo, 'w') as f:
        json.dump(species_detalhes, f, indent=4)

    print(f"🔥 Sucesso! Species salvos em {caminho_arquivo}")

def extrair_gameversion(quantidade=9):
    url = f"https://pokeapi.co/api/v2/generation?limit={quantidade}"
    destino = "data/raw"

    os.makedirs(destino, exist_ok=True)

    dados = get_json(url)

    if not dados:
        print("Erro ao acessar a API")
        return

    lista = []

    for gen in dados["results"]:
        gen_nome = gen["name"]
        gen_url = gen["url"]

        # 🔥 aqui está o pulo do gato
        gen_detalhe = get_json(gen_url)

        if not gen_detalhe:
            continue

        for vg in gen_detalhe["version_groups"]:
            lista.append({
                "generation": gen_nome,
                "version_group": vg["name"]
            })

    caminho_arquivo = f"{destino}/generation_version_group_raw.json"

    with open(caminho_arquivo, 'w') as f:
        json.dump(lista, f, indent=4)

    print(f"✅ Mapeamento generation → version_group salvo em {caminho_arquivo}")