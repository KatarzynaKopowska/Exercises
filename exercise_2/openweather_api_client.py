import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("weather_forecast_type", "city", "country", "current_weather", "temperature", "pressure")
    )


class OpenWeatherAPIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

    @property
    def current_weather(self):
        return CurrentWeather(self.api_key)

    @property
    def five_day_forecast(self):
        return FiveDayForecast(self.api_key)


class BaseEndpoint:
    base_url = None
    data_class = None

    def __init__(self, api_key=None):
        self.api_key = api_key

    def get(self, **kwargs):
        raise NotImplementedError


class CurrentWeather(BaseEndpoint):
    base_url = "http://api.openweathermap.org/data/2.5"
    data_class = WeatherForecast

    def get(self, **kwargs):
        url = "{}/weather?{}={}&APPID={}".format(
            self.base_url, kwargs, kwargs, self.api_key
        )
        weather_information = requests.get(url, params=kwargs).json()

        data = {
            "weather_forecast_type": "Current weather",
            "city": weather_information.get("name"),
            "country": weather_information["sys"].get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)


class FiveDayForecast(BaseEndpoint):
    base_url = "http://api.openweathermap.org/data/2.5"
    data_class = WeatherForecast

    def get(self, **kwargs):
        url = "{}/forecast?{}={}&APPID={}".format(
            self.base_url, kwargs, kwargs, self.api_key
        )

        city_information = requests.get(url, params=kwargs).json()["city"]
        weather_information = requests.get(url, params=kwargs).json()["list"][0]
        data = {
            "weather_forecast_type": "Five day forecast",
            "city": city_information.get("name"),
            "country": city_information.get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)
