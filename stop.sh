#!/bin/bash

# Stop all Pokemon Stream Bot services

PIDFILE="logs/services.pid"

echo "🛑 Stopping Pokemon Stream Bot services..."
echo "=========================================="

if [ ! -f "$PIDFILE" ]; then
    echo "⚠️  No PID file found. Searching for running processes..."
    
    # Try to find and kill processes anyway
    pkill -f "python main.py" 2>/dev/null && echo "✓ Stopped bot"
    pkill -f "uvicorn api:app" 2>/dev/null && echo "✓ Stopped API"
    pkill -f "vite preview" 2>/dev/null && echo "✓ Stopped website"
    
    echo ""
    echo "Done. Run ./status.sh to verify."
    exit 0
fi

# Read PIDs from file
PIDS=$(cat "$PIDFILE")

# Kill each process
for PID in $PIDS; do
    if kill -0 $PID 2>/dev/null; then
        kill $PID 2>/dev/null && echo "✓ Stopped process $PID"
    else
        echo "⚠ Process $PID not running"
    fi
done

# Also kill by process name as backup
pkill -f "python main.py" 2>/dev/null
pkill -f "uvicorn api:app" 2>/dev/null
pkill -f "vite preview" 2>/dev/null

# Remove PID file
rm -f "$PIDFILE"

echo ""
echo "✅ All services stopped!"
echo "   Run ./status.sh to verify"
echo ""
