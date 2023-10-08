# Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(),
# обращающийся к внешнему API для получения информации о текущей температуре.
# Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService.
# Создайте мок-объект для WeatherService с использованием Mockito.
from seminars.fourth.weather.weather_reporter import WeatherReporter
from seminars.fourth.weather.weather_service import WeatherService
from mockito import mock, verify, when


class TestWeatherReporter:
    def test_generate_report(self):
        mock_service = mock(WeatherService)
        when(mock_service).get_current_temperature().thenReturn(25)
        reporter = WeatherReporter(mock_service)

        report = reporter.generate_report()

        verify(mock_service, times=1).get_current_temperature()
        assert report == "Текущая температура: 25 градусов."
