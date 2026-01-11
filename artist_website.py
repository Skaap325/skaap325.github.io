import http.server
import socketserver

PORT = 8000

# Make the server serve files from current folder (including images folder)
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Website running! Open http://localhost:{PORT}")
    httpd.serve_forever()
