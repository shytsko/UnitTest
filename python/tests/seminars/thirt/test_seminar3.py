import pytest
from seminars.third.seminar3 import fizz_buzz, first_last_6


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
