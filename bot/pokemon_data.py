"""
Complete Pokemon data for Generations 1-4 (493 Pokemon)
Using PokeAPI v2 - sprites from https://pokeapi.co/
"""

POKEMON_DATA = {
    # GENERATION 1 (Kanto) - #1-151
    
    # Common Pokemon (High spawn rate)
    "Pidgey": {"rarity": "common", "spawn_weight": 1.2, "type": "Normal/Flying", "sprite": "16"},
    "Pidgeotto": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "17"},
    "Rattata": {"rarity": "common", "spawn_weight": 1.2, "type": "Normal", "sprite": "19"},
    "Raticate": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "20"},
    "Caterpie": {"rarity": "common", "spawn_weight": 1.1, "type": "Bug", "sprite": "10"},
    "Metapod": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug", "sprite": "11"},
    "Weedle": {"rarity": "common", "spawn_weight": 1.1, "type": "Bug/Poison", "sprite": "13"},
    "Kakuna": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Poison", "sprite": "14"},
    "Zubat": {"rarity": "common", "spawn_weight": 1.0, "type": "Poison/Flying", "sprite": "41"},
    "Golbat": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison/Flying", "sprite": "42"},
    "Magikarp": {"rarity": "common", "spawn_weight": 1.0, "type": "Water", "sprite": "129"},
    "Spearow": {"rarity": "common", "spawn_weight": 0.9, "type": "Normal/Flying", "sprite": "21"},
    "Fearow": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "22"},
    "Ekans": {"rarity": "common", "spawn_weight": 0.9, "type": "Poison", "sprite": "23"},
    "Arbok": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "24"},
    "Sandshrew": {"rarity": "common", "spawn_weight": 0.9, "type": "Ground", "sprite": "27"},
    "Sandslash": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground", "sprite": "28"},
    "Nidoran♀": {"rarity": "common", "spawn_weight": 0.8, "type": "Poison", "sprite": "29"},
    "Nidorina": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "30"},
    "Nidoran♂": {"rarity": "common", "spawn_weight": 0.8, "type": "Poison", "sprite": "32"},
    "Nidorino": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "33"},
    "Oddish": {"rarity": "common", "spawn_weight": 0.8, "type": "Grass/Poison", "sprite": "43"},
    "Gloom": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "44"},
    "Paras": {"rarity": "common", "spawn_weight": 0.8, "type": "Bug/Grass", "sprite": "46"},
    "Parasect": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Grass", "sprite": "47"},
    "Venonat": {"rarity": "common", "spawn_weight": 0.8, "type": "Bug/Poison", "sprite": "48"},
    "Venomoth": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Poison", "sprite": "49"},
    "Diglett": {"rarity": "common", "spawn_weight": 0.8, "type": "Ground", "sprite": "50"},
    "Dugtrio": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground", "sprite": "51"},
    "Meowth": {"rarity": "common", "spawn_weight": 0.7, "type": "Normal", "sprite": "52"},
    "Persian": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "53"},
    "Poliwag": {"rarity": "common", "spawn_weight": 0.7, "type": "Water", "sprite": "60"},
    "Poliwhirl": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "61"},
    "Bellsprout": {"rarity": "common", "spawn_weight": 0.7, "type": "Grass/Poison", "sprite": "69"},
    "Weepinbell": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "70"},
    "Tentacool": {"rarity": "common", "spawn_weight": 0.7, "type": "Water/Poison", "sprite": "72"},
    "Tentacruel": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Poison", "sprite": "73"},
    "Geodude": {"rarity": "common", "spawn_weight": 0.7, "type": "Rock/Ground", "sprite": "74"},
    "Graveler": {"rarity": "common", "spawn_weight": 0.4, "type": "Rock/Ground", "sprite": "75"},
    "Slowpoke": {"rarity": "common", "spawn_weight": 0.7, "type": "Water/Psychic", "sprite": "79"},
    "Slowbro": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Psychic", "sprite": "80"},
    "Magnemite": {"rarity": "common", "spawn_weight": 0.7, "type": "Electric/Steel", "sprite": "81"},
    "Magneton": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric/Steel", "sprite": "82"},
    "Doduo": {"rarity": "common", "spawn_weight": 0.7, "type": "Normal/Flying", "sprite": "84"},
    "Dodrio": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "85"},
    "Seel": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "86"},
    "Dewgong": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Ice", "sprite": "87"},
    "Grimer": {"rarity": "common", "spawn_weight": 0.6, "type": "Poison", "sprite": "88"},
    "Muk": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "89"},
    "Shellder": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "90"},
    "Gastly": {"rarity": "common", "spawn_weight": 0.6, "type": "Ghost/Poison", "sprite": "92"},
    "Haunter": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost/Poison", "sprite": "93"},
    "Drowzee": {"rarity": "common", "spawn_weight": 0.6, "type": "Psychic", "sprite": "96"},
    "Hypno": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic", "sprite": "97"},
    "Krabby": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "98"},
    "Kingler": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "99"},
    "Voltorb": {"rarity": "common", "spawn_weight": 0.6, "type": "Electric", "sprite": "100"},
    "Electrode": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric", "sprite": "101"},
    "Exeggcute": {"rarity": "common", "spawn_weight": 0.6, "type": "Grass/Psychic", "sprite": "102"},
    "Cubone": {"rarity": "common", "spawn_weight": 0.6, "type": "Ground", "sprite": "104"},
    "Marowak": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground", "sprite": "105"},
    "Koffing": {"rarity": "common", "spawn_weight": 0.6, "type": "Poison", "sprite": "109"},
    "Weezing": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "110"},
    "Horsea": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "116"},
    "Seadra": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "117"},
    "Goldeen": {"rarity": "common", "spawn_weight": 0.6, "type": "Water", "sprite": "118"},
    "Seaking": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "119"},
    "Staryu": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "120"},
    "Starmie": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Psychic", "sprite": "121"},
    "Ditto": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "132"},
    
    # Uncommon Gen 1
    "Pikachu": {"rarity": "uncommon", "spawn_weight": 0.8, "type": "Electric", "sprite": "25"},
    "Raichu": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Electric", "sprite": "26"},
    "Bulbasaur": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Grass/Poison", "sprite": "1"},
    "Ivysaur": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Grass/Poison", "sprite": "2"},
    "Charmander": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Fire", "sprite": "4"},
    "Charmeleon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fire", "sprite": "5"},
    "Squirtle": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Water", "sprite": "7"},
    "Wartortle": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Water", "sprite": "8"},
    "Butterfree": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "12"},
    "Beedrill": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug/Poison", "sprite": "15"},
    "Pidgeot": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "18"},
    "Eevee": {"rarity": "uncommon", "spawn_weight": 0.7, "type": "Normal", "sprite": "133"},
    "Vaporeon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Water", "sprite": "134"},
    "Jolteon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Electric", "sprite": "135"},
    "Flareon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fire", "sprite": "136"},
    "Psyduck": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Water", "sprite": "54"},
    "Golduck": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "55"},
    "Mankey": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fighting", "sprite": "56"},
    "Primeape": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fighting", "sprite": "57"},
    "Growlithe": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fire", "sprite": "58"},
    "Abra": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Psychic", "sprite": "63"},
    "Kadabra": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Psychic", "sprite": "64"},
    "Machop": {"rarity": "uncommon", "spawn_weight": 0.6, "type": "Fighting", "sprite": "66"},
    "Machoke": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fighting", "sprite": "67"},
    "Ponyta": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fire", "sprite": "77"},
    "Rapidash": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "78"},
    "Farfetch'd": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "83"},
    "Onix": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Rock/Ground", "sprite": "95"},
    "Rhyhorn": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Ground/Rock", "sprite": "111"},
    "Rhydon": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground/Rock", "sprite": "112"},
    "Tangela": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Grass", "sprite": "114"},
    "Kangaskhan": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal", "sprite": "115"},
    "Scyther": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "123"},
    "Pinsir": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Bug", "sprite": "127"},
    "Tauros": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal", "sprite": "128"},
    "Omanyte": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "138"},
    "Omastar": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "139"},
    "Kabuto": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "140"},
    "Kabutops": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Water", "sprite": "141"},
    "Clefairy": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fairy", "sprite": "35"},
    "Clefable": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy", "sprite": "36"},
    "Jigglypuff": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Normal/Fairy", "sprite": "39"},
    "Wigglytuff": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal/Fairy", "sprite": "40"},
    "Vileplume": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "45"},
    "Victreebel": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "71"},
    "Golem": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Ground", "sprite": "76"},
    "Poliwrath": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Fighting", "sprite": "62"},
    "Alakazam": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Psychic", "sprite": "65"},
    "Machamp": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fighting", "sprite": "68"},
    "Exeggutor": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Psychic", "sprite": "103"},
    "Vulpix": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Fire", "sprite": "37"},
    "Ninetales": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "38"},
    "Nidoqueen": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Poison/Ground", "sprite": "31"},
    "Nidoking": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Poison/Ground", "sprite": "34"},
    
    # Rare Gen 1
    "Dratini": {"rarity": "rare", "spawn_weight": 0.6, "type": "Dragon", "sprite": "147"},
    "Dragonair": {"rarity": "rare", "spawn_weight": 0.5, "type": "Dragon", "sprite": "148"},
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
    "Gengar": {"rarity": "rare", "spawn_weight": 0.4, "type": "Ghost/Poison", "sprite": "94"},
    "Cloyster": {"rarity": "rare", "spawn_weight": 0.4, "type": "Water/Ice", "sprite": "91"},
    "Venusaur": {"rarity": "rare", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "3"},
    "Charizard": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fire/Flying", "sprite": "6"},
    "Blastoise": {"rarity": "rare", "spawn_weight": 0.4, "type": "Water", "sprite": "9"},
    
    # Epic Gen 1
    "Dragonite": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon/Flying", "sprite": "149"},
    "Arcanine": {"rarity": "epic", "spawn_weight": 0.4, "type": "Fire", "sprite": "59"},
    "Gyarados": {"rarity": "epic", "spawn_weight": 0.4, "type": "Water/Flying", "sprite": "130"},
    
    # Legendary Gen 1
    "Articuno": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Ice/Flying", "sprite": "144"},
    "Zapdos": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Electric/Flying", "sprite": "145"},
    "Moltres": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Fire/Flying", "sprite": "146"},
    "Mewtwo": {"rarity": "legendary", "spawn_weight": 0.2, "type": "Psychic", "sprite": "150"},
    "Mew": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Psychic", "sprite": "151"},
    
    # GENERATION 2 (Johto) - #152-251
    
    # Common Gen 2
    "Hoothoot": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "163"},
    "Noctowl": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "164"},
    "Ledyba": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "165"},
    "Ledian": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "166"},
    "Spinarak": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Poison", "sprite": "167"},
    "Ariados": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Poison", "sprite": "168"},
    "Sentret": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "161"},
    "Furret": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "162"},
    "Hoppip": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Flying", "sprite": "187"},
    "Skiploom": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Flying", "sprite": "188"},
    "Jumpluff": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Flying", "sprite": "189"},
    "Sunkern": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "191"},
    "Sunflora": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass", "sprite": "192"},
    "Wooper": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Ground", "sprite": "194"},
    "Quagsire": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Ground", "sprite": "195"},
    "Swinub": {"rarity": "common", "spawn_weight": 0.5, "type": "Ice/Ground", "sprite": "220"},
    "Piloswine": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice/Ground", "sprite": "221"},
    "Remoraid": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "223"},
    "Octillery": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "224"},
    "Crobat": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison/Flying", "sprite": "169"},
    "Chinchou": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Electric", "sprite": "170"},
    "Lanturn": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Electric", "sprite": "171"},
    "Natu": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic/Flying", "sprite": "177"},
    "Xatu": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic/Flying", "sprite": "178"},
    "Wobbuffet": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic", "sprite": "202"},
    
    # Uncommon Gen 2
    "Chikorita": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "152"},
    "Bayleef": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "153"},
    "Meganium": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "154"},
    "Cyndaquil": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "155"},
    "Quilava": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "156"},
    "Typhlosion": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "157"},
    "Totodile": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "158"},
    "Croconaw": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "159"},
    "Feraligatr": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "160"},
    "Mareep": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "179"},
    "Flaaffy": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "180"},
    "Ampharos": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "181"},
    "Marill": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Fairy", "sprite": "183"},
    "Azumarill": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Fairy", "sprite": "184"},
    "Sudowoodo": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock", "sprite": "185"},
    "Politoed": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "186"},
    "Aipom": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "190"},
    "Yanma": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "193"},
    "Murkrow": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Flying", "sprite": "198"},
    "Slowking": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Psychic", "sprite": "199"},
    "Misdreavus": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ghost", "sprite": "200"},
    "Unown": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Psychic", "sprite": "201"},
    "Girafarig": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal/Psychic", "sprite": "203"},
    "Pineco": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug", "sprite": "204"},
    "Forretress": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Steel", "sprite": "205"},
    "Dunsparce": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "206"},
    "Gligar": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground/Flying", "sprite": "207"},
    "Steelix": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Steel/Ground", "sprite": "208"},
    "Qwilfish": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Poison", "sprite": "211"},
    "Scizor": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Steel", "sprite": "212"},
    "Shuckle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Rock", "sprite": "213"},
    "Heracross": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Fighting", "sprite": "214"},
    "Sneasel": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Ice", "sprite": "215"},
    "Teddiursa": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "216"},
    "Ursaring": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "217"},
    "Slugma": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "218"},
    "Magcargo": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire/Rock", "sprite": "219"},
    "Snubbull": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy", "sprite": "209"},
    "Granbull": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy", "sprite": "210"},
    "Corsola": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Rock", "sprite": "222"},
    "Delibird": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ice/Flying", "sprite": "225"},
    "Mantine": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Flying", "sprite": "226"},
    "Skarmory": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Steel/Flying", "sprite": "227"},
    "Houndour": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Fire", "sprite": "228"},
    "Houndoom": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dark/Fire", "sprite": "229"},
    "Phanpy": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground", "sprite": "231"},
    "Donphan": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground", "sprite": "232"},
    "Porygon2": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "233"},
    "Stantler": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "234"},
    "Smeargle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "235"},
    "Tyrogue": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fighting", "sprite": "236"},
    "Hitmontop": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fighting", "sprite": "237"},
    "Smoochum": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ice/Psychic", "sprite": "238"},
    "Elekid": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "239"},
    "Magby": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "240"},
    "Miltank": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "241"},
    "Blissey": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal", "sprite": "242"},
    "Pichu": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "172"},
    "Cleffa": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy", "sprite": "173"},
    "Igglybuff": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Normal/Fairy", "sprite": "174"},
    "Togepi": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy", "sprite": "175"},
    "Togetic": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fairy/Flying", "sprite": "176"},
    "Bellossom": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "182"},
    "Espeon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Psychic", "sprite": "196"},
    "Umbreon": {"rarity": "uncommon", "spawn_weight": 0.5, "type": "Dark", "sprite": "197"},
    "Kingdra": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Dragon", "sprite": "230"},
    
    # Rare Gen 2
    "Larvitar": {"rarity": "rare", "spawn_weight": 0.4, "type": "Rock/Ground", "sprite": "246"},
    "Pupitar": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock/Ground", "sprite": "247"},
    "Raikou": {"rarity": "rare", "spawn_weight": 0.3, "type": "Electric", "sprite": "243"},
    "Entei": {"rarity": "rare", "spawn_weight": 0.3, "type": "Fire", "sprite": "244"},
    "Suicune": {"rarity": "rare", "spawn_weight": 0.3, "type": "Water", "sprite": "245"},
    
    # Epic Gen 2
    "Tyranitar": {"rarity": "epic", "spawn_weight": 0.5, "type": "Rock/Dark", "sprite": "248"},
    
    # Legendary Gen 2
    "Lugia": {"rarity": "legendary", "spawn_weight": 0.15, "type": "Psychic/Flying", "sprite": "249"},
    "Ho-Oh": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Fire/Flying", "sprite": "250"},
    "Celebi": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Psychic/Grass", "sprite": "251"},
    
    # GENERATION 3 (Hoenn) - #252-386
    
    # Common Gen 3
    "Poochyena": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark", "sprite": "261"},
    "Mightyena": {"rarity": "common", "spawn_weight": 0.4, "type": "Dark", "sprite": "262"},
    "Zigzagoon": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "263"},
    "Linoone": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "264"},
    "Wurmple": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "265"},
    "Silcoon": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug", "sprite": "266"},
    "Beautifly": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "267"},
    "Cascoon": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug", "sprite": "268"},
    "Dustox": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Poison", "sprite": "269"},
    "Lotad": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Grass", "sprite": "270"},
    "Lombre": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Grass", "sprite": "271"},
    "Ludicolo": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Grass", "sprite": "272"},
    "Seedot": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "273"},
    "Nuzleaf": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Dark", "sprite": "274"},
    "Shiftry": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Dark", "sprite": "275"},
    "Taillow": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "276"},
    "Swellow": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "277"},
    "Wingull": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Flying", "sprite": "278"},
    "Pelipper": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Flying", "sprite": "279"},
    "Ralts": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic/Fairy", "sprite": "280"},
    "Kirlia": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic/Fairy", "sprite": "281"},
    "Surskit": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Water", "sprite": "283"},
    "Masquerain": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "284"},
    "Shroomish": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "285"},
    "Breloom": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Fighting", "sprite": "286"},
    "Slakoth": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "287"},
    "Vigoroth": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "288"},
    "Slaking": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "289"},
    "Whismur": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "293"},
    "Loudred": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "294"},
    "Exploud": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "295"},
    "Makuhita": {"rarity": "common", "spawn_weight": 0.5, "type": "Fighting", "sprite": "296"},
    "Hariyama": {"rarity": "common", "spawn_weight": 0.4, "type": "Fighting", "sprite": "297"},
    "Azurill": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Fairy", "sprite": "298"},
    "Nosepass": {"rarity": "common", "spawn_weight": 0.5, "type": "Rock", "sprite": "299"},
    "Skitty": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "300"},
    "Delcatty": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "301"},
    "Sableye": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark/Ghost", "sprite": "302"},
    "Mawile": {"rarity": "common", "spawn_weight": 0.5, "type": "Steel/Fairy", "sprite": "303"},
    "Aron": {"rarity": "common", "spawn_weight": 0.5, "type": "Steel/Rock", "sprite": "304"},
    "Lairon": {"rarity": "common", "spawn_weight": 0.4, "type": "Steel/Rock", "sprite": "305"},
    "Aggron": {"rarity": "common", "spawn_weight": 0.4, "type": "Steel/Rock", "sprite": "306"},
    "Meditite": {"rarity": "common", "spawn_weight": 0.5, "type": "Fighting/Psychic", "sprite": "307"},
    "Medicham": {"rarity": "common", "spawn_weight": 0.4, "type": "Fighting/Psychic", "sprite": "308"},
    "Gulpin": {"rarity": "common", "spawn_weight": 0.5, "type": "Poison", "sprite": "316"},
    "Swalot": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison", "sprite": "317"},
    "Wailmer": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "320"},
    "Wailord": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "321"},
    "Numel": {"rarity": "common", "spawn_weight": 0.5, "type": "Fire/Ground", "sprite": "322"},
    "Camerupt": {"rarity": "common", "spawn_weight": 0.4, "type": "Fire/Ground", "sprite": "323"},
    "Torkoal": {"rarity": "common", "spawn_weight": 0.5, "type": "Fire", "sprite": "324"},
    "Spoink": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic", "sprite": "325"},
    "Grumpig": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic", "sprite": "326"},
    "Spinda": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "327"},
    "Swablu": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "333"},
    "Zangoose": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "335"},
    "Seviper": {"rarity": "common", "spawn_weight": 0.5, "type": "Poison", "sprite": "336"},
    "Lunatone": {"rarity": "common", "spawn_weight": 0.5, "type": "Rock/Psychic", "sprite": "337"},
    "Solrock": {"rarity": "common", "spawn_weight": 0.5, "type": "Rock/Psychic", "sprite": "338"},
    "Barboach": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Ground", "sprite": "339"},
    "Whiscash": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Ground", "sprite": "340"},
    "Corphish": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "341"},
    "Crawdaunt": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Dark", "sprite": "342"},
    "Baltoy": {"rarity": "common", "spawn_weight": 0.5, "type": "Ground/Psychic", "sprite": "343"},
    "Claydol": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground/Psychic", "sprite": "344"},
    "Feebas": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "349"},
    "Castform": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "351"},
    "Kecleon": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "352"},
    "Shuppet": {"rarity": "common", "spawn_weight": 0.5, "type": "Ghost", "sprite": "353"},
    "Banette": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost", "sprite": "354"},
    "Duskull": {"rarity": "common", "spawn_weight": 0.5, "type": "Ghost", "sprite": "355"},
    "Dusclops": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost", "sprite": "356"},
    "Tropius": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Flying", "sprite": "357"},
    "Chimecho": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic", "sprite": "358"},
    "Absol": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark", "sprite": "359"},
    "Wynaut": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic", "sprite": "360"},
    "Snorunt": {"rarity": "common", "spawn_weight": 0.5, "type": "Ice", "sprite": "361"},
    "Glalie": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice", "sprite": "362"},
    "Spheal": {"rarity": "common", "spawn_weight": 0.5, "type": "Ice/Water", "sprite": "363"},
    "Sealeo": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice/Water", "sprite": "364"},
    "Walrein": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice/Water", "sprite": "365"},
    "Clamperl": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "366"},
    "Huntail": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "367"},
    "Gorebyss": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "368"},
    "Relicanth": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Rock", "sprite": "369"},
    "Luvdisc": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "370"},
    
    # Uncommon Gen 3
    "Treecko": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "252"},
    "Grovyle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "253"},
    "Sceptile": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "254"},
    "Torchic": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "255"},
    "Combusken": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire/Fighting", "sprite": "256"},
    "Blaziken": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire/Fighting", "sprite": "257"},
    "Mudkip": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "258"},
    "Marshtomp": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Ground", "sprite": "259"},
    "Swampert": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Ground", "sprite": "260"},
    "Gardevoir": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Psychic/Fairy", "sprite": "282"},
    "Nincada": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Ground", "sprite": "290"},
    "Ninjask": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "291"},
    "Shedinja": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Bug/Ghost", "sprite": "292"},
    "Electrike": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "309"},
    "Manectric": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "310"},
    "Plusle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "311"},
    "Minun": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Electric", "sprite": "312"},
    "Volbeat": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug", "sprite": "313"},
    "Illumise": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Bug", "sprite": "314"},
    "Roselia": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "315"},
    "Carvanha": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Dark", "sprite": "318"},
    "Sharpedo": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Dark", "sprite": "319"},
    "Cacnea": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "331"},
    "Cacturne": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Dark", "sprite": "332"},
    "Altaria": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Dragon/Flying", "sprite": "334"},
    "Trapinch": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground", "sprite": "328"},
    "Vibrava": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ground/Dragon", "sprite": "329"},
    "Lileep": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Grass", "sprite": "345"},
    "Cradily": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Grass", "sprite": "346"},
    "Anorith": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Bug", "sprite": "347"},
    "Armaldo": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Rock/Bug", "sprite": "348"},
    "Regirock": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Rock", "sprite": "377"},
    "Regice": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Ice", "sprite": "378"},
    "Registeel": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Steel", "sprite": "379"},
    "Latias": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Dragon/Psychic", "sprite": "380"},
    "Latios": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Dragon/Psychic", "sprite": "381"},
    
    # Rare Gen 3
    "Beldum": {"rarity": "rare", "spawn_weight": 0.4, "type": "Steel/Psychic", "sprite": "374"},
    "Metang": {"rarity": "rare", "spawn_weight": 0.3, "type": "Steel/Psychic", "sprite": "375"},
    "Bagon": {"rarity": "rare", "spawn_weight": 0.4, "type": "Dragon", "sprite": "371"},
    "Shelgon": {"rarity": "rare", "spawn_weight": 0.3, "type": "Dragon", "sprite": "372"},
    "Flygon": {"rarity": "rare", "spawn_weight": 0.4, "type": "Ground/Dragon", "sprite": "330"},
    "Kyogre": {"rarity": "rare", "spawn_weight": 0.2, "type": "Water", "sprite": "382"},
    "Groudon": {"rarity": "rare", "spawn_weight": 0.2, "type": "Ground", "sprite": "383"},
    
    # Epic Gen 3
    "Metagross": {"rarity": "epic", "spawn_weight": 0.5, "type": "Steel/Psychic", "sprite": "376"},
    "Salamence": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon/Flying", "sprite": "373"},
    "Milotic": {"rarity": "epic", "spawn_weight": 0.3, "type": "Water", "sprite": "350"},
    
    # Legendary Gen 3
    "Rayquaza": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Dragon/Flying", "sprite": "384"},
    "Jirachi": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Steel/Psychic", "sprite": "385"},
    "Deoxys": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Psychic", "sprite": "386"},
    
    # GENERATION 4 (Sinnoh) - #387-493
    
    # Common Gen 4
    "Bidoof": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "399"},
    "Bibarel": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Water", "sprite": "400"},
    "Starly": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "396"},
    "Staravia": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "397"},
    "Staraptor": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal/Flying", "sprite": "398"},
    "Kricketot": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "401"},
    "Kricketune": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug", "sprite": "402"},
    "Shinx": {"rarity": "common", "spawn_weight": 0.5, "type": "Electric", "sprite": "403"},
    "Luxio": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric", "sprite": "404"},
    "Luxray": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric", "sprite": "405"},
    "Budew": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Poison", "sprite": "406"},
    "Roserade": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Poison", "sprite": "407"},
    "Burmy": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug", "sprite": "412"},
    "Wormadam": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Grass", "sprite": "413"},
    "Mothim": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "414"},
    "Combee": {"rarity": "common", "spawn_weight": 0.5, "type": "Bug/Flying", "sprite": "415"},
    "Vespiquen": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "416"},
    "Pachirisu": {"rarity": "common", "spawn_weight": 0.5, "type": "Electric", "sprite": "417"},
    "Buizel": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "418"},
    "Floatzel": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "419"},
    "Cherubi": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "420"},
    "Cherrim": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass", "sprite": "421"},
    "Shellos": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "422"},
    "Gastrodon": {"rarity": "common", "spawn_weight": 0.4, "type": "Water/Ground", "sprite": "423"},
    "Ambipom": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "424"},
    "Drifloon": {"rarity": "common", "spawn_weight": 0.5, "type": "Ghost/Flying", "sprite": "425"},
    "Drifblim": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost/Flying", "sprite": "426"},
    "Buneary": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "427"},
    "Lopunny": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "428"},
    "Mismagius": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost", "sprite": "429"},
    "Honchkrow": {"rarity": "common", "spawn_weight": 0.4, "type": "Dark/Flying", "sprite": "430"},
    "Glameow": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "431"},
    "Purugly": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "432"},
    "Chingling": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic", "sprite": "433"},
    "Stunky": {"rarity": "common", "spawn_weight": 0.5, "type": "Poison/Dark", "sprite": "434"},
    "Skuntank": {"rarity": "common", "spawn_weight": 0.4, "type": "Poison/Dark", "sprite": "435"},
    "Bronzor": {"rarity": "common", "spawn_weight": 0.5, "type": "Steel/Psychic", "sprite": "436"},
    "Bronzong": {"rarity": "common", "spawn_weight": 0.4, "type": "Steel/Psychic", "sprite": "437"},
    "Bonsly": {"rarity": "common", "spawn_weight": 0.5, "type": "Rock", "sprite": "438"},
    "Mime Jr.": {"rarity": "common", "spawn_weight": 0.5, "type": "Psychic/Fairy", "sprite": "439"},
    "Happiny": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "440"},
    "Chatot": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal/Flying", "sprite": "441"},
    "Gible": {"rarity": "common", "spawn_weight": 0.5, "type": "Dragon/Ground", "sprite": "443"},
    "Gabite": {"rarity": "common", "spawn_weight": 0.4, "type": "Dragon/Ground", "sprite": "444"},
    "Munchlax": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "446"},
    "Hippopotas": {"rarity": "common", "spawn_weight": 0.5, "type": "Ground", "sprite": "449"},
    "Hippowdon": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground", "sprite": "450"},
    "Carnivine": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "455"},
    "Finneon": {"rarity": "common", "spawn_weight": 0.5, "type": "Water", "sprite": "456"},
    "Lumineon": {"rarity": "common", "spawn_weight": 0.4, "type": "Water", "sprite": "457"},
    "Mantyke": {"rarity": "common", "spawn_weight": 0.5, "type": "Water/Flying", "sprite": "458"},
    "Snover": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass/Ice", "sprite": "459"},
    "Abomasnow": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass/Ice", "sprite": "460"},
    "Weavile": {"rarity": "common", "spawn_weight": 0.4, "type": "Dark/Ice", "sprite": "461"},
    "Magnezone": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric/Steel", "sprite": "462"},
    "Lickilicky": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "463"},
    "Rhyperior": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground/Rock", "sprite": "464"},
    "Tangrowth": {"rarity": "common", "spawn_weight": 0.4, "type": "Grass", "sprite": "465"},
    "Electivire": {"rarity": "common", "spawn_weight": 0.4, "type": "Electric", "sprite": "466"},
    "Magmortar": {"rarity": "common", "spawn_weight": 0.4, "type": "Fire", "sprite": "467"},
    "Togekiss": {"rarity": "common", "spawn_weight": 0.4, "type": "Fairy/Flying", "sprite": "468"},
    "Yanmega": {"rarity": "common", "spawn_weight": 0.4, "type": "Bug/Flying", "sprite": "469"},
    "Leafeon": {"rarity": "common", "spawn_weight": 0.5, "type": "Grass", "sprite": "470"},
    "Glaceon": {"rarity": "common", "spawn_weight": 0.5, "type": "Ice", "sprite": "471"},
    "Gliscor": {"rarity": "common", "spawn_weight": 0.4, "type": "Ground/Flying", "sprite": "472"},
    "Mamoswine": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice/Ground", "sprite": "473"},
    "Porygon-Z": {"rarity": "common", "spawn_weight": 0.4, "type": "Normal", "sprite": "474"},
    "Gallade": {"rarity": "common", "spawn_weight": 0.4, "type": "Psychic/Fighting", "sprite": "475"},
    "Probopass": {"rarity": "common", "spawn_weight": 0.4, "type": "Rock/Steel", "sprite": "476"},
    "Dusknoir": {"rarity": "common", "spawn_weight": 0.4, "type": "Ghost", "sprite": "477"},
    "Froslass": {"rarity": "common", "spawn_weight": 0.4, "type": "Ice/Ghost", "sprite": "478"},
    
    # Uncommon Gen 4
    "Turtwig": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "387"},
    "Grotle": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass", "sprite": "388"},
    "Torterra": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Grass/Ground", "sprite": "389"},
    "Chimchar": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire", "sprite": "390"},
    "Monferno": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire/Fighting", "sprite": "391"},
    "Infernape": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Fire/Fighting", "sprite": "392"},
    "Piplup": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "393"},
    "Prinplup": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water", "sprite": "394"},
    "Empoleon": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Water/Steel", "sprite": "395"},
    "Spiritomb": {"rarity": "uncommon", "spawn_weight": 0.4, "type": "Ghost/Dark", "sprite": "442"},
    "Uxie": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Psychic", "sprite": "480"},
    "Mesprit": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Psychic", "sprite": "481"},
    "Azelf": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Psychic", "sprite": "482"},
    "Heatran": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Fire/Steel", "sprite": "485"},
    "Regigigas": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Normal", "sprite": "486"},
    "Cresselia": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Psychic", "sprite": "488"},
    "Phione": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Water", "sprite": "489"},
    "Manaphy": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Water", "sprite": "490"},
    "Darkrai": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Dark", "sprite": "491"},
    "Shaymin": {"rarity": "uncommon", "spawn_weight": 0.3, "type": "Grass", "sprite": "492"},
    
    # Rare Gen 4
    "Riolu": {"rarity": "rare", "spawn_weight": 0.4, "type": "Fighting", "sprite": "447"},
    "Cranidos": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock", "sprite": "408"},
    "Rampardos": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock", "sprite": "409"},
    "Shieldon": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock/Steel", "sprite": "410"},
    "Bastiodon": {"rarity": "rare", "spawn_weight": 0.3, "type": "Rock/Steel", "sprite": "411"},
    "Skorupi": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Bug", "sprite": "451"},
    "Drapion": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Dark", "sprite": "452"},
    "Croagunk": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Fighting", "sprite": "453"},
    "Toxicroak": {"rarity": "rare", "spawn_weight": 0.3, "type": "Poison/Fighting", "sprite": "454"},
    "Rotom": {"rarity": "rare", "spawn_weight": 0.3, "type": "Electric/Ghost", "sprite": "479"},
    
    # Epic Gen 4
    "Garchomp": {"rarity": "epic", "spawn_weight": 0.5, "type": "Dragon/Ground", "sprite": "445"},
    "Lucario": {"rarity": "epic", "spawn_weight": 0.5, "type": "Fighting/Steel", "sprite": "448"},
    
    # Legendary Gen 4
    "Dialga": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Steel/Dragon", "sprite": "483"},
    "Palkia": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Water/Dragon", "sprite": "484"},
    "Giratina": {"rarity": "legendary", "spawn_weight": 0.1, "type": "Ghost/Dragon", "sprite": "487"},
    "Arceus": {"rarity": "legendary", "spawn_weight": 0.05, "type": "Normal", "sprite": "493"},
    
    # GENERATION 5 (Bonus - from backup)
    "Patrat": {"rarity": "common", "spawn_weight": 0.5, "type": "Normal", "sprite": "504"},
    "Purrloin": {"rarity": "common", "spawn_weight": 0.5, "type": "Dark", "sprite": "509"},
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
