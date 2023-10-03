import pytest
from seminars.third.seminar3 import fizz_buzz, first_last_6, calculating_discount, lucky_sum
from decimal import Decimal


class TestFizzBuzz:

    @pytest.mark.parametrize("i, res", ((15, "FizzBuzz"), (45, "FizzBuzz"), (35, "Buzz"), (36, "Fizz"), (41, "41")))
    def test_fizz_buzz(self, i, res):
        assert fizz_buzz(i) == res


class TestFirstLast6:
    @pytest.mark.parametrize("items, res",
                             (([5, 8, 6], True),
                              ([6, 5, 9, 45, 2], True),
                              ([5, 9, 45, 2], False)))
    def test_first_last_6(self, items, res):
        assert first_last_6(items) == res


class TestCalculatingDiscount:
    @pytest.mark.parametrize("amount, discount, result",
                             ((Decimal(2000), 50, Decimal(1000)),
                              (Decimal(2000), 0, Decimal(2000)),
                              (Decimal(2000), 100, Decimal(0)),
                              (Decimal(562.33), 12, Decimal("494.85")),
                              (Decimal(333.33), 33, Decimal("223.33")),))
    def test_valid_param(self, amount, discount, result):
        assert calculating_discount(amount, discount) == result

    def test_invalid_amount_value(self):
        with pytest.raises(ValueError, match="Сумма покупки не может быть отрицательной"):
            calculating_discount(Decimal(-2000), 50)

    @pytest.mark.parametrize("amount", (100, "100", 100.1))
    def test_invalid_amount_type(self, amount):
        with pytest.raises(TypeError, match="Параметр purchase_amount должен быть Decimal"):
            calculating_discount(amount, 50)

    @pytest.mark.parametrize("discount", (-1, 101))
    def test_invalid_discount(self, discount):
        with pytest.raises(ValueError, match="Скидка должна быть в диапазоне от 0 до 100%"):
            calculating_discount(Decimal(2000), discount)

    @pytest.mark.parametrize("discount", ("100", 100.1, None))
    def test_invalid_discount_type(self, discount):
        with pytest.raises(TypeError, match="Параметр discount_amount должен быть int"):
            calculating_discount(Decimal(2000), discount)


class TestLuckySum:
    @pytest.mark.parametrize("a, b, c, res",
                             ((5, 6, 12, 23),
                              (5, 13, 12, 17),
                              (13, 6, 12, 18),
                              (5, 6, 13, 11)))
    def test_lucky_sum(self, a, b, c, res):
        assert lucky_sum(a, b, c) == res
