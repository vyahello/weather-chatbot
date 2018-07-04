from abc import ABC, abstractmethod
from typing import Dict, Any


class City(ABC):
    """Abstraction of a city weather data records."""

    @abstractmethod
    def summary(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def temp(self) -> float:
        pass

    @abstractmethod
    def country(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class CityWeather(City):
    """Some city weather data records."""

    def __init__(self, weather_data: Dict[Any, Any]) -> None:
        self._weather_data: Dict[Any, Any] = weather_data

    @property
    def description(self) -> str:
        return self._weather_data.get('weather')[0].get('description')

    @property
    def temp(self) -> float:
        return self._weather_data.get('main').get('temp')

    @property
    def country(self) -> str:
        return self._weather_data.get('sys').get('country')

    @property
    def name(self) -> str:
        return self._weather_data.get('name')

    def summary(self) -> Dict[str, Any]:
        return dict(description=self.description, temperature=self.temp, country=self.country, name=self.name)
