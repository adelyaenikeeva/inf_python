# 3.	Класс "Автомобиль": Создайте класс Автомобиль с закрытыми полями для марки,
# модели и скорости. Установите методы доступа и модификации, где скорость не может быть меньше 0 и больше 200 км/ч.

class Auto:
    def __init__(self, brand, model, speed):
        self.__brand = brand
        self.__model = model
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str):
            self.__brand = new_brand
        else:
            print('Значение должно быть строкой')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            print('Значение должно быть строкой')

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        if 0 <= new_speed <= 200:
            self.__speed = new_speed
        else:
            print('Недопустимое значение')

    def __str__(self):
        return f'Brand: {self.__brand}, Model: {self.__model}, Speed: {self.__speed}'


auto = Auto('Toyota', 'Rav4', 100)
print(auto)

# auto.speed = -200
# print(auto)

# auto.speed = 200
# print(auto)

