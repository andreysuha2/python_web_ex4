from ex_4.core.server import HTTPRequestHandler

class MainController:
    def index(self, request: HTTPRequestHandler):
        request.send_html_file("index.html")

main_controller = MainController()