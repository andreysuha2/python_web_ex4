from ex_4.core.server import HTTPRequestHandler
import json
import socket
import urllib.parse
import os 

class MainController:    
    def index(self, request: HTTPRequestHandler):
        request.send_html_file("index.html")

    def message(self, request: HTTPRequestHandler):
        request.send_html_file("message.html")
        
    def message_handler(self, request: HTTPRequestHandler):
        data = request.rfile.read(int(request.headers['Content-Length']))
        print(data)
        data_parse = urllib.parse.unquote_plus(data.decode())
        print(data_parse)
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        print(data_dict)
        self.send_message(data_dict)
        request.send_response(302)
        request.send_header('Location', '/')
        request.end_headers()

    def send_message(self, message):
        data = json.dumps(message).encode('utf-8')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (os.getenv("UDP_HOST"), int(os.getenv("UDP_PORT")))
        sock.sendto(data, server_address)
        response, address = sock.recvfrom(1024)
        print(f'Response data: {response.decode()} from address: {address}')
        sock.close()


main_controller = MainController()