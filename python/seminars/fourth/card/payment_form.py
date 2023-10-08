from seminars.fourth.card.credit_card import CreditCard


class PaymentForm:
    def __init__(self, credit_card: CreditCard):
        self._credit_card = credit_card

    def pay(self, amount: float):
        self._credit_card.charge(amount)
