from src.extract.extract import extrair_pokemons,get_json, extrair_detalhes_pokemons, extrair_species_pokemons
from src.transform.bronze import criar_dpokecharac, criar_dpokeegg, criar_dpokemon, criar_dpokemoves, criar_dpokestats, criar_dpoketype
from src.transform.silver import transformar_dpokecharac, transformar_dpokeegg, transformar_dpokemon, transformar_dpokemoves, transformar_dpokestats,transformar_dpoketype
from src.load.load import carregar_pokemoves, carregar_pokecharac,carregar_pokeegg,carregar_pokemon,carregar_pokestats,carregar_poketype, criar_tabelas
def run_pipeline(extract=True):
    
    print("🚀 --- INICIANDO PIPELINE ---")
    
    if extract:
        print("[EXTRACT] Extração de dados")
        extrair_pokemons(151)
        extrair_detalhes_pokemons()
        extrair_species_pokemons()

    print("[TRANSFORM] Processamento Bronze/Silver")
    transformar_dpokemon()
    transformar_dpokecharac()
    transformar_dpokeegg()
    transformar_dpokemoves()
    transformar_dpokestats()
    transformar_dpoketype()

    print("[LOAD] Criando tabelas e carregando dados")
    criar_tabelas()
    carregar_pokemon()
    carregar_pokecharac()
    carregar_pokeegg()
    carregar_pokemoves()
    carregar_pokestats()
    carregar_poketype()

    print("✅ --- PIPELINE FINALIZADO ---")

if __name__ == "__main__":
    run_pipeline(extract=False)