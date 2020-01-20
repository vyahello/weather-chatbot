from abc import ABC, ABCMeta, abstractmethod
from typing import Dict, Any
import requests
from chat.web.responses import Response, BotResponse
from chat.web.urls import Url


class Session(ABC):
    """Abstract interfaces for API Session."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self, data: Dict[Any, Any]) -> Response:
        pass


class BotSession(Session):
    """Provide interfaces for bot api session."""

    def __init__(self, url: Url) -> None:
        self._api: requests.Session = requests.Session()
        self._url: Url = url

    def get(self) -> Response:
        return BotResponse(self._api.get(self._url.compose()))

    def post(self, data: Dict[Any, Any]) -> Response:
        return BotResponse(self._api.post(self._url.compose(), json=data))
