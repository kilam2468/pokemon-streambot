#!/usr/bin/env python3
"""
Manual Pokemon Spawn Script
Usage: python spawn_pokemon.py <pokemon_name>
"""

import sys
import asyncio
import os
from dotenv import load_dotenv
from pokemon_data import POKEMON_DATA

load_dotenv()

async def spawn_pokemon(pokemon_name):
    """Trigger a manual spawn by writing to a trigger file"""
    
    # Validate pokemon name
    if pokemon_name not in POKEMON_DATA:
        print(f"❌ Error: '{pokemon_name}' is not a valid Pokemon!")
        print(f"\n📋 Available Pokemon:")
        for name in sorted(POKEMON_DATA.keys()):
            rarity = POKEMON_DATA[name]['rarity']
            print(f"   - {name} ({rarity})")
        return False
    
    # Write trigger file
    trigger_file = "manual_spawn.txt"
    with open(trigger_file, 'w') as f:
        f.write(pokemon_name)
    
    pokemon_info = POKEMON_DATA[pokemon_name]
    print(f"✅ Spawn trigger created for {pokemon_name}")
    print(f"   Type: {pokemon_info['type']}")
    print(f"   Rarity: {pokemon_info['rarity']}")
    print(f"\n💡 Note: The bot needs to have the manual spawn feature enabled to detect this.")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python spawn_pokemon.py <pokemon_name>")
        print("\nExample: python spawn_pokemon.py Pikachu")
        print("\nTo see all available Pokemon, run with any invalid name")
        sys.exit(1)
    
    pokemon_name = sys.argv[1].capitalize()
    asyncio.run(spawn_pokemon(pokemon_name))

if __name__ == "__main__":
    main()
