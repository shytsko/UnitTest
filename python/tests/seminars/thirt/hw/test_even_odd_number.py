import pytest
from seminars.third.hw.hw import even_odd_number


@pytest.mark.parametrize("num, res", ((0, True), (6, True), (50, True), (-16, True), (13, False), (-13, False)))
def test_even_odd_number(num, res):
    assert even_odd_number(num) == res
