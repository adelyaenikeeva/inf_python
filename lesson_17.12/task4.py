# Создайте класс Car с атрибутами brand, model, и year.
# Добавьте метод display_info, который выводит всю информацию об
# автомобиле.
# Создайте несколько инстансов класса Car и вызовите
# метод display_info для каждого из них.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}'

car = Car('BMW', 'X3', 2016)
car2 = Car('Toyota', 'Rav4', 2020)
print(car.display_info())
print(car2.display_info())