import pandas as pd
import os

def transformar_dpokemon():
    caminho = "data/processed/dpokemon.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)


    # 💾 Salvar no refined
    caminho_saida = f"{destino}/dpokemon_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"✅ dpokemon refinado salvo em {caminho_saida}")
    return True
    
def transformar_dpokestats():

    caminho = "data/processed/dpokestats.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    # 🔥 PADRONIZAÇÃO DE NOMES (HYPHEN → UNDERSCORE)
    df = df.rename(columns={
        "special-attack": "special_attack",
        "special-defense": "special_defense"
    })

    erros = []

    colunas_stats = [
        "hp", "attack", "defense",
        "special_attack", "special_defense", "speed"
    ]

    colunas_esperadas = ["pokemon_id"] + colunas_stats

    # 🧱 1. Estrutura
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 🧪 2. Nulls
    nulls = df[colunas_esperadas].isnull().sum()
    for col, qtd in nulls.items():
        if qtd > 0:
            erros.append(f"❌ {qtd} valores nulos em {col}")

    # 🔁 3. Duplicidade
    duplicados = df["pokemon_id"].duplicated().sum()
    if duplicados > 0:
        erros.append(f"❌ {duplicados} pokemon_id duplicados")

    # 📉 4. Valores inválidos
    for col in colunas_stats:
        if (df[col] <= 0).sum() > 0:
            erros.append(f"❌ Valores inválidos (<=0) em {col}")

    # 🧠 5. Tipos
    for col in colunas_esperadas:
        if not pd.api.types.is_numeric_dtype(df[col]):
            erros.append(f"❌ Coluna {col} não é numérica")

    # 📊 6. Soma stats
    soma_stats = df[colunas_stats].sum(axis=1)
    if (soma_stats > 800).sum() > 0:
        erros.append("❌ Soma de stats > 800 detectada")

    # 🚨 erro bloqueia
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 💾 salva refined
    caminho_saida = f"{destino}/dpokestats_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"🔥 dpokestats refinado salvo: {len(df)} linhas")
    return True

def transformar_dpoketype():
    caminho = "data/processed/dpoketype.csv"
    destino = "data/refined"
    
    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    # 1. Estrutura
    colunas_esperadas = ["pokemon_id", "type"]
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 2. Converter string → lista
    import ast
    try:
        df["type"] = df["type"].apply(ast.literal_eval)
    except:
        erros.append("❌ Erro ao converter 'type' para lista")

    # 3. Nulls
    if df["pokemon_id"].isnull().sum() > 0:
        erros.append("❌ Existem pokemon_id nulos")

    if df["type"].isnull().sum() > 0:
        erros.append("❌ Existem type nulos")

    # 4. Lista vazia
    vazios = df["type"].apply(lambda x: len(x) == 0).sum()
    if vazios > 0:
        erros.append("❌ Existem listas de type vazias")

    # 🚨 Se deu erro, para aqui
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 🔥 5. EXPLODE (1:N)
    df = df.explode("type")

    # 6. Remover duplicados (chave composta)
    duplicados = df.duplicated(subset=["pokemon_id", "type"]).sum()
    if duplicados > 0:
        print(f"⚠️ Removendo {duplicados} duplicados")
        df = df.drop_duplicates(subset=["pokemon_id", "type"])

    # 7. Salvar
    caminho_saida = f"{destino}/dpoketype_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"✅ dpoketype transformado com sucesso! {len(df)} linhas")
    return True

def transformar_dpokecharac():
    caminho = "data/processed/dpokecharac.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    # 1. Estrutura
    colunas_esperadas = ["pokemon_id", "abilities"]
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 2. Converter string → lista
    import ast
    try:
        df["abilities"] = df["abilities"].apply(ast.literal_eval)
    except:
        erros.append("❌ Erro ao converter abilities para lista")

    # 3. Nulls
    if df["pokemon_id"].isnull().sum() > 0:
        erros.append("❌ pokemon_id nulo")

    if df["abilities"].isnull().sum() > 0:
        erros.append("❌ abilities nulo")

    # 4. Lista vazia
    vazios = df["abilities"].apply(lambda x: isinstance(x, list) and len(x) == 0).sum()
    if vazios > 0:
        erros.append("❌ abilities vazias encontradas")

    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 🔥 EXPLODE (1:N)
    df = df.explode("abilities")

    # 5. Remove duplicados (chave composta)
    duplicados = df.duplicated(subset=["pokemon_id", "abilities"]).sum()
    if duplicados > 0:
        df = df.drop_duplicates(subset=["pokemon_id", "abilities"])

    # 6. Salvar
    caminho_saida = f"{destino}/dpokecharac_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"✅ dpokecharac transformado com sucesso! {len(df)} linhas")
    return True

