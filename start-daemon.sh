#!/bin/bash

# Daemon Mode Start Script
# Runs all services completely in background, survives terminal close

set -e

echo "🎮 Starting Pokemon Stream Bot (Daemon Mode)"
echo "=============================================="

# Check if .env exists
if [ ! -f "bot/.env" ]; then
    echo "❌ Error: bot/.env not found!"
    echo "Run ./setup.sh first or manually create bot/.env"
    exit 1
fi

# Create logs directory if it doesn't exist
mkdir -p logs

# Store PIDs
PIDFILE="logs/services.pid"

# Check if services are already running
if [ -f "$PIDFILE" ]; then
    echo "⚠️  Services may already be running. Check with ./status.sh"
    echo "   To force restart, run ./stop.sh first"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Activate virtual environment
echo "🐍 Activating Python environment..."
cd bot
source .venv/bin/activate
cd ..

# Start the Twitch bot in background (daemonized)
echo "🤖 Starting Twitch Bot..."
cd bot
nohup .venv/bin/python main.py > ../logs/bot.log 2>&1 &
BOT_PID=$!
cd ..
echo "   PID: $BOT_PID"

sleep 2

# Start the API server in background (daemonized)
echo "🌐 Starting API Server (port 8000)..."
cd bot
nohup .venv/bin/python -m uvicorn api:app --host 0.0.0.0 --port 8000 > ../logs/api.log 2>&1 &
API_PID=$!
cd ..
echo "   PID: $API_PID"

sleep 2

# Build website
echo "💻 Building website..."
cd website
npm run build > ../logs/build.log 2>&1
cd ..

# Start website in background (daemonized)
echo "🌍 Starting Website (port 4173)..."
cd website
nohup npm run preview -- --host 0.0.0.0 > ../logs/website.log 2>&1 &
WEB_PID=$!
cd ..
echo "   PID: $WEB_PID"

# Save PIDs to file
echo "$BOT_PID" > "$PIDFILE"
echo "$API_PID" >> "$PIDFILE"
echo "$WEB_PID" >> "$PIDFILE"

echo ""
echo "✅ All services started in daemon mode!"
echo ""
echo "📊 Service URLs:"
echo "   Bot: Running in background (check logs/bot.log)"
echo "   API: http://YOUR_IP:8000"
echo "   Website: http://YOUR_IP:4173"
echo "   Overlay: http://YOUR_IP:8000/overlay"
echo ""
echo "📝 Management commands:"
echo "   Check status: ./status.sh"
echo "   View logs:    tail -f logs/bot.log"
echo "   Stop all:     ./stop.sh"
echo ""
echo "🔒 Services will continue running even if you close this terminal"
echo ""
