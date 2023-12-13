from ex_4.core.server import HTTPRequestHandler

class MainController:
    def index(self, request: HTTPRequestHandler):
        request.send_html_file("index.html")

    def message(self, request: HTTPRequestHandler):
        request.send_html_file("message.html")

main_controller = MainController()