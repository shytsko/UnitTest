from mockito import mock, verify, when, spy, spy2

from seminars.fourth.main import Iterator


# Проверка работы mockito

class TestSimple:
    def test_simple(self):
        mocked_list = mock(list)
        when(mocked_list).append(...).thenReturn(None)
        mocked_list.append("b")
        verify(mocked_list).append("b")


# 4.1. Создать мок-объект Iterator, настроить поведение так,
# чтобы за два вызова next() Iterator вернул два слова  “Hello World”,
# и проверить это поведение с помощью утверждений
def test_iterator_will_return_hello_world():
    iterator_mock = mock(Iterator)
    when(iterator_mock).__next__().thenReturn("Hello").thenReturn("World")
    res = f"{iterator_mock.__next__()} {iterator_mock.__next__()}"
    assert "Hello World" == res


