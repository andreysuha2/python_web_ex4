from collections.abc import Callable
from socketserver import BaseRequestHandler, BaseServer
from typing import Any
from ex_4.core.router import HTTPRouter, HTTPMethods, RouterNotFoundException
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import urllib.parse

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server: BaseServer, router: HTTPRouter) -> None:
        self.router = router
        super().__init__(request, client_address, server)

    def _handle_request(self, method = HTTPMethods):
        parsed_url = urllib.parse.urlparse(self.path)
        try:
            self.router.use_route(method, parsed_url.path, self)
        except RouterNotFoundException:
            self.send_html_file("error404.html")

    def do_GET(self):
        self._handle_request(HTTPMethods.GET)

    def do_POST(self):
        self._handle_request(HTTPMethods.POST)

    def do_PUT(self):
        self._handle_request(HTTPMethods.PUT)

    def do_DELETE(self):
        self._handle_request(HTTPMethods.DELETE)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(f"ex_4/templates/{filename}", 'rb') as fd:
            self.wfile.write(fd.read())
    
class HTTPSuperServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, router: HTTPRouter, bind_and_activate: bool = True) -> None:
        self.router = router
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)

    def finish_request(self, request, client_address) -> None:
        self.RequestHandlerClass(request, client_address, self, self.router)

