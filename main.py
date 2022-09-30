currency = input('Hello, input the currency to convert''\n').upper()
rubles = input('how many rubles you want to convert?''\n')
currencys_dict = {
    'USD' : 0.0171,
    'EURO' : 0.0179,
    'TJS' : 0.178,
    'GBP' : 0.01621,
    'CNY' : 0.1252
}
def convert():
    if rubles.isdigit() and currency.isalpha():

        if currency in currencys_dict.keys():
            result = round(float(currencys_dict[currency])*int(rubles),3)
            return ('{} RUB converts to {} {}'.format(rubles,result,currency.upper()))
        else:
            print('this currency is not supported')
            anoter_curr_add = input('do you want to add another one?''\n')

            if anoter_curr_add == 'YES'.lower():
                second_curr = input('input your currency koefficent''\n')
                result1 = float(second_curr) * int(rubles)
                return ('{} RUB converts to {} {}'.format(rubles, round(result1, 2), currency))
            else:
                return 'Sorry i cant help you for now!\nHave a good day ser!'
    else:
        return 'Error!\nPlease check the currency and the quantity of rubles and try agan'

print(convert())