import requests
import collections
import config


WeatherForecast = collections.namedtuple(
    "WeatherForecast", ("city", "country", "current_weather", "temperature", "pressure")
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
            "city": city_information.get("name"),
            "country": city_information.get("country"),
            "current_weather": weather_information["weather"][0].get("main"),
            "temperature": weather_information["main"].get("temp"),
            "pressure": weather_information["main"].get("pressure"),
        }
        return self.data_class(**data)


openweather_client = OpenWeatherAPIClient(api_key=config.OPENWEATHER_API_KEY)
current = openweather_client.current_weather.get(zip=94040)
five_day = openweather_client.five_day_forecast.get(q='London')
print(current)
print(five_day)




# class WeatherForecastManager:
#     weather_forecast_classes = [CurrentWeatherApiClient, FiveDayForecastApiClient]
#
#     def __init__(self):
#         self.weather_forecast = []
#
#     def run(self, type=None, value=None, api_key=None):
#         for weather_forecast_class in self.weather_forecast_classes:
#             weather_api_client = weather_forecast_class()
#             weather = weather_api_client.get_weather(type, value, api_key)
#             self.weather_forecast.append(weather)
#         return self.weather_forecast
