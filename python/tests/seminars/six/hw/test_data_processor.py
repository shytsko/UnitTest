import pytest
import sys
import io
from seminars.six.hw.main import DataProcessor


class TestDataProcessor:
    @pytest.mark.parametrize("list1, list2, output",
                             (
                                     (
                                             [14, -6.59, 0, 88, 19, 11],
                                             [1, -6, 8, 5.46, -66, 14, 10, 8],
                                             "Первый список имеет большее среднее значение\n"
                                     ),
                                     (
                                             [1, -6, 8, 5.46, -66, 14, 10, 8],
                                             [14, -6.59, 0, 88, 19, 11],
                                             "Второй список имеет большее среднее значение\n"
                                     ),
                                     (
                                             [1, -6, 8, 5.46, -66, 14, 10, 8],
                                             [21, -6, 8, 10.46, -71, 14, -10, 8],
                                             "Средние значения равны\n"
                                     ),
                                     (
                                             [],
                                             [14, -6.59, 0, 88, 19, 11],
                                             "Второй список имеет большее среднее значение\n"
                                     ),
                                     (
                                             [1, -6, 8, 5.46, -66, 14, 10, 8],
                                             [],
                                             "Второй список имеет большее среднее значение\n"
                                     )
                             )
                             )
    def test_valid_args(self, list1, list2, output):
        """
        Тесты с различными вариантами допустимых параметров
        """
        tmp_out = sys.stdout
        new_out = io.StringIO()
        sys.stdout = new_out
        DataProcessor.compare_avg(list1, list2)
        assert new_out.getvalue() == output
        sys.stdout = tmp_out

    @pytest.mark.parametrize("list1, list2", (([14, -6.59, 0, 88, 19, 11], 0), (0, [14, -6.59, 0, 88, 19, 11])))
    def test_arg_not_list(self, list1, list2):
        """
        В качестве аргумента передается не список
        """
        with pytest.raises(TypeError, match="Аргументы должны быть списками"):
            DataProcessor.compare_avg(list1, list2)

    @pytest.mark.parametrize("list1, list2", (([14, -6.59, 0, 88, 19, 11], [1, -6, 8, "5.46", -66, 14, 10, 8]),
                                              ([1, -6, 8, "5.46", -66, 14, 10, 8], [14, -6.59, 0, 88, 19, 11])))
    def test_item_list_not_numeric(self, list1, list2):
        """
        Списки содержат элементы не числового типа
        """
        with pytest.raises(TypeError, match="Элементы списков должны быть числового типа"):
            DataProcessor.compare_avg(list1, list2)
