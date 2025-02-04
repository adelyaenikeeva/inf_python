# 19.	Создайте список всех чисел от 1 до 50, которые делятся на 3, но не делятся на 5.

result = [num for num in range(1, 51) if num % 3 == 0 and num % 5 != 0]
print(result)