def transformar_dpokeegg():
    caminho = "data/processed/dpokeegg.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    # 1. Estrutura
    colunas_esperadas = ["pokemon_id", "egg"]
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 2. Converter string → lista
    import ast
    try:
        df["egg"] = df["egg"].apply(ast.literal_eval)
    except:
        erros.append("❌ Erro ao converter egg para lista")

    # 3. Nulls
    if df["pokemon_id"].isnull().sum() > 0:
        erros.append("❌ pokemon_id nulo")

    if df["egg"].isnull().sum() > 0:
        erros.append("❌ egg nulo")

    # 4. Lista vazia
    vazios = df["egg"].apply(lambda x: isinstance(x, list) and len(x) == 0).sum()
    if vazios > 0:
        erros.append("❌ listas de egg vazias encontradas")

    # 🚨 Se erro, para aqui
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 🔥 EXPLODE (1:N)
    df = df.explode("egg")

    # 5. Remove duplicados (chave composta)
    duplicados = df.duplicated(subset=["pokemon_id", "egg"]).sum()
    if duplicados > 0:
        df = df.drop_duplicates(subset=["pokemon_id", "egg"])

    # 6. Salvar
    caminho_saida = f"{destino}/dpokeegg_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"✅ dpokeegg transformado com sucesso! {len(df)} linhas")
    return True

def transformar_dpokemoves():

    caminho = "data/processed/dPokeMoves.csv"
    destino = "data/refined"

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    # 🧱 Colunas obrigatórias
    colunas_esperadas = [
        "pokemon_id",
        "move",
        "level_requirement",
        "learn_method",
        "game_version"
    ]

    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 🧪 Nulls críticos
    for col in colunas_esperadas:
        if df[col].isnull().sum() > 0:
            erros.append(f"❌ {df[col].isnull().sum()} nulos em {col}")

    # 🔁 Duplicados (chave natural)
    df = df.drop_duplicates(subset=["pokemon_id", "move", "game_version"])

    # 📊 Tipos
    if not pd.api.types.is_numeric_dtype(df["pokemon_id"]):
        erros.append("❌ pokemon_id não é numérico")

    if not pd.api.types.is_numeric_dtype(df["level_requirement"]):
        erros.append("❌ level_requirement não é numérico")

    # 🧠 Regras de consistência
    if (df["level_requirement"] < 0).any():
        erros.append("❌ Existem level_requirement negativos")

    # 🚨 Se houver erros críticos, aborta
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    caminho_saida = f"{destino}/dpokemoves_refined.csv"
    df.to_csv(caminho_saida, index=False, encoding="utf-8")

    print(f"🔥 dpokemoves refinado validado e regravado: {len(df)} linhas")
    return True

def transformar_dpokesprites():

    caminho = "data/processed/dpokeSprites.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    colunas_esperadas = ["pokemon_id"]
    
    colunas_complementares = ["back_default",
                         "back_shiny",
                         "front_default",
                         "front_shiny"]

    # 🧱 1. Estrutura
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 🧪 2. Nulls
    nulls = df[colunas_esperadas].isnull().sum()
    for col, qtd in nulls.items():
        if qtd > 0:
            erros.append(f"❌ {qtd} valores nulos em {col}")

    # 🔁 3. Duplicidade
    duplicados = df["pokemon_id"].duplicated().sum()
    if duplicados > 0:
        erros.append(f"❌ {duplicados} pokemon_id duplicados")

    # 🧠 5. Tipos
    for col in colunas_complementares:
        if not pd.api.types.is_string_dtype(df[col]):
            erros.append(f"❌ Coluna {col} não é string")

    for col in colunas_esperadas:
        if not pd.api.types.is_numeric_dtype(df[col]):
            erros.append(f"❌ Coluna {col} não é numérica")

    # 🚨 erro bloqueia
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 💾 salva refined
    caminho_saida = f"{destino}/dpokesprites_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"🔥 dpokesprites refinado salvo: {len(df)} linhas")
    return True

def transformar_dpokegen():

    caminho = "data/processed/dpokeGen.csv"
    destino = "data/refined"

    os.makedirs(destino, exist_ok=True)

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False

    df = pd.read_csv(caminho)

    erros = []

    colunas_esperadas = ["game_gen", "version_group"]

    # 🧱 1. Estrutura
    for col in colunas_esperadas:
        if col not in df.columns:
            erros.append(f"❌ Coluna ausente: {col}")

    # 🧪 2. Nulls
    nulls = df[colunas_esperadas].isnull().sum()
    for col, qtd in nulls.items():
        if qtd > 0:
            erros.append(f"❌ {qtd} valores nulos em {col}")

    # 🔁 3. Duplicidade
    duplicados = df["version_group"].duplicated().sum()
    if duplicados > 0:
        erros.append(f"❌ {duplicados} version_group duplicados")

    # 🧠 5. Tipos
    for col in colunas_esperadas:
        if not pd.api.types.is_string_dtype(df[col]):
            erros.append(f"❌ Coluna {col} não é string")

    

    # 🚨 erro bloqueia
    if erros:
        print("🚨 ERROS ENCONTRADOS:")
        for erro in erros:
            print(erro)
        return False

    # 💾 salva refined
    caminho_saida = f"{destino}/dpokegen_refined.csv"
    df.to_csv(caminho_saida, index=False)

    print(f"🔥 dpokegen refinado salvo: {len(df)} linhas")
    return True
