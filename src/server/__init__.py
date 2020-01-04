# flake8: noqa
from src.server.core import Server, WebServer
from src.server.requests import Request, ServerRequest

server: Server = WebServer()

from . import routes
