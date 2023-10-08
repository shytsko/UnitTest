from seminars.fourth.weather.weather_service import WeatherService


class WeatherReporter:
    def __init__(self, weather_service: WeatherService):
        self._weather_service = weather_service

    def generate_report(self):
        temperature = self._weather_service.get_current_temperature()
        return f"Текущая температура: {temperature} градусов."
