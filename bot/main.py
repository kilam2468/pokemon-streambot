"""
Main Twitch bot with spawn and capture mechanics
"""

import asyncio
import random
import os
import logging
import aiohttp
from datetime import datetime, timedelta, timezone
from twitchio.ext import commands
from dotenv import load_dotenv
from pokemon_data import get_weighted_pokemon, get_capture_rate, POKEMON_DATA, POKEBALL_TYPES, SHOP_ITEMS, COINS_PER_CATCH
from db_utils import (
    init_db, get_or_create_user, get_user_inventory, update_user_inventory, 
    add_coins, catch_pokemon, get_user_stats, has_pokemon
)
import websockets
import json

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class PokemonBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.getenv('TWITCH_BOT_TOKEN'),
            client_id=os.getenv('TWITCH_CLIENT_ID'),
            nick=os.getenv('TWITCH_BOT_NICK'),
            prefix=['p!', 'p! ', '!p', '!p '],
            initial_channels=[os.getenv('TWITCH_CHANNEL')]
        )
        
        self.current_spawn = None
        self.spawn_time = None
        self.websocket_clients = set()
        self.active_raffle = None  # {amount: int, entries: [usernames]}
        self.raffle_task = None  # Timer task for auto-ending raffle
        
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'Connected to channel: {os.getenv("TWITCH_CHANNEL")}')
        
        # Initialize database
        await init_db()
        
        # Start spawn loop
        self.loop.create_task(self.spawn_pokemon_loop())
        
        # Start viewer rewards loop
        self.loop.create_task(self.viewer_rewards_loop())
        
        # Start WebSocket server for overlay
        self.loop.create_task(self.websocket_server())
    
    async def event_message(self, message):
        if message.echo:
            return
        
        # Handle commands
        await self.handle_commands(message)
    
    async def is_stream_live(self):
        """Check if the stream is currently live using Twitch API"""
        try:
            client_id = os.getenv('TWITCH_CLIENT_ID')
            channel_name = os.getenv('TWITCH_CHANNEL')
            token = os.getenv('TWITCH_BOT_TOKEN')
            
            if not client_id or not channel_name or not token:
                logger.warning("Missing Twitch credentials, assuming stream is live")
                return True
            
            # Remove 'oauth:' prefix if present
            if token.startswith('oauth:'):
                token = token[6:]
            
            url = f"https://api.twitch.tv/helix/streams?user_login={channel_name}"
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {token}'
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        # If data array has entries, stream is live
                        is_live = len(data.get('data', [])) > 0
                        return is_live
                    else:
                        logger.error(f"Failed to check stream status: {response.status}")
                        # Assume live on error to not break existing functionality
                        return True
        except Exception as e:
            logger.error(f"Error checking stream status: {e}")
            # Assume live on error
            return True
    
    async def get_chatters(self):
        """Get list of current chatters/viewers in the channel"""
        try:
            client_id = os.getenv('TWITCH_CLIENT_ID')
            channel_name = os.getenv('TWITCH_CHANNEL')
            token = os.getenv('TWITCH_BOT_TOKEN')
            
            if not client_id or not channel_name or not token:
                logger.warning("Missing Twitch credentials for chatters")
                return []
            
            # Remove 'oauth:' prefix if present
            if token.startswith('oauth:'):
                token = token[6:]
            
            # First, get the broadcaster's user ID
            user_url = f"https://api.twitch.tv/helix/users?login={channel_name}"
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {token}'
            }
            
            async with aiohttp.ClientSession() as session:
                # Get broadcaster ID
                async with session.get(user_url, headers=headers) as response:
                    if response.status != 200:
                        logger.error(f"Failed to get broadcaster ID: {response.status}")
                        return []
                    
                    data = await response.json()
                    if not data.get('data'):
                        logger.error("No broadcaster data found")
                        return []
                    
                    broadcaster_id = data['data'][0]['id']
                
                # Get chatters using the broadcaster ID
                chatters_url = f"https://api.twitch.tv/helix/chat/chatters?broadcaster_id={broadcaster_id}&moderator_id={broadcaster_id}"
                
                async with session.get(chatters_url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        # Extract usernames from the data
                        chatters = [user['user_login'] for user in data.get('data', [])]
                        return chatters
                    else:
                        logger.error(f"Failed to get chatters: {response.status}")
                        return []
        except Exception as e:
            logger.error(f"Error getting chatters: {e}")
            return []
    
    async def viewer_rewards_loop(self):
        """Award coins to viewers every minute"""
        while True:
            await asyncio.sleep(60)  # Wait 1 minute
            
            # Check if stream is live
            if not await self.is_stream_live():
                logger.info("⏸️ Stream is offline - skipping viewer rewards")
                continue
            
            # Get current chatters/viewers
            chatters = await self.get_chatters()
            
            if not chatters:
                logger.debug("No chatters found for rewards")
                continue
            
            # Award coins to each viewer who exists in database
            from sqlalchemy import select
            from db_utils import async_session
            from database import User
            
            rewarded_count = 0
            async with async_session() as session:
                for username in chatters:
                    # Check if user exists in database
                    result = await session.execute(
                        select(User).where(User.twitch_username == username)
                    )
                    user = result.scalar_one_or_none()
                    
                    if user:
                        # Award 1 coin for watching
                        await add_coins(username, 1, "watch_reward", "Watching stream")
                        rewarded_count += 1
            
            if rewarded_count > 0:
                logger.info(f"💰 Awarded 1 coin to {rewarded_count} viewers")
    
    async def spawn_pokemon_loop(self):
        """Continuously spawn pokemon at random intervals"""
        while True:
            # Random spawn interval (1-5 minutes)
            spawn_interval = random.randint(
                int(os.getenv('SPAWN_INTERVAL_MIN', 60)),
                int(os.getenv('SPAWN_INTERVAL_MAX', 300))
            )
            
            await asyncio.sleep(spawn_interval)
            
            # Check if stream is live before spawning
            #TODO: put this back
            if not await self.is_stream_live():
                logger.info("⏸️ Stream is offline - skipping Pokemon spawn")
                continue
            
            # Spawn a random pokemon
            pokemon_name = get_weighted_pokemon()
            self.current_spawn = pokemon_name
            self.spawn_time = datetime.now(timezone.utc)
            
            pokemon_info = POKEMON_DATA[pokemon_name]
            
            # Log spawn
            logger.info(f"🎮 SPAWN: {pokemon_name} ({pokemon_info['type']}) - {pokemon_info['rarity'].upper()}")
            
            channel = self.get_channel(os.getenv('TWITCH_CHANNEL'))
            if channel:
                rarity_emoji = {
                    "common": "⚪",
                    "uncommon": "🟢",
                    "rare": "🔵",
                    "epic": "🟣",
                    "legendary": "🟡"
                }
                
                await channel.send(
                    f"{rarity_emoji.get(pokemon_info['rarity'], '⚪')} A wild {pokemon_name} "
                    f"({pokemon_info['type']}) appeared! [{pokemon_info['rarity'].upper()}] "
                    f"Use !p catch <ball_type> to try to catch it! (Available: pokeball, greatball, ultraball, masterball)"
                )
                
                # Broadcast to overlay
                await self.broadcast_to_overlay({
                    "type": "spawn",
                    "pokemon": pokemon_name,
                    "rarity": pokemon_info['rarity'],
                    "sprite": pokemon_info['sprite']
                })
            
            # Despawn after 60 seconds if not caught
            await asyncio.sleep(60)
            if self.current_spawn == pokemon_name:
                self.current_spawn = None
                if channel:
                    await channel.send(f"The wild {pokemon_name} got away!")
                    await self.broadcast_to_overlay({"type": "despawn"})
    
    @commands.command(name='catch')
    async def catch_command(self, ctx, ball_type: str = None):
        """Try to catch the current spawned pokemon"""
        if not self.current_spawn:
            await ctx.send(f"@{ctx.author.name} There's no Pokemon to catch right now!")
            return
        
        # Check if user already has this Pokemon
        if await has_pokemon(ctx.author.name, self.current_spawn):
            await ctx.send(f"@{ctx.author.name} You already have this pokemon! Let someone else catch it.")
            return
        
        # Clean ball_type - remove whitespace and non-alphanumeric characters
        if ball_type is not None:
            # Remove all non-alphanumeric characters and strip whitespace
            cleaned = ''.join(c for c in ball_type if c.isalnum())
            ball_type = cleaned if cleaned else None
        
        # Get user and check inventory
        user = await get_or_create_user(ctx.author.name)
        inventory = user.inventory or {}
        
        # Auto-select ball if not specified
        if ball_type is None:
            # Try pokeball -> greatball -> ultraball (skip masterball)
            auto_select_order = ['pokeball', 'greatball', 'ultraball']
            ball_type = None
            for ball in auto_select_order:
                if inventory.get(ball, 0) > 0:
                    ball_type = ball
                    break
            
            if ball_type is None:
                await ctx.send(f"@{ctx.author.name} You don't have any balls! Use !p shop to buy more.")
                return
        else:
            ball_type = ball_type.lower()
            if ball_type not in POKEBALL_TYPES:
                await ctx.send(f"@{ctx.author.name} Invalid ball type! Use: pokeball, greatball, ultraball, or masterball")
                return
            
            if inventory.get(ball_type, 0) <= 0:
                await ctx.send(f"@{ctx.author.name} You don't have any {POKEBALL_TYPES[ball_type]['name']}s! Use !p shop to buy more.")
                return
        
        # Deduct ball from inventory (happens whether catch succeeds or fails)
        await update_user_inventory(ctx.author.name, ball_type, -1)
        
        # Calculate catch success
        pokemon_name = self.current_spawn
        pokemon_info = POKEMON_DATA[pokemon_name]
        catch_rate = get_capture_rate(pokemon_name, ball_type)
        success = random.random() < catch_rate
        
        # Broadcast catch attempt to overlay
        await self.broadcast_to_overlay({
            "type": "catch_attempt",
            "username": ctx.author.name,
            "pokemon": pokemon_name,
            "ball_type": ball_type,
            "success": success,
            "sprite": pokemon_info['sprite']
        })
        
        if success:
            # Successful catch
            await catch_pokemon(ctx.author.name, pokemon_name, pokemon_info, ball_type)
            await add_coins(ctx.author.name, COINS_PER_CATCH, "catch_reward", f"Caught {pokemon_name}")
            
            # Log successful capture
            logger.info(f"✅ CAUGHT: {ctx.author.name} caught {pokemon_name} ({pokemon_info['rarity']}) with {POKEBALL_TYPES[ball_type]['name']}")
            
            await ctx.send(
                f"🎉 @{ctx.author.name} successfully caught {pokemon_name} with a {POKEBALL_TYPES[ball_type]['name']}! "
                f"You earned {COINS_PER_CATCH} coins!"
            )
            
            # Clear spawn
            self.current_spawn = None
        else:
            # Failed catch
            logger.info(f"❌ FAILED: {ctx.author.name} failed to catch {pokemon_name} with {POKEBALL_TYPES[ball_type]['name']} (rate: {catch_rate:.0%})")
            
            await ctx.send(
                f"😢 @{ctx.author.name} The {pokemon_name} broke free from the {POKEBALL_TYPES[ball_type]['name']}!"
            )
    
    @commands.command(name='inventory', aliases=['inv', 'balls', 'bag', 'backpack'])
    async def inventory_command(self, ctx):
        """Check your ball inventory"""
        user = await get_or_create_user(ctx.author.name)
        inventory = user.inventory or {}
        
        inv_text = " | ".join([
            f"{POKEBALL_TYPES[ball]['name']}: {inventory.get(ball, 0)}"
            for ball in POKEBALL_TYPES.keys()
        ])
        
        await ctx.send(f"@{ctx.author.name} 💰 Coins: {user.coins} | 🎒 Inventory: {inv_text}")
    
    @commands.command(name='shop', aliases=['store'])
    async def shop_command(self, ctx):
        """View the shop"""
        shop_text = []
        for ball_type, item in SHOP_ITEMS.items():
            shop_text.append(
                f"{POKEBALL_TYPES[ball_type]['name']} x{item['quantity']}: {item['cost']} coins"
            )
        
        await ctx.send(f"🏪 SHOP: {' | '.join(shop_text)} | Use: !p buy <ball_type>")
    
    @commands.command(name='buy')
    async def buy_command(self, ctx, *args):
        """Buy balls from the shop"""
        if not args:
            await ctx.send(f"@{ctx.author.name} Please specify what to buy! Use !p shop to see available items.")
            return
        
        # Join all arguments and normalize (remove spaces, underscores, hyphens)
        ball_input = ' '.join(args).lower().replace(' ', '').replace('_', '').replace('-', '')
        
        if ball_input not in SHOP_ITEMS:
            await ctx.send(f"@{ctx.author.name} Invalid item! Use !p shop to see available items.")
            return
        
        user = await get_or_create_user(ctx.author.name)
        item = SHOP_ITEMS[ball_input]
        
        if user.coins < item['cost']:
            await ctx.send(
                f"@{ctx.author.name} Not enough coins! You need {item['cost']} coins but only have {user.coins}."
            )
            return
        
        # Process purchase
        await add_coins(ctx.author.name, -item['cost'], "purchase", f"Bought {item['quantity']}x {ball_input}")
        await update_user_inventory(ctx.author.name, ball_input, item['quantity'])
        
        await ctx.send(
            f"✅ @{ctx.author.name} Purchased {item['quantity']}x {POKEBALL_TYPES[ball_input]['name']} "
            f"for {item['cost']} coins!"
        )
    
    @commands.command(name='pokedex', aliases=['dex'])
    async def pokedex_command(self, ctx):
        """Check your pokedex progress"""
        await ctx.send(
            f"@{ctx.author.name} 📖 View your Pokédex at https://poke.hfdn.dev/"
        )
    
    @commands.command(name='cmds', aliases=['commands', 'help'])
    async def commands_command(self, ctx):
        """Show available commands"""
        await ctx.send(
            f"@{ctx.author.name} 📋 Commands: !p catch | !p inventory | !p shop | !p buy <ball> | "
            f"!p pokedex | !p stats | !p daily | !p give <user> <amount> | !p join | More at https://poke.hfdn.dev/"
        )
    
    @commands.command(name='stats')
    async def stats_command(self, ctx):
        """View your stats"""
        stats = await get_user_stats(ctx.author.name)
        
        if not stats:
            await ctx.send(f"@{ctx.author.name} No stats available yet!")
            return
        
        rarity_text = " | ".join([
            f"{r.capitalize()}: {c}"
            for r, c in stats['rarity_counts'].items()
        ])
        
        await ctx.send(
            f"@{ctx.author.name} 📊 Total: {stats['total_caught']} | "
            f"Unique: {stats['unique_pokemon']} | {rarity_text}"
        )
    
    @commands.command(name='daily')
    async def daily_command(self, ctx):
        """Claim daily coin bonus"""
        from datetime import datetime, timedelta
        from sqlalchemy import select
        from db_utils import async_session
        from database import User
        
        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.twitch_username == ctx.author.name)
            )
            user = result.scalar_one_or_none()
            
            if not user:
                user = await get_or_create_user(ctx.author.name)
            
            now = datetime.utcnow()
            
            # Check if already claimed today
            if user.last_daily_claim:
                time_since_claim = now - user.last_daily_claim
                if time_since_claim < timedelta(hours=24):
                    hours_left = 24 - (time_since_claim.total_seconds() / 3600)
                    await ctx.send(
                        f"@{ctx.author.name} You already claimed your daily bonus! "
                        f"Come back in {hours_left:.1f} hours."
                    )
                    return
            
            # Give daily bonus
            daily_bonus = 50
            await add_coins(ctx.author.name, daily_bonus, "daily_bonus", "Daily login bonus")
            
            # Update last claim time
            async with async_session() as session:
                result = await session.execute(
                    select(User).where(User.twitch_username == ctx.author.name)
                )
                user = result.scalar_one_or_none()
                user.last_daily_claim = now
                await session.commit()
            
            await ctx.send(
                f"🎁 @{ctx.author.name} claimed {daily_bonus} coins! Come back tomorrow for more!"
            )
    
    @commands.command(name='give')
    async def give_command(self, ctx, recipient: str, amount: int):
        """Give coins to another player"""
        # Remove @ from recipient if present
        recipient = recipient.lstrip('@')
        
        # Validate amount
        if amount <= 0:
            await ctx.send(f"@{ctx.author.name} Amount must be greater than 0!")
            return
        
        # Special admin privilege for JustASuspect - doesn't deduct from their balance
        is_admin = ctx.author.name.lower() == 'justasuspect'
        
        # Can't give to yourself (unless admin)
        if not is_admin and recipient.lower() == ctx.author.name.lower():
            await ctx.send(f"@{ctx.author.name} You can't give coins to yourself!")
            return
        
        # Get sender
        sender = await get_or_create_user(ctx.author.name)
        
        # Check if sender has enough coins (unless admin)
        if not is_admin and sender.coins < amount:
            await ctx.send(
                f"@{ctx.author.name} You don't have enough coins! You have {sender.coins} coins."
            )
            return
        
        # Get or create recipient
        await get_or_create_user(recipient)
        
        # Deduct from sender (unless admin)
        if not is_admin:
            await add_coins(ctx.author.name, -amount, "transfer_out", f"Gave {amount} coins to {recipient}")
        
        # Add to recipient
        await add_coins(recipient, amount, "transfer_in", f"Received {amount} coins from {ctx.author.name}")
        
        if is_admin:
            await ctx.send(
                f"💰 @{ctx.author.name} gave {amount} coins to @{recipient}!"
            )
        else:
            await ctx.send(
                f"💰 @{ctx.author.name} gave {amount} coins to @{recipient}! You now have {sender.coins - amount} coins."
            )
    
    @commands.command(name='raffle')
    async def raffle_command(self, ctx, amount: int = None):
        """Start a coin raffle (mods/admin only)"""
        # Check if user is mod or admin
        is_mod_or_admin = (
            ctx.author.is_mod or 
            ctx.author.name.lower() == 'justasuspect' or
            ctx.author.is_broadcaster
        )
        
        if not is_mod_or_admin:
            await ctx.send(f"@{ctx.author.name} Only mods and the broadcaster can start raffles!")
            return
        
        if amount is None:
            await ctx.send(f"@{ctx.author.name} Usage: !p raffle <amount>")
            return
        
        # Validate amount
        if amount <= 0:
            await ctx.send(f"@{ctx.author.name} Raffle amount must be greater than 0!")
            return
        
        if amount > 1000:
            await ctx.send(f"@{ctx.author.name} Raffle amount cannot exceed 1000 coins!")
            return
        
        # Check if raffle already active
        if self.active_raffle:
            await ctx.send(f"@{ctx.author.name} A raffle is already active! Use !p endraffle to end it first.")
            return
        
        # Start raffle
        self.active_raffle = {
            'amount': amount,
            'entries': [],
            'started_by': ctx.author.name
        }
        
        await ctx.send(
            f"🎉 @{ctx.author.name} started a raffle for {amount} coins! "
            f"Type !p join to enter! Raffle ends in 60 seconds."
        )
        
        # Start auto-end timer
        self.raffle_task = self.loop.create_task(self.auto_end_raffle())
    
    async def auto_end_raffle(self):
        """Automatically end raffle after 60 seconds"""
        await asyncio.sleep(60)
        
        if not self.active_raffle:
            return
        
        channel = self.get_channel(os.getenv('TWITCH_CHANNEL'))
        if not channel:
            return
        
        if len(self.active_raffle['entries']) == 0:
            await channel.send(f"⏰ Raffle ended! No one entered. Better luck next time!")
            self.active_raffle = None
            return
        
        # Pick random winner
        winner = random.choice(self.active_raffle['entries'])
        amount = self.active_raffle['amount']
        
        # Award coins
        await add_coins(winner, amount, "raffle_win", f"Won raffle for {amount} coins")
        
        await channel.send(
            f"🎊 @{winner} won the raffle and received {amount} coins! "
            f"({len(self.active_raffle['entries'])} total entries)"
        )
        
        # Clear raffle
        self.active_raffle = None
    
    @commands.command(name='join')
    async def join_command(self, ctx):
        """Join an active raffle"""
        if not self.active_raffle:
            await ctx.send(f"@{ctx.author.name} No raffle is currently active!")
            return
        
        # Check if already entered
        if ctx.author.name in self.active_raffle['entries']:
            await ctx.send(f"@{ctx.author.name} You're already in the raffle!")
            return
        
        # Add entry
        self.active_raffle['entries'].append(ctx.author.name)
        await ctx.send(
            f"✅ @{ctx.author.name} entered the raffle! Good luck!"
        )
    
    @commands.command(name='endraffle')
    async def endraffle_command(self, ctx):
        """End the raffle early and pick a winner (mods/admin only)"""
        # Check if user is mod or admin
        is_mod_or_admin = (
            ctx.author.is_mod or 
            ctx.author.name.lower() == 'justasuspect' or
            ctx.author.is_broadcaster
        )
        
        if not is_mod_or_admin:
            await ctx.send(f"@{ctx.author.name} Only mods and the broadcaster can end raffles!")
            return
        
        if not self.active_raffle:
            await ctx.send(f"@{ctx.author.name} No raffle is currently active!")
            return
        
        # Cancel auto-end timer
        if self.raffle_task:
            self.raffle_task.cancel()
            self.raffle_task = None
        
        if len(self.active_raffle['entries']) == 0:
            await ctx.send(f"@{ctx.author.name} No one entered the raffle! Raffle cancelled.")
            self.active_raffle = None
            return
        
        # Pick random winner
        winner = random.choice(self.active_raffle['entries'])
        amount = self.active_raffle['amount']
        
        # Award coins
        await add_coins(winner, amount, "raffle_win", f"Won raffle for {amount} coins")
        
        await ctx.send(
            f"🎊 @{winner} won the raffle and received {amount} coins! "
        )
        
        # Clear raffle
        self.active_raffle = None
    
    @commands.command(name='spawn')
    async def spawn_command(self, ctx, *, pokemon_name: str = None):
        """Manually spawn a specific Pokemon (mods/admin only)"""
        # Check if user is mod or admin
        is_mod_or_admin = (
            ctx.author.is_mod or 
            ctx.author.name.lower() == 'justasuspect' or
            ctx.author.is_broadcaster
        )
        
        if not is_mod_or_admin:
            await ctx.send(f"@{ctx.author.name} Only mods and the broadcaster can spawn Pokemon!")
            return
        
        if not pokemon_name:
            await ctx.send(f"@{ctx.author.name} Usage: !p spawn <pokemon_name>")
            return
        
        # Capitalize first letter of each word
        pokemon_name = pokemon_name.title()
        
        # Validate pokemon
        if pokemon_name not in POKEMON_DATA:
            await ctx.send(f"@{ctx.author.name} '{pokemon_name}' is not a valid Pokemon!")
            return
        
        # Check if there's already a spawn
        if self.current_spawn:
            await ctx.send(f"@{ctx.author.name} There's already a {self.current_spawn} spawned! Wait for it to despawn first.")
            return
        
        # Spawn the pokemon
        self.current_spawn = pokemon_name
        self.spawn_time = datetime.now(timezone.utc)
        
        pokemon_info = POKEMON_DATA[pokemon_name]
        
        # Log spawn
        logger.info(f"🎮 MANUAL SPAWN by {ctx.author.name}: {pokemon_name} ({pokemon_info['type']}) - {pokemon_info['rarity'].upper()}")
        
        rarity_emoji = {
            "common": "⚪",
            "uncommon": "🟢",
            "rare": "🔵",
            "epic": "🟣",
            "legendary": "🟡"
        }
        
        await ctx.send(
            f"{rarity_emoji.get(pokemon_info['rarity'], '⚪')} A wild {pokemon_name} "
            f"({pokemon_info['type']}) appeared! [{pokemon_info['rarity'].upper()}] "
            f"Use !p catch <ball_type> to try to catch it! (Available: pokeball, greatball, ultraball, masterball)"
        )
        
        # Broadcast to overlay
        await self.broadcast_to_overlay({
            "type": "spawn",
            "pokemon": pokemon_name,
            "rarity": pokemon_info['rarity'],
            "sprite": pokemon_info['sprite']
        })
        
        # Despawn after 60 seconds if not caught
        async def auto_despawn():
            await asyncio.sleep(60)
            if self.current_spawn == pokemon_name:
                self.current_spawn = None
                channel = self.get_channel(os.getenv('TWITCH_CHANNEL'))
                if channel:
                    await channel.send(f"The wild {pokemon_name} got away!")
                    await self.broadcast_to_overlay({"type": "despawn"})
        
        self.loop.create_task(auto_despawn())
    
    async def websocket_server(self):
        """WebSocket server for overlay communication"""
        async def handler(websocket, path):
            client_ip = websocket.remote_address[0]
            logger.info(f"🔗 Overlay connected from {client_ip}")
            self.websocket_clients.add(websocket)
            try:
                await websocket.wait_closed()
            finally:
                logger.info(f"❌ Overlay disconnected from {client_ip}")
                self.websocket_clients.remove(websocket)
        
        port = int(os.getenv('WEBSOCKET_PORT', 8001))
        async with websockets.serve(handler, "0.0.0.0", port):
            logger.info(f"🌐 WebSocket server started on 0.0.0.0:{port}")
            await asyncio.Future()  # Run forever
    
    async def broadcast_to_overlay(self, message):
        """Broadcast message to all connected overlay clients"""
        if self.websocket_clients:
            logger.info(f"📡 Broadcasting to {len(self.websocket_clients)} overlay(s): {message['type']}")
            message_json = json.dumps(message)
            await asyncio.gather(
                *[client.send(message_json) for client in self.websocket_clients],
                return_exceptions=True
            )
        else:
            logger.warning("⚠️ No overlays connected - spawn will not be shown")

if __name__ == "__main__":
    bot = PokemonBot()
    bot.run()
