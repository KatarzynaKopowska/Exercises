import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("city", "country", "current_weather", "temperature", "pressure")
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


class HourlytWeatherApiClient(BasicWeatherApiClient):
    data_class = WeatherForecast

    def get_weather(self, filter=None, value=None, api_key=None):
        url = "http://api.openweathermap.org/data/2.5/forecast?{}={}&APPID={}".format(filter, value, api_key)

        city_information = requests.get(url).json()["city"]
        weather_information = requests.get(url).json()["list"][0]
        data = {
            "city": city_information.get("name"),
            "country": city_information.get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
             "temperature": weather_information["main"].get("temp"),
             "pressure": weather_information["main"].get("pressure"),
        }
        print(data)
        return self.data_class(**data)
