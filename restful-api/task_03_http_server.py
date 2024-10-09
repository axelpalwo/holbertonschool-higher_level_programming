import http.server
import json

HOST = "localhost"
PORT = 8000

class NeuralHTTP(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(response_data)

            self.wfile.write(json_data.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {"version": "1.0", "description": "A simple API built with http.server"}
            json_data = json.dumps(response_data)

            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server = http.server.HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")
server.serve_forever()
server.server_close()