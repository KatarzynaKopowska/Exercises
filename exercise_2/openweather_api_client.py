import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("weather_forecast_type", "city", "country", "current_weather", "temperature", "pressure")
    )


class BasicWeatherApiClient:
    """
    """
    data_class = None

    def get_weather(self, filter, value, api_key):
        """Get a container of API data from self.url."""
        pass


class CurrentWeatherApiClient(BasicWeatherApiClient):
    data_class = WeatherForecast

    def get_weather(self, filter, value, api_key):
        url = "http://api.openweathermap.org/data/2.5/weather?{}={}&APPID={}".format(filter, value, api_key)
        weather_information = requests.get(url).json()
        data = {
            "weather_forecast_type": "Current weather",
            "city": weather_information.get("name"),
            "country": weather_information["sys"].get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)


class FiveDayForecastApiClient(BasicWeatherApiClient):
    data_class = WeatherForecast

    def get_weather(self, filter, value, api_key):
        url = "http://api.openweathermap.org/data/2.5/forecast?{}={}&APPID={}".format(filter, value, api_key)

        city_information = requests.get(url).json()["city"]
        weather_information = requests.get(url).json()["list"][0]
        data = {
            "weather_forecast_type": "5 days forecast",
            "city": city_information.get("name"),
            "country": city_information.get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)


class WeatherForecastManager:
    weather_forecast_classes = [CurrentWeatherApiClient, FiveDayForecastApiClient]

    def __init__(self):
        self.weather_forecast = []

    def run(self, filter=None, value=None, api_key=None):
        for weather_forecast_class in self.weather_forecast_classes:
            weather_api_client = weather_forecast_class()
            weather = weather_api_client.get_weather(filter, value, api_key)
            self.weather_forecast.append(weather)
        return self.weather_forecast




