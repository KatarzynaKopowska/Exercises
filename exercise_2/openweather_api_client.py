import requests
import collections


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("weather_forecast_type", "city", "country", "current_weather", "temperature", "pressure")
    )


class OpenWeatherAPIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.current_weather = CurrentWeather(api_key)
        self.five_day_forecast = FiveDayForecast(api_key)


class CurrentWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.data_class = WeatherForecast

    def get(self, **kwargs):
        parameters = [(identification_type, value) for identification_type, value in kwargs.items()][0]
        url = "http://api.openweathermap.org/data/2.5/weather?{}={}&APPID={}".format(
            parameters[0], parameters[1], self.api_key
        )
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


class FiveDayForecast:
    def __init__(self, api_key):
        self.api_key = api_key
        self.data_class = WeatherForecast

    def get(self, **kwargs):
        parameters = [(identification_type, value) for identification_type, value in kwargs.items()][0]
        url = "http://api.openweathermap.org/data/2.5/forecast?{}={}&APPID={}".format(
            parameters[0], parameters[1], self.api_key
        )

        city_information = requests.get(url).json()["city"]
        weather_information = requests.get(url).json()["list"][0]
        data = {
            "weather_forecast_type": "Five day forecast",
            "city": city_information.get("name"),
            "country": city_information.get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)
