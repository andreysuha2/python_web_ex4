from ex_4.core.server import HTTPRequestHandler
import urllib.parse

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
        request.send_response(302)
        request.send_header('Location', '/')
        request.end_headers()

main_controller = MainController()