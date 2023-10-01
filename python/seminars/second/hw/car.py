from .vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company: str, model: str, year: int):
        super().__init__(company, model, year)
        self._num_wheels = 4

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0
