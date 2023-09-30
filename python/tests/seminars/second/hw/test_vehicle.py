import pytest

from seminars.second.hw.car import Car
from seminars.second.hw.motorcycle import Motorcycle
from seminars.second.hw.vehicle import Vehicle


@pytest.fixture
def car():
    print("car fixture")
    return Car("Lamborghini", "Urus", 2023)


@pytest.fixture
def motorcycle():
    return Motorcycle("Minsk", "125", 1992)


class TestCar:
    # проверка того, что экземпляр объекта Car также является экземпляром транспортного средства
    def test_car_instance_of_vehicle(self, car):
        assert isinstance(car, Vehicle)

    # проверка того, объект Car создается с 4 - мя колесами
    def test_car_num_wheels(self, car):
        assert car.num_wheels == 4

    # проверка того, объект Car развивает скорость 60 в режиме тестового вождения(testDrive())
    def test_car_drive_speed(self, car):
        car.test_drive()
        assert car.speed == 60

    # проверить, что в режиме парковки(сначала testDrive, потом park, т.е эмуляция движения транспорта)
    # машина останавливается(speed=0)
    def test_car_park_speed(self, car):
        car.test_drive()
        car.park()
        assert car.speed == 0


class TestMotorcycle:

    # проверка того, объект Motorcycle создается с 2 - мя колесами
    def test_motorcycle_num_wheels(self, motorcycle):
        assert motorcycle.num_wheels == 2

    # проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения(testDrive())

    def test_motorcycle_drive_speed(self, motorcycle):
        motorcycle.test_drive()
        assert motorcycle.speed == 75

    # проверить, что в режиме парковки(сначала testDrive, потом park т.е эмуляция движения транспорта)
    # мотоцикл останавливается(speed=0)
    def test_motorcycle_park_speed(self, motorcycle):
        motorcycle.test_drive()
        motorcycle.park()
        assert motorcycle.speed == 0
