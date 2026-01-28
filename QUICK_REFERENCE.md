# Pokemon Stream Bot - Quick Reference Card

## 🚀 Initial Setup
```bash
chmod +x setup.sh && ./setup.sh
# Edit bot/.env with your Twitch credentials
./start.sh
```

## 🎯 Starting Services

| Method | Command | Use Case |
|--------|---------|----------|
| Development | `./start.sh` | Testing, development, see output in terminal |
| Production | `./start-production.sh` | Running in background with logs |
| Systemd | `sudo systemctl start pokemon-*` | Auto-start on boot |

## 🔍 Monitoring

```bash
./status.sh                           # Check if everything is running
tail -f logs/bot.log                  # Watch bot logs
tail -f logs/api.log                  # Watch API logs
sudo journalctl -u pokemon-bot -f    # Systemd logs (if using systemd)
```

## 🛑 Stopping Services

```bash
# If started with start.sh
Ctrl+C in the terminal

# If started with start-production.sh
pkill -f "python.*main.py"
pkill -f "python.*api.py"
pkill -f "npm run"

# If using systemd
sudo systemctl stop pokemon-bot pokemon-api pokemon-website
```

## 📍 Service URLs

| Service | URL | Port |
|---------|-----|------|
| API | `http://YOUR_IP:8000` | 8000 |
| Website (Dev) | `http://YOUR_IP:5173` | 5173 |
| Website (Prod) | `http://YOUR_IP:4173` | 4173 |
| OBS Overlay | `http://YOUR_IP:8000/overlay` | 8000 |
| WebSocket | `ws://YOUR_IP:8001` | 8001 |

## 🎮 Twitch Chat Commands

| Command | Description |
|---------|-------------|
| `p!catch pokeball` | Catch Pokemon with Pokéball |
| `p!catch greatball` | Catch with Great Ball |
| `p!catch ultraball` | Catch with Ultra Ball |
| `p!catch masterball` | Catch with Master Ball (100% success) |
| `p!catch` | Auto-select best available ball |
| `p!inventory` or `p!inv` | View your items and coins |
| `p!shop` | View the shop |
| `p!buy pokeball` | Buy Pokéballs |
| `p!buy greatball` | Buy Great Balls |
| `p!buy ultraball` | Buy Ultra Balls |
| `p!buy masterball` | Buy Master Balls |
| `p!pokedex` or `p!dex` | View Pokédex progress |
| `p!stats` | View your statistics |
| `p!daily` | Claim daily coin bonus (50 coins, once per 24h) |
| `p!give @user 100` | Give coins to another player |

## 🎪 Mod/Admin Commands

| Command | Description |
|---------|-------------|
| `p!raffle 500` | Start a coin raffle (mods only) |
| `p!enter` | Enter the raffle (viewers) |
| `p!draw` | Draw raffle winner (mods only) |

## 💰 Economy

| Item | Cost | Catch Rate Bonus |
|------|------|------------------|
| Pokéball | Free (starter) | 1x |
| Great Ball | 50 coins | 1.5x |
| Ultra Ball | 200 coins | 2x |
| Master Ball | 1000 coins | 100% catch |

**Earning Coins:**
- 10 coins per successful catch
- 50 coins from daily bonus (`p!daily`)
- Raffle wins
- Gifts from other players/admin

## 🎨 OBS Setup

1. Add **Browser Source**
2. URL: `http://YOUR_CT_IP:8000/overlay`
3. Width: `1920`
4. Height: `1080`
5. ✅ Refresh browser when scene becomes active
6. ✅ Shutdown source when not visible

## 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `bot/.env` | Twitch credentials and bot settings |
| `website/.env` | API URL for website |
| `bot/data/pokemon.db` | SQLite database (user data) |

## 📝 Important File Locations

```
pokemon-streambot/
├── bot/.env                    # YOUR TWITCH CREDENTIALS
├── bot/data/pokemon.db         # DATABASE (backup this!)
├── logs/                       # Log files
│   ├── bot.log
│   ├── api.log
│   └── website.log
└── start.sh                    # Start script
```

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot won't start | Check `bot/.env` has valid OAuth token |
| No Pokemon spawning | Check if stream is live (bot checks this now!) |
| Overlay not working | Verify API is running on port 8000 |
| Website can't connect | Check API URL in `website/.env` |
| Permission denied on scripts | Run `chmod +x *.sh` |

## 🔐 Getting Twitch Credentials

1. **OAuth Token**: https://twitchapps.com/tmi/
2. **Client ID/Secret**: https://dev.twitch.tv/console/apps
   - Create new application
   - OAuth Redirect: `http://localhost:3000`
   - Get Client ID and Client Secret

## 💾 Backup

**Important files to backup:**
```bash
tar -czf pokemon-backup-$(date +%Y%m%d).tar.gz bot/.env bot/data/
```

## 📊 Database Queries (Advanced)

```bash
cd bot
source .venv/bin/activate
sqlite3 data/pokemon.db

# View users
SELECT * FROM users LIMIT 10;

# View catches
SELECT * FROM caught_pokemon LIMIT 10;

# Top players by coins
SELECT twitch_username, coins FROM users ORDER BY coins DESC LIMIT 10;
```

## 🔄 Updating

```bash
git pull
cd bot && source .venv/bin/activate && pip install -r requirements.txt
cd ../website && npm install
# Restart services
```

## 📞 Quick Help

- `./status.sh` - Check everything
- `./start.sh` - Start in dev mode
- `./start-production.sh` - Start in production
- Check logs in `logs/` directory
- Read [PROXMOX_SETUP.md](./PROXMOX_SETUP.md) for full details
