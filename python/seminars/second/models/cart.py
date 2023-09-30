import time

from .product import Product
from .shop import Shop
from decimal import Decimal


class Cart:
    def __init__(self, shop: Shop):
        self.shop: Shop = shop
        self._total_price: Decimal = Decimal(0)
        self.cart_items: list[Product] = list()

    def add_product(self, pk: int):
        product = self.get_product_by_id(pk)
        self._add_to_cart(product)
        self.recalculate()

    def recalculate(self):
        self._total_price = sum((product.price * product.quantity for product in self.cart_items), start=Decimal(0))

    def get_product_by_id(self, pk: int) -> Product:
        product: Product = None

        for p in self.shop.product_shop:
            if p.pk == pk:
                product = p
                break

        if pk > len(self.shop.product_shop) or pk < 0:
            raise ValueError(f"Не найден продукт с id: {pk}")

        return product

    def _add_to_cart(self, product: Product):
        product_in_cart: Product = Product(product.pk, product.name, product.price, 0)
        product_in_shop: Product = self.shop.product_shop[product.pk - 1]

        if product_in_shop.quantity == 0:
            print("Этого товара нет в наличии")
            return

        if self._has_contain_product(product_in_cart):
            self._get_contain_product(product_in_cart).quantity += 1
        else:
            product_in_cart.quantity = 1
            self.cart_items.append(product_in_cart)

        self.recalculate()

        self.shop.product_shop[product.pk - 1].quantity -= 1

    def _has_contain_product(self, product: Product) -> bool:
        for item in self.cart_items:
            if item.pk == product.pk:
                return True
        return False

    def _has_contain_product_id(self, pk: int) -> bool:
        for item in self.cart_items:
            if item.pk == pk:
                return True
        return False

    def _get_contain_product(self, product: Product) -> Product | None:
        for item in self.cart_items:
            if item.pk == product.pk:
                return item
        return None

    def remove_product(self, pk: int):
        if not self._has_contain_product_id(pk):
            raise ValueError(f"В корзине не найден продукт с id: {pk} ")

        product = self.get_product_by_id(pk)

        if self._has_contain_product(product) and self._get_contain_product(product).quantity > 1:
            self._get_contain_product(product).quantity -= 1
        elif self._has_contain_product(product) and self._get_contain_product(product).quantity == 1:
            self.cart_items.remove(self._get_contain_product(product))

        # time.sleep(2)

        self.recalculate()

        self.shop.product_shop[pk - 1].quantity += 1

    def print_cart_items(self):
        print("Сейчас у вас в корзине:")
        for product in self.cart_items:
            print(f"{product.pk} {product.name} {product.price} {product.quantity}")

        print(f"Общая стоимость корзины: {self._total_price}")

    @property
    def total_price(self):
        return self._total_price
