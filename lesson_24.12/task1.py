# 1.	Класс "Банк": Разработайте класс Банк, который будет иметь закрытое поле для баланса счета.
# Реализуйте методы для зачисления и снятия денег с баланса, где снятие не может превысить доступный баланс.

class Bank:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            print('Недопустимое значение')

    def deposit(self, value):
        if value > 0:
            self.__balance += value
            print(f'Новый баланс: {self.__balance}')
        else:
            print('Недопустимое значение для зачисления')

    def withdraw(self, value):
        if value <= self.__balance:
            self.__balance -= value
            print(f'Остаток на счете: {self.__balance}')
        else:
            print('Сумма снятия больше, чем текущий баланс')


    def __str__(self):
        return f'Баланс: {self.__balance}'


bank = Bank(1000)
print(bank)
bank.deposit(1000)
bank.withdraw(500)
print(bank)

