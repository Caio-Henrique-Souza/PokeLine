from src.extract.extract import extrair_pokemons, extrair_detalhes_pokemons
def run_pipeline():
    
    print("--- INICIANDO PIPELINE ---")
    
    print("Passo 1: Extraindo dados e gerando JSON")
    extrair_pokemons(1)

    print("Passo 2: Extraindo detalhes da base")
    extrair_detalhes_pokemons()

    print("--- PIPELINE FINALIZADA... POR ENQUANTO ---")

if __name__ == "__main__":
    run_pipeline()