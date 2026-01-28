# Nginx Setup for Pokemon Stream Bot

Complete guide to set up nginx reverse proxy for poke.hfdn.dev

## Prerequisites

1. Domain `poke.hfdn.dev` pointing to your Proxmox CT IP
2. Ports 80 and 443 open in firewall

## Step 1: Install Nginx

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# Start and enable nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Step 2: Initial HTTP Setup (Testing)

First, let's test with HTTP only:

```bash
# Copy HTTP-only config
sudo cp nginx/poke.hfdn.dev-http-only.conf /etc/nginx/sites-available/poke.hfdn.dev

# Create symlink
sudo ln -s /etc/nginx/sites-available/poke.hfdn.dev /etc/nginx/sites-enabled/

# Test nginx configuration
sudo nginx -t

# Reload nginx
sudo systemctl reload nginx
```

**Test:** Visit `http://poke.hfdn.dev` in your browser

## Step 3: SSL Setup with Let's Encrypt

### Install Certbot

```bash
# Ubuntu/Debian
sudo apt install certbot python3-certbot-nginx

# Or use snap (recommended)
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

### Option A: Automatic SSL Setup (Easiest)

```bash
# Let certbot modify nginx config automatically
sudo certbot --nginx -d poke.hfdn.dev
```

### Option B: Manual SSL Setup (More Control)

```bash
# Get certificate only
sudo certbot certonly --nginx -d poke.hfdn.dev

# Then replace config with HTTPS version
sudo cp nginx/poke.hfdn.dev.conf /etc/nginx/sites-available/poke.hfdn.dev

# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

### Auto-renewal

Certbot automatically sets up renewal. Test it:

```bash
sudo certbot renew --dry-run
```

## Step 4: Update Application Configuration

### Update Website Environment

Edit `website/.env`:

```env
VITE_API_URL=https://poke.hfdn.dev
```

### Update Bot Environment (if needed)

Edit `bot/.env` - no changes needed for basic setup.

### Rebuild Website

```bash
cd website
npm run build
cd ..
```

## Step 5: Restart Services

```bash
# Restart all services
./start-production.sh
```

## Firewall Configuration

### UFW (Ubuntu/Debian)

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'
sudo ufw enable
```

### Firewalld (RHEL/CentOS)

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### Proxmox Firewall

If using Proxmox firewall, allow:
- Port 80 (HTTP)
- Port 443 (HTTPS)

## URLs After Setup

| Service | URL |
|---------|-----|
| Website | https://poke.hfdn.dev |
| API | https://poke.hfdn.dev/api/ |
| OBS Overlay | https://poke.hfdn.dev/overlay |
| WebSocket | wss://poke.hfdn.dev/ws |

## OBS Browser Source

Update your OBS Browser Source:
- URL: `https://poke.hfdn.dev/overlay`
- Width: 1920
- Height: 1080

## Nginx Commands

```bash
# Test configuration
sudo nginx -t

# Reload (keeps connections alive)
sudo systemctl reload nginx

# Restart (drops connections)
sudo systemctl restart nginx

# View logs
sudo tail -f /var/log/nginx/poke.hfdn.dev.access.log
sudo tail -f /var/log/nginx/poke.hfdn.dev.error.log

# Check status
sudo systemctl status nginx
```

## Troubleshooting

### Site not loading

```bash
# Check nginx status
sudo systemctl status nginx

# Check nginx logs
sudo tail -f /var/log/nginx/error.log

# Check if services are running
./status.sh
```

### SSL certificate issues

```bash
# Check certificate
sudo certbot certificates

# Renew certificate
sudo certbot renew

# Test renewal
sudo certbot renew --dry-run
```

### WebSocket not connecting

1. Check nginx config has proper WebSocket headers
2. Verify port 8001 is open and bot is running
3. Check browser console for WebSocket errors

### 502 Bad Gateway

This means nginx can't reach your backend services:

```bash
# Check if services are running
./status.sh

# Check specific ports
sudo netstat -tlnp | grep -E '4173|8000|8001'

# Check logs
tail -f logs/bot.log
tail -f logs/api.log
```

## Security Best Practices

### 1. Restrict API access (optional)

In nginx config, add IP whitelist:

```nginx
location /api/ {
    # Only allow specific IPs
    allow 192.168.1.0/24;
    deny all;
    
    proxy_pass http://localhost:8000/api/;
    # ... rest of config
}
```

### 2. Rate limiting

Add to nginx config:

```nginx
# In http block
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

# In location /api/
limit_req zone=api burst=20;
```

### 3. Fail2ban (optional)

Protect against brute force:

```bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
```

### 4. Regular updates

```bash
sudo apt update && sudo apt upgrade
sudo certbot renew
```

## Performance Tuning

### Enable Gzip compression

Already included in main config, but verify:

```nginx
# In http block
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
gzip_comp_level 6;
```

### Enable caching

For static assets:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

## Monitoring

### Check nginx status

```bash
curl https://poke.hfdn.dev/health
```

### Monitor logs

```bash
# Access logs
sudo tail -f /var/log/nginx/poke.hfdn.dev.access.log

# Error logs
sudo tail -f /var/log/nginx/poke.hfdn.dev.error.log

# Application logs
tail -f logs/bot.log
tail -f logs/api.log
```

## Backup

Important nginx files to backup:

```bash
# Backup nginx config
sudo cp /etc/nginx/sites-available/poke.hfdn.dev ~/nginx-backup.conf

# Backup SSL certificates (done automatically by certbot)
# Located in: /etc/letsencrypt/
```

## Updating Configuration

After making changes to nginx config:

```bash
# Edit config
sudo nano /etc/nginx/sites-available/poke.hfdn.dev

# Test
sudo nginx -t

# Reload
sudo systemctl reload nginx
```
