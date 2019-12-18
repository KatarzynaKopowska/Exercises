from openweather_api_client import WeatherForecastManager

if __name__ == "__main__":
    weather_forecast_manager = WeatherForecastManager()
    weather_forecast = weather_forecast_manager.run(
        filter="q",
        value="London",
        api_key="8141563408c821030aa7cdacd8bd0eff"
    )

    print(f"Weather forecast for city {weather_forecast[0].city}, {weather_forecast[0].country}:")
    for weather in weather_forecast:
        print(f"{weather.weather_forecast_type}:".rjust(20, " "),
              f"{weather.current_weather}, "
              f"temp: {weather.temperature}(°F), "
              f"pressure: {weather.pressure}(hPa)"
              )
