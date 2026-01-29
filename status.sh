#!/bin/bash

# Status checker for Pokemon Stream Bot

echo "🎮 Pokemon Stream Bot - Status Check"
echo "====================================="
echo ""

# Check if processes are running
check_process() {
    local name=$1
    local pattern=$2
    
    if pgrep -f "$pattern" > /dev/null; then
        echo "✅ $name: Running (PID: $(pgrep -f "$pattern" | head -1))"
        return 0
    else
        echo "❌ $name: Not running"
        return 1
    fi
}

# Check services
check_process "Twitch Bot" ".venv/bin/python main.py"
check_process "API Server" "uvicorn api:app"
check_process "Website" "vite preview"

echo ""
echo "📡 Port Status:"
echo "---------------"

# Check if ports are listening
check_port() {
    local port=$1
    local service=$2
    
    if lsof -i :$port -sTCP:LISTEN > /dev/null 2>&1 || netstat -tuln 2>/dev/null | grep ":$port " > /dev/null; then
        echo "✅ Port $port ($service): Open"
    else
        echo "❌ Port $port ($service): Closed"
    fi
}

check_port 8000 "API"
check_port 8001 "WebSocket"
check_port 4173 "Website (Preview)"
check_port 5173 "Website (Dev)"

echo ""
echo "📂 Files:"
echo "---------"

# Check important files
if [ -f "bot/.env" ]; then
    echo "✅ bot/.env: Exists"
else
    echo "❌ bot/.env: Missing (run setup.sh or copy from .env.example)"
fi

if [ -d "bot/.venv" ]; then
    echo "✅ Python venv: Exists"
else
    echo "❌ Python venv: Missing (run setup.sh)"
fi

if [ -d "website/node_modules" ]; then
    echo "✅ Website dependencies: Installed"
else
    echo "❌ Website dependencies: Missing (run 'cd website && npm install')"
fi

if [ -f "bot/data/pokemon.db" ]; then
    DB_SIZE=$(du -h bot/data/pokemon.db | cut -f1)
    echo "✅ Database: Exists ($DB_SIZE)"
else
    echo "⚠️  Database: Not created yet (will be created on first run)"
fi

echo ""
echo "📊 Recent Logs (if available):"
echo "------------------------------"

if [ -f "logs/bot.log" ]; then
    echo "Bot (last 3 lines):"
    tail -3 logs/bot.log 2>/dev/null | sed 's/^/  /'
fi

if [ -f "logs/api.log" ]; then
    echo "API (last 3 lines):"
    tail -3 logs/api.log 2>/dev/null | sed 's/^/  /'
fi

echo ""
echo "💡 Quick Commands:"
echo "  Start (interactive): ./start-production.sh"
echo "  Start (daemon):      ./start-daemon.sh"
echo "  Stop all:            ./stop.sh"
echo "  Logs (bot):          tail -f logs/bot.log"
echo "  Logs (api):          tail -f logs/api.log"
echo "  Logs (website):      tail -f logs/website.log"
echo ""
