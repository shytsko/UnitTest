import pytest
from seminars.five.number.random_number_module import RandomNumber
from seminars.five.number.max_number_module import MaxNumberModule


class TestIntegratedNumbers:
    def test_get_random_list_and_find_max(self):
        test_list = RandomNumber.random_list(10)
        max_num = MaxNumberModule.max_number(test_list)

        assert max_num == max(test_list)
