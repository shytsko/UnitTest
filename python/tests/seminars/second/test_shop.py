from contextlib import redirect_stdout
import io

import pytest
from decimal import Decimal

from seminars.second.models.cart import Cart
from seminars.second.models.product import Product
from seminars.second.models.shop import Shop


@pytest.fixture
def store_items():
    # ID | Название | Цена, р. | Кол - во в магазине, шт.
    # 1  | bacon    | 170.0    | 10
    # 2  | beef     | 250.0    | 10
    # 3  | ham      | 200.0    | 10
    # 4  | salmon   | 150.0    | 10
    # 5  | carrot   | 15.0     | 10
    # 6  | potato   | 30.0     | 10
    # 7  | onion    | 20.0     | 10
    # 8  | apple    | 59.0     | 70
    # 9  | melon    | 88.0     | 13
    # 10 | rice     | 100.0    | 30
    # 11 | eggs     | 80.0     | 40
    # 12 | yogurt   | 55.0     | 60

    product_names = ["bacon", "beef", "ham", "salmon", "carrot", "potato", "onion", "apple", "melon", "rice",
                     "eggs",
                     "yogurt"]
    product_price = [Decimal(170.00), Decimal(250.00), Decimal(200.00), Decimal(150.00), Decimal(15.00),
                     Decimal(0.00),
                     Decimal(20.00), Decimal(59.00), Decimal(88.00), Decimal(100.00), Decimal(80.00),
                     Decimal(55.00)]
    stock = [10, 10, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60]
    return [Product(pk + 1, *param) for pk, param in enumerate(zip(product_names, product_price, stock))]


@pytest.fixture
def cart(store_items):
    return Cart(Shop(store_items))


class TestShop:

    # 2.1. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь положил в корзину несколько продуктов разной стоимости
    # <br><b>Ожидаемый результат:</b>
    # Стоимость корзины посчиталась корректно
    def test_price_cart_is_correct_calculated(self, cart):
        add_products_pk = 1, 5, 8, 11
        expected_total_price = Decimal(0)
        for pk in add_products_pk:
            cart.add_product(pk)
            expected_total_price += cart.get_product_by_id(pk).price

        assert cart.total_price == expected_total_price

    # 2.2. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь положил в корзину несколько продуктов разной стоимости (несколько продуктов одного вида)
    # <br><b>Ожидаемый результат:</b>
    # Стоимость корзины посчиталась корректно
    def test_price_cart_products_same_type_is_correct_calculated(self, cart):
        add_products_pk = 1, 5, 8, 11, 5, 11, 11
        expected_total_price = Decimal(0)
        for pk in add_products_pk:
            cart.add_product(pk)
            expected_total_price += cart.get_product_by_id(pk).price

        assert cart.total_price == expected_total_price

    # 2.3. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь удаляет товар из корзины
    # <br><b>Ожидаемый результат:</b>
    # Вызывается метод пересчета стоимости корзины, стоимость корзины меняется
    def test_when_changing_cart_cost_recalculation_is_called(self, cart):
        add_products_pk = 1, 5, 8, 11, 5, 11, 11
        remove_products_pk = 1, 11
        expected_total_price = Decimal(0)

        for pk in add_products_pk:
            cart.add_product(pk)
            expected_total_price += cart.get_product_by_id(pk).price

        for pk in remove_products_pk:
            cart.remove_product(pk)
            expected_total_price -= cart.get_product_by_id(pk).price

        assert cart.total_price == expected_total_price

    # 2.4. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь кладет в корзину продукт в некотором количестве (не весь оставшийся)
    # <br><b>Ожидаемый результат:</b>
    # Количество товара в магазине уменьшается на число продуктов в корзине пользователя
    def test_quantity_products_store_changing(self, cart):
        add_product_pk = 8
        add_quantity = 3

        start_quantity = cart.get_product_by_id(add_product_pk).quantity

        for _ in range(add_quantity):
            cart.add_product(add_product_pk)

        assert cart.get_product_by_id(add_product_pk).quantity == start_quantity - add_quantity

    # 2.5. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь забрал последние оставшиеся продукты из магазина
    # <br><b>Ожидаемый результат:</b>
    # Больше такой продукт заказать нельзя, он не появляется на полке
    def test_products_disappear_from_store(self, cart):
        add_product_pk = 8
        extra_attempts = 2

        product = cart.get_product_by_id(add_product_pk)

        with redirect_stdout(io.StringIO()) as out_string:
            for _ in range(product.quantity + extra_attempts):
                cart.add_product(product.pk)

        assert product.quantity == 0 and out_string.getvalue() == "Этого товара нет в наличии\n" * extra_attempts

    # * 2.6. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # * Пользователь удаляет продукт из корзины
    # * <br><b>Ожидаемый результат:</b>
    # * Количество продуктов этого типа на складе увеличивается на число удаленных из корзины продуктов
    def test_deleted_product_is_returned_to_shop(self, cart):
        add_product_pk = 8
        add_quantity = 5
        remove_quantity = 3

        start_quantity = cart.get_product_by_id(add_product_pk).quantity

        for _ in range(add_quantity):
            cart.add_product(add_product_pk)

        for _ in range(remove_quantity):
            cart.remove_product(add_product_pk)

        assert cart.get_product_by_id(add_product_pk).quantity == start_quantity - add_quantity + remove_quantity

    # 2.7. Нужно написать юнит-тест для проверки следующей <b>ситуации</b>:
    # Пользователь вводит неверный номер продукта
    # <br><b>Ожидаемый результат:</b>
    # Исключение типа RuntimeException и сообщение Не найден продукт с id
    # *Сделать тест параметризованным

    @pytest.mark.parametrize("incorrect_add_product_pk", [20, -8, 100])
    def test_incorrect_product_selection_causes_exception(self, cart, incorrect_add_product_pk):
        with pytest.raises(ValueError, match=f"Не найден продукт с id: {incorrect_add_product_pk}"):
            cart.add_product(incorrect_add_product_pk)

    # 2.10. Нужно изменить тест по следующим критериям:
    # <br> 1. Отображаемое имя - "Advanced test for calculating TotalPrice"
    # <br> 2. Тест повторяется 10 раз
    # <br> 3. Установлен таймаут на выполнение теста 70 Миллисекунд (unit = TimeUnit.MILLISECONDS)
    # <br> 4. После проверки работоспособности теста, его нужно выключить
    @pytest.mark.parametrize("i", range(10))
    @pytest.mark.timeout(0.07)
    def test_price_cart_is_correct_calculated_ext(self, cart, i):
        add_product_pk = 8
        cart.add_product(add_product_pk)
