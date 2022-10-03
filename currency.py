class Currency_service():
    def __init__(self):
        self.currency_dict = {
                'USD': 0.0171,
                'EURO': 0.0179,
                'TJS': 0.178,
                'GBP': 0.01621,
                'CNY': 0.1252
        }

    def get_currency_by_type(self,currency_type):
        return self.currency_dict[currency_type]


