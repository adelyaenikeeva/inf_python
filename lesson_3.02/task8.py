# 8.	Напишите программу, которая объединяет два списка ключей и значений в словарь с использованием функции zip.

key = [1, 2, 3]
values = [1, 2, 3]

result = dict(zip(key, values))
print(result)