# Authentication Setup Guide

## I have Client ID and Client Secret - What do I do?

If you have your **Client ID** and **Client Secret** from the [Twitch Developer Console](https://dev.twitch.tv/console/apps), here's how to get your OAuth token:

## ✅ Recommended Method: Use the Helper Script

```bash
cd pokemon-streambot/bot
python3 get_oauth_token.py
```

**What it does:**
1. Asks for your Client ID
2. Opens your browser for Twitch authorization
3. Automatically captures the OAuth token
4. Displays it for you to copy to `.env`

**Example output:**
```
🎮 Twitch OAuth Token Generator
==================================================

Enter your Twitch Client ID: abc123xyz...

1. Starting local server on port 3000...
2. Opening browser for authorization...
3. Waiting for authorization...

✅ Token received successfully!

Your OAuth Token:
oauth:a1b2c3d4e5f6g7h8i9j0

==================================================

Add this to your .env file:
TWITCH_BOT_TOKEN=oauth:a1b2c3d4e5f6g7h8i9j0
```

## Alternative Methods

### Method 2: Manual Browser Method

1. Replace `YOUR_CLIENT_ID` in this URL:
   ```
   https://id.twitch.tv/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:3000&response_type=token&scope=chat:read+chat:edit
   ```

2. Open the URL in your browser
3. Click "Authorize"
4. **Extract token from the redirected URL:**
   - You'll see: `http://localhost:3000/#access_token=YOUR_TOKEN&scope=...`
   - Copy everything between `access_token=` and the next `&`
   - Example: `http://localhost:3000/#access_token=abc123xyz&scope=...`
   - Your token is: `abc123xyz`
5. Add the `oauth:` prefix: `oauth:abc123xyz`

**Note:** You may get a "page not found" error - that's OK! The token is still in the URL.

### Method 3: Use TwitchApps (Simplest but less control)

1. Visit: https://twitchapps.com/tmi/
2. Click "Connect"
3. Authorize the application
4. Copy the full token (already has `oauth:` prefix)

## Final .env Configuration

Once you have your OAuth token, your `.env` should look like:

```env
# Required
TWITCH_BOT_TOKEN=oauth:your_generated_token
TWITCH_CLIENT_ID=your_client_id
TWITCH_CLIENT_SECRET=your_client_secret
TWITCH_BOT_NICK=your_bot_username
TWITCH_CHANNEL=your_channel_name

# Optional (defaults shown)
API_HOST=0.0.0.0
API_PORT=8000
WEBSOCKET_PORT=8001
SPAWN_INTERVAL_MIN=60
SPAWN_INTERVAL_MAX=300
```

## Important Notes

- **OAuth Token**: Used by the bot to send messages in chat
- **Client ID & Secret**: Used for API calls and advanced features
- **Bot Nick**: The Twitch username of your bot account
- **Channel**: Your Twitch channel name (where the bot will operate)

## Troubleshooting

**"Invalid OAuth token" error:**
- Make sure the token starts with `oauth:`
- Token must be for the same account as `TWITCH_BOT_NICK`
- Generate a new token if it's expired

**"Connection failed" error:**
- Verify your bot account exists on Twitch
- Check that the channel name is correct and lowercase
- Ensure your bot has no restrictions/bans

**Port 3000 already in use (for helper script):**
```bash
# Find and kill process using port 3000
lsof -ti:3000 | xargs kill -9

# Or change the port in get_oauth_token.py
```

## Security Best Practices

⚠️ **Never commit your .env file to git!**

```bash
# Make sure .gitignore includes:
.env
*.db
```

🔒 **Keep your tokens secret:**
- Don't share your OAuth token
- Don't share your Client Secret
- Regenerate tokens if they're exposed

✅ **Use environment variables in production:**
```bash
# Instead of .env file, set environment variables:
export TWITCH_BOT_TOKEN="oauth:..."
export TWITCH_CLIENT_ID="..."
# etc.
```

## Ready to Go!

Once your `.env` is configured:

```bash
# Test the bot
python3 bot/main.py

# If it connects successfully, you'll see:
# Logged in as | your_bot_name
# Connected to channel: your_channel
```

🎉 You're all set! Happy streaming!
