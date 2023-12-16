from socketserver import BaseServer
from ex_4.core.router import HTTPRouter, HTTPMethods, RouterNotFoundException
from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader
from ex_4.definitions import ROOT_DIR
import pathlib
import mimetypes
import urllib.parse
import os


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server: BaseServer, router: HTTPRouter) -> None:
        self.router = router
        self.frontend_path = f'{ROOT_DIR}/{os.getenv("FRONTEND_PATH")}'
        self.staic_path = f'{self.frontend_path}/static'
        self.env = Environment(loader=FileSystemLoader(self.frontend_path))
        super().__init__(request, client_address, server)

    def _handle_request(self, method = HTTPMethods):
        parsed_url = urllib.parse.urlparse(self.path)
        try:
            self.router.use_route(method, parsed_url.path, self)
        except RouterNotFoundException:
            if pathlib.Path().joinpath(f'{self.staic_path}/{parsed_url.path}').exists():
                self._send_static()
            else:
                self.send_html_file("error404.html", 404)
            
            
    def _send_static(self):
        try:
            self.send_response(200)
            mt = mimetypes.guess_type(self.path)
            if mt:
                self.send_header("Content-type", mt[0])
            else:
                self.send_header("Content-type", "text/plain")
            self.end_headers()
            with open(f'{self.staic_path}/{self.path}', 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_response(404)

    def do_GET(self):
        self._handle_request(HTTPMethods.GET)

    def do_POST(self):
        self._handle_request(HTTPMethods.POST)

    def do_PUT(self):
        self._handle_request(HTTPMethods.PUT)

    def do_DELETE(self):
        self._handle_request(HTTPMethods.DELETE)

    def send_html_file(self, filename, status=200, *args, **kwargs):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        template = self.env.get_template(f"templates/{filename}")
        content = template.render(*args, **kwargs)
        self.wfile.write(content.encode("utf-8"))
    
class HTTPSuperServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, router: HTTPRouter, bind_and_activate: bool = True) -> None:
        self.router = router
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)

    def finish_request(self, request, client_address) -> None:
        self.RequestHandlerClass(request, client_address, self, self.router)

