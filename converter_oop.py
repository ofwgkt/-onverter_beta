from currency import Currency


class Converter():
    # модель конвертера

    def __init__(self, currency, rubles):
        # инициализация атрибутов конвертера - валюта, кол-во рублей
        self.currency_service = Currency()
        self.currency = currency
        self.rubles = rubles

    def convert(self):

            koeff = self.currency_service.get_currency_by_type(self.currency)
            result = koeff * self.rubles
            return result
