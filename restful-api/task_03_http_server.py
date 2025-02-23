#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    #  Este metod se llama cada vez que recibe un request
    def do_GET(self):
        if self.path == "/":
            #  Código 200, está todo bien
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            #  Esta info la vamos a enviar
            data = {
                "name": "John",
                "age": "30",
                "city": "New York"
            }
            #  Con json.dumps convertimos el dicc a una string en formato JSON
            json_data = json.dumps(data).encode("utf-8")
            self.send_response(200)
            #  Indica el contenido de la respuesta es JSON
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.end_headers()
            self.wfile.write(json_data)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
    
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor HTTP corriendo en el puerto {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
