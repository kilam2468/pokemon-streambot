#!/bin/bash

# Install systemd service for Pokemon Stream Bot
# This will run start-production.sh automatically on boot

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURRENT_USER=$(whoami)

echo "🎮 Pokemon Stream Bot - Service Installer"
echo "========================================="
echo ""
echo "Install directory: $SCRIPT_DIR"
echo "Run as user: $CURRENT_USER"
echo ""

# Create the systemd service file
echo "📝 Creating systemd service..."

sudo tee /etc/systemd/system/pokemon-streambot.service > /dev/null << EOF
[Unit]
Description=Pokemon Stream Bot (Bot + API + Website)
After=network.target

[Service]
Type=forking
User=$CURRENT_USER
WorkingDirectory=$SCRIPT_DIR
ExecStart=$SCRIPT_DIR/start-production.sh
ExecStop=/usr/bin/pkill -f "python.*main.py"
ExecStop=/usr/bin/pkill -f "uvicorn"
ExecStop=/usr/bin/pkill -f "vite preview"
Restart=on-failure
RestartSec=10
StandardOutput=append:$SCRIPT_DIR/logs/service.log
StandardError=append:$SCRIPT_DIR/logs/service-error.log

[Install]
WantedBy=multi-user.target
EOF

echo "✅ Service file created at /etc/systemd/system/pokemon-streambot.service"
echo ""

# Reload systemd
echo "🔄 Reloading systemd daemon..."
sudo systemctl daemon-reload
echo "✅ Daemon reloaded"
echo ""

# Enable the service
echo "⚙️  Enabling service (will start on boot)..."
sudo systemctl enable pokemon-streambot.service
echo "✅ Service enabled"
echo ""

echo "========================================="
echo "✅ Service installation complete!"
echo "========================================="
echo ""
echo "📝 Service Commands:"
echo ""
echo "  Start:   sudo systemctl start pokemon-streambot"
echo "  Stop:    sudo systemctl stop pokemon-streambot"
echo "  Restart: sudo systemctl restart pokemon-streambot"
echo "  Status:  sudo systemctl status pokemon-streambot"
echo "  Logs:    sudo journalctl -u pokemon-streambot -f"
echo ""
echo "  Or view logs in:"
echo "    $SCRIPT_DIR/logs/bot.log"
echo "    $SCRIPT_DIR/logs/api.log"
echo "    $SCRIPT_DIR/logs/website.log"
echo ""
echo "🚀 To start now: sudo systemctl start pokemon-streambot"
echo ""
