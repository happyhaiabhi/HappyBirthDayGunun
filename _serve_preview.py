#!/usr/bin/env python3
"""Preview server for the repo.

Root '/' redirects to Shristi's site (/shristi/index.html).
Gungun's original site stays reachable at /index.html.
All other paths serve repo files (shared media lives at repo root).
"""
import http.server
import os
import socketserver

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/shristi/index.html")
            self.end_headers()
            return
        super().do_GET()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
