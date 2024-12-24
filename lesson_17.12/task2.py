# 2.	Управление банковским счётом:
# Создайте класс BankAccount с атрибутами account_number и balance.
# Реализуйте методы для внесения (deposit) и снятия денег (withdraw).
# Добавьте метод для вывода текущего баланса.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        return self.balance

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
        else:
            print('Сумма снятия больше, чем текущий баланс')
        return self.balance

    def __str__(self):
        return f'Номер счета: {self.account_number}, Баланс: {self.balance}'

bank = BankAccount("01", 1000)
print(bank)
print(bank.deposit(1000))
print(bank)
print(bank.withdraw(500))
print(bank)

bank2 = BankAccount("02")
print(bank2)
print(bank2.deposit(10000))
print(bank2)
print(bank2.withdraw(5000))
print(bank2)

