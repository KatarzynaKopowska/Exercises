from openweather_api_client import OpenWeatherAPIClient
import config


if __name__ == "__main__":
    open_weather_client = OpenWeatherAPIClient(api_key=config.OPENWEATHER_API_KEY)
    current = open_weather_client.current_weather.get(zip=94040)
    five_day = open_weather_client.five_day_forecast.get(q='London')

    weather_forecasts = [current, five_day]

    for weather_forecast in weather_forecasts:
        print(f" {weather_forecast.weather_forecast_type} for city: {weather_forecast.city}, "
              f"{weather_forecast.country}: "
              f"{weather_forecast.current_weather}, "
              f"temp: {weather_forecast.temperature}(°F), "
              f"pressure: {weather_forecast.pressure}(hPa)"
              )
