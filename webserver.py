#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8084

web_dir = os.path.join(os.path.dirname(__file__), 'camera-livestream')
os.chdir("camera-livestream")

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()