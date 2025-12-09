from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"   # IMPORTANT: allows connections from anywhere
port = 3000        # You can change this if you want

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server running on port {port}...")
server.serve_forever()
