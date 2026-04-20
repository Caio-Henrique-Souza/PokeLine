from src.extract.extract import extrair_pokemons, extrair_detalhes_pokemons, extrair_species_pokemons
from transform.bronze import criar_dpokecharac, criar_dpokeegg, criar_dpokemon, criar_dpokemoves, criar_dpokestats, criar_dpoketype
def run_pipeline():
    
    print("--- INICIANDO PIPELINE ---")
    
    print("Passo 1: Extraindo dados e gerando JSON")
    extrair_pokemons(1)

    print("Passo 2: Extraindo detalhes da base")
    extrair_detalhes_pokemons()

    print("Passo 3: Extraindo detalhes do ovo")
    extrair_species_pokemons()

    print("Passo 4: Criando o dPokemon")


    print("--- PIPELINE FINALIZADA... POR ENQUANTO ---")

if __name__ == "__main__":
    run_pipeline()