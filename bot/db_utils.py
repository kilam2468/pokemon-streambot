"""
Database utilities and helper functions
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from database import Base, User, CaughtPokemon, SpawnHistory, Transaction
from pokemon_data import STARTER_INVENTORY
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Use absolute path for database
DB_PATH = DATA_DIR / "pokemon_bot.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{DB_PATH}")

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    """Initialize the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session():
    """Get a database session"""
    async with async_session() as session:
        yield session

async def get_or_create_user(username: str):
    """Get or create a user by username"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            user = User(
                twitch_username=username,
                inventory=STARTER_INVENTORY.copy()
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
        
        return user

async def get_user_inventory(username: str):
    """Get user's ball inventory"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return None
        
        return user.inventory

async def update_user_inventory(username: str, ball_type: str, quantity_change: int):
    """Update user's ball inventory"""
    from sqlalchemy.orm.attributes import flag_modified
    
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return False
        
        inventory = user.inventory or STARTER_INVENTORY.copy()
        current = inventory.get(ball_type, 0)
        inventory[ball_type] = max(0, current + quantity_change)
        
        user.inventory = inventory
        flag_modified(user, "inventory")  # Tell SQLAlchemy the JSON field changed
        await session.commit()
        return True

async def add_coins(username: str, amount: int, transaction_type: str, description: str = None):
    """Add coins to user's balance"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return False
        
        user.coins += amount
        
        transaction = Transaction(
            user_id=user.id,
            transaction_type=transaction_type,
            amount=amount,
            description=description
        )
        session.add(transaction)
        
        await session.commit()
        return True

async def has_pokemon(username: str, pokemon_name: str) -> bool:
    """Check if user already has a specific Pokemon"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return False
        
        result = await session.execute(
            select(CaughtPokemon).where(
                CaughtPokemon.user_id == user.id,
                CaughtPokemon.pokemon_name == pokemon_name
            )
        )
        return result.scalar_one_or_none() is not None

async def catch_pokemon(username: str, pokemon_name: str, pokemon_data: dict, ball_type: str):
    """Record a caught pokemon"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return False
        
        caught = CaughtPokemon(
            user_id=user.id,
            pokemon_name=pokemon_name,
            pokemon_type=pokemon_data["type"],
            rarity=pokemon_data["rarity"],
            caught_with=ball_type
        )
        session.add(caught)
        await session.commit()
        return True

async def get_user_pokedex(username: str):
    """Get all pokemon caught by user"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return []
        
        result = await session.execute(
            select(CaughtPokemon).where(CaughtPokemon.user_id == user.id)
        )
        return result.scalars().all()

async def get_user_stats(username: str):
    """Get user statistics"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.twitch_username == username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            return None
        
        result = await session.execute(
            select(CaughtPokemon).where(CaughtPokemon.user_id == user.id)
        )
        caught_pokemon = result.scalars().all()
        
        # Count by rarity
        rarity_counts = {}
        for pokemon in caught_pokemon:
            rarity = pokemon.rarity
            rarity_counts[rarity] = rarity_counts.get(rarity, 0) + 1
        
        return {
            "username": user.twitch_username,
            "coins": user.coins,
            "inventory": user.inventory,
            "total_caught": len(caught_pokemon),
            "rarity_counts": rarity_counts,
            "unique_pokemon": len(set(p.pokemon_name for p in caught_pokemon))
        }
