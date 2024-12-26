# 6.	Класс "Курс обмена валют": Напишите класс КурсОбмена, который будет иметь закрытые поля для текущего обменного курса валюты.
# Реализуйте методы для получения и установки курса, где проверка обеспечивает разумные пределы курса (например, 0.01 до 500).

class CurrencyExchange:
    def __init__(self, currency=100):
        self.__currency = currency
        self.__min_value = 0.01
        self.__max_value = 500

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if self.__min_value <= value <= self.__max_value:
            self.__currency = value
        else:
            print('Недопустимое значение')

    def __str__(self):
        return f'Текущий курс: {self.__currency}'

currency = CurrencyExchange()
print(currency)
currency.currency = 500
print(currency)
currency.currency = 1000
