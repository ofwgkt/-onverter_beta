from converter_oop import Converter

converter_usd = Converter('USD', 2500)
converter_euro = Converter('EURO', 2500)
s = converter_euro.convert()
s1 = converter_usd.convert()
print('{} RUB converts to {} {}'.format(converter_euro.rubles,s,converter_euro.currency.upper()))
print('{} RUB converts to {} {}'.format(converter_usd.rubles,s1,converter_usd.currency.upper()))
