from .vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year: int):
        super().__init__(company, model, year)
        self._num_wheels = 2

    def test_drive(self):
        self._speed = 75

    def park(self):
        self._speed = 0
