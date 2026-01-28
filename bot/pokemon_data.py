"""
Pokemon data with spawn rates and rarity tiers
Using PokeAPI v2 - sprites from https://pokeapi.co/
"""

POKEMON_DATA = {
    # Common Pokemon (60% spawn rate total) - 75 Pokemon
    "Pidgey": {"rarity": "common", "spawn_weight": 1.2, "type": "Normal/Flying", "sprite": "16"},
    "Rattata": {"rarity": "common", "spawn_weight": 1.2, "type": "Normal", "sprite": "19"},
    "Caterpie": {"rarity": "common", "spawn_weight": 1.1, "type": "Bug", "sprite": "10"},
    "Weedle": {"rarity": "common", "spawn_weight": 1.1, "type": "Bug/Poison", "sprite": "13"},
    "Zubat": {"rarity": "common", "spawn_weight": 1.0, "type": "Poison/Flying", "sprite": "41"},
    "Magikarp": {"rarity": "common", "spawn_weight": 1.0, "type": "Water", "sprite": "129"},
    "Spearow": {"rarity": "common", "spawn_weight": 0.9, "type": "Normal/Flying", "sprite": "21"},
    "Ekans": {"rarity": "common", "spawn_weight": 0.9, "type": "Poison", "sprite": "23"},
    "Sandshrew": {"rarity": "common", "spawn_weight": 0.9, "type": "Ground", "sprite": "27"},
    "Nidoran♀": {"rarity": "common", "spawn_weight": 0.8, "type": "Poison", "sprite": "29"},
    "Nidoran♂": {"rarity": "common", "spawn_weight": 0.8, "type": "Poison", "sprite": "32"},
    "Oddish": {"rarity": "common", "spawn_weight": 0.8, "type": "Grass/Poison", "sprite": "43"},
    "Paras": {"rarity": "common", "spawn_weight": 0.8, "type": "Bug/Grass", "sprite": "46"},
    "Venonat": {"rarity": "common", "spawn_weight": 0.8, "type": "Bug/Poison", "sprite": "48"},
    "Diglett": {"rarity": "common", "spawn_weight": 0.8, "type": "Ground", "sprite": "50"},
    "Meowth": {"rarity": "common", "spawn_weight": 0.7, "type": "Normal", "sprite": "52"},
    "Poliwag": {"rarity": "common", "spawn_weight": 0.7, "type": "Water", "sprite": "60"},
    "Bellsprout": {"rarity": "common", "spawn_weight": 0.7, "type": "Grass/Poison", "sprite": "69"},
    "Tentacool": {"rarity": "common", "spawn_weight": 0.7, "type": "Water/Poison", "sprite": "72"},
    "Geodude": {"rarity": "common", "spawn_weight": 0.7, "type": "Rock/Ground", "sprite": "74"},
    "Slowpoke": {"rarity": "common", "spawn_weight": 0.7, "type": "Water/Psychic", "sprite": "79"},
    "Magnemite": {"rarity": "common", "spawn_weight": 0.7, "type": "Electric/Steel", "sprite": "81"},
    "Doduo": {"rarity": "common", "spawn_weight": 0.7, "type": "Normal/Flying", "sprite": "84"},
    "Seel": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "86"},
    "Grimer": {"rarity": "common", "spawn_weight": 0.6, "type": "Poison", "sprite": "88"},
    "Shellder": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "90"},
    "Gastly": {"rarity": "common", "spawn_weight": 0.6, "type": "Ghost/Poison", "sprite": "92"},
    "Drowzee": {"rarity": "common", "spawn_weight": 0.6, "type": "Psychic", "sprite": "96"},
    "Krabby": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "98"},
    "Voltorb": {"rarity": "common", "spawn_weight": 0.6, "type": "Electric", "sprite": "100"},
    "Exeggcute": {"rarity": "common", "spawn_weight": 0.6, "type": "Grass/Psychic", "sprite": "102"},
    "Cubone": {"rarity": "common", "spawn_weight": 0.6, "type": "Ground", "sprite": "104"},
    "Koffing": {"rarity": "common", "spawn_weight": 0.6, "type": "Poison", "sprite": "109"},
    "Horsea": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "116"},
    "Goldeen": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "118"},
    "Staryu": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "120"},
    "Hoothoot": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "163"},
    "Ledyba": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "165"},
    "Spinarak": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Poison", "sprite": "167"},
    "Sentret": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "161"},
    "Hoppip": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Flying", "sprite": "187"},
    "Sunkern": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "191"},
    "Wooper": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Ground", "sprite": "194"},
    "Swinub": {"rarity": "common", "spawn_weight": 0.5, "type": "Ice/Ground", "sprite": "220"},
    "Remoraid": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "223"},
    "Poochyena": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark", "sprite": "261"},
    "Zigzagoon": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "263"},
    "Wurmple": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "265"},
    "Lotad": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Grass", "sprite": "270"},
    "Seedot": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "273"},
    "Taillow": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "276"},
    "Wingull": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Flying", "sprite": "278"},
    "Ralts": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic/Fairy", "sprite": "280"},
    "Whismur": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "293"},
    "Azurill": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Fairy", "sprite": "298"},
    "Skitty": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "300"},
    "Aron": {"rarity": "common", "spawn_weight": 0.5, "type": "Steel/Rock", "sprite": "304"},
    "Gulpin": {"rarity": "common", "spawn_weight": 0.5, "type": "Poison", "sprite": "316"},
    "Wailmer": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "320"},
    "Spoink": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic", "sprite": "325"},
    "Swablu": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "333"},
    "Barboach": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Ground", "sprite": "339"},
    "Corphish": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "341"},
    "Feebas": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "349"},
    "Bidoof": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "399"},
    "Starly": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "396"},
    "Kricketot": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "401"},
    "Shinx": {"rarity": "common", "spawn_weight": 0.5, "type": "Electric", "sprite": "403"},
    "Budew": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Poison", "sprite": "406"},
    "Burmy": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "412"},
    "Cherubi": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "420"},
    "Buizel": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "418"},
    "Patrat": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "504"},
    "Purrloin": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark", "sprite": "509"},
    
    # Uncommon Pokemon (25% spawn rate total) - 50 Pokemon
    "Pikachu": {"rarity": "uncommon", "spawn_weight": 0.8, "type": "Electric", "sprite": "25"},
    "Bulbasaur": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Grass/Poison", "sprite": "1"},
    "Charmander": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Fire", "sprite": "4"},
    "Squirtle": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Water", "sprite": "7"},
    "Eevee": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Normal", "sprite": "133"},
    "Psyduck": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Water", "sprite": "54"},
    "Mankey": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fighting", "sprite": "56"},
    "Growlithe": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fire", "sprite": "58"},
    "Abra": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Psychic", "sprite": "63"},
    "Machop": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fighting", "sprite": "66"},
    "Ponyta": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fire", "sprite": "77"},
    "Farfetch'd": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "83"},
    "Onix": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Rock/Ground", "sprite": "95"},
    "Rhyhorn": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Ground/Rock", "sprite": "111"},
    "Tangela": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Grass", "sprite": "114"},
    "Scyther": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "123"},
    "Pinsir": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug", "sprite": "127"},
    "Tauros": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal", "sprite": "128"},
    "Omanyte": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "138"},
    "Kabuto": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "140"},
    "Chikorita": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "152"},
    "Cyndaquil": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "155"},
    "Totodile": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "158"},
    "Mareep": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "179"},
    "Marill": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Fairy", "sprite": "183"},
    "Sudowoodo": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock", "sprite": "185"},
    "Aipom": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "190"},
    "Yanma": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "193"},
    "Murkrow": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Flying", "sprite": "198"},
    "Misdreavus": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ghost", "sprite": "200"},
    "Girafarig": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal/Psychic", "sprite": "203"},
    "Pineco": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug", "sprite": "204"},
    "Dunsparce": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "206"},
    "Qwilfish": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Poison", "sprite": "211"},
    "Shuckle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Rock", "sprite": "213"},
    "Sneasel": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Ice", "sprite": "215"},
    "Teddiursa": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "216"},
    "Houndour": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Fire", "sprite": "228"},
    "Phanpy": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground", "sprite": "231"},
    "Treecko": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "252"},
    "Torchic": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "255"},
    "Mudkip": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "258"},
    "Nincada": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Ground", "sprite": "290"},
    "Electrike": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "309"},
    "Cacnea": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "331"},
    "Trapinch": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground", "sprite": "328"},
    "Lileep": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Grass", "sprite": "345"},
    "Anorith": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Bug", "sprite": "347"},
    "Snorunt": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ice", "sprite": "361"},
    "Turtwig": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "387"},
    
    # Rare Pokemon (10% spawn rate total) - 25 Pokemon
    "Dratini": {"rarity": "rare", "spawn_weight": 0.6, "type": "Dragon", "sprite": "147"},
    "Lapras": {"rarity": "rare", "spawn_weight": 0.5, "type": "Water/Ice", "sprite": "131"},
    "Snorlax": {"rarity": "rare", "spawn_weight": 0.5, "type": "Normal", "sprite": "143"},
    "Aerodactyl": {"rarity": "rare", "spawn_weight": 0.5, "type": "Rock/Flying", "sprite": "142"},
    "Porygon": {"rarity": "rare", "spawn_weight": 0.5, "type": "Normal", "sprite": "137"},
    "Chansey": {"rarity": "rare", "spawn_weight": 0.5, "type": "Normal", "sprite": "113"},
    "Hitmonlee": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fighting", "sprite": "106"},
    "Hitmonchan": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fighting", "sprite": "107"},
    "Lickitung": {"rarity": "rare", "spawn_weight": 0.4, "type": "Normal", "sprite": "108"},
    "Mr. Mime": {"rarity": "rare", "spawn_weight": 0.4, "type": "Psychic/Fairy", "sprite": "122"},
    "Jynx": {"rarity": "rare", "spawn_weight": 0.4, "type": "Ice/Psychic", "sprite": "124"},
    "Electabuzz": {"rarity": "rare", "spawn_weight": 0.4, "type": "Electric", "sprite": "125"},
    "Magmar": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fire", "sprite": "126"},
    "Larvitar": {"rarity": "rare", "spawn_weight": 0.4, "type": "Rock/Ground", "sprite": "246"},
    "Pupitar": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock/Ground", "sprite": "247"},
    "Beldum": {"rarity": "rare", "spawn_weight": 0.4, "type": "Steel/Psychic", "sprite": "374"},
    "Bagon": {"rarity": "rare", "spawn_weight": 0.4, "type": "Dragon", "sprite": "371"},
    "Gible": {"rarity": "rare", "spawn_weight": 0.4, "type": "Dragon/Ground", "sprite": "443"},
    "Riolu": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fighting", "sprite": "447"},
    "Cranidos": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock", "sprite": "408"},
    "Shieldon": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock/Steel", "sprite": "410"},
    "Skorupi": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Bug", "sprite": "451"},
    "Croagunk": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Fighting", "sprite": "453"},
    "Rotom": {"rarity": "rare", "spawn_weight": 0.3, "type": "Electric/Ghost", "sprite": "479"},
    "Spiritomb": {"rarity": "rare", "spawn_weight": 0.3, "type": "Ghost/Dark", "sprite": "442"},
    
    # Epic Pokemon (4% spawn rate total) - 10 Pokemon
    "Dragonair": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon", "sprite": "148"},
    "Dragonite": {"rarity": "epic", "spawn_weight": 0.4, "type": "Dragon/Flying", "sprite": "149"},
    "Tyranitar": {"rarity": "epic", "spawn_weight": 0.5, "type": "Rock/Dark", "sprite": "248"},
    "Metagross": {"rarity": "epic", "spawn_weight": 0.5, "type": "Steel/Psychic", "sprite": "376"},
    "Salamence": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon/Flying", "sprite": "373"},
    "Garchomp": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon/Ground", "sprite": "445"},
    "Lucario": {"rarity": "epic", "spawn_weight": 0.5, "type": "Fighting/Steel", "sprite": "448"},
    "Arcanine": {"rarity": "epic", "spawn_weight": 0.4, "type": "Fire", "sprite": "59"},
    "Gyarados": {"rarity": "epic", "spawn_weight": 0.4, "type": "Water/Flying", "sprite": "130"},
    "Milotic": {"rarity": "epic", "spawn_weight": 0.3, "type": "Water", "sprite": "350"},
    
    # Legendary Pokemon (1% spawn rate total) - 7 Pokemon
    "Articuno": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Ice/Flying", "sprite": "144"},
    "Zapdos": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Electric/Flying", "sprite": "145"},
    "Moltres": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Fire/Flying", "sprite": "146"},
    "Mewtwo": {"rarity": "legendary", "spawn_weight": 0.2, "type": "Psychic", "sprite": "150"},
    "Lugia": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Psychic/Flying", "sprite": "249"},
    "Ho-Oh": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Fire/Flying", "sprite": "250"},
    "Rayquaza": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Dragon/Flying", "sprite": "384"},
}

