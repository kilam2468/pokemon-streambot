"""
Database models for the Pokemon Stream Bot
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    twitch_username = Column(String, unique=True, nullable=False)
    twitch_id = Column(String, unique=True, nullable=True)
    coins = Column(Integer, default=50)  # Starting coins
    inventory = Column(JSON, default=dict)  # Ball inventory
    created_at = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    last_daily_claim = Column(DateTime, nullable=True)
    
    # Relationships
    caught_pokemon = relationship("CaughtPokemon", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.twitch_username}>"

class CaughtPokemon(Base):
    __tablename__ = "caught_pokemon"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pokemon_name = Column(String, nullable=False)
    pokemon_type = Column(String, nullable=False)
    rarity = Column(String, nullable=False)
    caught_with = Column(String, nullable=False)  # Ball type used
    caught_at = Column(DateTime, default=datetime.utcnow)
    nickname = Column(String, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="caught_pokemon")
    
    def __repr__(self):
        return f"<CaughtPokemon {self.pokemon_name} by {self.user_id}>"

class SpawnHistory(Base):
    __tablename__ = "spawn_history"
    
    id = Column(Integer, primary_key=True)
    pokemon_name = Column(String, nullable=False)
    spawned_at = Column(DateTime, default=datetime.utcnow)
    was_caught = Column(Boolean, default=False)
    caught_by = Column(String, nullable=True)
    despawned_at = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<Spawn {self.pokemon_name} at {self.spawned_at}>"

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    transaction_type = Column(String, nullable=False)  # purchase, catch_reward, daily_bonus, etc
    amount = Column(Integer, nullable=False)  # Positive for gains, negative for spending
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Transaction {self.transaction_type} {self.amount}>"
