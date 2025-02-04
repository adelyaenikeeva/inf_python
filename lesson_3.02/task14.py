# 14.	Напишите генератор, который принимает список целых чисел и возвращает только четные числа.

def number_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6]
print(list(number_generator(numbers)))

