# Pokemon Stream Bot - Proxmox CT Setup

This project is optimized for running on a Proxmox container or any Linux environment.

## 🚀 Quick Setup (One Command)

```bash
chmod +x setup.sh && ./setup.sh
```

This will:
- ✅ Install all system dependencies (Python, Node.js)
- ✅ Create Python virtual environment
- ✅ Install all Python packages
- ✅ Install all Node.js packages
- ✅ Create configuration files
- ✅ Optionally create systemd services for auto-start

## 📋 Manual Setup

If you prefer to set things up manually:

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm

# 2. Setup Python bot
cd bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
cd ..

# 3. Setup website
cd website
npm install
cd ..
```

## 🎯 Running the Bot

### Option 1: Development Mode (start.sh)
```bash
./start.sh
```
Runs all services in foreground with live reload.

### Option 2: Production Mode (start-production.sh)
```bash
chmod +x start-production.sh
./start-production.sh
```
Runs optimized production build with logging to files.

### Option 3: Production with Nginx (Recommended)

For production with a domain (e.g., poke.hfdn.dev):

```bash
# 1. Setup nginx reverse proxy
chmod +x setup-nginx.sh && ./setup-nginx.sh

# 2. Update website configuration
cd website
echo "VITE_API_URL=https://poke.hfdn.dev" > .env
npm run build
cd ..

# 3. Start services
./start-production.sh
```

See [nginx/NGINX_SETUP.md](nginx/NGINX_SETUP.md) for detailed nginx configuration.

### Option 4: Systemd Services (Auto-start on boot)

If you created systemd services during setup:

```bash
# Enable services to start on boot
sudo systemctl enable pokemon-bot pokemon-api pokemon-website

# Start services now
sudo systemctl start pokemon-bot pokemon-api pokemon-website

# Check status
sudo systemctl status pokemon-bot
sudo systemctl status pokemon-api
sudo systemctl status pokemon-website

# View logs
sudo journalctl -u pokemon-bot -f
sudo journalctl -u pokemon-api -f

# Stop services
sudo systemctl stop pokemon-bot pokemon-api pokemon-website
```

## 🔧 Configuration

### 1. Twitch Credentials (bot/.env)

```env
TWITCH_BOT_TOKEN=oauth:your_token_here
TWITCH_CLIENT_ID=your_client_id_here
TWITCH_CLIENT_SECRET=your_client_secret_here
TWITCH_BOT_NICK=your_bot_username
TWITCH_CHANNEL=your_channel_name
```

**Get credentials:**
- OAuth Token: https://twitchapps.com/tmi/
- Client ID/Secret: https://dev.twitch.tv/console/apps

### 2. Spawn Settings (bot/.env)

```env
SPAWN_INTERVAL_MIN=60    # Minimum seconds between spawns
SPAWN_INTERVAL_MAX=300   # Maximum seconds between spawns
```

### 3. Ports (bot/.env)

```env
WEBSOCKET_PORT=8001  # WebSocket for overlay
API_PORT=8000        # API server
```

Website runs on:
- Port 5173 in development mode (`./start.sh` or `npm run dev`)
- Port 4173 in production mode (`./start-production.sh` or `npm run preview`)

## 🌐 Accessing Services

After starting, services are available at:

- **API**: `http://YOUR_CT_IP:8000`
- **Website (Dev)**: `http://YOUR_CT_IP:5173`
- **Website (Production)**: `http://YOUR_CT_IP:4173`
- **OBS Overlay**: `http://YOUR_CT_IP:8000/overlay`

## 🎨 OBS Setup

1. Add **Browser Source** in OBS
2. URL: `http://YOUR_CT_IP:8000/overlay`
3. Width: **1920**
4. Height: **1080**
5. Check "Shutdown source when not visible" for better performance

## 🔥 Firewall (if needed)

Open required ports:

```bash
# UFW (Ubuntu/Debian)
sudo ufw allow 8000/tcp   # API
sudo ufw allow 4173/tcp   # Website (Production)
sudo ufw allow 5173/tcp   # Website (Dev - optional)
sudo ufw allow 8001/tcp   # WebSocket

# Firewalld (RHEL/CentOS)
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --permanent --add-port=4173/tcp
sudo firewall-cmd --permanent --add-port=5173/tcp
sudo firewall-cmd --permanent --add-port=8001/tcp
sudo firewall-cmd --reload
```

## 📊 Monitoring

### Check Logs
```bash
# If running with start.sh (check terminal)
# If running with start-production.sh
tail -f logs/bot.log
tail -f logs/api.log
tail -f logs/website.log

# If running with systemd
sudo journalctl -u pokemon-bot -f
sudo journalctl -u pokemon-api -f
sudo journalctl -u pokemon-website -f
```

### Check Database
```bash
cd bot
source .venv/bin/activate
sqlite3 data/pokemon.db

# Inside sqlite3:
.tables
SELECT * FROM users LIMIT 5;
SELECT * FROM caught_pokemon LIMIT 10;
.exit
```

## 🔄 Updating

```bash
git pull
cd bot
source .venv/bin/activate
pip install -r requirements.txt
cd ../website
npm install
cd ..
./start.sh  # or restart systemd services
```

## 🆘 Troubleshooting

### Bot won't start
- Check `bot/.env` has correct Twitch credentials
- Verify OAuth token starts with `oauth:`
- Check logs: `tail -f logs/bot.log`

### Website won't load
- Check if port 4173 (production) or 5173 (dev) is accessible
- Verify `website/.env` has correct API URL
- Run `cd website && npm run build` to rebuild

### Overlay not showing in OBS
- Verify API is running: `curl http://localhost:8000/overlay`
- Check WebSocket port 8001 is not blocked
- Open browser to overlay URL first to test

### Pokemon not spawning
- Check bot logs for errors
- Verify stream is live (bot now checks stream status)
- Check spawn interval settings in .env

## 💾 Backup

Important files to backup:
```bash
bot/.env              # Your configuration
bot/data/pokemon.db   # User data and pokemon catches
```

Backup command:
```bash
tar -czf pokemon-backup-$(date +%Y%m%d).tar.gz bot/.env bot/data/
```

## 🔐 Security Notes

For production on Proxmox:

1. **Don't expose unnecessary ports** - Only open what you need
2. **Use environment variables** - Never commit `.env` files
3. **Update regularly** - Keep dependencies updated
4. **Use HTTPS in production** - Consider nginx reverse proxy
5. **Restrict API access** - Configure CORS properly in api.py

## 📚 Additional Resources

- [QUICKSTART.md](./QUICKSTART.md) - Quick start guide
- [AUTHENTICATION.md](./AUTHENTICATION.md) - Twitch authentication details
- [README.md](./README.md) - Full feature documentation
