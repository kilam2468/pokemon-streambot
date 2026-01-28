"""
Script to remove duplicate Pokemon from users' collections.
Keeps the one caught with the highest tier ball.
"""

import asyncio
from sqlalchemy import select, delete
from database import User, CaughtPokemon
from db_utils import async_session

# Ball priority (higher value = better ball)
BALL_PRIORITY = {
    'masterball': 4,
    'ultraball': 3,
    'greatball': 2,
    'pokeball': 1,
    None: 0  # In case caught_with is missing
}

async def remove_duplicates():
    """Remove duplicate Pokemon, keeping the one with the best ball"""
    async with async_session() as session:
        # Get all users
        result = await session.execute(select(User))
        users = result.scalars().all()
        
        total_removed = 0
        
        for user in users:
            # Get all caught Pokemon for this user
            result = await session.execute(
                select(CaughtPokemon)
                .where(CaughtPokemon.user_id == user.id)
                .order_by(CaughtPokemon.pokemon_name, CaughtPokemon.caught_at)
            )
            caught_pokemon = result.scalars().all()
            
            # Group by Pokemon name
            pokemon_groups = {}
            for pokemon in caught_pokemon:
                if pokemon.pokemon_name not in pokemon_groups:
                    pokemon_groups[pokemon.pokemon_name] = []
                pokemon_groups[pokemon.pokemon_name].append(pokemon)
            
            # Remove duplicates
            user_removed = 0
            for pokemon_name, pokemon_list in pokemon_groups.items():
                if len(pokemon_list) > 1:
                    # Sort by ball priority (highest first)
                    pokemon_list.sort(
                        key=lambda p: BALL_PRIORITY.get(p.caught_with, 0),
                        reverse=True
                    )
                    
                    # Keep the first one (best ball), delete the rest
                    to_keep = pokemon_list[0]
                    to_delete = pokemon_list[1:]
                    
                    print(f"User {user.twitch_username}: {pokemon_name} - Keeping {to_keep.caught_with or 'unknown'}, removing {len(to_delete)} duplicate(s)")
                    
                    for duplicate in to_delete:
                        await session.delete(duplicate)
                        user_removed += 1
            
            if user_removed > 0:
                print(f"  → Removed {user_removed} duplicates from {user.twitch_username}")
                total_removed += user_removed
        
        # Commit all changes
        await session.commit()
        print(f"\n✅ Total duplicates removed: {total_removed}")

if __name__ == "__main__":
    print("Removing duplicate Pokemon from database...\n")
    asyncio.run(remove_duplicates())
    print("\nDone!")
