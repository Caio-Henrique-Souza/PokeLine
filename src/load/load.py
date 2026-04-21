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


# 🔧 conexão única
def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}",
        pool_size=5,
        max_overflow=10
    )


# 🧱 criar tabelas
def criar_tabelas(engine):
    print("🧱 Criando tabelas no banco...")

    with open("src/load/sqltable.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(sql))

    print("✅ Tabelas criadas/verificadas com sucesso")


# 🔥 função genérica de carga
def carregar_csv_para_banco(caminho_csv, nome_tabela, engine):
    
    print(f"📥 Carregando {nome_tabela}...")

    df = pd.read_csv(caminho_csv, encoding="utf-8")

    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {nome_tabela}"))

    df.to_sql(
        nome_tabela,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(f"🔥 {nome_tabela}: {len(df)} linhas carregadas")


# 🧩 funções específicas (agora simples e limpas)

def carregar_pokemon(engine):
    carregar_csv_para_banco(
        "data/refined/dpokemon_refined.csv",
        "fact_pokemon",
        engine
    )


def carregar_pokecharac(engine):
    carregar_csv_para_banco(
        "data/refined/dpokecharac_refined.csv",
        "fact_pokecharac",
        engine
    )


def carregar_pokeegg(engine):
    carregar_csv_para_banco(
        "data/refined/dpokeegg_refined.csv",
        "fact_pokeegg",
        engine
    )


def carregar_pokemoves(engine):
    carregar_csv_para_banco(
        "data/refined/dpokemoves_refined.csv",
        "fact_pokemon_moves",
        engine
    )


def carregar_pokestats(engine):
    carregar_csv_para_banco(
        "data/refined/dpokestats_refined.csv",
        "fact_pokestats",
        engine
    )


def carregar_poketype(engine):
    carregar_csv_para_banco(
        "data/refined/dpoketype_refined.csv",
        "fact_poketype",
        engine
    )