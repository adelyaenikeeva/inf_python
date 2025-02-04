# 15.	Напишите генератор, который возвращает факториалы целых чисел от 0 до n (включительно).

def factorial_generator(number):
    factorial = 1
    for i in range(number + 1):
        if i == 0 or i == 1:
            factorial = 1  # Факториал 0! и 1! равен 1
        else:
            factorial *= i
        yield factorial

number = 4
print(list(factorial_generator(number)))