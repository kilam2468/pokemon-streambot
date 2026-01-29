#!/bin/bash

# Quick Production Start Script
# Runs all services with proper production settings

set -e

echo "🎮 Starting Pokemon Stream Bot (Production Mode)"
echo "================================================"

# Check if .env exists
if [ ! -f "bot/.env" ]; then
    echo "❌ Error: bot/.env not found!"
    echo "Run ./setup.sh first or manually create bot/.env"
    exit 1
fi

# Function to kill all processes on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down all services..."
    kill $BOT_PID $API_PID $WEB_PID 2>/dev/null
    pkill -P $$ 2>/dev/null
    exit 0
}

# Only trap SIGINT (Ctrl+C), not SIGTERM or SIGHUP
trap cleanup SIGINT

# Create logs directory if it doesn't exist
mkdir -p logs

# Activate virtual environment
echo "🐍 Activating Python environment..."
cd bot
source .venv/bin/activate
cd ..

# Start the Twitch bot in background
echo "🤖 Starting Twitch Bot..."
cd bot
.venv/bin/python main.py > ../logs/bot.log 2>&1 &
BOT_PID=$!
cd ..
echo "   PID: $BOT_PID"

sleep 2

# Start the API server in background
echo "🌐 Starting API Server (port 8000)..."
cd bot
.venv/bin/python -m uvicorn api:app --host 0.0.0.0 --port 8000 > ../logs/api.log 2>&1 &
API_PID=$!
cd ..
echo "   PID: $API_PID"

sleep 2

# Build and serve website for production
echo "💻 Building website..."
cd website
npm run build > ../logs/build.log 2>&1

echo "🌍 Starting Website (port 4173)..."
npm run preview -- --host 0.0.0.0 > ../logs/website.log 2>&1 &
WEB_PID=$!
cd ..
echo "   PID: $WEB_PID"

echo ""
echo "✅ All services started!"
echo ""
echo "📊 Service URLs:"
echo "   Bot: Running in background (check logs/bot.log)"
echo "   API: http://YOUR_IP:8000"
echo "   Website: http://YOUR_IP:4173"
echo "   Overlay: http://YOUR_IP:8000/overlay"
echo ""
echo "📝 Log files:"
echo "   Bot: tail -f logs/bot.log"
echo "   API: tail -f logs/api.log"
echo "   Website: tail -f logs/website.log"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for all processes
wait
