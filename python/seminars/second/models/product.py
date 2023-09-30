from decimal import Decimal


class Product:
    def __init__(self, pk: int, name: str, price: Decimal, quantity: int):
        self.pk = pk
        self.name = name
        self.price = Decimal(price)
        self.quantity = quantity

    def __eq__(self, other):
        if id(self) == id(other):
            return True
        if other is None:
            return False
        if not isinstance(other, self.__class__):
            return False
        return all((self.pk == other.pk, self.name == other.name, self.price == other.price,
                    self.quantity == other.quantity))

    def __str__(self):
        return self.name
