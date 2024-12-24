# 5. Создание класса "Круг":
# Создайте класс Circle с атрибутами radius.
# Реализуйте методы для вычисления площади (area) и периметра
# (circumference) круга.
# Добавьте метод сравнения двух кругов по площади.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'Площадь: {math.pi * (self.radius**2)}'

    def circumference(self):
        return f'Периметр: {2 * math.pi * self.radius}'

    def area_comparison(self, area1, area2):
        if area1 < area2:
            return 'Площадь второго круга больше'
        return 'Площадь первого круга больше'


circle = Circle(4)
area1 = circle.area()
print(area1)
print(circle.circumference())

circle2 = Circle(2)
area2 = circle2.area()
print(area2)
print(circle2.circumference())

print(circle.area_comparison(area1, area2))