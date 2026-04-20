from src.extract.extract import extrair_pokemons, extrair_detalhes_pokemons, extrair_species_pokemons
from src.transform.bronze import criar_dpokecharac, criar_dpokeegg, criar_dpokemon, criar_dpokemoves, criar_dpokestats, criar_dpoketype
from src.transform.silver import transformar_dpokecharac, transformar_dpokeegg, transformar_dpokemon, transformar_dpokemoves, transformar_dpokestats,transformar_dpoketype
from src.load.load import carregar_pokemoves, carregar_pokecharac,carregar_pokeegg,carregar_pokemon,carregar_pokestats,carregar_poketype
def run_pipeline():
    
    print("--- INICIANDO PIPELINE ---")
    
    print("Passo 1: Extraindo dados e gerando JSON")
    extrair_pokemons(1)

    print("Passo 2: Extraindo detalhes da base")
    extrair_detalhes_pokemons()

    print("Passo 3: Extraindo detalhes do ovo")
    extrair_species_pokemons()

    print("Passo 4: Criando Tabelas dPokemon, dPokeCharac, dPokeEgg, dPokeMoves, dPokeStats e dPokeType")
    criar_dpokemon()
    criar_dpokecharac()
    criar_dpokeegg()
    criar_dpokemoves()
    criar_dpokestats()
    criar_dpoketype()



    print("passo 5: Limpar os dados")
    transformar_dpokemon()
    transformar_dpokecharac()
    transformar_dpokeegg()
    transformar_dpokemoves()
    transformar_dpokestats()
    transformar_dpoketype()

    print("passo 6: Carregar os dados")
    carregar_pokemon()
    carregar_pokecharac()
    carregar_pokeegg()
    carregar_pokemoves()
    carregar_pokestats()
    carregar_poketype()

    print("--- PIPELINE FINALIZADA... POR ENQUANTO ---")

if __name__ == "__main__":
    run_pipeline()