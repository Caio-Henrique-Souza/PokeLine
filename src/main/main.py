from src.extract.extract import extrair_pokemons, extrair_especie

def run_pipeline():
    
    print("--- INICIANDO PIPELINE ---")
    
    print("Passo 1: Extraindo dados e gerando JSON")
    extrair_pokemons(151)

    print("Passo 2: Extraindo especies e gerando JSON")
    extrair_especie(151)


    print("--- PIPELINE FINALIZADA... POR ENQUANTO ---")

if __name__ == "__main__":
    run_pipeline()