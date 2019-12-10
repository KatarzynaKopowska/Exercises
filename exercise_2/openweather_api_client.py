import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("city", "country", "current_weather", "temperature", "pressure")
    )


class BasicWeatherApiClient:
    """Basic abstraction for services to handle serializing data from service
      and wrap them around data class.
    """

    city = None
    url = None
    data_class = None

    def get_weather(self):
        """Get a container of API data from self.url."""
        pass

    def parse_weather(self, data):
        """Parse single API data structure into self.data_class."""
        pass


class OpenWeatherApi(BasicWeatherApiClient):
    city = "wisla"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=bfc7d01991d939f6c91a824036ffcd34".format(city)
    data_class = WeatherForecast

    def get_weather(self):
        response = requests.get(self.url).json()
        return response

    def parse_weather(self, weather):
        data = {
            "city": weather.get("name"),
            "country": weather["sys"].get("country"),
            "current_weather": weather["weather"][0].get("main"),
            "temperature": weather["main"].get("temp"),
            "pressure": weather["main"].get("pressure"),
        }
        return self.data_class(**data)
