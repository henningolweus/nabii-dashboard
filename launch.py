"""
Quick launch script for NABII Impact Investment Dashboard
Opens the dashboard in the default web browser
"""

import http.server
import socketserver
import webbrowser
import os
from threading import Timer

PORT = 8000

def open_browser():
    """Open the dashboard in the default browser"""
    webbrowser.open(f'http://localhost:{PORT}/index.html')

# Change to the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set up the server
Handler = http.server.SimpleHTTPRequestHandler

print("=" * 60)
print("  NABII - Zambia Impact Investment Dashboard")
print("=" * 60)
print(f"\nStarting server on http://localhost:{PORT}")
print(f"Opening dashboard in your browser...")
print(f"\nDashboard will be available at:")
print(f"   Main Dashboard: http://localhost:{PORT}/index.html")
print(f"   Geographic Map: http://localhost:{PORT}/map.html")
print(f"\nPress Ctrl+C to stop the server\n")
print("=" * 60)

# Open browser after 1.5 seconds
Timer(1.5, open_browser).start()

# Start the server
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\nShutting down server... Thanks for using NABII Dashboard!")
    print("=" * 60)
