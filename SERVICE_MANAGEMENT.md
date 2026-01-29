# Service Management Guide

## The Problem

Your services were being terminated because the `start-production.sh` script was exiting, which triggered the cleanup function that kills all child processes. This happened because:

1. **Terminal Dependency**: When you close the terminal or SSH session, the script receives SIGHUP and terminates
2. **Process Wait**: The script uses `wait` which completes when any background process exits
3. **Cleanup Trap**: The cleanup function was trapping both SIGINT and SIGTERM, causing premature shutdowns

## The Solutions

### Option 1: Interactive Mode (Updated)
```bash
./start-production.sh
```

**Changes Made:**
- Removed SIGTERM from the trap (only traps SIGINT/Ctrl+C now)
- Keeps terminal attached so you can see live output
- Gracefully stops all services when you press Ctrl+C

**Use When:**
- Testing or debugging
- You want to see live logs
- You're actively monitoring the system

### Option 2: Daemon Mode (New - Recommended)
```bash
./start-daemon.sh
```

**Features:**
- Runs completely in background using `nohup`
- Survives terminal/SSH disconnection
- Saves PIDs to `logs/services.pid`
- Services continue running even after you logout

**Use When:**
- Production deployment
- You need persistent services
- Running on a remote server

## Management Commands

### Check Status
```bash
./status.sh
```
Shows:
- Running services with PIDs
- Open ports (8000, 8001, 4173)
- File checks (.env, venv, dependencies)
- Recent log entries
- Quick command references

### Stop All Services
```bash
./stop.sh
```
- Reads PIDs from file
- Gracefully terminates all services
- Falls back to pkill if needed
- Cleans up PID file

### View Logs
```bash
# Real-time logs
tail -f logs/bot.log
tail -f logs/api.log
tail -f logs/website.log

# All logs together
tail -f logs/*.log

# Last 50 lines
tail -50 logs/bot.log
```

## Service Details

### Bot (main.py)
- **Port**: 8001 (WebSocket)
- **Log**: `logs/bot.log`
- **PID**: First line in `logs/services.pid`

### API Server (uvicorn)
- **Port**: 8000 (HTTP/REST)
- **Log**: `logs/api.log`
- **PID**: Second line in `logs/services.pid`

### Website (Vite)
- **Port**: 4173 (Production preview)
- **Log**: `logs/website.log`
- **PID**: Third line in `logs/services.pid`

## Troubleshooting

### Services Keep Stopping
**Symptom**: Services start but stop after a while

**Causes**:
1. Application error/crash (check logs)
2. Port conflict (another service using 8000/8001/4173)
3. Memory/resource issues
4. SSH connection dropped (use daemon mode)

**Solution**:
```bash
# Check what's wrong
./status.sh
tail -50 logs/bot.log
tail -50 logs/api.log

# Use daemon mode instead
./stop.sh
./start-daemon.sh
```

### Can't Connect to Services
**Symptom**: Services running but can't access from browser

**Check**:
```bash
# Verify ports are open
netstat -tuln | grep -E "8000|8001|4173"

# Check firewall (if applicable)
sudo ufw status

# Test locally
curl http://localhost:8000/api/pokemon
```

### Database Issues
**Symptom**: "Database not created yet" in status

**Solution**: Database is created automatically on first run. Just use the bot once and it will initialize.

## Best Practices

### For Development
1. Use interactive mode: `./start-production.sh`
2. Keep terminal open
3. Use Ctrl+C to stop cleanly
4. Check logs frequently

### For Production
1. Use daemon mode: `./start-daemon.sh`
2. Set up monitoring (check status every 5-10 minutes)
3. Implement log rotation
4. Consider systemd service (see SYSTEMD.md)

### For Remote Servers
1. **Always use daemon mode** or screen/tmux
2. Set up automatic startup (cron @reboot or systemd)
3. Monitor logs remotely
4. Set up alerts for service failures

## Example Workflows

### Starting Fresh
```bash
./stop.sh                  # Stop any running services
./start-daemon.sh          # Start in background
./status.sh                # Verify everything is running
tail -f logs/bot.log       # Monitor logs
```

### Restarting After Changes
```bash
./stop.sh                  # Stop all services
# Make your code changes
./start-daemon.sh          # Start again
./status.sh                # Verify
```

### Debugging Issues
```bash
./stop.sh                  # Stop daemon mode
./start-production.sh      # Start in interactive mode
# Watch output in terminal
# Press Ctrl+C when done
```

## Log Files Explained

### service.log
Records the main script output (start/stop events)

### service-error.log
Captures script-level errors (usually just "Terminated" messages)

### bot.log
Twitch bot activity:
- Connection to Twitch
- Chat messages
- Commands processed
- Pokemon spawns
- WebSocket events

### api.log
API server requests:
- HTTP requests
- Endpoint hits
- Startup/shutdown
- Errors

### website.log
Vite preview server output

### build.log
Website build process (npm run build)

## Quick Reference Card

```
┌─────────────────────────────────────────┐
│ Pokemon Stream Bot - Quick Reference    │
├─────────────────────────────────────────┤
│ START (interactive):  ./start-production.sh
│ START (background):   ./start-daemon.sh
│ STOP all services:    ./stop.sh
│ CHECK status:         ./status.sh
│                                          │
│ LOGS:                                    │
│   Bot:     tail -f logs/bot.log         │
│   API:     tail -f logs/api.log         │
│   Website: tail -f logs/website.log     │
│   All:     tail -f logs/*.log           │
│                                          │
│ PORTS:                                   │
│   8000 - API Server                      │
│   8001 - WebSocket (Bot)                 │
│   4173 - Website                         │
└─────────────────────────────────────────┘
```
