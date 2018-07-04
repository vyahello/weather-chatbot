from abc import ABC, abstractmethod
from typing import Dict, Any


class EmptyDict(ABC):
    """Abstraction of an empty dictionary."""

    @abstractmethod
    def get(self, value: str) -> str:
        pass


class EmptyDictOf(EmptyDict):
    """Represent empty dictionary."""

    def __init__(self, dct: Dict[Any, Any]) -> None:
        self._dct: Dict[Any, Any] = dct

    def get(self, value: str) -> str:
        try:
            return self._dct.get(value)
        except AttributeError:
            return ''
