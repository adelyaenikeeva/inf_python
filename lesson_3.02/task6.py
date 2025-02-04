# 6.	Напишите функцию, которая с помощью reduce и lambda вычисляет сложение всех чисел в списке.
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print("Сумма всех чисел:", product)