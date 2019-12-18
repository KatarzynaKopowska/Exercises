import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("city", "country", "current_weather", "temperature", "pressure")
    )


class BasicWeatherApiClient:
    """Basic abstraction for services to handle serializing data from service
      and wrap them around data class.
    """
    data_class = None

    def get_weather(self, filter, value, api_key):
        """Get a container of API data from self.url."""
        pass


class CurrentWeatherApiClient(BasicWeatherApiClient):
    data_class = WeatherForecast

    def get_weather(self, filter=None, value=None, api_key=None):
        url = "http://api.openweathermap.org/data/2.5/weather?{}={}&APPID={}".format(filter, value, api_key)
        response = requests.get(url).json()
        data = {
            "city": response.get("name"),
            "country": response["sys"].get("country"),
            "current_weather": response["weather"][0].get("main"),
            "temperature": response["main"].get("temp"),
            "pressure": response["main"].get("pressure"),
        }

        return self.data_class(**data)
