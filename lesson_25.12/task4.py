# 4.	Создайте базовый класс Shape, а затем реализуйте подклассы Circle, Rectangle, Triangle.
# Каждый класс должен содержать метод для вычисления площади и метод draw, который будет выводить информацию о фигуре.

import math


class Shape:
    def area(self):
        print('area')

    def draw(self):
        print('draw')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print(f'Это круг: радиус {self.radius}. Площадь: {self.area()}')


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f'Это прямоугольник: ширина: {self.width}, высота {self.height}. Площадь: {self.area()}')

circle = Circle(5)
circle.draw()

rectangle = Rectangle(4, 7)
rectangle.draw()
