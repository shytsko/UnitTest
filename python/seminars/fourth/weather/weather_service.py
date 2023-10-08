from random import randint


class WeatherService:
    # Метод, который в реальной ситуации обращается к внешнему API для получения температуры
    @staticmethod
    def get_current_temperature() -> int:
        return 22 + randint(0, 9)
