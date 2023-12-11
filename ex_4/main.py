from ex_4.core.server import server
from ex_4.core.router import router
from routes import use_routes

if __name__ == "__main__":
    try:
        use_routes(router)
        print('Server started')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server stoped')
        server.server_close()