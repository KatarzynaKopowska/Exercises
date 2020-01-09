from openweather_api_client import WeatherForecastManager
import config

if __name__ == "__main__":
    weather_forecast_manager = WeatherForecastManager()
    weather_forecast = weather_forecast_manager.run(
        type="q",
        value="London",
        api_key=config.OPENWEATHER_API_KEY
    )

    print(f"Weather forecast for city {weather_forecast[0].city}, {weather_forecast[0].country}:")
    for weather in weather_forecast:
        print(f"{weather.weather_forecast_type}:".rjust(20, " "),
              f"{weather.current_weather}, "
              f"temp: {weather.temperature}(°F), "
              f"pressure: {weather.pressure}(hPa)"
              )
