# 2.	Создайте собственный класс исключения (например, NegativeValueError), который вызывается,
# если пользователь вводит отрицательное число. Напишите функцию, принимающую число от пользователя,
# и проверьте, что оно положительное. В случае отрицательного числа вызывайте собственное исключение.

class NegativeValueError(Exception):
    def __init__(self, number):
        super().__init__(f'Введено отрицательное число: {number}')

def check_number(number):
    if number < 0:
        raise NegativeValueError(number)
    return number

try:
    print(check_number(10))
    print(check_number(-5))
except NegativeValueError as e:
    print(e)