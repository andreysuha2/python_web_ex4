from ex_4.core.router import router, HTTPMethods, RouterNotFoundException
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        try:
            router.use_route(HTTPMethods.GET, parsed_url.path, self)
        except RouterNotFoundException:
            self.send_html_file("error404.html")

    def do_POST(self, method: HTTPMethods = HTTPMethods.POST):
        parsed_url = urllib.parse.urlparse(self.path)
        try:
            router.use_route(method, parsed_url.path, self)
        except RouterNotFoundException:
            self.send_html_file("error404.html", 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(f"ex_4/templates/{filename}", 'rb') as fd:
            self.wfile.write(fd.read())
    
    def do_PUT(self):
        self.do_POST(HTTPMethods.PUT)

    def do_DELETE(self):
        self.do_POST(HTTPMethods.DELETE)

server = HTTPServer(("localhost", 8080), HTTPRequestHandler)
