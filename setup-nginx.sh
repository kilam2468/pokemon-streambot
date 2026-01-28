#!/bin/bash

# Nginx Setup Script for Pokemon Stream Bot
# Domain: poke.hfdn.dev

set -e

echo "🌐 Pokemon Stream Bot - Nginx Setup"
echo "===================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "⚠️  This script needs sudo privileges"
    echo "It will prompt for your password when needed"
    echo ""
fi

DOMAIN="poke.hfdn.dev"
NGINX_AVAILABLE="/etc/nginx/sites-available"
NGINX_ENABLED="/etc/nginx/sites-enabled"

# Check if nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "📦 Nginx not found. Installing..."
    sudo apt update
    sudo apt install -y nginx
    sudo systemctl enable nginx
    echo "✅ Nginx installed"
else
    echo "✅ Nginx is already installed"
fi

echo ""
echo "Which configuration do you want to use?"
echo "1) HTTP only (for testing)"
echo "2) HTTPS with Let's Encrypt (recommended for production)"
echo ""
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    # HTTP only setup
    echo ""
    echo "📝 Setting up HTTP-only configuration..."
    
    sudo cp nginx/poke.hfdn.dev-http-only.conf $NGINX_AVAILABLE/$DOMAIN
    
    # Create symlink if it doesn't exist
    if [ ! -L "$NGINX_ENABLED/$DOMAIN" ]; then
        sudo ln -s $NGINX_AVAILABLE/$DOMAIN $NGINX_ENABLED/$DOMAIN
    fi
    
    # Test configuration
    echo ""
    echo "🧪 Testing nginx configuration..."
    sudo nginx -t
    
    # Reload nginx
    echo "🔄 Reloading nginx..."
    sudo systemctl reload nginx
    
    echo ""
    echo "✅ HTTP configuration complete!"
    echo ""
    echo "🌍 Your site should be accessible at:"
    echo "   http://$DOMAIN"
    echo ""
    echo "⚠️  Remember to:"
    echo "   1. Update website/.env to use http://$DOMAIN"
    echo "   2. Restart services: ./start-production.sh"
    echo "   3. Set up SSL when ready (run this script again and choose option 2)"
    
elif [ "$choice" = "2" ]; then
    # HTTPS setup
    echo ""
    
    # Check if certbot is installed
    if ! command -v certbot &> /dev/null; then
        echo "📦 Certbot not found. Installing..."
        sudo apt update
        sudo apt install -y certbot python3-certbot-nginx
        echo "✅ Certbot installed"
    else
        echo "✅ Certbot is already installed"
    fi
    
    echo ""
    echo "🔐 Setting up SSL with Let's Encrypt..."
    echo ""
    echo "⚠️  Make sure:"
    echo "   - DNS A record for $DOMAIN points to this server's IP"
    echo "   - Ports 80 and 443 are open in firewall"
    echo ""
    read -p "Press Enter to continue or Ctrl+C to cancel..."
    
    # First, set up HTTP config for certbot validation
    sudo cp nginx/poke.hfdn.dev-http-only.conf $NGINX_AVAILABLE/$DOMAIN
    
    if [ ! -L "$NGINX_ENABLED/$DOMAIN" ]; then
        sudo ln -s $NGINX_AVAILABLE/$DOMAIN $NGINX_ENABLED/$DOMAIN
    fi
    
    sudo nginx -t
    sudo systemctl reload nginx
    
    # Get SSL certificate
    echo ""
    echo "📜 Obtaining SSL certificate..."
    sudo certbot --nginx -d $DOMAIN
    
    # Copy HTTPS config
    echo ""
    echo "📝 Installing HTTPS configuration..."
    sudo cp nginx/poke.hfdn.dev.conf $NGINX_AVAILABLE/$DOMAIN
    
    # Test and reload
    sudo nginx -t
    sudo systemctl reload nginx
    
    echo ""
    echo "✅ HTTPS configuration complete!"
    echo ""
    echo "🌍 Your site should be accessible at:"
    echo "   https://$DOMAIN"
    echo ""
    echo "⚠️  Remember to:"
    echo "   1. Update website/.env to use https://$DOMAIN"
    echo "   2. Rebuild website: cd website && npm run build"
    echo "   3. Restart services: ./start-production.sh"
    echo ""
    echo "🔄 SSL certificate will auto-renew"
    echo "   Test renewal: sudo certbot renew --dry-run"
    
else
    echo "❌ Invalid choice. Exiting."
    exit 1
fi

echo ""
echo "📚 For more details, see nginx/NGINX_SETUP.md"
