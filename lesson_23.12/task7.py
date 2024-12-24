# 8. Виртуальный сад:
#    - Создайте класс `Plant` с атрибутами `__species`, `__height`, `__water_level`.
#    - Добавьте методы для роста растений, полива и проверки текущего состояния.
#    - Разработайте класс `Garden` для управления несколькими растениями и оптимизации их роста.

class Plant:
    def __init__(self, species, height=0, water_level=0):
        self.__species = species
        self.__height = height
        self.__water_level = water_level

    @property
    def species(self):
        return self.__species

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value

    @property
    def water_level(self):
        return self.__water_level

    @water_level.setter
    def water_level(self, value):
        if value >= 0:
            self.__water_level = value

    def grow(self):
        if self.__water_level > 0:
            self.__height += 1
            self.__water_level -= 1
            print(f'{self.__species}, высота: {self.__height}')

    def water(self, amount):
        self.__water_level += amount
        print(f'{self.__species}, текущий уровень воды: {self.__water_level}')

    # def check_status(self):
    #     print(f'Вид: {self.__species}, Высота: {self.__height}, Уровень воды: {self.__water_level}')

    def __str__(self):
        return f'Вид: {self.__species}, Высота: {self.__height}, Уровень воды: {self.__water_level}'

print("PLANT")
plant1 = Plant('Plant', 10, 5)
plant2 = Plant('Plant2', 15, 10)

print(plant1)
print(plant2)

plant1.water_level += 3
plant2.water_level += 5

plant1.grow()
plant2.grow()

print(plant1)
print(plant2)


class Garden:
    def __init__(self):
        self.__plants = []

    def add_plant(self, plant):
        if isinstance(plant, Plant):
            self.__plants.append(plant)
            print(f'Добавлено растение {plant.species}')
        else:
            print('Можно добавлять только объекты класса Plant')

    def water_all(self, amount):
        for plant in self.__plants:
            plant.water(amount)

    def grow_all(self):
        for plant in self.__plants:
            plant.grow()

    def check_plant_statuses(self):
        for plant in self.__plants:
            print(plant)

print('\nGARDEN')
my_garden = Garden()

my_garden.add_plant(plant1)
my_garden.add_plant(plant2)

my_garden.water_all(5)

my_garden.grow_all()

my_garden.check_plant_statuses()