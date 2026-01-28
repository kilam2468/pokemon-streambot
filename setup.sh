#!/bin/bash

# Pokemon Stream Bot - One-Click Setup Script
# For Proxmox CT or any Linux environment

set -e  # Exit on error

echo "🎮 Pokemon Stream Bot - Setup Script"
echo "===================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    echo -e "${YELLOW}⚠️  Warning: Running as root. Consider using a regular user.${NC}"
fi

# Detect package manager and install dependencies
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    # Debian/Ubuntu
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv nodejs npm git
elif command -v yum &> /dev/null; then
    # RHEL/CentOS
    sudo yum install -y python3 python3-pip nodejs npm git
elif command -v dnf &> /dev/null; then
    # Fedora
    sudo dnf install -y python3 python3-pip nodejs npm git
else
    echo -e "${RED}❌ Could not detect package manager. Please install python3, nodejs, and npm manually.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ System dependencies installed${NC}"
echo ""

# Setup Python bot
echo "🐍 Setting up Python bot..."
cd bot

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
fi

# Activate virtual environment
source .venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✅ Python dependencies installed${NC}"

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo -e "${YELLOW}📝 Creating .env file...${NC}"
    cat > .env << 'EOF'
# Twitch Bot Configuration
TWITCH_BOT_TOKEN=oauth:your_token_here
TWITCH_CLIENT_ID=your_client_id_here
TWITCH_CLIENT_SECRET=your_client_secret_here
TWITCH_BOT_NICK=your_bot_username
TWITCH_CHANNEL=your_channel_name

# Spawn Settings (in seconds)
SPAWN_INTERVAL_MIN=60
SPAWN_INTERVAL_MAX=300

# WebSocket Port for Overlay
WEBSOCKET_PORT=8001

# API Port
API_PORT=8000
EOF
    echo -e "${GREEN}✅ Created .env file at bot/.env${NC}"
    echo -e "${YELLOW}⚠️  You MUST edit bot/.env with your Twitch credentials!${NC}"
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

cd ..
echo ""

# Setup Website
echo "🌐 Setting up website..."
cd website

# Install npm dependencies
npm install
echo -e "${GREEN}✅ Website dependencies installed${NC}"

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    cat > .env << 'EOF'
VITE_API_URL=http://localhost:8000
EOF
    echo -e "${GREEN}✅ Created website/.env file${NC}"
fi

cd ..
echo ""

# Make start script executable
chmod +x start.sh

# Create systemd service files (optional)
echo ""
echo -e "${YELLOW}Would you like to create systemd services for auto-start? (y/n)${NC}"
read -r CREATE_SERVICES

if [[ $CREATE_SERVICES =~ ^[Yy]$ ]]; then
    CURRENT_DIR=$(pwd)
    CURRENT_USER=$(whoami)
    
    # Bot service
    sudo tee /etc/systemd/system/pokemon-bot.service > /dev/null << EOF
[Unit]
Description=Pokemon Twitch Bot
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR/bot
Environment="PATH=$CURRENT_DIR/bot/.venv/bin"
ExecStart=$CURRENT_DIR/bot/.venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    # API service
    sudo tee /etc/systemd/system/pokemon-api.service > /dev/null << EOF
[Unit]
Description=Pokemon API Server
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR/bot
Environment="PATH=$CURRENT_DIR/bot/.venv/bin"
ExecStart=$CURRENT_DIR/bot/.venv/bin/python api.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    # Website service
    sudo tee /etc/systemd/system/pokemon-website.service > /dev/null << EOF
[Unit]
Description=Pokemon Website
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR/website
ExecStart=/usr/bin/npm run dev
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    sudo systemctl daemon-reload
    echo -e "${GREEN}✅ Systemd services created${NC}"
    echo ""
    echo "To enable and start services:"
    echo "  sudo systemctl enable pokemon-bot pokemon-api pokemon-website"
    echo "  sudo systemctl start pokemon-bot pokemon-api pokemon-website"
    echo ""
    echo "To view logs:"
    echo "  sudo journalctl -u pokemon-bot -f"
    echo "  sudo journalctl -u pokemon-api -f"
    echo "  sudo journalctl -u pokemon-website -f"
fi

echo ""
echo "=================================="
echo -e "${GREEN}🎉 Setup Complete!${NC}"
echo "=================================="
echo ""
echo "📝 Next Steps:"
echo "   1. Edit bot/.env with your Twitch credentials"
echo "      Get OAuth token: https://twitchapps.com/tmi/"
echo "      Get Client ID: https://dev.twitch.tv/console/apps"
echo ""
echo "   2. Start the bot:"
echo "      ./start.sh"
echo ""
echo "   3. Add OBS overlay:"
echo "      Browser Source URL: http://YOUR_SERVER_IP:8000/overlay"
echo "      Width: 1920, Height: 1080"
echo ""
echo "   4. Access the website:"
echo "      http://YOUR_SERVER_IP:5173"
echo ""
echo "📚 Documentation:"
echo "   - QUICKSTART.md - Quick start guide"
echo "   - AUTHENTICATION.md - Twitch auth details"
echo "   - README.md - Full documentation"
echo ""

deactivate 2>/dev/null || true
