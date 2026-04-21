from src.extract.extract import extrair_pokemons, extrair_detalhes_pokemons, extrair_species_pokemons
from src.transform.bronze import criar_dpokecharac, criar_dpokeegg, criar_dpokemon, criar_dpokemoves, criar_dpokestats, criar_dpoketype
from src.transform.silver import transformar_dpokecharac, transformar_dpokeegg, transformar_dpokemon, transformar_dpokemoves, transformar_dpokestats,transformar_dpoketype
from src.load.load import get_engine,carregar_pokemoves, carregar_pokecharac,carregar_pokeegg,carregar_pokemon,carregar_pokestats,carregar_poketype, criar_tabelas
def run_pipeline(extract=True):
    engine = get_engine()
    print("🚀 --- INICIANDO PIPELINE ---")
    
    if extract:
        print("[EXTRACT] Extração de dados")
        extrair_pokemons(3)
        extrair_detalhes_pokemons()
        extrair_species_pokemons()

    print("[CRIAR CSV]")
    criar_dpokecharac()
    criar_dpokeegg()
    criar_dpokemon()
    criar_dpokemoves()
    criar_dpokestats()
    criar_dpoketype()

    print("[TRANSFORM] Processamento Bronze/Silver")
    transformar_dpokemon()
    transformar_dpokecharac()
    transformar_dpokeegg()
    transformar_dpokemoves()
    transformar_dpokestats()
    transformar_dpoketype()

    print("[LOAD] Criando tabelas e carregando dados")
    criar_tabelas(engine)

    carregar_pokemon(engine)
    carregar_pokecharac(engine)
    carregar_pokeegg(engine)
    carregar_pokemoves(engine)
    carregar_pokestats(engine)
    carregar_poketype(engine)

    print("✅ --- PIPELINE FINALIZADO ---")

if __name__ == "__main__":
    run_pipeline(extract=True)