import sys
import socket
import http.server
import socketserver
import os

PORT = 8080
IP = socket.gethostbyname(socket.gethostname()) 

if len(sys.argv) == 2:
    PORT = int(sys.argv[1])

if __name__ == "__main__":
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f">> Serving on port : {PORT}")
    print(f">> Shared folder '{os.getcwd()}'")
    print(f">> Enter {IP}:{PORT} on any device's browser to access this folder!")
    httpd.serve_forever()

# pyinstaller --onefile --icon=youricon.ico filename.py
