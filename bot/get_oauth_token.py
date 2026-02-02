#!/usr/bin/env python3
"""
Helper script to generate Twitch OAuth token using Client ID and Secret
"""

import webbrowser
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

# Configuration
CLIENT_ID = input("Enter your Twitch Client ID: ").strip()
REDIRECT_URI = "http://localhost:3000"
SCOPES = ["chat:read", "chat:edit", "channel:read:subscriptions", "moderator:read:chatters"]

# Global to store the token
oauth_token = None

class OAuthHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler to capture OAuth redirect"""
    
    def do_GET(self):
        global oauth_token
        
        # Parse the URL
        if '#access_token=' in self.path:
            # Extract token from fragment (JavaScript would normally handle this)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Send HTML page that extracts token from URL fragment
            html = """
            <html>
            <head><title>Twitch OAuth</title></head>
            <body>
                <h1>Processing OAuth Token...</h1>
                <script>
                    // Extract token from URL fragment
                    const hash = window.location.hash.substring(1);
                    const params = new URLSearchParams(hash);
                    const token = params.get('access_token');
                    
                    if (token) {
                        // Send token to Python server
                        fetch('/token?access_token=' + token)
                            .then(() => {
                                document.body.innerHTML = '<h1 style="color: green;">✓ Success!</h1><p>Token captured. You can close this window.</p>';
                            });
                    } else {
                        document.body.innerHTML = '<h1 style="color: red;">✗ Error</h1><p>No token found in URL.</p>';
                    }
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        
        elif '/token' in self.path:
            # Receive token from JavaScript
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            
            if 'access_token' in params:
                oauth_token = params['access_token'][0]
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'OK')
            else:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress log messages
        pass

def main():
    print("\n🎮 Twitch OAuth Token Generator")
    print("=" * 50)
    
    if not CLIENT_ID:
        print("❌ Error: Client ID is required")
        sys.exit(1)
    
    # Build authorization URL
    scope_string = "+".join(SCOPES)
    auth_url = (
        f"https://id.twitch.tv/oauth2/authorize?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={urllib.parse.quote(REDIRECT_URI)}&"
        f"response_type=token&"
        f"scope={scope_string}"
    )
    
    print(f"\n1. Starting local server on port 3000...")
    try:
        server = HTTPServer(('localhost', 3000), OAuthHandler)
    except OSError as e:
        if "Address already in use" in str(e):
            print("❌ Error: Port 3000 is already in use!")
            print("   Kill the process using port 3000 or use a different port.")
            print("   Run: lsof -ti:3000 | xargs kill -9")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)
    
    print(f"   ✓ Server running on http://localhost:3000")
    
    print(f"\n2. Opening browser for authorization...")
    print(f"\n   If browser doesn't open, visit this URL:")
    print(f"   {auth_url}\n")
    
    import threading
    import time
    
    # Start server in background thread
    server_thread = threading.Thread(target=lambda: server.serve_forever())
    server_thread.daemon = True
    server_thread.start()
    
    # Wait a moment for server to be ready
    time.sleep(0.5)
    
    # Now open browser
    webbrowser.open(auth_url)
    
    print("3. Waiting for authorization...")
    print("   (Authorize in the browser window that opened)\n")
    
    # Wait for token with timeout
    timeout = 120  # 2 minutes
    start_time = time.time()
    while oauth_token is None:
        if time.time() - start_time > timeout:
            print("\n⏱️  Timeout waiting for authorization.")
            print("\nIf you see the token in your browser URL, extract it manually:")
            print("Look for: http://localhost:3000/#access_token=YOUR_TOKEN")
            print("Your token is the part after 'access_token=' and before '&'")
            server.shutdown()
            sys.exit(1)
        time.sleep(0.1)
    
    server.shutdown()
    
    print("\n✅ Token received successfully!\n")
    print("=" * 50)
    print(f"\nYour OAuth Token:")
    print(f"oauth:{oauth_token}")
    print("\n" + "=" * 50)
    print("\nAdd this to your .env file:")
    print(f"TWITCH_BOT_TOKEN=oauth:{oauth_token}")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
