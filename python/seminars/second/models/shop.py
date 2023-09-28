from .product import Product


class Shop:
    def __init__(self, product_shop: list[Product]):
        self.product_shop = product_shop
