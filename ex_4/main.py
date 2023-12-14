from dotenv import load_dotenv
from ex_4.core.server import HTTPSuperServer, HTTPRequestHandler
from ex_4.core.router import HTTPRouter
from .routes import use_routes
import os

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def main():
    router = HTTPRouter()
    server = HTTPSuperServer((HOST, int(PORT)), HTTPRequestHandler, router)
    try: 
        use_routes(router)
        print(f'Server started: {HOST}:{PORT}')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server stoped')
        server.server_close()

if __name__ == "__main__":
    main()