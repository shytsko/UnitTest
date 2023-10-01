from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company: str, model: str, year: int):
        self._company = company
        self._model = model
        self._year_release = year
        self._num_wheels = 0
        self._speed = 0

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year_release

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def speed(self):
        return self._speed

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass
