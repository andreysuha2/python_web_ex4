from enum import Enum
from collections.abc import Callable
from http.server import BaseHTTPRequestHandler

class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

class RouterNotFoundException(Exception):
    pass

class RouteAlreadyRegistred(Exception):
    pass

class HTTPRouter():
    __router = None

    def __new__(cls):
        if cls.__router is None:
            cls.__router = super().__new__(HTTPRouter)
        return cls.__router

    def __init__(self):
        self.__routes = {}

    def __str__(self) -> str:
        return ", ".join(list(self.__routes.keys()))

    def use_route(self, method: HTTPMethods, path: str, request_handler: BaseHTTPRequestHandler):
        handler = self.__routes.get((method, path), None)
        if handler is None:
            raise RouterNotFoundException
        else:
            handler(request_handler)

    def route(self, method: HTTPMethods, path: str, handler: Callable):
        if (method, path) in self.__routes:
            raise RouteAlreadyRegistred
        self.__routes[(method, path)] = handler
        
    def get(self, path: str, handler: Callable):
        self.route(HTTPMethods.GET, path, handler)

    def post(self, path: str, handler: Callable):
        self.route(HTTPMethods.POST, path, handler)

    def put(self, path: str, handler: Callable):
        self.route(HTTPMethods.POST, path, handler)

    def delete(self, path: str, handler: Callable):
        self.route(HTTPMethods.DELETE, path, handler)

router = HTTPRouter()