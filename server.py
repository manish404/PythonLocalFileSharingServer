import sys
import http.server
import socketserver

PORT = 8080

if len(sys.argv) == 2:
    PORT = int(sys.argv[1])

if __name__ == "__main__":
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f"Serving on port : {PORT}")
    httpd.serve_forever()

# pyinstaller --onefile --icon=youricon.ico filename.py
