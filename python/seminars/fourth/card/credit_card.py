class CreditCard:
    def __init__(self, card_number: str, card_holder: str, expiry_date: str, cvv: str):
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvv = cvv

    def get_card_number(self):
        return self._card_number

    def get_card_holder(self):
        return self._card_holder

    def get_expiry_date(self):
        return self._expiry_date

    def get_cvv(self):
        return self._cvv

    def charge(self, amount):
        return print(f"Charged amount {amount} from the card: {self._card_number}")
