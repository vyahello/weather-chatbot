from abc import ABC, abstractmethod
from typing import Any, Sequence


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def compose(self) -> str:
        pass


class CommonUrl(Url):
    """Gather url components together."""

    def __init__(self, *url_elements: Sequence[Any]) -> None:
        self._url: Sequence[Any] = url_elements

    def compose(self) -> str:
        return "".join(map(str, self._url))
