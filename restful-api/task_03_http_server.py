#!/usr/bin/python3

import http.server
import json

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "name": "John", 
                "age": 30, 
                "city": "New York"
                }
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    print("Servidor corriendo en http://localhost:8000")
    httpd.serve_forever()
