from core.server import server
from core.router import router
from routes import use_routes

if __name__ == "__main__":
    try:
        use_routes(router)
        print('Server starts')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server stoped')
        server.server_close()