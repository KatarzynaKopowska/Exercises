from openweather_api_client import OpenWeatherAPIClient

import pytest
import requests


@pytest.fixture
def open_weather_APIClient_object():
    open_weather_client = OpenWeatherAPIClient()
    return open_weather_client

def test_OpenWeatherAPIClient(open_weather_APIClient_object):
    assert open_weather_APIClient_object.current_weather.__name__ == "CurrentWeather"


test_OpenWeatherAPIClient(OpenWeatherAPIClient)


@pytest.fixture
def patched_requests(monkeypatch):
    old_get_method = requests.get

    def mock_get(*args, **kwargs):
        pass
