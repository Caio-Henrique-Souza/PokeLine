from src.extract.extract import extrair_pokemons, extrair_gameversion, extrair_detalhes_pokemons, extrair_species_pokemons
from src.transform.bronze import criar_dpokegen,criar_dpokecharac, criar_dpokeegg, criar_dpokemon, criar_dpokemoves, criar_dpokestats, criar_dpoketype, criar_dpokesprites
from src.transform.silver import transformar_dpokegen,transformar_dpokecharac, transformar_dpokeegg, transformar_dpokemon, transformar_dpokemoves, transformar_dpokestats,transformar_dpoketype, transformar_dpokesprites
from src.load.load import get_engine,carregar_pokegen,carregar_pokemoves, carregar_pokecharac,carregar_pokeegg,carregar_pokemon,carregar_pokestats,carregar_poketype, criar_tabelas, carregar_pokesprite
def run_pipeline(extract=True):
    engine = get_engine()
    print("🚀 --- INICIANDO PIPELINE ---")
    
    if extract:
        print("[EXTRACT] Extração de dados")
        extrair_pokemons(151)
        extrair_gameversion(9)
        extrair_detalhes_pokemons()
        extrair_species_pokemons()

    print("[CRIAR CSV]")
    criar_dpokecharac()
    criar_dpokeegg()
    criar_dpokemon()
    criar_dpokemoves()
    criar_dpokestats()
    criar_dpoketype()
    criar_dpokesprites()
    criar_dpokegen()

    print("[TRANSFORM] Processamento Bronze/Silver")
    transformar_dpokemon()
    transformar_dpokecharac()
    transformar_dpokeegg()
    transformar_dpokemoves()
    transformar_dpokestats()
    transformar_dpoketype()
    transformar_dpokesprites()
    transformar_dpokegen()

    print("[LOAD] Criando tabelas e carregando dados")
    criar_tabelas(engine)

    carregar_pokemon(engine)
    carregar_pokecharac(engine)
    carregar_pokeegg(engine)
    carregar_pokemoves(engine)
    carregar_pokestats(engine)
    carregar_poketype(engine)
    carregar_pokesprite(engine)
    carregar_pokegen(engine)

    print("✅ --- PIPELINE FINALIZADO ---")

if __name__ == "__main__":
    run_pipeline(extract=False)