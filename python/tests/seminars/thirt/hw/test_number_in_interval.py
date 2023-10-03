import pytest
from seminars.third.hw.hw import number_in_interval


@pytest.mark.parametrize("num, res", ((25, True), (100, True), (50, True), (24, False), (101, False)))
def test_number_in_interval(num, res):
    assert number_in_interval(num) == res
