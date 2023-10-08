# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли
# переданное число четным или нечетным:

def even_odd_number(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


# Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли
# переданное число в интервал (25;100)

def number_in_interval(n: int) -> bool:
    return 25 <= n <= 100
