# Pokemon Stream Bot

A comprehensive Twitch bot that lets viewers catch Pokemon during your stream! Features include:
- 🎮 Interactive Pokemon catching in Twitch chat
- 📱 Web-based Pokedex to view your collection
- 🎨 Animated OBS overlay for stream integration
- 💰 Currency system with shop for Pokeballs
- 📊 Statistics and leaderboards
- ⚡ Optimized for Proxmox CT deployment

## 🚀 Quick Setup (Proxmox/Linux)

**One-command setup:**
```bash
chmod +x setup.sh && ./setup.sh
```

Then edit `bot/.env` with your Twitch credentials and run:
```bash
./start.sh
```

**That's it!** Full setup guide: [PROXMOX_SETUP.md](./PROXMOX_SETUP.md)

## 📚 Documentation

- **[PROXMOX_SETUP.md](./PROXMOX_SETUP.md)** - Complete Proxmox CT setup guide
- **[QUICKSTART.md](./QUICKSTART.md)** - Quick start for development
- **[AUTHENTICATION.md](./AUTHENTICATION.md)** - Twitch authentication details
- **[PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)** - Technical overview

## Project Structure

```
pokemon-streambot/
├── bot/                    # Python Twitch bot & API
│   ├── main.py            # Twitch bot main file
│   ├── api.py             # FastAPI backend
│   ├── database.py        # Database models
│   ├── db_utils.py        # Database utilities
│   ├── pokemon_data.py    # Pokemon data (167 Pokemon!)
│   ├── requirements.txt   # Python dependencies
│   ├── .env.example       # Environment variables template
│   └── data/              # SQLite database location
├── website/               # React website
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── api/          # API client
│   │   └── App.jsx       # Main app
│   └── package.json
└── overlay/               # OBS overlay
    └── index.html        # Animated overlay
```

## Features

### Pokemon Collection (167 Pokemon!)
- **Common** (75 Pokemon): 60% spawn rate
- **Uncommon** (50 Pokemon): 25% spawn rate
- **Rare** (25 Pokemon): 10% spawn rate
- **Epic** (10 Pokemon): 4% spawn rate
- **Legendary** (7 Pokemon): 1% spawn rate

### Pokeball Types
- **Poké Ball**: Free starter balls, basic catch rates
- **Great Ball**: Better catch rates (50 coins)
- **Ultra Ball**: High catch rates (200 coins)
- **Master Ball**: 100% catch rate! (1000 coins)

### Twitch Commands
- `!catch <ball_type>` - Try to catch spawned Pokemon
- `!inventory` or `!inv` - View your Pokeballs
- `!shop` - View the shop
- `!buy <ball_type>` - Purchase Pokeballs
- `!pokedex` or `!dex` - View Pokedex progress
- `!stats` - View your statistics

## Setup Instructions

### 1. Bot Setup (Python)

```bash
cd bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
```

Edit `.env` with your details:
```env
TWITCH_BOT_TOKEN=your_oauth_token_here
TWITCH_CLIENT_ID=your_client_id_here
TWITCH_CLIENT_SECRET=your_client_secret_here
TWITCH_BOT_NICK=your_bot_username
TWITCH_CHANNEL=your_channel_name
```

**Getting Twitch Credentials:**
1. Go to https://dev.twitch.tv/console/apps
2. Create a new application
3. Get your Client ID and Client Secret
4. **Generate OAuth Token** (choose one method):
   
   **Method 1: Using the helper script (Easiest)**
   ```bash
   python3 bot/get_oauth_token.py
   # Enter your Client ID when prompted
   # Browser will open for authorization
   # Token will be displayed automatically
   ```
   
   **Method 2: Manual URL method**
   ```
   Visit: https://id.twitch.tv/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:3000&response_type=token&scope=chat:read+chat:edit
   
   Replace YOUR_CLIENT_ID with your actual Client ID
   After authorizing, copy the token from the URL
   Add "oauth:" prefix to the token
   ```
   
   **Method 3: Quick method**
   ```
   Visit: https://twitchapps.com/tmi/
   Click "Connect" and authorize
   Copy the OAuth token (already has "oauth:" prefix)
   ```

### 2. Run the Bot

```bash
# Terminal 1 - Run Twitch bot
python main.py

# Terminal 2 - Run API server
python api.py
```

