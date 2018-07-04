from typing import Tuple
from bin.server.core import Server, WebServer
from bin.server.requests import Request, ServerRequest

SERVER: Server = WebServer()
WELCOME_MESSAGE: str = '<h1>Weather bot server powered by flask micro-web framework. Core is written by V.Yahello</h1>'
METHODS: Tuple[str, ...] = ('POST', 'GET')
POST = 'POST'

from . import routes
