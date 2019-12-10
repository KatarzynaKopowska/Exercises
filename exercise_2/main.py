import sys
from openweather_api_client import BasicWeatherApiClient


if __name__ == "__main__":
    try:
        weather = BasicWeatherApiClient()
        complete_weather = weather.get_weather()
        current_weather = weather.parse_weather(complete_weather)
    except KeyError:
        print("City not found.")
        sys.exit()

    print(f"Current weather for city: "
          f"{current_weather.city}, "
          f"{current_weather.country}: "
          f"{current_weather.current_weather}, "
          f"temp: {current_weather.temperature}(°F), "
          f"pressure: {current_weather.pressure}(hPa)"
          )
