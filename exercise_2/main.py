import sys
from openweather_api_client import CurrentWeatherApiClient
from openweather_api_client import HourlytWeatherApiClient

if __name__ == "__main__":
    try:
        weather = CurrentWeatherApiClient()
        current_weather = weather.get_weather(filter='q', value='London', api_key='8141563408c821030aa7cdacd8bd0eff')
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


    weather1 = HourlytWeatherApiClient()
    hourly_weather = weather1.get_weather(filter='id', value='524901', api_key='8141563408c821030aa7cdacd8bd0eff')
    print(hourly_weather)