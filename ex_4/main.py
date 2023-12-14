from dotenv import load_dotenv
from ex_4.core.server import HTTPSuperServer, HTTPRequestHandler
from ex_4.core.router import HTTPRouter
from ex_4.core.soketServer import SocketServer
from .routes import use_routes
import concurrent.futures
import os

load_dotenv()

HTTP_HOST = os.getenv("HTTP_HOST")
HTTP_PORT = int(os.getenv("HTTP_PORT"))
UDP_HOST = os.getenv("UDP_HOST")
UDP_PORT = int(os.getenv("UDP_PORT"))

def start_http_server():
    router = HTTPRouter()
    server = HTTPSuperServer((HTTP_HOST, HTTP_PORT), HTTPRequestHandler, router)
    try: 
        use_routes(router)
        print(f'HTTP Server started: {HTTP_HOST}:{HTTP_PORT}')
        server.serve_forever()
    except KeyboardInterrupt:
        print('HTTP Server stoped')
        server.server_close()

def start_udp_server():
    server = SocketServer(UDP_HOST, int(UDP_PORT))
    server.start()

def main():
    try:
        tasks = [ start_http_server, start_udp_server ]
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(lambda task: task(), tasks)
    except KeyboardInterrupt:
        print("Interupted")

if __name__ == "__main__":
    main()