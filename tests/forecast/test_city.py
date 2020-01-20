from typing import Dict, Any
import pytest
from chat.forecast.city import City, CityWeather, CityWeatherSummary


_weather_data: Dict[str, Any] = {
    "weather": [{"description": "cloudy"}],
    "main": {"temp": 17.1},
    "sys": {"country": "Ukraine"},
    "name": "Lviv",
}


@pytest.fixture(scope="module")
def city_weather() -> City:
    return CityWeather(_weather_data)


def test_city_description(city_weather: City) -> None:
    assert city_weather.description() == "cloudy"


def test_city_temp(city_weather: City) -> None:
    assert city_weather.temp() == 17.1


def test_city_country(city_weather: City) -> None:
    assert city_weather.country() == "Ukraine"


def test_city_name(city_weather: City) -> None:
    assert city_weather.name() == "Lviv"


def test_city_summary() -> None:
    assert CityWeatherSummary(_weather_data).get() == {
        "description": "cloudy",
        "temperature": 17.1,
        "country": "Ukraine",
        "name": "Lviv",
    }
