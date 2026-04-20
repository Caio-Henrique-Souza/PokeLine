import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB = os.getenv("POSTGRES_DB")


def criar_tabelas():
    print("🧱 Criando tabelas no banco...")

    engine = create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )

    with open("src/load/sqltable.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(sql))

    print("✅ Tabelas criadas/verificadas com sucesso")

def carregar_pokemoves():
    
    df = pd.read_csv("data/refined/dpokemoves_refined.csv", encoding="utf-8")

    engine = create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_pokemon_moves"))

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
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_pokemon"))

    df.to_sql(
        "fact_pokemon",
        engine,
        if_exists="append",
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")

def carregar_pokeegg():
    
    df = pd.read_csv("data/refined/dpokeegg_refined.csv", encoding="utf-8")

    engine = create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_pokeegg"))

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
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_pokecharac"))

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
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_pokestats"))


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
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE fact_poketype"))

    # 🚀 envia pro banco
    df.to_sql(
        "fact_poketype",
        engine,
        if_exists="append", 
        index=False
    )

    print(f"🔥 Dados carregados no PostgreSQL: {len(df)} linhas")
