-- =========================
-- FACT POKEMON
-- =========================
CREATE TABLE IF NOT EXISTS fact_pokemon (
    pokemon_id SMALLINT PRIMARY KEY,
    name TEXT
);

-- =========================
-- FACT POKEMON TYPES
-- =========================
CREATE TABLE IF NOT EXISTS fact_poketype (
    pokemon_id SMALLINT,
    type TEXT,
    PRIMARY KEY (pokemon_id, type)
);

-- =========================
-- FACT POKEMON STATS
-- =========================
CREATE TABLE IF NOT EXISTS fact_pokestats (
    pokemon_id SMALLINT PRIMARY KEY,
    hp SMALLINT,
    attack SMALLINT,
    defense SMALLINT,
    special_attack SMALLINT,
    special_defense SMALLINT,
    speed SMALLINT
);

-- =========================
-- FACT POKEMON MOVES
-- =========================
CREATE TABLE IF NOT EXISTS fact_pokemon_moves (
    pokemon_id SMALLINT,
    move TEXT,
    level_requirement SMALLINT,
    learn_method TEXT,
    game_version TEXT,
    PRIMARY KEY (pokemon_id, move, game_version)
);

-- =========================
-- FACT POKEMON CHARACTERISTICS
-- =========================
CREATE TABLE IF NOT EXISTS fact_pokecharac (
    pokemon_id SMALLINT,
    base_xp SMALLINT,
    height SMALLINT,
    weight SMALLINT,
    abilities TEXT,
    PRIMARY KEY (pokemon_id, abilities)
);

-- =========================
-- FACT POKEMON EGG
-- =========================
CREATE TABLE IF NOT EXISTS fact_pokeegg (
    pokemon_id SMALLINT,
    is_legendary BOOLEAN,
    is_mythical BOOLEAN,
    hatch_counter SMALLINT,
    generation TEXT,
    growth_rate TEXT,
    habitat TEXT,
    evolves_from TEXT,
    egg TEXT,
    PRIMARY KEY (pokemon_id, egg)
);