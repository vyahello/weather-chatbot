from abc import ABC, abstractmethod
from typing import Dict
from chat.forecast import WEATHER_ID
from chat.web.requests import Request, SafeBotRequest
from chat.web.urls import CommonUrl


class Weather(ABC):
    """Abstraction of a weather."""

    @abstractmethod
    def data_records(self) -> Dict[str, str]:
        pass


class OpenWeatherMap(Weather):
    """Concrete weather object."""

    def __init__(self, city: str) -> None:
        self._req: Request = SafeBotRequest(
            CommonUrl("http://api.openweathermap.org/data/2.5/weather?q=", city, "&units=metric&appid=", WEATHER_ID)
        )

    def data_records(self) -> Dict[str, str]:
        return self._req.get().json()
