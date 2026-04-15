import pandas as pd
from sqlalchemy import create_engine

def carregar_moves():
    
    df = pd.read_csv("data/refined/dpokemoves_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_pokemon_moves",
        engine,
        if_exists="append",  # troca tabela toda
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_pokemon():
    
    df = pd.read_csv("data/refined/dpokemon_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_pokemon",
        engine,
        if_exists="append",  # troca tabela toda
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_pokeegg():
    
    df = pd.read_csv("data/refined/dpokeegg_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_pokeegg",
        engine,
        if_exists="append",  # troca tabela toda
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_pokecharac():
    
    df = pd.read_csv("data/refined/dpokecharac_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_pokecharac",
        engine,
        if_exists="append",  # troca tabela toda
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_pokestats():
    
    df = pd.read_csv("data/refined/dpokestats_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_pokestats",
        engine,
        if_exists="append",  # troca tabela toda
        index=False,
        method="multi"
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_poketype():
    
    df = pd.read_csv("data/refined/dpoketype_refined.csv", encoding="utf-8")

    engine = create_engine(
        "postgresql+psycopg2://postgres:auth102@localhost:5432/pokelineDB"
    )

    # 🚀 envia pro banco
    df.to_sql(
        "fact_poketype",
        engine,
        if_exists="append", 
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

carregar_pokemon()
carregar_moves()