# Pokeball types with capture rates
POKEBALL_TYPES = {
    "pokeball": {
        "name": "Poké Ball",
        "cost": 0,  # Free starter balls
        "capture_rates": {
            "common": 0.70,      # 70% catch rate for common
            "uncommon": 0.50,    # 50% catch rate for uncommon
            "rare": 0.30,        # 30% catch rate for rare
            "epic": 0.15,        # 15% catch rate for epic
            "legendary": 0.05    # 5% catch rate for legendary
        },
        "color": "#FF0000"
    },
    "greatball": {
        "name": "Great Ball",
        "cost": 50,
        "capture_rates": {
            "common": 0.90,
            "uncommon": 0.70,
            "rare": 0.50,
            "epic": 0.30,
            "legendary": 0.10
        },
        "color": "#0066CC"
    },
    "ultraball": {
        "name": "Ultra Ball",
        "cost": 200,
        "capture_rates": {
            "common": 0.99,
            "uncommon": 0.90,
            "rare": 0.70,
            "epic": 0.50,
            "legendary": 0.20
        },
        "color": "#FFD700"
    },
    "masterball": {
        "name": "Master Ball",
        "cost": 1000,
        "capture_rates": {
            "common": 1.0,
            "uncommon": 1.0,
            "rare": 1.0,
            "epic": 1.0,
            "legendary": 1.0  # 100% catch rate for everything
        },
        "color": "#A020F0"
    }
}

