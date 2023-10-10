import pytest

from seminars.five.number.max_number_module import MaxNumberModule


class TestMaxNumber:
    def test_find_max_number(self):
        test_list = [456, 7, 4, 2, -56456, 6643, -99, 3, 8975, 3]

        res = MaxNumberModule.max_number(test_list)

        assert res == 8975

    def test_raise_if_empty_list(self):
        test_list = []

        with pytest.raises(ValueError):
            MaxNumberModule.max_number(test_list)

    def test_raise_if_not_iterable(self):
        test_list = 5

        with pytest.raises(TypeError):
            MaxNumberModule.max_number(test_list)
