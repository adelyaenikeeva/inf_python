# 7.	Используя filter, напишите программу, которая из списка удаляет все нечетные числа.
def is_even(number):
    return number % 2 == 0

input_list = [1, 5, 3, 10, 7, 2, 4]
even_numbers = filter(lambda x: x % 2 == 0, input_list)
# even_numbers = filter(is_even, input_list)
print(list(even_numbers))
