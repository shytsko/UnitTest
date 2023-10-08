#  4.2. Используя библиотеку Mockito, напишите модульные тесты для проверки функциональности формы оплаты на сайте.
#  * Вместо реальной кредитной карты используйте мок-объект.
#  Создайте класс `CreditCard` с методами `getCardNumber()`, `getCardHolder()`, `getExpiryDate()`, `getCvv()`, `charge(double amount)`.
#  Создайте класс `PaymentForm` с методом `pay(double amount)`.
#  В тестовом классе, создайте мок-объект для класса `CreditCard`.
#  Определите поведение мок-объекта с помощью метода `when()`.
#  Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
#  Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`
from mockito import mock, verify, when

from seminars.fourth.card.credit_card import CreditCard
from seminars.fourth.card.payment_form import PaymentForm


class TestPaymentForm:
    def test_charge_method_called(self):
        mock_card = mock(CreditCard)
        when(mock_card).charge(...).thenReturn(None)
        form = PaymentForm(mock_card)
        form.pay(1)
        verify(mock_card, times=1).charge(1)

