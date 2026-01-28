"""
FastAPI backend for the website
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from pathlib import Path
from contextlib import asynccontextmanager
import os

from database import User, CaughtPokemon
from db_utils import (
    init_db, get_session, get_user_stats, get_user_pokedex,
    get_or_create_user
)
from pokemon_data import POKEMON_DATA, POKEBALL_TYPES

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database on startup"""
    await init_db()
    yield

app = FastAPI(title="Pokemon Stream Bot API", lifespan=lifespan)

# Get paths
BASE_DIR = Path(__file__).parent.parent
OVERLAY_PATH = BASE_DIR / "overlay" / "index.html"

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class UserStats(BaseModel):
    username: str
    coins: int
    inventory: dict
    total_caught: int
    unique_pokemon: int
    rarity_counts: dict

class PokemonEntry(BaseModel):
    id: int
    pokemon_name: str
    pokemon_type: str
    rarity: str
    caught_with: str
    caught_at: datetime
    nickname: Optional[str] = None
    sprite_url: str

class UserInventory(BaseModel):
    username: str
    coins: int
    pokeball: int
    greatball: int
    ultraball: int
    masterball: int

@app.get("/")
async def root():
    return {"message": "Pokemon Stream Bot API", "version": "1.0.0"}

@app.get("/overlay", response_class=HTMLResponse)
async def get_overlay():
    """Serve the OBS overlay HTML"""
    if not OVERLAY_PATH.exists():
        raise HTTPException(status_code=404, detail="Overlay file not found")
    
    with open(OVERLAY_PATH, "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/api/user/{username}/stats", response_model=UserStats)
async def get_user_statistics(username: str):
    """Get user statistics"""
    stats = await get_user_stats(username)
    
    if not stats:
        raise HTTPException(status_code=404, detail="User not found")
    
    return stats

@app.get("/api/user/{username}/pokedex", response_model=List[PokemonEntry])
async def get_pokedex(username: str):
    """Get user's caught pokemon"""
    pokemon_list = await get_user_pokedex(username)
    
    if pokemon_list is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Add sprite URLs
    result = []
    for p in pokemon_list:
        sprite_id = POKEMON_DATA.get(p.pokemon_name, {}).get("sprite", "0")
        result.append(
            PokemonEntry(
                id=p.id,
                pokemon_name=p.pokemon_name,
                pokemon_type=p.pokemon_type,
                rarity=p.rarity,
                caught_with=p.caught_with,
                caught_at=p.caught_at,
                nickname=p.nickname,
                sprite_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{sprite_id}.png"
            )
        )
    
    return result

@app.get("/api/user/{username}/inventory", response_model=UserInventory)
async def get_inventory(username: str):
    """Get user's inventory"""
    user = await get_or_create_user(username)
    
    inventory = user.inventory or {}
    
    return UserInventory(
        username=user.twitch_username,
        coins=user.coins,
        pokeball=inventory.get("pokeball", 0),
        greatball=inventory.get("greatball", 0),
        ultraball=inventory.get("ultraball", 0),
        masterball=inventory.get("masterball", 0)
    )

@app.get("/api/pokemon")
async def get_all_pokemon():
    """Get all available pokemon data"""
    pokemon_list = []
    for name, data in POKEMON_DATA.items():
        pokemon_list.append({
            "name": name,
            "type": data["type"],
            "rarity": data["rarity"],
            "sprite_url": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{data['sprite']}.png"
        })
    
    return pokemon_list

@app.get("/api/leaderboard")
async def get_leaderboard():
    """Get leaderboard of top collectors"""
    async with get_session().__anext__() as session:
        result = await session.execute(
            select(User).order_by(User.coins.desc()).limit(10)
        )
        users = result.scalars().all()
        
        leaderboard = []
        for user in users:
            stats = await get_user_stats(user.twitch_username)
            if stats:
                leaderboard.append({
                    "rank": len(leaderboard) + 1,
                    "username": user.twitch_username,
                    "coins": user.coins,
                    "total_caught": stats["total_caught"],
                    "unique_pokemon": stats["unique_pokemon"]
                })
        
        return leaderboard

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
