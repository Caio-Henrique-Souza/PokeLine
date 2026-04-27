CREATE TABLE IF NOT EXISTS dimension_pokemon (
    pokemon_id SMALLINT PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS dimension_poketype (
    pokemon_id SMALLINT,
    type TEXT,
    PRIMARY KEY (pokemon_id, type)
);

CREATE TABLE IF NOT EXISTS dimension_pokestats (
    pokemon_id SMALLINT PRIMARY KEY,
    hp SMALLINT,
    attack SMALLINT,
    defense SMALLINT,
    special_attack SMALLINT,
    special_defense SMALLINT,
    speed SMALLINT
);

CREATE TABLE IF NOT EXISTS dimension_pokemoves (
    pokemon_id SMALLINT,
    move TEXT,
    level_requirement SMALLINT,
    learn_method TEXT,
    game_version TEXT,
    PRIMARY KEY (pokemon_id, move, game_version)
);

CREATE TABLE IF NOT EXISTS dimension_pokecharac (
    pokemon_id SMALLINT,
    base_xp SMALLINT,
    height SMALLINT,
    weight SMALLINT,
    abilities TEXT,
    PRIMARY KEY (pokemon_id, abilities)
);

CREATE TABLE IF NOT EXISTS dimension_pokeegg (
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

CREATE TABLE IF NOT EXISTS dimension_pokesprites (
    pokemon_id SMALLINT PRIMARY KEY,
    back_default TEXT,
    back_shiny TEXT,   
    front_default TEXT,
    front_shiny TEXT
);

CREATE TABLE IF NOT EXISTS dimension_pokegen (
    game_gen TEXT,
    version_group text,
    PRIMARY KEY(game_gen,version_group)
);