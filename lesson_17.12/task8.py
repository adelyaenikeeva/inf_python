# Создайте класс Point3D с атрибутами x, y, z.
# Реализуйте метод distance_to, который вычисляет расстояние до другой
# точки Point3D.
# Разработайте метод для вывода координат точки.
import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, x, y, z):
        return math.sqrt((self.x - x) ** 2 +
                         (self.y - y) ** 2 +
                         (self.z - z) ** 2)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)

print(point1)
print(point2)
print(f'Расстояние от point1 до точки (2, 3, 6): {point1.distance_to(2, 3, 6)}')