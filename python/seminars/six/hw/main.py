class DataProcessor:
    @staticmethod
    def compare_avg(list1: list[int | float], list2: list[int | float]) -> None:
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise TypeError("Аргументы должны быть списками")

        if any(map(lambda x: not isinstance(x, (int, float)), list1 + list2)):
            raise TypeError("Элементы списков должны быть числового типа")

        avg1 = sum(list1) / len(list1) if list1 else 0
        avg2 = sum(list2) / len(list2) if list2 else 0
        if avg1 > avg2:
            print("Первый список имеет большее среднее значение")
        elif avg2 > avg1:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
