# flake8: noqa
from chat.server.core import Server, WebServer
from chat.server.requests import Request, ServerRequest

server: Server = WebServer()

from . import routes
