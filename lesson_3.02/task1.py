# 1.	Напишите функцию, которая запрашивает у пользователя два числа, выполняет их деление и выводит результат.
# Если пользователь вводит некорректное число (например, отрицательное число), обработайте исключение
# ValueError и попросите ввести данные снова. Обработайте также деление на ноль с помощью исключения ZeroDivisionError.

def divide(a, b):
    if a < 0 or b < 0:
        raise ValueError('Ошибка: Отрицательное число')

    if b == 0:
        raise ZeroDivisionError('Ошибка: Деление на ноль')

    return a/b

while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

        print(f'Результат деления: {divide(a, b)}')
        break
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)