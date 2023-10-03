from decimal import Decimal, Rounded


# 3.1. Создайте набор тестов, полностью покрывающих все ветви кода функции fizzBuzz. Эта
# функция принимает на вход число и возвращает "Fizz", если число делится на 3, "Buzz",
# если число делится на 5, и "FizzBuzz", если число делится на 15. Если число не делится ни
# на 3, ни на 5, ни на 15, функция возвращает входное число в виде строки.

def fizz_buzz(i: int) -> str:
    if i % 15 == 0:
        return "FizzBuzz"
    if i % 5 == 0:
        return "Buzz"
    if i % 3 == 0:
        return "Fizz"
    return str(i)


# 3.2. Метод возвращает true для массивов, которые начинаются или заканчиваются 6,
# и false - если 6 нет ни в начале ни в конце массива
def first_last_6(data: list) -> bool:
    return data[0] == 6 or data[-1] == 6


# Создайте тесты, обеспечивающие полное покрытие кода метода calculatingDiscount, который принимает сумму
# покупки и размер скидки, затем вычисляет и возвращает сумму с учетом скидки. Метод должен обрабатывать
# исключения, связанные с некорректным размером скидки или отрицательной суммой покупки.

def calculating_discount(purchase_amount: Decimal, discount_amount: int) -> Decimal:
    if not isinstance(purchase_amount, Decimal):
        raise TypeError("Параметр purchase_amount должен быть Decimal")

    if not isinstance(discount_amount, int):
        raise TypeError("Параметр discount_amount должен быть int")

    if purchase_amount < 0:
        raise ValueError("Сумма покупки не может быть отрицательной")

    if not (0 <= discount_amount <= 100):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")

    return (purchase_amount * (1 - Decimal(discount_amount) / 100)).quantize(Decimal("1.00"))


# Разработайте метод luckySum и напишите для него тесты. Этот метод принимает на вход три числа и возвращает
# их сумму. Однако, если одно из чисел равно 13, то оно не учитывается при подсчете суммы.
def lucky_sum(a, b, c):
    return sum(filter(lambda x: x != 13, (a, b, c)))
