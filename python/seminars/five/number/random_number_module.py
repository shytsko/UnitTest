import random


class RandomNumber:
    @staticmethod
    def random_list(length: int) -> list[int]:
        if length < 0:
            raise ValueError("Размер списка не может быть отрицательным")
        return [random.randint(-1000, 1000) for _ in range(length)]