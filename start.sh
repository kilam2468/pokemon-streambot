#!/bin/bash

# Pokemon Stream Bot Startup Script

echo "🎮 Starting Pokemon Stream Bot..."

# Check if .env exists
if [ ! -f "bot/.env" ]; then
    echo "❌ Error: bot/.env not found!"
    echo "📝 Copy bot/.env.example to bot/.env and configure it first"
    exit 1
fi

# Function to kill all processes on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down Pokemon Stream Bot..."
    kill $BOT_PID $API_PID $WEB_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start the Twitch bot
echo "🤖 Starting Twitch Bot..."
cd bot
python3 main.py &
BOT_PID=$!
cd ..

sleep 2

# Start the API server
echo "🌐 Starting API Server..."
cd bot
python3 api.py &
API_PID=$!
cd ..

sleep 2

# Start the website (if node_modules exists)
if [ -d "website/node_modules" ]; then
    echo "💻 Starting Website..."
    cd website
    npm run dev &
    WEB_PID=$!
    cd ..
else
    echo "⚠️  Website dependencies not installed. Run 'cd website && npm install' first"
    WEB_PID=""
fi

echo ""
echo "✅ Pokemon Stream Bot is running!"
echo ""
echo "📊 Services:"
echo "   - Twitch Bot: Running (PID: $BOT_PID)"
echo "   - API Server: http://localhost:8000 (PID: $API_PID)"
if [ -n "$WEB_PID" ]; then
    echo "   - Website: http://localhost:3000 (PID: $WEB_PID)"
fi
echo "   - Overlay: file://$(pwd)/overlay/index.html"
echo ""
echo "🎯 Add overlay to OBS:"
echo "   Browser Source -> $(pwd)/overlay/index.html"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for all processes
wait
