# Quick Start Guide

## Getting Started in 5 Minutes

### 1. Setup Bot

```bash
cd pokemon-streambot/bot

# Install Python dependencies
pip install -r requirements.txt

# Configure your Twitch credentials
cp .env.example .env
nano .env  # or use your favorite editor
```

### 2. Get Twitch OAuth Token

#### Option A: Quick Method (Easiest)

1. Visit: https://twitchapps.com/tmi/
2. Click "Connect"
3. Copy the OAuth token (starts with "oauth:")
4. Paste it in your `.env` file

#### Option B: Using Client ID & Client Secret

If you already have Client ID and Client Secret from https://dev.twitch.tv/console/apps:

1. Visit this URL (replace YOUR_CLIENT_ID):
   ```
   https://id.twitch.tv/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:3000&response_type=token&scope=chat:read+chat:edit
   ```

2. Authorize your app
3. Copy the token from the URL (after `#access_token=`)
4. Add "oauth:" prefix: `oauth:your_token_here`

#### Option C: Using Twitch CLI (Advanced)

```bash
# Install Twitch CLI
brew install twitch  # Mac
# Or download from https://github.com/twitchdev/twitch-cli

# Login and get token
twitch token
```

### 3. Update .env File

```env
TWITCH_BOT_TOKEN=oauth:your_token_here
TWITCH_CLIENT_ID=your_client_id_here
TWITCH_CLIENT_SECRET=your_client_secret_here
TWITCH_BOT_NICK=your_bot_username
TWITCH_CHANNEL=your_channel_name
```

**Note:** You need both the OAuth token AND the Client ID/Secret for full functionality.

### 4. Start Everything

```bash
# Terminal 1 - Start the Twitch bot
cd bot
python main.py

# Terminal 2 - Start the API server  
cd bot
python api.py

# Terminal 3 - Start the website
cd website
npm install
npm run dev
```

### 5. Add to OBS

1. Add **Browser Source** in OBS
2. URL: `http://localhost:8000/overlay` (or your server IP)
3. Width: 1920, Height: 1080
4. Done! Pokemon will appear on stream

**Note:** The API server must be running for the overlay to work!

## Testing

1. Join your Twitch channel
2. Wait for a Pokemon to spawn (or reduce spawn time in .env)
3. Type: `!catch pokeball`
4. Visit http://localhost:3000 and enter your username

## Common Commands

```
!catch pokeball     # Catch with Poké Ball
!catch greatball    # Catch with Great Ball
!inventory         # Check your balls
!shop              # View shop
!buy pokeball      # Buy 5 Poké Balls
!pokedex           # View collection
!stats             # View statistics
```

## Next Steps

- Read full README.md for production deployment
- Customize Pokemon spawn rates in pokemon_data.py
- Adjust shop prices and catch rates
- Set up systemd services for auto-restart

Happy catching! 🎮