# Shop items (coins to purchase balls)
SHOP_ITEMS = {
    "pokeball": {"quantity": 5, "cost": 10},
    "greatball": {"quantity": 3, "cost": 100},
    "ultraball": {"quantity": 1, "cost": 200},
    "masterball": {"quantity": 1, "cost": 1000}
}

# Starting inventory for new users
STARTER_INVENTORY = {
    "pokeball": 5,
    "greatball": 0,
    "ultraball": 0,
    "masterball": 0
}

# Coin rewards
COINS_PER_CATCH = 10
COINS_PER_MINUTE_WATCHING = 1
DAILY_LOGIN_BONUS = 50

def get_weighted_pokemon():
    """Return a random pokemon based on spawn weights"""
    import random
    
    pokemon_list = []
    weights = []
    
    for name, data in POKEMON_DATA.items():
        pokemon_list.append(name)
        weights.append(data["spawn_weight"])
    
    return random.choices(pokemon_list, weights=weights, k=1)[0]

def get_capture_rate(pokemon_name, ball_type):
    """Get the capture rate for a pokemon with a specific ball"""
    if pokemon_name not in POKEMON_DATA:
        return 0.0
    
    rarity = POKEMON_DATA[pokemon_name]["rarity"]
    
    if ball_type not in POKEBALL_TYPES:
        return 0.0
    
    return POKEBALL_TYPES[ball_type]["capture_rates"][rarity]

def get_pokemon_sprite_url(pokemon_name):
    """Get the sprite URL for a pokemon"""
    if pokemon_name not in POKEMON_DATA:
        return None
    
    sprite_id = POKEMON_DATA[pokemon_name]["sprite"]
    # Using PokeAPI sprites
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{sprite_id}.png"
