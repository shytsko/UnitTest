import pytest
from seminars.five.number.random_number_module import RandomNumber


class TestRandomNumber:
    def test_random_list_is_random(self):
        length = 10
        test_list1 = RandomNumber.random_list(length)
        test_list2 = RandomNumber.random_list(length)
        assert test_list1 != test_list2

    def test_random_list_length(self):
        length = 10
        test_list = RandomNumber.random_list(length)
        assert length == len(test_list)

    def test_empty_list_if_length_zero(self):
        length = 0
        test_list = RandomNumber.random_list(length)
        assert test_list == []

    def test_raise_if_negative_length(self):
        length = -10
        with pytest.raises(ValueError, match="Размер списка не может быть отрицательным"):
            RandomNumber.random_list(length)