The bot will:
- Connect to Twitch chat
- Spawn Pokemon every 1-5 minutes
- Start WebSocket server on port 8001 (for overlay)
- Start API server on port 8000 (for website)

### 3. Website Setup (React)

```bash
cd website

# Install dependencies
npm install

# Start development server
npm run dev
```

Website will be available at http://localhost:3000

For production:
```bash
npm run build
npm run preview
```

### 4. OBS Overlay Setup

1. Open OBS Studio
2. Add a new **Browser Source**
3. Set URL to: `http://your-server-ip:8000/overlay`
   - Replace `your-server-ip` with your Proxmox server IP
   - Example: `http://192.168.1.100:8000/overlay`
   - For local testing: `http://localhost:8000/overlay`
4. Set dimensions: 1920x1080 (or your stream resolution)
5. Check "Shutdown source when not visible" for performance
6. The overlay will automatically connect to the bot's WebSocket

**Important:** Make sure the API server is running (`python api.py`) for the overlay to work!

**Features:**
- Animated Pokemon spawn notifications
- 8-bit pixel art style sprites
- Capture attempt animations with trainer name
- Success/fail indicators with particle effects

## Production Deployment

### Bot & API (Proxmox Server)

1. **Using systemd services:**

Create `/etc/systemd/system/pokemon-bot.service`:
```ini
[Unit]
Description=Pokemon Twitch Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/pokemon-streambot/bot
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Create `/etc/systemd/system/pokemon-api.service`:
```ini
[Unit]
Description=Pokemon API Server
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/pokemon-streambot/bot
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python api.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable pokemon-bot pokemon-api
sudo systemctl start pokemon-bot pokemon-api
```

2. **Using PM2:**
```bash
pm2 start bot/main.py --name pokemon-bot --interpreter python3
pm2 start bot/api.py --name pokemon-api --interpreter python3
pm2 save
pm2 startup
```

### Website (Proxmox Server)

1. **Build for production:**
```bash
cd website
npm run build
```

2. **Serve with nginx:**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    root /path/to/pokemon-streambot/website/dist;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

3. **Or use PM2 with serve:**
```bash
npm install -g serve
pm2 start "serve -s dist -p 3000" --name pokemon-website
```

## Configuration

### Spawn Settings

Edit `bot/.env`:
```env
SPAWN_INTERVAL_MIN=60    # Minimum seconds between spawns
SPAWN_INTERVAL_MAX=300   # Maximum seconds between spawns
```

### Capture Rates

Edit `bot/pokemon_data.py` to adjust capture rates for each ball type and rarity tier.

### Economy Settings

Edit `bot/pokemon_data.py`:
- `SHOP_ITEMS`: Change ball prices and quantities
- `COINS_PER_CATCH`: Reward for catching Pokemon
- `DAILY_LOGIN_BONUS`: Daily coin bonus

## Database

The bot uses SQLite by default (`data/pokemon_bot.db`). Database schema:
- **users**: Twitch users, coins, inventory
- **caught_pokemon**: All caught Pokemon records
- **spawn_history**: Spawn tracking
- **transactions**: Coin transaction history

## API Endpoints

- `GET /api/user/{username}/stats` - User statistics
- `GET /api/user/{username}/pokedex` - Caught Pokemon
- `GET /api/user/{username}/inventory` - Ball inventory
- `GET /api/pokemon` - All available Pokemon
- `GET /api/leaderboard` - Top collectors

## Troubleshooting

**Bot not connecting to Twitch:**
- Verify OAuth token is valid
- Check bot username matches token
- Ensure channel name is lowercase

**Overlay not showing:**
- Check WebSocket URL in overlay/index.html
- Verify bot is running and WebSocket server started
- Check browser console for errors in OBS

**Website can't fetch data:**
- Verify API server is running on port 8000
- Check CORS settings in api.py
- Update VITE_API_URL in website/.env if needed

## Future Features
- ⚔️ Pokemon battles between users
- 🎁 Trading system
- 🏆 Achievements and badges
- 📈 Evolution system
- 🌟 Shiny Pokemon variants

## Credits

- Pokemon sprites from [PokeAPI](https://pokeapi.co/)
- Not affiliated with Nintendo, Game Freak, or The Pokemon Company

## License

This is a fan project for entertainment purposes. Pokemon is © Nintendo/Game Freak.
