# 1.	Создайте базовый класс Animal, который будет иметь атрибуты name (имя) и age(возраст).
# Затем создайте два дочерних класса: Dog и Cat.
# Требования:
# В классе Animal добавьте метод speak(), который возвращает строку с общим звуком животного (например, "Some sound").
# В классе Dog переопределите метод speak() так, чтобы он возвращал "Woof!" и добавьте новый атрибут breed (порода).
# В классе Cat переопределите метод speak() так, чтобы он возвращал "Meow!" и добавьте новый атрибут color (цвет).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print('Недопустимое значение')

    def speak(self):
        print('Some sound')

    def display_info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}')


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print('Гав')

    def display_info(self):
        super().display_info()
        print(f'Порода: {self.breed}')
        # print(f'Имя: {self.name}, Возраст: {self.age}, Порода: {self.breed}')

class Cat(Animal):
    def speak(self):
        print('Мяу')

print('DOG')
dog = Dog('Name', 12, 'Корги')
# print(dog.name)
dog.age = -20
print(dog.age)
dog.speak()
dog.display_info()

print('\nCAT')
cat = Cat('cat name', 12)
print(cat.name)
cat.display_info()
cat.speak()
