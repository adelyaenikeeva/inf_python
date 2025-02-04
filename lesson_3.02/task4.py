# 4.	Создайте список из чисел. Напишите программу, которая итерируется по списку и выполняет деление числа на предыдущее.
# Обработайте случай, когда число делится на ноль, с помощью исключения. Добавьте собственное исключение EmptyListError,
# которое вызывается, если список пуст.

class EmptyListError(Exception):
    def __init__(self):
        super().__init__('Список пуст')


def list_division(input_list):
    if not input_list:
        raise EmptyListError()

    result = []
    for i in range(1, len(input_list)):
        try:
            numerator = input_list[i]
            denominator = input_list[i - 1]
            if denominator == 0:
                raise ZeroDivisionError('Ошибка: деление на ноль невозможно')
            result.append(numerator / denominator)

        except ZeroDivisionError as e:
            print(e)
            result.append(None)

    return result

numbers = [1, 2, 0, 3, 5, 10]
try:
    print(list_division(numbers))
except EmptyListError as e:
    print(e)



